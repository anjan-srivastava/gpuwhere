#!/usr/bin/env bash
# Deploy dist/ to Cloudflare Pages with a locally downloaded wrangler.
#
#   make deploy                    # build + upload (the normal path)
#   ./scripts/deploy_cloudflare.sh # upload an existing dist/
#
# Options:
#   --project NAME   Pages project (default: $CF_PROJECT or gpuwhere)
#   --branch NAME    production branch (default: $CF_BRANCH or main)
#   --check          verify the artifact and authentication, do not upload
#
# Authentication, one of:
#   export CLOUDFLARE_API_TOKEN=...   # Pages:Edit + Account:Read, recommended for CI
#   .tools/npm/node_modules/.bin/wrangler login
#
# The CLI is not installed globally: it is downloaded into .tools/npm/ on first use.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="${CF_PROJECT:-gpuwhere}"
BRANCH="${CF_BRANCH:-main}"
WRANGLER="${WRANGLER:-$ROOT/.tools/npm/node_modules/.bin/wrangler}"
WRANGLER_SPEC="${WRANGLER_SPEC:-wrangler@4}"
CHECK_ONLY=0

if [[ -n "${CF_ACCOUNT_ID:-}" ]]; then
  export CLOUDFLARE_ACCOUNT_ID="$CF_ACCOUNT_ID"
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) PROJECT="$2"; shift 2 ;;
    --branch)  BRANCH="$2";  shift 2 ;;
    --check)   CHECK_ONLY=1; shift ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 64 ;;
  esac
done

log() { printf '==> %s\n' "$*"; }
die() { printf 'error: %s\n' "$*" >&2; exit 1; }

# 1. Cloudflare CLI -----------------------------------------------------------
if [[ ! -x "$WRANGLER" ]]; then
  command -v node >/dev/null 2>&1 || die "node is required to install wrangler (brew install node)"
  log "downloading Cloudflare CLI ($WRANGLER_SPEC) into .tools/npm"
  mkdir -p "$ROOT/.tools/npm"
  npm install --prefix "$ROOT/.tools/npm" --no-audit --no-fund --no-save "$WRANGLER_SPEC" >/dev/null
fi
log "wrangler $("$WRANGLER" --version 2>/dev/null | tail -1)"

# 2. Artifact -----------------------------------------------------------------
[[ -f "$ROOT/dist/index.html" ]] || die "dist/index.html is missing — run: make build"
[[ -f "$ROOT/dist/v1/catalog.json" ]] || die "dist/v1/catalog.json is missing — run: make build"
log "artifact: $(du -sh "$ROOT/dist" | cut -f1) in dist/"

# 3. Authentication -----------------------------------------------------------
auth_output=""
if ! auth_output="$("$WRANGLER" whoami 2>&1)" \
   || grep -qiE 'not authenticated|not logged in|no account' <<<"$auth_output"; then
  cat >&2 <<'EOF'
error: wrangler is not authenticated.

Pick one:
  export CLOUDFLARE_API_TOKEN=...   # token with Pages:Edit + Account:Read
  .tools/npm/node_modules/.bin/wrangler login

Then re-run: make deploy
EOF
  exit 2
fi

if [[ $CHECK_ONLY -eq 1 ]]; then
  log "check passed (artifact present, wrangler authenticated); not uploading"
  exit 0
fi

# 4. Pages project ------------------------------------------------------------
cd "$ROOT"
log "ensuring Pages project '$PROJECT' (branch '$BRANCH')"
if ! "$WRANGLER" pages project list 2>/dev/null | grep -qE "[[:space:]]${PROJECT}[[:space:]]"; then
  # --force keeps the classic Pages path instead of delegating to Workers static assets,
  # which is what the project (with `_worker.js` and `_headers`) needs.
  "$WRANGLER" pages project create "$PROJECT" --production-branch "$BRANCH" --force \
    || die "could not create the Pages project"
else
  log "project '$PROJECT' already exists"
fi

# 5. Upload -------------------------------------------------------------------
log "uploading dist/ to Cloudflare Pages"
if ! deploy_output="$("$WRANGLER" pages deploy "$ROOT/dist" \
      --project-name "$PROJECT" \
      --branch "$BRANCH" \
      --commit-dirty=true 2>&1)"; then
  printf '%s\n' "$deploy_output" >&2
  die "deployment failed"
fi
printf '%s\n' "$deploy_output"

url="$(grep -Eo 'https://[a-z0-9.-]+\.pages\.dev' <<<"$deploy_output" | tail -1 || true)"
if [[ -n "$url" ]]; then
  log "live at $url"
  log "canonical host: https://${PROJECT}.pages.dev"
fi
log "set the API secret once: $WRANGLER pages secret put API_KEYS --project-name $PROJECT"
log "traffic report: make analytics (needs CF_ACCOUNT_ID + CF_ANALYTICS_TOKEN)"
