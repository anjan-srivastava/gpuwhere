# Pricing refresh 2026-11-15 21:50 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=1, changed=169, unchanged=269, stale=11, retired=0, failed=0

## e2e-networks

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {3: 7.27} → {3: 7.25}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: spot 0.94 → 0.93  [REVIEW: pricing]; committed {3: 4.93} → {3: 4.91}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: spot 0.75 → 0.74  [REVIEW: pricing]; committed {3: 3.7} → {3: 3.69}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {3: 2.32} → {3: 2.31}  [REVIEW: pricing]
- STALE `skus/e2e-networks/IN-DEL/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/e2e-networks/IN-DEL/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- Listed but not a SKU: Monthly/annual GPU plans: 'Contact Sales' (feed termPricing).

## jarvislabs

- STALE `skus/jarvislabs/EU1/H100/1x/standard.json` — no current source covers H100 1x; left for human review
- STALE `skus/jarvislabs/EU1/H100/2x/standard.json` — no current source covers H100 2x; left for human review
- STALE `skus/jarvislabs/EU1/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/jarvislabs/EU1/H100/8x/standard.json` — no current source covers H100 8x; left for human review
- STALE `skus/jarvislabs/EU1/H200/1x/standard.json` — no current source covers H200 1x; left for human review
- STALE `skus/jarvislabs/EU1/H200/2x/standard.json` — no current source covers H200 2x; left for human review
- STALE `skus/jarvislabs/EU1/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- STALE `skus/jarvislabs/EU1/H200/8x/standard.json` — no current source covers H200 8x; left for human review

## acecloud

- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-16-128`: on_demand 4.52 → 3.61  [REVIEW: pricing]; committed {1: 3.61, 6: 3.43, 12: 3.25} → {6: 3.43, 12: 3.25}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-24-192`: on_demand 4.87 → 3.9  [REVIEW: pricing]; committed {1: 3.9, 6: 3.7, 12: 3.51} → {6: 3.7, 12: 3.51}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-28-282`: on_demand 5.37 → 4.3  [REVIEW: pricing]; committed {1: 4.3, 6: 4.08, 12: 3.87} → {6: 4.08, 12: 3.87}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/H200/2x/n-h200-48-384`: on_demand 4.88 → 3.9  [REVIEW: pricing]; committed {1: 3.9, 6: 3.7, 12: 3.51} → {6: 3.7, 12: 3.51}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/H200/2x/n-h200-56-564`: on_demand 5.37 → 4.3  [REVIEW: pricing]; committed {1: 4.3, 6: 4.08, 12: 3.87} → {6: 4.08, 12: 3.87}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/H200/4x/n-h200-96-768`: on_demand 4.88 → 3.9  [REVIEW: pricing]; committed {1: 3.9, 6: 3.7, 12: 3.51} → {6: 3.7, 12: 3.51}  [REVIEW: pricing]; billing_model hourly → monthly
- CHANGED `acecloud/IN-NOI/L40S/1x/n-l40s-64`: on_demand 1.5 → 1.87  [REVIEW: pricing]; committed {6: 1.42, 12: 1.35} → {1: 1.5, 6: 1.42, 12: 1.35}  [REVIEW: pricing]; billing_model monthly → hourly
- CHANGED `acecloud/IN-NOI/L40S/1x/n-l40s-128`: on_demand 1.82 → 2.27  [REVIEW: pricing]; committed {6: 1.73, 12: 1.64} → {1: 1.82, 6: 1.73, 12: 1.64}  [REVIEW: pricing]; billing_model monthly → hourly
- CHANGED `acecloud/IN-NOI/L40S/2x/n-l40s-192`: on_demand 1.65 → 2.06  [REVIEW: pricing]; committed {6: 1.57, 12: 1.49} → {1: 1.65, 6: 1.57, 12: 1.49}  [REVIEW: pricing]; billing_model monthly → hourly
- CHANGED `acecloud/IN-NOI/L40S/2x/n-l40s-256`: on_demand 1.82 → 2.27  [REVIEW: pricing]; committed {6: 1.73, 12: 1.64} → {1: 1.82, 6: 1.73, 12: 1.64}  [REVIEW: pricing]; billing_model monthly → hourly
- CHANGED `acecloud/IN-NOI/L40S/4x/n-l40s-512`: on_demand 1.82 → 2.27  [REVIEW: pricing]; committed {6: 1.73, 12: 1.64} → {1: 1.82, 6: 1.73, 12: 1.64}  [REVIEW: pricing]; billing_model monthly → hourly
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- no changes

