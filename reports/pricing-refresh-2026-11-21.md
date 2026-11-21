# Pricing refresh 2026-11-21 10:10 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=167, unchanged=272, stale=11, retired=0, failed=0, price_rows=158

## e2e-networks

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {3: 7.27} → {3: 7.37}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: spot 0.94 → 0.95  [REVIEW: pricing]; committed {3: 4.93} → {3: 4.99}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: spot 0.75 → 0.76  [REVIEW: pricing]; committed {3: 3.7} → {3: 3.75}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {3: 2.32} → {3: 2.35}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/A100/1x/standard`: spot 0.7 → 0.71  [REVIEW: pricing]
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

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.03 → 3.08  [REVIEW: pricing]; committed {1: 2.43, 6: 2.43, 12: 1.94} → {1: 2.46, 6: 2.46, 12: 1.96}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H200/8x/standard`: on_demand 3.03 → 3.07  [REVIEW: pricing]; committed {1: 2.42, 6: 2.42, 12: 1.94} → {1: 2.46, 6: 2.46, 12: 1.97}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.63 → 2.67  [REVIEW: pricing]; committed {1: 2.11, 6: 2.11, 12: 1.68} → {1: 2.14, 6: 2.14, 12: 1.7}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/L40S/1x/standard`: on_demand 1.57 → 1.59  [REVIEW: pricing]; committed {1: 1.26, 6: 1.26, 12: 1.0} → {1: 1.27, 6: 1.27, 12: 1.01}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.67 → 2.71  [REVIEW: pricing]; committed {1: 2.14, 6: 2.14, 12: 1.71} → {1: 2.17, 6: 2.17, 12: 1.74}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/8x/standard`: on_demand 2.67 → 2.71  [REVIEW: pricing]; committed {1: 2.14, 6: 2.14, 12: 1.71} → {1: 2.17, 6: 2.17, 12: 1.73}  [REVIEW: pricing]
- Price history: 6 changed observation(s) appended to `data/price-history/nxtgen.jsonl`

## leapswitch

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.31 → 4.36  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: on_demand 1.95 → 1.97  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A5000/1x/standard`: on_demand 0.29 → 0.3  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A6000/1x/standard`: on_demand 0.46 → 0.47  [REVIEW: pricing]
- CHANGED `leapswitch/IN/A100/1x/standard`: on_demand 1.62 → 1.65  [REVIEW: pricing]
- CHANGED `leapswitch/IN/A40/1x/standard`: on_demand 0.48 → 0.49  [REVIEW: pricing]

