# Pricing refresh 2026-11-26 00:02 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=121, unchanged=318, stale=11, retired=0, failed=0, price_rows=117

## e2e-networks

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {3: 7.35} → {3: 7.41}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: committed {3: 4.98} → {3: 5.02}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: spot 0.75 → 0.76  [REVIEW: pricing]; committed {3: 3.74} → {3: 3.77}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {3: 2.34} → {3: 2.36}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/A100/1x/standard`: spot 0.71 → 0.72  [REVIEW: pricing]
- STALE `skus/e2e-networks/IN-DEL/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/e2e-networks/IN-DEL/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- Price history: 4 changed observation(s) appended to `data/price-history/e2e-networks.jsonl`
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

- no changes
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- no changes

## nxtgen

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.07 → 3.09  [REVIEW: pricing]; committed {1: 2.45, 6: 2.45, 12: 1.96} → {1: 2.47, 6: 2.47, 12: 1.97}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H200/8x/standard`: on_demand 3.06 → 3.08  [REVIEW: pricing]; committed {1: 2.45, 6: 2.45, 12: 1.96} → {1: 2.47, 6: 2.47, 12: 1.97}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.66 → 2.68  [REVIEW: pricing]; committed {1: 2.13, 6: 2.13, 12: 1.7} → {1: 2.15, 6: 2.15, 12: 1.71}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/L40S/1x/standard`: on_demand 1.58 → 1.59  [REVIEW: pricing]; committed {1: 1.27, 6: 1.27, 12: 1.01} → {1: 1.28, 6: 1.28, 12: 1.02}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.7 → 2.72  [REVIEW: pricing]; committed {1: 2.16, 6: 2.16, 12: 1.73} → {1: 2.18, 6: 2.18, 12: 1.75}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/8x/standard`: on_demand 2.7 → 2.72  [REVIEW: pricing]; committed {1: 2.16, 6: 2.16, 12: 1.73} → {1: 2.18, 6: 2.18, 12: 1.74}  [REVIEW: pricing]
- Price history: 6 changed observation(s) appended to `data/price-history/nxtgen.jsonl`

## leapswitch

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.35 → 4.38  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: on_demand 1.97 → 1.98  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A4000/1x/standard`: on_demand 0.21 → 0.22  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A5000/1x/standard`: on_demand 0.29 → 0.3  [REVIEW: pricing]
- CHANGED `leapswitch/IN/A100/1x/standard`: on_demand 1.64 → 1.65  [REVIEW: pricing]

## cyfuture-ai

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `cyfuture-ai/IN/B300/1x/standard`: committed {1: 8.18, 6: 7.67, 12: 6.13} → {1: 8.24, 6: 7.72, 12: 6.18}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/2x/standard`: committed {1: 8.18, 6: 7.67, 12: 6.13} → {1: 8.24, 6: 7.72, 12: 6.18}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/4x/standard`: committed {1: 6.13, 6: 5.75, 12: 4.6} → {1: 6.18, 6: 5.79, 12: 4.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/8x/standard`: committed {1: 4.09, 6: 3.83, 12: 3.07} → {1: 4.12, 6: 3.86, 12: 3.09}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: on_demand 2.76 → 2.78  [REVIEW: pricing]; committed {1: 2.61, 6: 2.45, 12: 2.3} → {1: 2.63, 6: 2.47, 12: 2.32}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: on_demand 2.76 → 2.78  [REVIEW: pricing]; committed {1: 2.61, 6: 2.45, 12: 2.3} → {1: 2.63, 6: 2.47, 12: 2.32}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: on_demand 2.76 → 2.78  [REVIEW: pricing]; committed {1: 2.61, 6: 2.45, 12: 2.3} → {1: 2.63, 6: 2.47, 12: 2.32}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: on_demand 2.76 → 2.78  [REVIEW: pricing]; committed {1: 2.61, 6: 2.45, 12: 2.3} → {1: 2.63, 6: 2.47, 12: 2.32}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/1x/standard`: on_demand 1.33 → 1.34  [REVIEW: pricing]; committed {1: 0.8, 6: 0.73, 12: 0.66} → {1: 0.8, 6: 0.74, 12: 0.66}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/2x/standard`: on_demand 1.32 → 1.33  [REVIEW: pricing]; committed {1: 0.78, 6: 0.7, 12: 0.63} → {1: 0.79, 6: 0.71, 12: 0.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/4x/standard`: on_demand 1.3 → 1.31  [REVIEW: pricing]; committed {1: 0.77, 6: 0.7, 12: 0.63} → {1: 0.78, 6: 0.7, 12: 0.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: on_demand 1.29 → 1.3  [REVIEW: pricing]; committed {1: 0.76, 6: 0.69, 12: 0.62} → {1: 0.77, 6: 0.7, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: on_demand 2.95 → 2.97  [REVIEW: pricing]; committed {1: 2.36, 6: 2.12, 12: 1.76} → {1: 2.37, 6: 2.14, 12: 1.78}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: on_demand 2.92 → 2.94  [REVIEW: pricing]; committed {1: 2.31, 6: 2.06, 12: 1.7} → {1: 2.33, 6: 2.07, 12: 1.71}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: on_demand 2.89 → 2.91  [REVIEW: pricing]; committed {1: 2.28, 6: 2.03, 12: 1.68} → {1: 2.3, 6: 2.05, 12: 1.69}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: on_demand 2.86 → 2.88  [REVIEW: pricing]; committed {1: 2.26, 6: 2.01, 12: 1.66} → {1: 2.28, 6: 2.03, 12: 1.67}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.54 → 3.57  [REVIEW: pricing]; committed {1: 3.19, 6: 2.83, 12: 2.36} → {1: 3.21, 6: 2.85, 12: 2.37}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: on_demand 3.5 → 3.53  [REVIEW: pricing]; committed {1: 3.12, 6: 2.74, 12: 2.26} → {1: 3.14, 6: 2.76, 12: 2.28}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: on_demand 3.47 → 3.49  [REVIEW: pricing]; committed {1: 3.09, 6: 2.72, 12: 2.24} → {1: 3.11, 6: 2.74, 12: 2.26}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: on_demand 3.43 → 3.46  [REVIEW: pricing]; committed {1: 3.06, 6: 2.69, 12: 2.21} → {1: 3.08, 6: 2.71, 12: 2.23}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: on_demand 0.58 → 0.59  [REVIEW: pricing]; committed {1: 0.52, 6: 0.46, 12: 0.42} → {1: 0.52, 6: 0.47, 12: 0.42}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/4x/standard`: committed {1: 0.51, 6: 0.44, 12: 0.39} → {1: 0.51, 6: 0.45, 12: 0.4}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/8x/standard`: on_demand 0.56 → 0.57  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: on_demand 2.13 → 2.15  [REVIEW: pricing]; committed {1: 2.11, 6: 2.09, 12: 2.01} → {1: 2.13, 6: 2.1, 12: 2.03}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: on_demand 2.11 → 2.13  [REVIEW: pricing]; committed {1: 2.07, 6: 2.02, 12: 1.93} → {1: 2.08, 6: 2.04, 12: 1.95}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: on_demand 2.09 → 2.1  [REVIEW: pricing]; committed {1: 2.04, 6: 2.0, 12: 1.91} → {1: 2.06, 6: 2.01, 12: 1.93}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: on_demand 2.07 → 2.08  [REVIEW: pricing]; committed {1: 2.02, 6: 1.98, 12: 1.89} → {1: 2.04, 6: 1.99, 12: 1.91}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: on_demand 1.09 → 1.1  [REVIEW: pricing]; committed {1: 0.87, 6: 0.74, 12: 0.63} → {1: 0.88, 6: 0.75, 12: 0.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: committed {1: 0.86, 6: 0.72, 12: 0.61} → {1: 0.87, 6: 0.73, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/4x/standard`: on_demand 1.07 → 1.08  [REVIEW: pricing]; committed {1: 0.85, 6: 0.72, 12: 0.61} → {1: 0.86, 6: 0.72, 12: 0.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/8x/standard`: committed {1: 0.84, 6: 0.71, 12: 0.6} → {1: 0.85, 6: 0.71, 12: 0.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: on_demand 3.21 → 3.23  [REVIEW: pricing]; committed {1: 2.34, 6: 1.95, 12: 1.61} → {1: 2.35, 6: 1.96, 12: 1.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: on_demand 3.17 → 3.2  [REVIEW: pricing]; committed {1: 2.29, 6: 1.88, 12: 1.56} → {1: 2.3, 6: 1.9, 12: 1.57}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: on_demand 3.14 → 3.16  [REVIEW: pricing]; committed {1: 2.27, 6: 1.86, 12: 1.54} → {1: 2.28, 6: 1.88, 12: 1.55}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: on_demand 3.11 → 3.13  [REVIEW: pricing]; committed {1: 2.24, 6: 1.85, 12: 1.52} → {1: 2.26, 6: 1.86, 12: 1.53}  [REVIEW: pricing]
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review
- Price history: 36 changed observation(s) appended to `data/price-history/cyfuture-ai.jsonl`

## tata-communications

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: on_demand 5.25 → 5.29  [REVIEW: pricing]; committed {3: 5.11, 6: 4.53, 12: 4.03, 36: 3.82, 48: 3.62} → {3: 5.14, 6: 4.56, 12: 4.06, 36: 3.84, 48: 3.65}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: on_demand 5.71 → 5.76  [REVIEW: pricing]; committed {3: 5.55, 6: 4.93, 12: 4.38, 36: 4.15, 48: 3.94} → {3: 5.59, 6: 4.96, 12: 4.41, 36: 4.18, 48: 3.97}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: on_demand 5.55 → 5.59  [REVIEW: pricing]; committed {3: 5.39, 6: 4.78, 12: 4.25, 36: 4.03, 48: 3.83} → {3: 5.43, 6: 4.82, 12: 4.28, 36: 4.06, 48: 3.85}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: on_demand 3.16 → 3.18  [REVIEW: pricing]; committed {3: 3.07, 6: 2.72, 12: 2.42, 36: 2.3, 48: 2.18} → {3: 3.09, 6: 2.74, 12: 2.44, 36: 2.31, 48: 2.2}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: on_demand 4.33 → 4.36  [REVIEW: pricing]; committed {3: 4.21, 6: 3.73, 12: 3.31, 36: 3.14, 48: 2.99} → {3: 4.24, 6: 3.76, 12: 3.34, 36: 3.17, 48: 3.01}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: on_demand 4.69 → 4.73  [REVIEW: pricing]; committed {3: 4.56, 6: 4.05, 12: 3.59, 36: 3.41, 48: 3.24} → {3: 4.6, 6: 4.08, 12: 3.62, 36: 3.44, 48: 3.26}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: on_demand 4.85 → 4.89  [REVIEW: pricing]; committed {3: 4.71, 6: 4.19, 12: 3.72, 36: 3.53, 48: 3.35} → {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.56, 48: 3.37}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: on_demand 4.33 → 4.36  [REVIEW: pricing]; committed {3: 4.21, 6: 3.73, 12: 3.32, 36: 3.14, 48: 2.99} → {3: 4.24, 6: 3.76, 12: 3.34, 36: 3.17, 48: 3.01}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: on_demand 4.69 → 4.73  [REVIEW: pricing]; committed {3: 4.56, 6: 4.05, 12: 3.6, 36: 3.41, 48: 3.24} → {3: 4.6, 6: 4.08, 12: 3.63, 36: 3.44, 48: 3.26}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: on_demand 4.85 → 4.89  [REVIEW: pricing]; committed {3: 4.72, 6: 4.19, 12: 3.72, 36: 3.52, 48: 3.35} → {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.55, 48: 3.38}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: on_demand 5.11 → 5.15  [REVIEW: pricing]; committed {3: 4.97, 6: 4.41, 12: 3.92, 36: 3.71, 48: 3.53} → {3: 5.01, 6: 4.45, 12: 3.95, 36: 3.74, 48: 3.56}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: on_demand 5.84 → 5.89  [REVIEW: pricing]; committed {3: 5.68, 6: 5.04, 12: 4.48, 36: 4.25, 48: 4.03} → {3: 5.72, 6: 5.07, 12: 4.51, 36: 4.28, 48: 4.06}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: on_demand 4.86 → 4.89  [REVIEW: pricing]; committed {3: 4.72, 6: 4.19, 12: 3.72, 36: 3.53, 48: 3.35} → {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.55, 48: 3.37}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: on_demand 2.15 → 2.17  [REVIEW: pricing]; committed {3: 2.09, 6: 1.86, 12: 1.65, 36: 1.56, 48: 1.49} → {3: 2.1, 6: 1.88, 12: 1.66, 36: 1.57, 48: 1.5}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: on_demand 2.35 → 2.36  [REVIEW: pricing]; committed {3: 2.28, 6: 2.02, 12: 1.8, 36: 1.7, 48: 1.61} → {3: 2.3, 6: 2.04, 12: 1.81, 36: 1.71, 48: 1.63}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: on_demand 2.43 → 2.45  [REVIEW: pricing]; committed {3: 2.36, 6: 2.1, 12: 1.86, 36: 1.76, 48: 1.68} → {3: 2.37, 6: 2.11, 12: 1.88, 36: 1.78, 48: 1.69}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: on_demand 2.51 → 2.53  [REVIEW: pricing]; committed {3: 2.44, 6: 2.16, 12: 1.93, 36: 1.83, 48: 1.73} → {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.84, 48: 1.75}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: on_demand 2.15 → 2.17  [REVIEW: pricing]; committed {3: 2.09, 6: 1.86, 12: 1.65, 36: 1.57, 48: 1.49} → {3: 2.11, 6: 1.87, 12: 1.66, 36: 1.58, 48: 1.5}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: on_demand 2.35 → 2.36  [REVIEW: pricing]; committed {3: 2.28, 6: 2.02, 12: 1.8, 36: 1.71, 48: 1.62} → {3: 2.3, 6: 2.04, 12: 1.81, 36: 1.72, 48: 1.63}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: on_demand 2.51 → 2.53  [REVIEW: pricing]; committed {3: 2.44, 6: 2.17, 12: 1.93, 36: 1.82, 48: 1.73} → {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.84, 48: 1.75}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: on_demand 0.97 → 0.98  [REVIEW: pricing]; committed {3: 0.94, 6: 0.84, 12: 0.74, 36: 0.7, 48: 0.67} → {3: 0.94, 6: 0.85, 12: 0.75, 36: 0.7, 48: 0.67}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: on_demand 1.04 → 1.05  [REVIEW: pricing]; committed {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.75, 48: 0.72} → {3: 1.02, 6: 0.91, 12: 0.8, 36: 0.76, 48: 0.73}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: on_demand 1.11 → 1.12  [REVIEW: pricing]; committed {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.76} → {3: 1.08, 6: 0.96, 12: 0.86, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: on_demand 1.26 → 1.27  [REVIEW: pricing]; committed {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.91, 48: 0.87} → {3: 1.24, 6: 1.1, 12: 0.98, 36: 0.92, 48: 0.88}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: on_demand 1.04 → 1.05  [REVIEW: pricing]; committed {3: 1.02, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72} → {3: 1.02, 6: 0.91, 12: 0.81, 36: 0.76, 48: 0.73}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: on_demand 1.11 → 1.12  [REVIEW: pricing]; committed {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.76} → {3: 1.08, 6: 0.96, 12: 0.86, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: on_demand 1.26 → 1.27  [REVIEW: pricing]; committed {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.92, 48: 0.87} → {3: 1.24, 6: 1.1, 12: 0.98, 36: 0.93, 48: 0.88}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: on_demand 1.04 → 1.05  [REVIEW: pricing]; committed {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.75, 48: 0.72} → {3: 1.02, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu`: on_demand 1.15 → 1.16  [REVIEW: pricing]; committed {3: 1.12, 6: 1.0, 12: 0.89, 36: 0.84, 48: 0.8} → {3: 1.13, 6: 1.0, 12: 0.89, 36: 0.84, 48: 0.8}  [REVIEW: pricing]
- Price history: 29 changed observation(s) appended to `data/price-history/tata-communications.jsonl`

## yotta-shakti

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 4.61 → 4.64  [REVIEW: pricing]; committed {6: 4.09, 12: 3.79, 24: 3.38} → {6: 4.12, 12: 3.82, 24: 3.4}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: on_demand 2.56 → 2.58  [REVIEW: pricing]; committed {6: 2.15, 12: 1.95, 24: 1.74} → {6: 2.17, 12: 1.96, 24: 1.76}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 5.09 → 5.13  [REVIEW: pricing]; committed {6: 5.09, 12: 5.09, 24: 5.09, 36: 4.07, 48: 3.4, 60: 3.0} → {6: 5.13, 12: 5.13, 24: 5.13, 36: 4.1, 48: 3.43, 60: 3.02}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: committed {12: 11.36, 24: 9.3, 36: 7.23, 48: 5.17, 60: 4.09} → {12: 11.45, 24: 9.37, 36: 7.29, 48: 5.2, 60: 4.12}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 6.41 → 6.46  [REVIEW: pricing]; committed {1: 5.79, 3: 5.62, 6: 5.5, 12: 5.33} → {1: 5.83, 3: 5.66, 6: 5.54, 12: 5.37}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 6.32 → 6.37  [REVIEW: pricing]; committed {1: 5.7, 3: 5.53, 6: 5.41, 12: 5.24} → {1: 5.74, 3: 5.57, 6: 5.45, 12: 5.28}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 6.3 → 6.34  [REVIEW: pricing]; committed {1: 5.67, 3: 5.5, 6: 5.39, 12: 5.22} → {1: 5.71, 3: 5.54, 6: 5.43, 12: 5.25}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: on_demand 3.25 → 3.27  [REVIEW: pricing]; committed {1: 2.63, 3: 2.55, 6: 2.49, 12: 2.42} → {1: 2.65, 3: 2.57, 6: 2.51, 12: 2.43}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: on_demand 3.19 → 3.21  [REVIEW: pricing]; committed {1: 2.57, 3: 2.49, 6: 2.44, 12: 2.36} → {1: 2.59, 3: 2.51, 6: 2.46, 12: 2.38}  [REVIEW: pricing]
- Price history: 9 changed observation(s) appended to `data/price-history/yotta-shakti.jsonl`

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
- WARNING: unmapped AWS accelerated type g7.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## ovhcloud

- FX: USD/INR 92.235 (2026-11-25, ECB reference rate)
- CHANGED `ovhcloud/EU-FR/H100/4x/h100-1520`: on_demand 3.07 → 3.06  [REVIEW: pricing]; committed {1: 2.92} → {1: 2.91}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/1x/h100-380`: on_demand 3.07 → 3.06  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/2x/h100-760`: on_demand 3.07 → 3.06  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920`: on_demand 5.76 → 5.74  [REVIEW: pricing]; committed {1: 5.76} → {1: 5.74}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920-eph`: on_demand 5.76 → 5.74  [REVIEW: pricing]; committed {1: 5.76} → {1: 5.74}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/2x/win-l4-180`: on_demand 1.68 → 1.67  [REVIEW: pricing]; committed {1: 1.68} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/win-l4-360`: on_demand 1.68 → 1.67  [REVIEW: pricing]; committed {1: 1.68} → {1: 1.67}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/win-l4-90`: on_demand 1.66 → 1.65  [REVIEW: pricing]
- Price history: 9 changed observation(s) appended to `data/price-history/ovhcloud.jsonl`
- Listed but not a SKU: a10-180: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-45: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-90: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: b300-1920: B300 HGX has no accelerator spec in the catalogue
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

- CHANGED `nebius/EU-WEST2/B300/1x/hgx-b300-1x`: spot 11.1 → 3.6  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST2/B300/8x/hgx-b300-8x`: spot 11.1 → 3.6  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/1x/hgx-b300-1x`: spot 6.49 → 1.99  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/8x/hgx-b300-8x`: spot 6.49 → 1.99  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/1x/hgx-b300-1x`: spot 8.89 → 2.59  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/8x/hgx-b300-8x`: spot 8.89 → 2.59  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/1x/hgx-b200-1x`: spot 2.4 → 2.8  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/8x/hgx-b200-8x`: spot 2.4 → 2.8  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/1x/hgx-b200-1x`: spot 2.1 → 3.9  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/8x/hgx-b200-8x`: spot 2.1 → 3.9  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/1x/hgx-h200-1x`: spot 2.3 → 1.4  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/8x/hgx-h200-8x`: spot 2.3 → 1.4  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/1x/hgx-h200-1x`: spot 1.7 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/8x/hgx-h200-8x`: spot 1.7 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/1x/hgx-h200-1x`: spot 1.4 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/8x/hgx-h200-8x`: spot 1.4 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/1x/hgx-h100-1x`: spot 2.15 → 1.05  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/8x/hgx-h100-8x`: spot 2.15 → 1.05  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 1.2 → 0.89  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 1.2 → 0.89  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 0.79 → 1.09  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 0.79 → 1.09  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 1.09 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 1.09 → 0.79  [REVIEW: pricing]
- Price history: 24 changed observation(s) appended to `data/price-history/nebius.jsonl`
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## verda

- no changes
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

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 302aca37c45e
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 6473 B sha1 bbf0d0090dba
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4966 B sha1 c390391d10fe
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 322f9109dc61
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 0f15e89197ab
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 62bdcacb27d7
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 0f730a030178
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 9471b7317ed5
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 fe2609b6d871
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 15b3c4426ce8
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 17d70dedba02
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 86a10130e735
- `jl gpus --json` 3240 B sha1 cb26bdadd551
- `https://jarvislabs.ai/pricing` 156217 B sha1 b1ddeb6613e3
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 114366 B sha1 35e3b2e304c6
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 113700 B sha1 3af681573fd8
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 113389 B sha1 c6091a58147b
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 114019 B sha1 246d19606652
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 113954 B sha1 7abaa7f3372d
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 113633 B sha1 f836ef906a2e
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 113041 B sha1 18face814ca1
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 114063 B sha1 94ffa53fa3fe
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 114354 B sha1 8cd5d2feb222
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 113462 B sha1 72e957f6f5cc
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 113416 B sha1 c4c9bce36eff
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 114352 B sha1 8d77cc1ca6f2
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 113734 B sha1 2c2f01f605e3
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 113396 B sha1 aa82bb0961f4
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 114038 B sha1 bd3d1b40b02d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 113982 B sha1 47632a70bf43
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 113658 B sha1 8419066a066e
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 113057 B sha1 f5c605f32e0d
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 114069 B sha1 ea2e8acde39f
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 114376 B sha1 ae479f1e82ed
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 113484 B sha1 52db7a3527b0
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 113415 B sha1 125ead456525
- `https://neysa.ai/pricing/` 330084 B sha1 5eabcf01f2a9
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 131248 B sha1 7b0df72d94e8
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145741 B sha1 c304726b8f94
- `https://cyfuture.ai/pricing` 523395 B sha1 08b95d49a5f7
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301291 B sha1 9ae5c13b49bb
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1508 B sha1 f8e4c0633daf
- `https://www.olakrutrim.com/gpu-services` 47037 B sha1 751d4792c91f
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 104579 B sha1 0f2cc3885d5b
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45958 B sha1 e054072629de
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35940 B sha1 46028dc0f1e1
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21634 B sha1 8757aa67352f
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7991523 B sha1 199fc022c34a
- `https://nebius.com/prices` 280525 B sha1 be08a0976fd0
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3533 B sha1 713d805363d6
- `https://api.verda.com/v1/instance-types` 187757 B sha1 6e15c65c4ada
- `https://www.hyperstack.cloud/gpu-pricing` 148668 B sha1 c8c5e365d7c4