## nxtgen

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.03 → 3.02  [REVIEW: pricing]; committed {1: 2.43, 6: 2.43, 12: 1.94} → {1: 2.42, 6: 2.42, 12: 1.93}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H200/8x/standard`: on_demand 3.03 → 3.02  [REVIEW: pricing]; committed {1: 2.42, 6: 2.42, 12: 1.94} → {1: 2.42, 6: 2.42, 12: 1.93}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.63 → 2.62  [REVIEW: pricing]; committed {1: 2.11, 6: 2.11, 12: 1.68} → {1: 2.1, 6: 2.1, 12: 1.68}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/L40S/1x/standard`: on_demand 1.57 → 1.56  [REVIEW: pricing]; committed {1: 1.26, 6: 1.26, 12: 1.0} → {1: 1.25, 6: 1.25, 12: 1.0}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.67 → 2.66  [REVIEW: pricing]; committed {1: 2.14, 6: 2.14, 12: 1.71} → {1: 2.13, 6: 2.13, 12: 1.71}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/8x/standard`: on_demand 2.68 → 2.67  [REVIEW: pricing]; committed {1: 2.14, 6: 2.14, 12: 1.71} → {1: 2.13, 6: 2.13, 12: 1.71}  [REVIEW: pricing]

## leapswitch

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.31 → 4.29  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: on_demand 1.95 → 1.94  [REVIEW: pricing]

## cyfuture-ai

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `cyfuture-ai/IN/B300/1x/standard`: committed {1: 6.07, 6: 5.81, 12: 5.57} → {1: 6.05, 6: 5.79, 12: 5.55}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/2x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 6.05, 6: 5.8, 12: 5.54}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/4x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 6.05, 6: 5.8, 12: 5.54}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/8x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 6.05, 6: 5.8, 12: 5.54}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: on_demand 2.73 → 2.72  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.57, 6: 2.42, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: on_demand 2.73 → 2.72  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.57, 6: 2.42, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: on_demand 2.73 → 2.72  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.57, 6: 2.42, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: on_demand 2.73 → 2.72  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.57, 6: 2.42, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: on_demand 1.28 → 1.27  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: on_demand 2.92 → 2.91  [REVIEW: pricing]; committed {1: 2.33, 6: 2.1, 12: 1.75} → {1: 2.32, 6: 2.09, 12: 1.74}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: on_demand 2.89 → 2.88  [REVIEW: pricing]; committed {1: 2.28, 6: 2.03, 12: 1.68} → {1: 2.28, 6: 2.03, 12: 1.67}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: on_demand 2.86 → 2.85  [REVIEW: pricing]; committed {1: 2.26, 6: 2.01, 12: 1.66} → {1: 2.25, 6: 2.01, 12: 1.65}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: on_demand 2.83 → 2.82  [REVIEW: pricing]; committed {1: 2.24, 6: 1.99, 12: 1.64} → {1: 2.23, 6: 1.98, 12: 1.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.5 → 3.49  [REVIEW: pricing]; committed {1: 3.15, 6: 2.8, 12: 2.33} → {1: 3.14, 6: 2.79, 12: 2.32}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: on_demand 3.47 → 3.45  [REVIEW: pricing]; committed {1: 3.09, 6: 2.72, 12: 2.24} → {1: 3.08, 6: 2.71, 12: 2.23}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: on_demand 3.43 → 3.42  [REVIEW: pricing]; committed {1: 3.06, 6: 2.69, 12: 2.21} → {1: 3.05, 6: 2.68, 12: 2.21}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: on_demand 3.4 → 3.38  [REVIEW: pricing]; committed {1: 3.03, 6: 2.66, 12: 2.19} → {1: 3.01, 6: 2.65, 12: 2.18}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: committed {1: 0.51, 6: 0.46, 12: 0.42} → {1: 0.51, 6: 0.46, 12: 0.41}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/2x/standard`: committed {1: 0.51, 6: 0.44, 12: 0.39} → {1: 0.5, 6: 0.44, 12: 0.39}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/8x/standard`: on_demand 0.56 → 0.55  [REVIEW: pricing]; committed {1: 0.5, 6: 0.43, 12: 0.39} → {1: 0.49, 6: 0.43, 12: 0.38}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: on_demand 2.11 → 2.1  [REVIEW: pricing]; committed {1: 2.09, 6: 2.07, 12: 1.99} → {1: 2.08, 6: 2.06, 12: 1.98}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: on_demand 2.09 → 2.08  [REVIEW: pricing]; committed {1: 2.04, 6: 2.0, 12: 1.91} → {1: 2.04, 6: 1.99, 12: 1.9}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: on_demand 2.07 → 2.06  [REVIEW: pricing]; committed {1: 2.02, 6: 1.98, 12: 1.89} → {1: 2.02, 6: 1.97, 12: 1.89}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: committed {1: 2.0, 6: 1.96, 12: 1.87} → {1: 1.99, 6: 1.95, 12: 1.86}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: on_demand 1.08 → 1.07  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: committed {1: 0.85, 6: 0.71, 12: 0.61} → {1: 0.85, 6: 0.71, 12: 0.6}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/4x/standard`: on_demand 1.06 → 1.05  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: on_demand 3.17 → 3.16  [REVIEW: pricing]; committed {1: 2.31, 6: 1.93, 12: 1.6} → {1: 2.3, 6: 1.92, 12: 1.59}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: on_demand 3.14 → 3.13  [REVIEW: pricing]; committed {1: 2.26, 6: 1.86, 12: 1.54} → {1: 2.25, 6: 1.86, 12: 1.53}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: on_demand 3.11 → 3.1  [REVIEW: pricing]; committed {1: 2.24, 6: 1.84, 12: 1.52} → {1: 2.23, 6: 1.84, 12: 1.52}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: on_demand 3.08 → 3.07  [REVIEW: pricing]; committed {1: 2.22, 6: 1.83, 12: 1.51} → {1: 2.21, 6: 1.82, 12: 1.5}  [REVIEW: pricing]
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review