## cyfuture-ai

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `cyfuture-ai/IN/B300/1x/standard`: committed {1: 6.07, 6: 5.81, 12: 5.57} → {1: 8.2, 6: 7.69, 12: 6.15}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/2x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 8.2, 6: 7.69, 12: 6.15}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/4x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 6.15, 6: 5.77, 12: 4.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/8x/standard`: committed {1: 6.07, 6: 5.82, 12: 5.56} → {1: 4.1, 6: 3.84, 12: 3.08}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: on_demand 2.73 → 2.77  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.61, 6: 2.46, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: on_demand 2.73 → 2.77  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.61, 6: 2.46, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: on_demand 2.73 → 2.77  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.61, 6: 2.46, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: on_demand 2.73 → 2.77  [REVIEW: pricing]; committed {1: 2.58, 6: 2.43, 12: 2.28} → {1: 2.61, 6: 2.46, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/1x/standard`: on_demand 1.32 → 1.34  [REVIEW: pricing]; committed {1: 0.79, 6: 0.72, 12: 0.65} → {1: 0.8, 6: 0.73, 12: 0.66}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/2x/standard`: on_demand 1.3 → 1.32  [REVIEW: pricing]; committed {1: 0.77, 6: 0.7, 12: 0.63} → {1: 0.78, 6: 0.71, 12: 0.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/4x/standard`: on_demand 1.29 → 1.31  [REVIEW: pricing]; committed {1: 0.76, 6: 0.69, 12: 0.62} → {1: 0.77, 6: 0.7, 12: 0.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: on_demand 1.28 → 1.29  [REVIEW: pricing]; committed {1: 0.75, 6: 0.68, 12: 0.61} → {1: 0.76, 6: 0.69, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: on_demand 2.92 → 2.96  [REVIEW: pricing]; committed {1: 2.33, 6: 2.1, 12: 1.75} → {1: 2.36, 6: 2.13, 12: 1.77}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: on_demand 2.89 → 2.92  [REVIEW: pricing]; committed {1: 2.28, 6: 2.03, 12: 1.68} → {1: 2.31, 6: 2.06, 12: 1.7}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: on_demand 2.86 → 2.9  [REVIEW: pricing]; committed {1: 2.26, 6: 2.01, 12: 1.66} → {1: 2.29, 6: 2.04, 12: 1.68}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: on_demand 2.83 → 2.87  [REVIEW: pricing]; committed {1: 2.24, 6: 1.99, 12: 1.64} → {1: 2.27, 6: 2.02, 12: 1.66}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.5 → 3.55  [REVIEW: pricing]; committed {1: 3.15, 6: 2.8, 12: 2.33} → {1: 3.19, 6: 2.84, 12: 2.36}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: on_demand 3.47 → 3.51  [REVIEW: pricing]; committed {1: 3.09, 6: 2.71, 12: 2.24} → {1: 3.13, 6: 2.75, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: on_demand 3.43 → 3.48  [REVIEW: pricing]; committed {1: 3.06, 6: 2.69, 12: 2.21} → {1: 3.1, 6: 2.72, 12: 2.24}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: on_demand 3.4 → 3.44  [REVIEW: pricing]; committed {1: 3.02, 6: 2.66, 12: 2.19} → {1: 3.07, 6: 2.69, 12: 2.22}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: on_demand 0.57 → 0.58  [REVIEW: pricing]; committed {1: 0.51, 6: 0.46, 12: 0.42} → {1: 0.52, 6: 0.46, 12: 0.42}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/2x/standard`: on_demand 0.57 → 0.58  [REVIEW: pricing]; committed {1: 0.51, 6: 0.44, 12: 0.39} → {1: 0.51, 6: 0.45, 12: 0.4}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/4x/standard`: on_demand 0.56 → 0.57  [REVIEW: pricing]; committed {1: 0.5, 6: 0.44, 12: 0.39} → {1: 0.51, 6: 0.45, 12: 0.39}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/8x/standard`: committed {1: 0.5, 6: 0.43, 12: 0.39} → {1: 0.5, 6: 0.44, 12: 0.39}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: on_demand 2.11 → 2.14  [REVIEW: pricing]; committed {1: 2.09, 6: 2.07, 12: 1.99} → {1: 2.11, 6: 2.09, 12: 2.02}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: on_demand 2.09 → 2.11  [REVIEW: pricing]; committed {1: 2.04, 6: 2.0, 12: 1.91} → {1: 2.07, 6: 2.03, 12: 1.94}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: on_demand 2.07 → 2.09  [REVIEW: pricing]; committed {1: 2.02, 6: 1.98, 12: 1.89} → {1: 2.05, 6: 2.0, 12: 1.92}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: on_demand 2.04 → 2.07  [REVIEW: pricing]; committed {1: 2.0, 6: 1.96, 12: 1.87} → {1: 2.03, 6: 1.98, 12: 1.9}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: on_demand 1.08 → 1.09  [REVIEW: pricing]; committed {1: 0.86, 6: 0.73, 12: 0.63} → {1: 0.87, 6: 0.74, 12: 0.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: on_demand 1.06 → 1.08  [REVIEW: pricing]; committed {1: 0.85, 6: 0.71, 12: 0.61} → {1: 0.86, 6: 0.72, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/4x/standard`: on_demand 1.06 → 1.07  [REVIEW: pricing]; committed {1: 0.84, 6: 0.71, 12: 0.6} → {1: 0.85, 6: 0.72, 12: 0.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/8x/standard`: on_demand 1.04 → 1.06  [REVIEW: pricing]; committed {1: 0.83, 6: 0.7, 12: 0.59} → {1: 0.84, 6: 0.71, 12: 0.6}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: on_demand 3.17 → 3.22  [REVIEW: pricing]; committed {1: 2.31, 6: 1.93, 12: 1.6} → {1: 2.34, 6: 1.95, 12: 1.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: on_demand 3.14 → 3.18  [REVIEW: pricing]; committed {1: 2.26, 6: 1.86, 12: 1.54} → {1: 2.29, 6: 1.89, 12: 1.56}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: on_demand 3.11 → 3.15  [REVIEW: pricing]; committed {1: 2.24, 6: 1.84, 12: 1.52} → {1: 2.27, 6: 1.87, 12: 1.54}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: on_demand 3.08 → 3.12  [REVIEW: pricing]; committed {1: 2.22, 6: 1.83, 12: 1.51} → {1: 2.25, 6: 1.85, 12: 1.53}  [REVIEW: pricing]
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review
- Price history: 36 changed observation(s) appended to `data/price-history/cyfuture-ai.jsonl`

## tata-communications

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: on_demand 5.2 → 5.27  [REVIEW: pricing]; committed {3: 5.05, 6: 4.48, 12: 3.98, 36: 3.77, 48: 3.59} → {3: 5.12, 6: 4.54, 12: 4.04, 36: 3.83, 48: 3.63}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: on_demand 5.65 → 5.73  [REVIEW: pricing]; committed {3: 5.49, 6: 4.87, 12: 4.33, 36: 4.11, 48: 3.9} → {3: 5.57, 6: 4.94, 12: 4.39, 36: 4.16, 48: 3.95}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: on_demand 5.49 → 5.56  [REVIEW: pricing]; committed {3: 5.33, 6: 4.73, 12: 4.21, 36: 3.98, 48: 3.78} → {3: 5.4, 6: 4.79, 12: 4.26, 36: 4.04, 48: 3.84}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: on_demand 3.12 → 3.17  [REVIEW: pricing]; committed {3: 3.04, 6: 2.69, 12: 2.4, 36: 2.27, 48: 2.16} → {3: 3.08, 6: 2.73, 12: 2.43, 36: 2.3, 48: 2.19}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: on_demand 4.28 → 4.34  [REVIEW: pricing]; committed {3: 4.16, 6: 3.69, 12: 3.28, 36: 3.11, 48: 2.96} → {3: 4.22, 6: 3.74, 12: 3.32, 36: 3.15, 48: 3.0}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: on_demand 4.64 → 4.7  [REVIEW: pricing]; committed {3: 4.51, 6: 4.0, 12: 3.56, 36: 3.37, 48: 3.2} → {3: 4.58, 6: 4.06, 12: 3.6, 36: 3.42, 48: 3.25}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: on_demand 4.8 → 4.87  [REVIEW: pricing]; committed {3: 4.66, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.31} → {3: 4.73, 6: 4.2, 12: 3.73, 36: 3.54, 48: 3.36}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: on_demand 4.29 → 4.34  [REVIEW: pricing]; committed {3: 4.16, 6: 3.69, 12: 3.28, 36: 3.11, 48: 2.95} → {3: 4.22, 6: 3.74, 12: 3.33, 36: 3.15, 48: 2.99}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: on_demand 4.64 → 4.7  [REVIEW: pricing]; committed {3: 4.51, 6: 4.0, 12: 3.56, 36: 3.37, 48: 3.2} → {3: 4.58, 6: 4.06, 12: 3.61, 36: 3.42, 48: 3.25}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: on_demand 4.8 → 4.87  [REVIEW: pricing]; committed {3: 4.67, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.32} → {3: 4.73, 6: 4.2, 12: 3.73, 36: 3.53, 48: 3.36}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: on_demand 5.06 → 5.13  [REVIEW: pricing]; committed {3: 4.92, 6: 4.37, 12: 3.88, 36: 3.67, 48: 3.49} → {3: 4.99, 6: 4.42, 12: 3.93, 36: 3.72, 48: 3.54}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: on_demand 5.78 → 5.86  [REVIEW: pricing]; committed {3: 5.62, 6: 4.98, 12: 4.43, 36: 4.2, 48: 3.99} → {3: 5.69, 6: 5.05, 12: 4.49, 36: 4.26, 48: 4.04}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: on_demand 4.8 → 4.87  [REVIEW: pricing]; committed {3: 4.67, 6: 4.14, 12: 3.68, 36: 3.49, 48: 3.31} → {3: 4.73, 6: 4.2, 12: 3.73, 36: 3.54, 48: 3.36}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: on_demand 2.13 → 2.16  [REVIEW: pricing]; committed {3: 2.07, 6: 1.84, 12: 1.63, 36: 1.54, 48: 1.47} → {3: 2.09, 6: 1.87, 12: 1.65, 36: 1.56, 48: 1.49}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: on_demand 2.32 → 2.35  [REVIEW: pricing]; committed {3: 2.26, 6: 2.0, 12: 1.78, 36: 1.68, 48: 1.6} → {3: 2.29, 6: 2.03, 12: 1.8, 36: 1.7, 48: 1.62}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: on_demand 2.41 → 2.44  [REVIEW: pricing]; committed {3: 2.33, 6: 2.08, 12: 1.84, 36: 1.75, 48: 1.66} → {3: 2.36, 6: 2.1, 12: 1.87, 36: 1.77, 48: 1.68}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: on_demand 2.48 → 2.51  [REVIEW: pricing]; committed {3: 2.42, 6: 2.14, 12: 1.91, 36: 1.81, 48: 1.71} → {3: 2.45, 6: 2.17, 12: 1.93, 36: 1.83, 48: 1.74}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: on_demand 2.13 → 2.16  [REVIEW: pricing]; committed {3: 2.07, 6: 1.84, 12: 1.63, 36: 1.55, 48: 1.47} → {3: 2.1, 6: 1.86, 12: 1.66, 36: 1.57, 48: 1.49}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: on_demand 2.32 → 2.35  [REVIEW: pricing]; committed {3: 2.26, 6: 2.0, 12: 1.78, 36: 1.69, 48: 1.6} → {3: 2.29, 6: 2.03, 12: 1.8, 36: 1.71, 48: 1.62}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: on_demand 2.49 → 2.52  [REVIEW: pricing]; committed {3: 2.42, 6: 2.15, 12: 1.91, 36: 1.8, 48: 1.71} → {3: 2.45, 6: 2.17, 12: 1.93, 36: 1.83, 48: 1.74}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: on_demand 0.96 → 0.97  [REVIEW: pricing]; committed {3: 0.93, 6: 0.83, 12: 0.73, 36: 0.69, 48: 0.66} → {3: 0.94, 6: 0.84, 12: 0.74, 36: 0.7, 48: 0.67}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: on_demand 1.03 → 1.05  [REVIEW: pricing]; committed {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 1.01, 6: 0.91, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: on_demand 1.1 → 1.11  [REVIEW: pricing]; committed {3: 1.06, 6: 0.95, 12: 0.84, 36: 0.8, 48: 0.76} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: on_demand 1.25 → 1.26  [REVIEW: pricing]; committed {3: 1.21, 6: 1.08, 12: 0.96, 36: 0.9, 48: 0.86} → {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.92, 48: 0.87}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: on_demand 1.03 → 1.05  [REVIEW: pricing]; committed {3: 1.01, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 1.02, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: on_demand 1.1 → 1.11  [REVIEW: pricing]; committed {3: 1.06, 6: 0.95, 12: 0.84, 36: 0.8, 48: 0.76} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: on_demand 1.25 → 1.27  [REVIEW: pricing]; committed {3: 1.21, 6: 1.08, 12: 0.96, 36: 0.91, 48: 0.86} → {3: 1.23, 6: 1.1, 12: 0.97, 36: 0.92, 48: 0.87}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: on_demand 1.03 → 1.04  [REVIEW: pricing]; committed {3: 1.0, 6: 0.89, 12: 0.79, 36: 0.75, 48: 0.71} → {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu`: on_demand 1.14 → 1.16  [REVIEW: pricing]; committed {3: 1.11, 6: 0.98, 12: 0.88, 36: 0.83, 48: 0.79} → {3: 1.12, 6: 1.0, 12: 0.89, 36: 0.84, 48: 0.8}  [REVIEW: pricing]
- Price history: 29 changed observation(s) appended to `data/price-history/tata-communications.jsonl`

## yotta-shakti

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 4.56 → 4.62  [REVIEW: pricing]; committed {6: 4.05, 12: 3.75, 24: 3.34} → {6: 4.1, 12: 3.8, 24: 3.39}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: on_demand 2.53 → 2.57  [REVIEW: pricing]; committed {6: 2.13, 12: 1.93, 24: 1.72} → {6: 2.16, 12: 1.95, 24: 1.75}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 5.04 → 5.1  [REVIEW: pricing]; committed {6: 5.04, 12: 5.04, 24: 5.04, 36: 4.02, 48: 3.36, 60: 2.97} → {6: 5.1, 12: 5.1, 24: 5.1, 36: 4.08, 48: 3.41, 60: 3.01}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: committed {12: 11.24, 24: 9.2, 36: 7.15, 48: 5.11, 60: 4.05} → {12: 11.39, 24: 9.32, 36: 7.25, 48: 5.18, 60: 4.1}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 6.35 → 6.43  [REVIEW: pricing]; committed {1: 5.73, 3: 5.56, 6: 5.44, 12: 5.27} → {1: 5.81, 3: 5.63, 6: 5.51, 12: 5.34}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 6.25 → 6.34  [REVIEW: pricing]; committed {1: 5.64, 3: 5.47, 6: 5.36, 12: 5.19} → {1: 5.71, 3: 5.54, 6: 5.43, 12: 5.26}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 6.23 → 6.31  [REVIEW: pricing]; committed {1: 5.61, 3: 5.44, 6: 5.33, 12: 5.16} → {1: 5.68, 3: 5.51, 6: 5.4, 12: 5.23}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: on_demand 3.22 → 3.26  [REVIEW: pricing]; committed {1: 2.6, 3: 2.52, 6: 2.47, 12: 2.39} → {1: 2.63, 3: 2.55, 6: 2.5, 12: 2.42}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: on_demand 3.16 → 3.2  [REVIEW: pricing]; committed {1: 2.54, 3: 2.46, 6: 2.41, 12: 2.34} → {1: 2.57, 3: 2.5, 6: 2.44, 12: 2.37}  [REVIEW: pricing]
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
- WARNING: unmapped AWS accelerated type g7.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## ovhcloud

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- CHANGED `ovhcloud/EU-FR/A100/1x/a100-180`: on_demand 3.03 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/2x/a100-360`: on_demand 3.03 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/4x/a100-720`: on_demand 3.03 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/4x/h100-1520`: committed {1: 2.93} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/1x/h100-380`: committed {1: 2.93} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/2x/h100-760`: committed {1: 2.93} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920`: on_demand 5.78 → 5.77  [REVIEW: pricing]; committed {1: 5.78} → {1: 5.77}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920-eph`: on_demand 5.78 → 5.77  [REVIEW: pricing]; committed {1: 5.78} → {1: 5.77}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/2x/l4-180`: on_demand 0.83 → 0.82  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/2x/win-l4-180`: on_demand 1.69 → 1.68  [REVIEW: pricing]; committed {1: 1.69} → {1: 1.68}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/l4-360`: on_demand 0.83 → 0.82  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/win-l4-360`: on_demand 1.69 → 1.68  [REVIEW: pricing]; committed {1: 1.69} → {1: 1.68}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/l4-90`: on_demand 0.83 → 0.82  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/win-l4-90`: committed {1: 1.67} → {1: 1.66}  [REVIEW: pricing]
- Price history: 12 changed observation(s) appended to `data/price-history/ovhcloud.jsonl`
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

- CHANGED `nebius/EU-WEST2/B300/1x/hgx-b300-1x`: spot 4.7 → 12.5  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST2/B300/8x/hgx-b300-8x`: on_demand 76.0 → 9.5  [REVIEW: pricing]; spot 37.6 → 12.5  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/1x/hgx-b300-1x`: spot 4.5 → 10.4  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/8x/hgx-b300-8x`: on_demand 76.0 → 9.5  [REVIEW: pricing]; spot 36.0 → 10.4  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/1x/hgx-b300-1x`: spot 5.6 → 9.49  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/8x/hgx-b300-8x`: on_demand 76.0 → 9.5  [REVIEW: pricing]; spot 44.8 → 9.49  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/1x/hgx-b200-1x`: spot 3.0 → 2.5  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/8x/hgx-b200-8x`: on_demand 68.0 → 8.5  [REVIEW: pricing]; spot 24.0 → 2.5  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/1x/hgx-b200-1x`: spot 5.2 → 11.3  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/8x/hgx-b200-8x`: on_demand 68.0 → 8.5  [REVIEW: pricing]; spot 41.6 → 11.3  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/1x/hgx-h200-1x`: spot 2.18 → 2.3  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/8x/hgx-h200-8x`: on_demand 43.2 → 5.4  [REVIEW: pricing]; spot 17.44 → 2.3  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/1x/hgx-h200-1x`: spot 2.5 → 0.99  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/8x/hgx-h200-8x`: on_demand 43.2 → 5.4  [REVIEW: pricing]; spot 20.0 → 0.99  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/1x/hgx-h200-1x`: spot 2.78 → 2.48  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/8x/hgx-h200-8x`: on_demand 43.2 → 5.4  [REVIEW: pricing]; spot 22.24 → 2.48  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/1x/hgx-h100-1x`: spot 2.37 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/8x/hgx-h100-8x`: on_demand 36.0 → 4.5  [REVIEW: pricing]; spot 18.96 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 1.19 → 1.5  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/8x/rtx-pro-6000-8x`: on_demand 14.4 → 1.8  [REVIEW: pricing]; spot 9.52 → 1.5  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/8x/rtx-pro-6000-8x`: on_demand 14.4 → 1.8  [REVIEW: pricing]; spot 11.04 → 1.38  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 1.68 → 1.38  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH2/RTX PRO 6000/8x/rtx-pro-6000-8x`: on_demand 14.4 → 1.8  [REVIEW: pricing]; spot 13.44 → 1.38  [REVIEW: pricing]
- Price history: 23 changed observation(s) appended to `data/price-history/nebius.jsonl`
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## verda

- CHANGED `verda/EU-FI/B300/1x/30cpu-255gb-268gb`: on_demand 12.53 → 13.05  [REVIEW: pricing]; spot 6.26 → 6.53  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/2x/60cpu-510gb-536gb`: on_demand 12.53 → 13.05  [REVIEW: pricing]; spot 6.26 → 6.53  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/4x/120cpu-1020gb-1072gb`: on_demand 12.53 → 13.05  [REVIEW: pricing]; spot 6.26 → 6.53  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/8x/240cpu-2040gb-2144gb`: on_demand 12.53 → 13.05  [REVIEW: pricing]; spot 6.26 → 6.53  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/1x/30cpu-170gb-180gb`: on_demand 9.6 → 9.75  [REVIEW: pricing]; spot 4.8 → 4.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/2x/60cpu-340gb-360gb`: on_demand 9.61 → 9.74  [REVIEW: pricing]; spot 4.8 → 4.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/4x/120cpu-680gb-720gb`: on_demand 9.6 → 9.75  [REVIEW: pricing]; spot 4.8 → 4.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/8x/240cpu-1360gb-1440gb`: on_demand 9.6 → 9.75  [REVIEW: pricing]; spot 4.8 → 4.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/1x/44cpu-170gb-141gb`: on_demand 6.77 → 7.04  [REVIEW: pricing]; spot 3.38 → 3.52  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/2x/88cpu-340gb-282gb`: on_demand 6.77 → 7.04  [REVIEW: pricing]; spot 3.38 → 3.52  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/4x/176cpu-680gb-564gb`: on_demand 6.77 → 7.04  [REVIEW: pricing]; spot 3.38 → 3.52  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/8x/176cpu-1360gb-1128gb`: on_demand 6.77 → 7.04  [REVIEW: pricing]; spot 3.38 → 3.52  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/30cpu-120gb-80gb`: on_demand 5.29 → 5.51  [REVIEW: pricing]; spot 2.65 → 2.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/32cpu-170gb-80gb`: on_demand 5.29 → 5.51  [REVIEW: pricing]; spot 2.65 → 2.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/2x/80cpu-340gb-160gb`: on_demand 5.29 → 5.51  [REVIEW: pricing]; spot 2.65 → 2.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/4x/176cpu-680gb-320gb`: on_demand 5.29 → 5.51  [REVIEW: pricing]; spot 2.65 → 2.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/8x/176cpu-1360gb-640gb`: on_demand 5.29 → 5.51  [REVIEW: pricing]; spot 2.65 → 2.75  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/1x/22cpu-120gb-80gb`: on_demand 2.4 → 2.47  [REVIEW: pricing]; spot 1.2 → 1.24  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/1x/22cpu-120gb-40gb`: on_demand 1.72 → 1.73  [REVIEW: pricing]; spot 0.86 → 0.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/2x/44cpu-240gb-160gb`: on_demand 2.4 → 2.47  [REVIEW: pricing]; spot 1.2 → 1.24  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/4x/88cpu-480gb-320gb`: on_demand 2.4 → 2.47  [REVIEW: pricing]; spot 1.2 → 1.24  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/8x/176cpu-960gb-640gb`: on_demand 2.4 → 2.47  [REVIEW: pricing]; spot 1.2 → 1.24  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/8x/176cpu-960gb-320gb`: on_demand 1.72 → 1.73  [REVIEW: pricing]; spot 0.86 → 0.87  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/1x/30cpu-90gb-96gb`: on_demand 2.86 → 2.98  [REVIEW: pricing]; spot 1.43 → 1.49  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/2x/60cpu-180gb-192gb`: on_demand 2.86 → 2.98  [REVIEW: pricing]; spot 1.43 → 1.49  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/4x/120cpu-360gb-384gb`: on_demand 2.87 → 2.98  [REVIEW: pricing]; spot 1.43 → 1.49  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/8x/240cpu-720gb-768gb`: on_demand 2.86 → 2.98  [REVIEW: pricing]; spot 1.43 → 1.49  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/1x/20cpu-60gb-48gb`: on_demand 2.04 → 2.08  [REVIEW: pricing]; spot 1.02 → 1.04  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/2x/40cpu-120gb-96gb`: on_demand 2.04 → 2.08  [REVIEW: pricing]; spot 1.02 → 1.04  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/4x/80cpu-240gb-192gb`: on_demand 2.04 → 2.08  [REVIEW: pricing]; spot 1.02 → 1.04  [REVIEW: pricing]
- CHANGED `verda/EU-FI/L40S/8x/160cpu-480gb-384gb`: on_demand 2.04 → 2.08  [REVIEW: pricing]; spot 1.02 → 1.04  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/1x/10cpu-60gb-48gb`: on_demand 1.62 → 1.67  [REVIEW: pricing]; spot 0.81 → 0.84  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/2x/20cpu-120gb-96gb`: on_demand 1.62 → 1.67  [REVIEW: pricing]; spot 0.81 → 0.84  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/4x/40cpu-240gb-192gb`: on_demand 1.62 → 1.67  [REVIEW: pricing]; spot 0.81 → 0.84  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/8x/80cpu-480gb-384gb`: on_demand 1.62 → 1.67  [REVIEW: pricing]; spot 0.81 → 0.84  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/1x/10cpu-60gb-48gb`: on_demand 0.9 → 0.93  [REVIEW: pricing]; spot 0.45 → 0.47  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/2x/20cpu-120gb-96gb`: on_demand 0.9 → 0.93  [REVIEW: pricing]; spot 0.45 → 0.47  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/4x/40cpu-240gb-192gb`: on_demand 0.9 → 0.93  [REVIEW: pricing]; spot 0.45 → 0.47  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/8x/80cpu-480gb-384gb`: on_demand 0.9 → 0.93  [REVIEW: pricing]; spot 0.45 → 0.47  [REVIEW: pricing]
- Price history: 39 changed observation(s) appended to `data/price-history/verda.jsonl`
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

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 4c5e3d1d3b1b
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 6473 B sha1 dac4588b39ec
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4966 B sha1 77af8958ea75
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 82b6a65bbf6a
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 2ce2ac5a57d8
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 87f39a8a4ed7
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 10f8e9412520
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 94f056d5ee33
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 cbb9887b8999
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 0f6c92c914e0
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 01968b332e76
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 a507e67b9346
- `jl gpus --json` 3240 B sha1 a0ab0203cc3a
- `https://jarvislabs.ai/pricing` 199139 B sha1 e42fb1711217
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 114498 B sha1 d13e762c976e
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 113832 B sha1 a3ca37668d9b
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 113521 B sha1 5cf8d1921aeb
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 114151 B sha1 666e2fc799dc
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 114086 B sha1 08edfc076eff
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 113765 B sha1 169c7fcd9b1e
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 113173 B sha1 ab938f346589
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 114195 B sha1 a86530061df0
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 114486 B sha1 1408904dd348
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 113594 B sha1 809b25f8a39e
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 113548 B sha1 2fb045c8241c
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 114484 B sha1 805d2b2087a2
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 113866 B sha1 e7e2abb0d80e
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 113528 B sha1 d2083ec80455
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 114170 B sha1 b96829fc4948
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 114114 B sha1 8fc6ca14ca3f
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 113790 B sha1 a1369a793186
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 113452 B sha1 11a0fea21aac
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 114464 B sha1 d579f072ef7b
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 114771 B sha1 8d3f8a3eda18
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 113879 B sha1 610760194d22
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 113810 B sha1 4f8804cc333b
- `https://neysa.ai/pricing/` 327967 B sha1 66b112664575
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 131248 B sha1 7b0df72d94e8
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145743 B sha1 17cf781a97df
- `https://cyfuture.ai/pricing` 521481 B sha1 6e5e4fbec011
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301290 B sha1 d75f849133e5
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1383 B sha1 abc68ea42e0a
- `https://www.olakrutrim.com/gpu-services` 47034 B sha1 a5406c841fb6
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35966 B sha1 3965c00c24c8
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21592 B sha1 9b37a71c9220
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7932461 B sha1 8a740962fbb8
- `https://nebius.com/prices` 280264 B sha1 67832c68de7f
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3530 B sha1 fa1ef928cb9c
- `https://api.verda.com/v1/instance-types` 184775 B sha1 b953dc465124
- `https://www.hyperstack.cloud/gpu-pricing` 148668 B sha1 113215cef9c5


---

# Pricing refresh 2026-11-21 10:14 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=0, unchanged=439, stale=11, retired=0, failed=0, price_rows=0

## e2e-networks

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
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

- no changes
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- no changes

## nxtgen

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)

## leapswitch

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)

## cyfuture-ai

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review

## tata-communications

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)

## yotta-shakti

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)

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
- WARNING: unmapped AWS accelerated type g7.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## ovhcloud

