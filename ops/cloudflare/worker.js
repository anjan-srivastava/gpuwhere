/**
 * Cloudflare Worker cron -> GitHub Actions dispatch.
 *
 * Cloudflare's free tier runs Cron Triggers on Workers, but a Worker cannot run the
 * Python scrapers. So the Worker is just a clock with a token: on schedule it asks
 * GitHub Actions to run the refresh workflow, which does the scraping and commits.
 *
 * wrangler.toml:
 *   name = "gpu-catalog-scheduler"
 *   main = "worker.js"
 *   compatibility_date = "2026-01-01"
 *   [triggers]
 *   crons = ["5 * * * *", "15 4 * * *"]
 *
 * Secrets (wrangler secret put ...):
 *   GITHUB_TOKEN  fine-grained PAT, Actions: write on the repository only
 *   GITHUB_REPO   "owner/repo"
 *   HOURLY_WORKFLOW      default "refresh-availability.yml"
 *   DAILY_WORKFLOW       default "refresh-pricing.yml"
 *   GITHUB_REF           default "main"
 */
export default {
  async scheduled(controller, env, ctx) {
    const cron = controller.cron;
    // The hourly cron runs every hour; the daily one runs once a day.
    const workflow = cron === "15 4 * * *"
      ? (env.DAILY_WORKFLOW || "refresh-pricing.yml")
      : (env.HOURLY_WORKFLOW || "refresh-availability.yml");

    const res = await fetch(
      `https://api.github.com/repos/${env.GITHUB_REPO}/actions/workflows/${workflow}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "User-Agent": "gpu-catalog-scheduler",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ ref: env.GITHUB_REF || "main" }),
      },
    );
    if (!res.ok && res.status !== 204) {
      console.error(`dispatch ${workflow} failed: ${res.status} ${await res.text()}`);
    }
  },

  // Manual trigger for debugging: GET /?workflow=refresh-pricing.yml
  async fetch(request, env) {
    const url = new URL(request.url);
    const workflow = url.searchParams.get("workflow");
    if (!workflow) return new Response("pass ?workflow=<file.yml>\n", { status: 400 });
    const res = await fetch(
      `https://api.github.com/repos/${env.GITHUB_REPO}/actions/workflows/${workflow}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "User-Agent": "gpu-catalog-scheduler",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ ref: env.GITHUB_REF || "main" }),
      },
    );
    return new Response(`dispatch ${workflow}: ${res.status}\n`, { status: 200 });
  },
};
