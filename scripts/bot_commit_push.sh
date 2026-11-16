#!/usr/bin/env bash
# Commit bot-generated data and push it to main, surviving a push race.
#
# The pricing and availability refreshes both write to main. They share one
# concurrency group so they queue rather than overlap, but a human push (or a
# second refresh landing while a run is in flight) can still move the branch
# under a run. A plain `git push` then fails with "Updates were rejected" and
# the whole run goes red for no reason.
#
# So: push, and if it is rejected, fetch the new tip, rebase the bot commit onto
# it and retry. A genuine conflict still fails loudly rather than silently
# dropping an observation.
#
#   scripts/bot_commit_push.sh "pricing refresh 2026-11-16" data reports
#
# Set `id:` on the workflow step to read `changed=true|false` afterwards.
set -euo pipefail

message="${1:?commit message required}"
shift

git config user.name  "catalogue-bot"
git config user.email "bot@users.noreply.github.com"

if [ "$#" -gt 0 ]; then
  git add -- "$@"
else
  git add -- .
fi

if git diff --cached --quiet; then
  echo "no changes"
  echo "changed=false" >> "${GITHUB_OUTPUT:-/dev/null}"
  exit 0
fi

git commit -m "$message"

for attempt in 1 2 3; do
  if git push origin "HEAD:${GITHUB_REF_NAME:-main}"; then
    echo "pushed $(git rev-parse --short HEAD) on attempt ${attempt}"
    echo "changed=true" >> "${GITHUB_OUTPUT:-/dev/null}"
    exit 0
  fi
  echo "::warning::push rejected (attempt ${attempt}); rebasing onto origin/${GITHUB_REF_NAME:-main}"
  git fetch --no-tags origin "${GITHUB_REF_NAME:-main}"
  if ! git rebase "origin/${GITHUB_REF_NAME:-main}"; then
    git rebase --abort || true
    echo "::error::the bot commit conflicts with the new tip of ${GITHUB_REF_NAME:-main}; commit it by hand."
    exit 1
  fi
done

echo "::error::push rejected after 3 attempts"
exit 1