## tata-communications

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: on_demand 5.2 → 5.18  [REVIEW: pricing]; committed {3: 5.05, 6: 4.48, 12: 3.98, 36: 3.77, 48: 3.59} → {3: 5.03, 6: 4.47, 12: 3.97, 36: 3.76, 48: 3.57}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: on_demand 5.65 → 5.63  [REVIEW: pricing]; committed {3: 5.49, 6: 4.88, 12: 4.33, 36: 4.11, 48: 3.9} → {3: 5.48, 6: 4.86, 12: 4.32, 36: 4.09, 48: 3.89}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: on_demand 5.49 → 5.47  [REVIEW: pricing]; committed {3: 5.33, 6: 4.73, 12: 4.21, 36: 3.98, 48: 3.79} → {3: 5.31, 6: 4.72, 12: 4.19, 36: 3.97, 48: 3.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: on_demand 3.12 → 3.11  [REVIEW: pricing]; committed {3: 3.04, 6: 2.69, 12: 2.4, 36: 2.27, 48: 2.16} → {3: 3.03, 6: 2.68, 12: 2.39, 36: 2.26, 48: 2.15}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: on_demand 4.28 → 4.27  [REVIEW: pricing]; committed {3: 4.16, 6: 3.69, 12: 3.28, 36: 3.11, 48: 2.96} → {3: 4.15, 6: 3.68, 12: 3.27, 36: 3.1, 48: 2.95}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: on_demand 4.64 → 4.63  [REVIEW: pricing]; committed {3: 4.51, 6: 4.0, 12: 3.56, 36: 3.38, 48: 3.2} → {3: 4.5, 6: 3.99, 12: 3.54, 36: 3.36, 48: 3.19}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: on_demand 4.8 → 4.79  [REVIEW: pricing]; committed {3: 4.66, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.31} → {3: 4.65, 6: 4.13, 12: 3.67, 36: 3.48, 48: 3.3}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: on_demand 4.29 → 4.27  [REVIEW: pricing]; committed {3: 4.16, 6: 3.69, 12: 3.28, 36: 3.11, 48: 2.95} → {3: 4.15, 6: 3.68, 12: 3.27, 36: 3.1, 48: 2.94}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: on_demand 4.64 → 4.63  [REVIEW: pricing]; committed {3: 4.51, 6: 4.0, 12: 3.56, 36: 3.38, 48: 3.2} → {3: 4.5, 6: 3.99, 12: 3.55, 36: 3.36, 48: 3.19}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: on_demand 4.8 → 4.79  [REVIEW: pricing]; committed {3: 4.67, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.32} → {3: 4.65, 6: 4.13, 12: 3.67, 36: 3.48, 48: 3.31}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: on_demand 5.06 → 5.04  [REVIEW: pricing]; committed {3: 4.92, 6: 4.37, 12: 3.88, 36: 3.67, 48: 3.49} → {3: 4.9, 6: 4.35, 12: 3.87, 36: 3.66, 48: 3.48}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: on_demand 5.78 → 5.76  [REVIEW: pricing]; committed {3: 5.62, 6: 4.98, 12: 4.43, 36: 4.2, 48: 3.99} → {3: 5.6, 6: 4.97, 12: 4.41, 36: 4.19, 48: 3.97}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: on_demand 4.8 → 4.79  [REVIEW: pricing]; committed {3: 4.67, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.31} → {3: 4.65, 6: 4.13, 12: 3.67, 36: 3.48, 48: 3.3}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: on_demand 2.13 → 2.12  [REVIEW: pricing]; committed {3: 2.07, 6: 1.84, 12: 1.63, 36: 1.54, 48: 1.47} → {3: 2.06, 6: 1.84, 12: 1.62, 36: 1.54, 48: 1.46}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: on_demand 2.32 → 2.31  [REVIEW: pricing]; committed {3: 2.26, 6: 2.0, 12: 1.78, 36: 1.68, 48: 1.6} → {3: 2.25, 6: 1.99, 12: 1.77, 36: 1.68, 48: 1.59}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: on_demand 2.41 → 2.4  [REVIEW: pricing]; committed {3: 2.33, 6: 2.08, 12: 1.84, 36: 1.75, 48: 1.66} → {3: 2.32, 6: 2.07, 12: 1.84, 36: 1.74, 48: 1.66}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: on_demand 2.48 → 2.47  [REVIEW: pricing]; committed {3: 2.42, 6: 2.14, 12: 1.91, 36: 1.81, 48: 1.71} → {3: 2.41, 6: 2.13, 12: 1.9, 36: 1.8, 48: 1.71}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: on_demand 2.13 → 2.12  [REVIEW: pricing]; committed {3: 2.07, 6: 1.84, 12: 1.63, 36: 1.55, 48: 1.47} → {3: 2.06, 6: 1.83, 12: 1.63, 36: 1.54, 48: 1.46}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: on_demand 2.32 → 2.31  [REVIEW: pricing]; committed {3: 2.26, 6: 2.0, 12: 1.78, 36: 1.69, 48: 1.6} → {3: 2.25, 6: 1.99, 12: 1.77, 36: 1.68, 48: 1.6}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: on_demand 2.49 → 2.48  [REVIEW: pricing]; committed {3: 2.42, 6: 2.15, 12: 1.91, 36: 1.8, 48: 1.71} → {3: 2.41, 6: 2.14, 12: 1.9, 36: 1.8, 48: 1.71}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: on_demand 0.96 → 0.95  [REVIEW: pricing]; committed {3: 0.93, 6: 0.83, 12: 0.73, 36: 0.69, 48: 0.66} → {3: 0.92, 6: 0.83, 12: 0.73, 36: 0.69, 48: 0.66}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: committed {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.74, 48: 0.71}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: on_demand 1.1 → 1.09  [REVIEW: pricing]; committed {3: 1.06, 6: 0.95, 12: 0.84, 36: 0.8, 48: 0.76} → {3: 1.06, 6: 0.94, 12: 0.84, 36: 0.8, 48: 0.75}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: on_demand 1.25 → 1.24  [REVIEW: pricing]; committed {3: 1.21, 6: 1.08, 12: 0.96, 36: 0.91, 48: 0.86} → {3: 1.21, 6: 1.07, 12: 0.95, 36: 0.9, 48: 0.86}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: committed {3: 1.01, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: on_demand 1.1 → 1.09  [REVIEW: pricing]; committed {3: 1.06, 6: 0.95, 12: 0.84, 36: 0.8, 48: 0.76} → {3: 1.06, 6: 0.94, 12: 0.84, 36: 0.8, 48: 0.75}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: committed {3: 1.21, 6: 1.08, 12: 0.96, 36: 0.91, 48: 0.86} → {3: 1.21, 6: 1.08, 12: 0.95, 36: 0.91, 48: 0.86}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: on_demand 1.03 → 1.02  [REVIEW: pricing]; committed {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 0.99, 6: 0.88, 12: 0.79, 36: 0.74, 48: 0.71}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu`: committed {3: 1.11, 6: 0.98, 12: 0.88, 36: 0.83, 48: 0.79} → {3: 1.11, 6: 0.98, 12: 0.87, 36: 0.82, 48: 0.79}  [REVIEW: pricing]

## yotta-shakti

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 4.56 → 4.54  [REVIEW: pricing]; committed {6: 4.05, 12: 3.75, 24: 3.34} → {6: 4.03, 12: 3.74, 24: 3.33}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: committed {6: 2.13, 12: 1.93, 24: 1.72} → {6: 2.12, 12: 1.92, 24: 1.72}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 5.04 → 5.02  [REVIEW: pricing]; committed {6: 5.04, 12: 5.04, 24: 5.04, 36: 4.02, 48: 3.36, 60: 2.97} → {6: 5.02, 12: 5.02, 24: 5.02, 36: 4.01, 48: 3.35, 60: 2.96}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: committed {12: 11.24, 24: 9.2, 36: 7.15, 48: 5.11, 60: 4.05} → {12: 11.21, 24: 9.17, 36: 7.13, 48: 5.09, 60: 4.03}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 3.79 → 6.32  [REVIEW: pricing]; committed {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79} → {1: 5.71, 3: 5.54, 6: 5.42, 12: 5.25}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 3.79 → 6.23  [REVIEW: pricing]; committed {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79} → {1: 5.62, 3: 5.45, 6: 5.34, 12: 5.17}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 3.79 → 6.21  [REVIEW: pricing]; committed {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79} → {1: 5.59, 3: 5.42, 6: 5.31, 12: 5.14}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: on_demand 1.46 → 3.2  [REVIEW: pricing]; committed {1: 1.17, 3: 1.13, 6: 1.11, 12: 1.08} → {1: 2.59, 3: 2.51, 6: 2.46, 12: 2.38}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: on_demand 1.46 → 3.15  [REVIEW: pricing]; committed {1: 1.14, 3: 1.11, 6: 1.08, 12: 1.05} → {1: 2.53, 3: 2.45, 6: 2.4, 12: 2.33}  [REVIEW: pricing]

## krutrim-cloud

- no changes
- Listed but not a SKU: Spliced (fractional) GPUs: not a whole-GPU shape

## microsoft-azure

- no changes
- WARNING: unmapped Azure GPU size Standard_ND128isr_NDR_GB200_v6 in southindia; add it to SKUS
- Listed but not a SKU: NVadsA10v5_Type1 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV12ads_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV18ads_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36adms_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36ads_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV6ads_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV72ads_A10_v5 (centralindia): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: NVadsA10v5_Type1 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV12ads_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV18ads_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36adms_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36ads_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV6ads_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV72ads_A10_v5 (jioindiawest): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: NVadsA10v5_Type1 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV12ads_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV18ads_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36adms_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV36ads_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV6ads_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled
- Listed but not a SKU: Standard_NV72ads_A10_v5 (jioindiacentral): A10 size (fractional or no A10 accelerator spec), not modelled

## aws

- no changes
- WARNING: unmapped AWS accelerated type g7.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## ovhcloud

- FX: USD/INR 94.2431 (2026-11-13, ECB reference rate)
- CHANGED `ovhcloud/EU-FR/A100/1x/a100-180`: on_demand 3.07 → 3.04  [REVIEW: pricing]; committed {1: 1.68} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/2x/a100-360`: on_demand 3.07 → 3.04  [REVIEW: pricing]; committed {1: 1.68} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/4x/a100-720`: on_demand 3.07 → 3.04  [REVIEW: pricing]; committed {1: 1.68} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/4x/h100-1520`: on_demand 3.13 → 3.09  [REVIEW: pricing]; committed {1: 2.97} → {1: 2.94}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/1x/h100-380`: on_demand 3.13 → 3.09  [REVIEW: pricing]; committed {1: 2.97} → {1: 2.94}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/2x/h100-760`: on_demand 3.13 → 3.09  [REVIEW: pricing]; committed {1: 2.97} → {1: 2.94}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920`: on_demand 5.86 → 5.8  [REVIEW: pricing]; committed {1: 5.86} → {1: 5.8}  [REVIEW: pricing]
- NEW `ovhcloud/EU-FR/H200/8x/h200-1920-eph` — $5.8/GPU-hr, 224 vCPU, 1920 GB RAM
- CHANGED `ovhcloud/EU-FR/L4/2x/l4-180`: on_demand 0.84 → 0.83  [REVIEW: pricing]; committed {1: 0.83} → {1: 0.82}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/2x/win-l4-180`: on_demand 1.71 → 1.69  [REVIEW: pricing]; committed {1: 1.71} → {1: 1.69}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/l4-360`: on_demand 0.84 → 0.83  [REVIEW: pricing]; committed {1: 0.83} → {1: 0.82}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/win-l4-360`: on_demand 1.71 → 1.69  [REVIEW: pricing]; committed {1: 1.71} → {1: 1.69}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/l4-90`: on_demand 0.84 → 0.83  [REVIEW: pricing]; committed {1: 0.83} → {1: 0.82}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/win-l4-90`: on_demand 1.69 → 1.67  [REVIEW: pricing]; committed {1: 1.69} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/2x/l40s-180`: on_demand 1.56 → 1.55  [REVIEW: pricing]; committed {1: 1.54} → {1: 1.53}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/4x/l40s-360`: on_demand 1.56 → 1.55  [REVIEW: pricing]; committed {1: 1.54} → {1: 1.53}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/1x/l40s-90`: on_demand 1.56 → 1.55  [REVIEW: pricing]; committed {1: 1.54} → {1: 1.53}  [REVIEW: pricing]
- Listed but not a SKU: a10-180: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-45: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-90: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: b300-1990: B300 HGX has no accelerator spec in the catalogue
- Listed but not a SKU: g1-15: GEFORCE GTX 1060 has no accelerator spec in the catalogue
- Listed but not a SKU: g1-30: GEFORCE GTX 1060 has no accelerator spec in the catalogue
- Listed but not a SKU: g2-15: GEFORCE GTX 1070 has no accelerator spec in the catalogue
- Listed but not a SKU: g2-30: GEFORCE GTX 1070 has no accelerator spec in the catalogue
- Listed but not a SKU: g3-120: GEFORCE GTX 1080 TI has no accelerator spec in the catalogue
- Listed but not a SKU: g3-30: GEFORCE GTX 1080 TI has no accelerator spec in the catalogue
- Listed but not a SKU: rtx5000-28: QUADRO-RTX5000 has no accelerator spec in the catalogue
- Listed but not a SKU: rtx5000-56: QUADRO-RTX5000 has no accelerator spec in the catalogue
- Listed but not a SKU: rtx5000-84: QUADRO-RTX5000 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-180: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-45: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-90: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-le-180: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-le-45: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t1-le-90: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: t2-180: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: t2-45: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: t2-90: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: t2-le-180: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: t2-le-45: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: t2-le-90: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: win-g1-15: GEFORCE GTX 1060 has no accelerator spec in the catalogue
- Listed but not a SKU: win-g1-30: GEFORCE GTX 1060 has no accelerator spec in the catalogue
- Listed but not a SKU: win-g2-15: GEFORCE GTX 1070 has no accelerator spec in the catalogue
- Listed but not a SKU: win-g2-30: GEFORCE GTX 1070 has no accelerator spec in the catalogue
- Listed but not a SKU: win-g3-120: GEFORCE GTX 1080 TI has no accelerator spec in the catalogue
- Listed but not a SKU: win-g3-30: GEFORCE GTX 1080 TI has no accelerator spec in the catalogue
- Listed but not a SKU: win-t1-180: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: win-t1-45: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: win-t1-90: TESLA V100 has no accelerator spec in the catalogue
- Listed but not a SKU: win-t2-180: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: win-t2-45: TESLA V100S has no accelerator spec in the catalogue
- Listed but not a SKU: win-t2-90: TESLA V100S has no accelerator spec in the catalogue

## nebius

- CHANGED `nebius/EU-WEST2/B300/1x/hgx-b300-1x`: spot 5.2 → 1.4  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST2/B300/8x/hgx-b300-8x`: spot 41.6 → 11.2  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/1x/hgx-b300-1x`: spot 3.1 → 3.5  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/8x/hgx-b300-8x`: spot 24.8 → 28.0  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/1x/hgx-b300-1x`: spot 4.0 → 4.32  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/8x/hgx-b300-8x`: spot 32.0 → 34.56  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/1x/hgx-b200-1x`: spot 2.75 → 2.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/8x/hgx-b200-8x`: spot 22.0 → 22.32  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/1x/hgx-b200-1x`: spot 2.5 → 2.7  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/8x/hgx-b200-8x`: spot 20.0 → 21.6  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/1x/hgx-h200-1x`: spot 1.4 → 2.48  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/8x/hgx-h200-8x`: spot 11.2 → 19.84  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/1x/hgx-h200-1x`: spot 2.89 → 1.58  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/8x/hgx-h200-8x`: spot 23.12 → 12.64  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/1x/hgx-h200-1x`: spot 1.5 → 1.88  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/8x/hgx-h200-8x`: spot 12.0 → 15.04  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/1x/hgx-h100-1x`: spot 0.79 → 1.47  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/8x/hgx-h100-8x`: spot 6.32 → 11.76  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 0.82 → 1.38  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 6.53 → 11.04  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 0.79 → 1.08  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 6.32 → 8.64  [REVIEW: pricing]
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## verda

- CHANGED `verda/EU-FI/B300/1x/30cpu-255gb-268gb`: on_demand 11.69 → 12.41  [REVIEW: pricing]; spot 5.84 → 6.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/2x/60cpu-510gb-536gb`: on_demand 11.69 → 12.41  [REVIEW: pricing]; spot 5.84 → 6.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/4x/120cpu-1020gb-1072gb`: on_demand 11.69 → 12.41  [REVIEW: pricing]; spot 5.84 → 6.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/8x/240cpu-2040gb-2144gb`: on_demand 11.69 → 12.41  [REVIEW: pricing]; spot 5.84 → 6.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/1x/30cpu-170gb-180gb`: on_demand 9.14 → 9.51  [REVIEW: pricing]; spot 4.57 → 4.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/2x/60cpu-340gb-360gb`: on_demand 9.14 → 9.51  [REVIEW: pricing]; spot 4.57 → 4.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/4x/120cpu-680gb-720gb`: on_demand 9.14 → 9.51  [REVIEW: pricing]; spot 4.57 → 4.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/8x/240cpu-1360gb-1440gb`: on_demand 9.14 → 9.51  [REVIEW: pricing]; spot 4.57 → 4.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/1x/44cpu-170gb-141gb`: on_demand 6.44 → 6.7  [REVIEW: pricing]; spot 3.22 → 3.35  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/2x/88cpu-340gb-282gb`: on_demand 6.44 → 6.7  [REVIEW: pricing]; spot 3.22 → 3.35  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/4x/176cpu-680gb-564gb`: on_demand 6.44 → 6.7  [REVIEW: pricing]; spot 3.22 → 3.35  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/8x/176cpu-1360gb-1128gb`: on_demand 6.44 → 6.7  [REVIEW: pricing]; spot 3.22 → 3.35  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/30cpu-120gb-80gb`: on_demand 4.94 → 5.24  [REVIEW: pricing]; spot 2.47 → 2.62  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/32cpu-170gb-80gb`: on_demand 4.94 → 5.24  [REVIEW: pricing]; spot 2.47 → 2.62  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/2x/80cpu-340gb-160gb`: on_demand 4.94 → 5.24  [REVIEW: pricing]; spot 2.47 → 2.62  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/4x/176cpu-680gb-320gb`: on_demand 4.94 → 5.24  [REVIEW: pricing]; spot 2.47 → 2.62  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/8x/176cpu-1360gb-640gb`: on_demand 4.94 → 5.24  [REVIEW: pricing]; spot 2.47 → 2.62  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/1x/22cpu-120gb-80gb`: on_demand 2.32 → 2.39  [REVIEW: pricing]; spot 1.16 → 1.19  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/1x/22cpu-120gb-40gb`: on_demand 1.66 → 1.7  [REVIEW: pricing]; spot 0.83 → 0.85  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/2x/44cpu-240gb-160gb`: on_demand 2.32 → 2.39  [REVIEW: pricing]; spot 1.16 → 1.19  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/4x/88cpu-480gb-320gb`: on_demand 2.32 → 2.39  [REVIEW: pricing]; spot 1.16 → 1.19  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/8x/176cpu-960gb-640gb`: on_demand 2.32 → 2.39  [REVIEW: pricing]; spot 1.16 → 1.19  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/8x/176cpu-960gb-320gb`: on_demand 1.66 → 1.7  [REVIEW: pricing]; spot 0.83 → 0.85  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/1x/30cpu-90gb-96gb`: on_demand 2.73 → 2.84  [REVIEW: pricing]; spot 1.36 → 1.42  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/2x/60cpu-180gb-192gb`: on_demand 2.73 → 2.84  [REVIEW: pricing]; spot 1.36 → 1.42  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/4x/120cpu-360gb-384gb`: on_demand 2.73 → 2.83  [REVIEW: pricing]; spot 1.36 → 1.42  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/8x/240cpu-720gb-768gb`: on_demand 2.73 → 2.84  [REVIEW: pricing]; spot 1.36 → 1.42  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/1x/20cpu-60gb-48gb`: on_demand 1.94 → 2.02  [REVIEW: pricing]; spot 0.97 → 1.01  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/2x/40cpu-120gb-96gb`: on_demand 1.94 → 2.02  [REVIEW: pricing]; spot 0.97 → 1.01  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/4x/80cpu-240gb-192gb`: on_demand 1.94 → 2.02  [REVIEW: pricing]; spot 0.97 → 1.01  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/8x/160cpu-480gb-384gb`: on_demand 1.94 → 2.02  [REVIEW: pricing]; spot 0.97 → 1.01  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/1x/10cpu-60gb-48gb`: on_demand 1.54 → 1.61  [REVIEW: pricing]; spot 0.77 → 0.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/2x/20cpu-120gb-96gb`: on_demand 1.54 → 1.61  [REVIEW: pricing]; spot 0.77 → 0.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/4x/40cpu-240gb-192gb`: on_demand 1.54 → 1.61  [REVIEW: pricing]; spot 0.77 → 0.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/8x/80cpu-480gb-384gb`: on_demand 1.54 → 1.61  [REVIEW: pricing]; spot 0.77 → 0.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/1x/10cpu-60gb-48gb`: on_demand 0.85 → 0.89  [REVIEW: pricing]; spot 0.43 → 0.44  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/2x/20cpu-120gb-96gb`: on_demand 0.85 → 0.89  [REVIEW: pricing]; spot 0.43 → 0.44  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/4x/40cpu-240gb-192gb`: on_demand 0.85 → 0.89  [REVIEW: pricing]; spot 0.43 → 0.44  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/8x/80cpu-480gb-384gb`: on_demand 0.85 → 0.89  [REVIEW: pricing]; spot 0.43 → 0.44  [REVIEW: pricing]
- Listed but not a SKU: 1x GB300 SXM6 288GB: no accelerator file for this SKU
- Listed but not a SKU: 2x GB300 SXM6 288GB: no accelerator file for this SKU
- Listed but not a SKU: 4x GB300 SXM6 288GB: no accelerator file for this SKU
- Listed but not a SKU: 1x Tesla V100 16GB: no accelerator file for this SKU
- Listed but not a SKU: 2x Tesla V100 16GB: no accelerator file for this SKU
- Listed but not a SKU: 4x Tesla V100 16GB: no accelerator file for this SKU
- Listed but not a SKU: 8x Tesla V100 16GB: no accelerator file for this SKU

## hyperstack

- no changes

## Fetched

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 6bf212a8d528
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 5066 B sha1 381b9059a60b
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4950 B sha1 c71742cbfa8d
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 87e47c03409b
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 4943e9e91526
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 c2015395531e
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 4910e2927a36
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 e63b4aa93fdf
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 6a94d67579eb
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 e781516d5bbc
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 54e6b960d905
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 ebc9cde16ae6
- `jl gpus --json` 3565 B sha1 0e8efbc2034e
- `https://jarvislabs.ai/pricing` 165434 B sha1 f17eb3d1794b
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 113417 B sha1 5fbfb38c346d
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 112751 B sha1 4128e2b1ab33
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 112440 B sha1 c6d63aa1fb10
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 113070 B sha1 b9f599a98c05
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 113005 B sha1 3a6ddab422ed
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 112684 B sha1 b95ded2c839c
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 112092 B sha1 60a8795fb41f
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 113114 B sha1 3a6798a9527b
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 113405 B sha1 011d17dd3f30
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 112513 B sha1 1bc81a01001c
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 112467 B sha1 0cabf97b5281
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 113403 B sha1 de4286d306e8
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 112785 B sha1 08f73119736a
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 112447 B sha1 5473f9d44cea
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 113089 B sha1 e70b27f7e0c9
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 113033 B sha1 715a021da615
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 112709 B sha1 1ab1170220ad
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 112108 B sha1 977bea0ecbbd
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 113120 B sha1 4e24cbc9a754
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 113427 B sha1 e68b2fe2091d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 112535 B sha1 866e682503fa
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 112466 B sha1 e2ec2511e4a3
- `https://neysa.ai/pricing/` 327979 B sha1 2c21f28ec09b
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 120727 B sha1 befdc0b756e4
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145745 B sha1 f93470c30c93
- `https://cyfuture.ai/pricing` 521483 B sha1 2938f84c9d7e
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301290 B sha1 a4537ebdf8a5
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1383 B sha1 abc68ea42e0a
- `https://www.olakrutrim.com/gpu-services` 46299 B sha1 b0f3243c2a23
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35984 B sha1 60c4b1578b13
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21601 B sha1 8e7563e1abb4
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7932461 B sha1 8a740962fbb8
- `https://nebius.com/prices` 278287 B sha1 b39e4f8c48ed
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3170 B sha1 90a4cb0fb02c
- `https://api.verda.com/v1/instance-types` 184262 B sha1 ca3aa857c643
- `https://www.hyperstack.cloud/gpu-pricing` 158073 B sha1 aad278b71fb1