- FX: USD/INR 92.6752 (2026-11-20, ECB reference rate)
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

- no changes
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

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 b0b27db89436
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 6473 B sha1 dac4588b39ec
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4966 B sha1 77af8958ea75
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 82b6a65bbf6a
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 2ce2ac5a57d8
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 87f39a8a4ed7
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 10f8e9412520
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 94f056d5ee33
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 cbb9887b8999
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 0f6c92c914e0
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 01968b332e76
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 a507e67b9346
- `jl gpus --json` 3240 B sha1 0dbcf0e1ffb9
- `https://jarvislabs.ai/pricing` 199139 B sha1 e42fb1711217
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 114498 B sha1 1dd2b431f77a
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 113832 B sha1 7a32516fc0de
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 113521 B sha1 bc117e239b18
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 114151 B sha1 7ca5954c9fe1
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 114086 B sha1 9652c321cd01
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 113765 B sha1 c49b6803cc35
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 113173 B sha1 16799fd78caf
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 114195 B sha1 acc37f234263
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 114486 B sha1 4d2cb1b9a556
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 113594 B sha1 0ace2ccd782e
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 113548 B sha1 7e5796469985
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 114484 B sha1 6cad48253ff7
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 113866 B sha1 5a104e8369f4
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 113528 B sha1 96ca41e19d7d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 114170 B sha1 ed06a6d56f9e
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 114114 B sha1 98224d6c56de
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 113790 B sha1 48364619461b
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 113189 B sha1 151cf07cb9a6
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 114201 B sha1 ce86e820b2e2
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 114508 B sha1 02250ed2b6af
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 113616 B sha1 e143cac87964
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 113547 B sha1 86cb75d2b516
- `https://neysa.ai/pricing/` 327967 B sha1 16020ec9ce6c
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 131248 B sha1 7b0df72d94e8
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145743 B sha1 4cc35654407d
- `https://cyfuture.ai/pricing` 521481 B sha1 247d19ddded3
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301290 B sha1 d75f849133e5
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1383 B sha1 abc68ea42e0a
- `https://www.olakrutrim.com/gpu-services` 47032 B sha1 f9db99128803
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35966 B sha1 3965c00c24c8
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21592 B sha1 9b37a71c9220
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7932461 B sha1 8a740962fbb8
- `https://nebius.com/prices` 280264 B sha1 67832c68de7f
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3530 B sha1 94f87d2256bf
- `https://api.verda.com/v1/instance-types` 184775 B sha1 b953dc465124
- `https://www.hyperstack.cloud/gpu-pricing` 148668 B sha1 113215cef9c5

