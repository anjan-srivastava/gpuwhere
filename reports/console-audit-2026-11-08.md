# Console audit — can you actually launch a GPU?

Date: 2026-11-08 · Method: signed-in walkthrough of each console (browser), driven to the
final purchase/launch action. No paid resource was created; where a launch was blocked the
blocker is recorded.

Scope: the six Indian providers whose catalogue entry is `provisioning: console`
(Cyfuture AI, Leapswitch, Neysa, NxtGen, Tata Communications, Yotta Shakti).

## Verdict

| Provider | Self-serve signup | GPU catalogue in console | Live stock | Reaches launch | Blocked at | Verdict |
|---|---|---|---|---|---|---|
| **Cyfuture AI** | Yes (name/email/mobile/password) | Yes — 8 GPU types, 1x–8x, hourly/monthly/6m/yearly | **Yes** | **Yes** (4-step wizard to SUBMIT) | Prepaid balance: needs ₹1,529 for 24 h of the cheapest in-stock V100; trial credit ₹100 | **Self-serve, gated by stock + prepaid day** |
| **Yotta Shakti** | Keycloak login works | Portal present (VM, Bare Metal, Subscribe) — **all catalogues empty** | n/a | No | "No Virtual Machines Profiles available"; "No Subscribe Profiles available" | **Account works, no entitlements — needs enablement** |
| **Leapswitch** | WHMCS account | Store has dedicated servers, hosting, domains — **no GPU product** | n/a | No | GPU "Buy Now" lands on portal with no GPU product; L4 only via CloudPe (other brand) | **Sales / manual order** |
| **Tata Communications (Vayu)** | Business/freemium signup (email OTP) | Quote builder: location → CPU series A–T | n/a | No | No GPU SKUs in the Vayu configuration flow; GPU page routes to "Schedule a conversation" | **Quote / sales** |
| **NxtGen SpeedCloud** | Company-details signup, but login works | Wizard exists (Create AI instance, 5 steps) | n/a | No | **0 virtual data centers and no way to create one**; 0 subscriptions → "Add GPU" stays disabled | **Console works, account unprovisioned** |
| **Neysa** | No console host resolves (`console.neysa.ai` NXDOMAIN) | n/a | n/a | No | Pricing page + "Contact Sales" only | **Sales** |

## NxtGen SpeedCloud — wizard exists, account is empty

The login is real and the flow is the most modern of the six: **Create AI instance → Configure
AI instance → AI platforms → AI services → Managed services → Review and deploy**, with a
live charges panel (₹0), public-IP pricing (₹560/IP) and SSH-key/security-group setup.

It cannot start, because the account has no project to run in:

- **Virtual Data Centers (0)** — the VDC list is empty and the page offers **no create action**;
  the project picker in the wizard opens an empty panel.
- **Subscriptions** — none of the four tabs (instance / AI platform / OEM / project managed
  services) has anything.
- With no project selected, **"Add GPU" is disabled**, so no GPU catalogue is ever shown.

So NxtGen behaves like Yotta: portal is functional, but the account is not provisioned.
Getting a VDC appears to be an onboarding/sales step, not something the console lets you do.

## Cyfuture AI — the only one that gets to the launch button

Flow: Dashboard → GPUaaS → Get Started → 4 steps (OS Details → GPU Resource → GPU Details →
Manage Node). Step 2 lists GPU types and per-shape plans with hourly/monthly/6-month/yearly
rates; step 4 is a single SUBMIT.

Stock at audit time (console labels):

| GPU type | 1x hourly | Stock |
|---|---|---|
| V100 | ₹54 | **available** |
| Gaudi2 | ₹101 | out of stock |
| L40S | ₹124 | out of stock |
| A100 | ₹198 | out of stock |
| MI300X | ₹274 | out of stock |
| MI325X | ₹298 | out of stock |
| H100 SXM | ₹299 | out of stock |
| H100 (SXM5) | ₹329 | out of stock |

Submitting a V100 1x hourly (₹1,296 + 18 % GST = ₹1,529.28 for 24 h) redirects to Billing
with "Apply Coupon Success"; no deployment record is created. So the gate is **money, not
sales**: an account with ≥ ₹1,530 can provision the V100 immediately.

Two catalogue-relevant observations:

1. **Prices match the catalogue exactly** — H100 $3.50 vs ₹329/h, A100 $2.11 vs ₹198,
   L40S $1.32 vs ₹124, V100 $0.57 vs ₹54, MI300X $2.92 vs ₹274, MI325X $3.17 vs ₹298,
   Gaudi2 $1.08 vs ₹101. The scraped rate card is trustworthy.
2. **The console offers fewer GPU types than the catalogue**: no B200/B300, no H200, no
   RTX PRO 6000 in the GPU dropdown, although the catalogue carries B300 (`quote_only`),
   H200 (`quote_only`) and RTX PRO 6000 at $2.73. Those are not self-serve today.
3. **"API Key" on the dashboard is for model inference (AIaaS), not VM provisioning.**
   The API Gateway product is API management, not a provisioning API — `provisioning:
   console` is correct for Cyfuture.

## What this changes in the catalogue

- **Cyfuture stock is now directly observed** (one console snapshot, 8 GPU types). It is a
  legitimate `availability` observation with `observed_via: "console"`, but it is a single
  point in time — record it with `confidence: medium` and do not infer capacity from it.
- **Cyfuture B300/H200/RTX PRO 6000** are catalogue packages that the console cannot launch
  today. Keep them (they are published rates) but a `note` that they are not in the
  self-serve console would stop the catalogue over-promising.
- **Yotta** looks like a working console with an unprovisioned account. That is a
  sales-onboarding step, not a UI issue — worth a line in its `api.notes`.
- **Leapswitch / Tata / NxtGen / Neysa** confirm `console` → effectively `sales` for GPUs.
  If the catalogue wants to be strict, `provisioning: sales` with `api.notes` would describe
  reality better than `console` for these four.

## Follow-ups

1. Record the Cyfuture stock snapshot as an availability observation (manual, console).
2. Add `api.notes` on the four sales-gated providers.
3. Re-run the Cyfuture stock check weekly until an API or account with balance lets it be
   automated; only V100 in stock makes the rate card largely theoretical.
5. Ask NxtGen what creates a VDC (self-serve missing vs sales) — until then its catalogue
   entry should say the console exists but new accounts cannot provision.
4. If Yotta's account can be enabled by sales, repeat the walkthrough — the portal is the
   most complete of the six (VM, bare metal, clusters, AI Lab, storage).
