# Pricing refresh 2026-11-28 00:04 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=113, unchanged=307, stale=30, retired=0, failed=0, price_rows=113

## e2e-networks

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {3: 7.39} → {3: 7.34}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: committed {3: 5.0} → {3: 4.97}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: spot 0.76 → 0.75  [REVIEW: pricing]; committed {3: 3.76} → {3: 3.74}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {3: 2.35} → {3: 2.34}  [REVIEW: pricing]
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

- STALE `skus/neysa/IN-BOM/B300/8x/bare-metal-quote.json` — no current source covers B300 8x; left for human review
- STALE `skus/neysa/IN-BOM/H100/1x/standard.json` — no current source covers H100 1x; left for human review
- STALE `skus/neysa/IN-BOM/H100/2x/standard.json` — no current source covers H100 2x; left for human review
- STALE `skus/neysa/IN-BOM/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/neysa/IN-BOM/H100/8x/bare-metal-reserved.json` — no current source covers H100 8x; left for human review
- STALE `skus/neysa/IN-BOM/H200/1x/standard.json` — no current source covers H200 1x; left for human review
- STALE `skus/neysa/IN-BOM/H200/2x/standard.json` — no current source covers H200 2x; left for human review
- STALE `skus/neysa/IN-BOM/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- STALE `skus/neysa/IN-BOM/H200/8x/bare-metal-reserved.json` — no current source covers H200 8x; left for human review
- STALE `skus/neysa/IN-BOM/L4/1x/standard.json` — no current source covers L4 1x; left for human review
- STALE `skus/neysa/IN-BOM/L4/2x/standard.json` — no current source covers L4 2x; left for human review
- STALE `skus/neysa/IN-BOM/L4/4x/standard.json` — no current source covers L4 4x; left for human review
- STALE `skus/neysa/IN-BOM/L40S/1x/standard.json` — no current source covers L40S 1x; left for human review
- STALE `skus/neysa/IN-BOM/L40S/2x/standard.json` — no current source covers L40S 2x; left for human review
- STALE `skus/neysa/IN-BOM/L40S/4x/standard.json` — no current source covers L40S 4x; left for human review
- STALE `skus/neysa/IN-BOM/L40S/8x/bare-metal-reserved.json` — no current source covers L40S 8x; left for human review
- STALE `skus/neysa/IN-BOM/MI300X/8x/bare-metal-reserved.json` — no current source covers MI300X 8x; left for human review
- STALE `skus/neysa/IN-BOM/RTX PRO 6000/1x/quote.json` — no current source covers RTX PRO 6000 1x; left for human review
- STALE `skus/neysa/IN-BOM/RTX PRO 6000/8x/bare-metal-quote.json` — no current source covers RTX PRO 6000 8x; left for human review
- WARNING: shape statement '1x, 2x and 4x' not found; shapes may have changed
- WARNING: no per-GPU rows parsed

## nxtgen

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.08 → 3.06  [REVIEW: pricing]; committed {1: 2.47, 6: 2.47, 12: 1.97} → {1: 2.45, 6: 2.45, 12: 1.96}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H200/8x/standard`: on_demand 3.08 → 3.06  [REVIEW: pricing]; committed {1: 2.46, 6: 2.46, 12: 1.97} → {1: 2.45, 6: 2.45, 12: 1.96}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.67 → 2.66  [REVIEW: pricing]; committed {1: 2.14, 6: 2.14, 12: 1.71} → {1: 2.13, 6: 2.13, 12: 1.7}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/L40S/1x/standard`: on_demand 1.59 → 1.58  [REVIEW: pricing]; committed {1: 1.28, 6: 1.28, 12: 1.02} → {1: 1.27, 6: 1.27, 12: 1.01}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.71 → 2.7  [REVIEW: pricing]; committed {1: 2.17, 6: 2.17, 12: 1.74} → {1: 2.16, 6: 2.16, 12: 1.73}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/8x/standard`: on_demand 2.72 → 2.7  [REVIEW: pricing]; committed {1: 2.17, 6: 2.17, 12: 1.74} → {1: 2.16, 6: 2.16, 12: 1.73}  [REVIEW: pricing]
- Price history: 6 changed observation(s) appended to `data/price-history/nxtgen.jsonl`

## leapswitch

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.37 → 4.35  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: on_demand 1.98 → 1.97  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A5000/1x/standard`: on_demand 0.3 → 0.29  [REVIEW: pricing]
- CHANGED `leapswitch/IN/A100/1x/standard`: on_demand 1.65 → 1.64  [REVIEW: pricing]

## cyfuture-ai

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `cyfuture-ai/IN/B300/1x/standard`: committed {1: 8.22, 6: 7.71, 12: 6.17} → {1: 8.17, 6: 7.66, 12: 6.13}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/2x/standard`: committed {1: 8.22, 6: 7.71, 12: 6.17} → {1: 8.17, 6: 7.66, 12: 6.13}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/4x/standard`: committed {1: 6.17, 6: 5.78, 12: 4.62} → {1: 6.13, 6: 5.75, 12: 4.6}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/8x/standard`: committed {1: 4.11, 6: 3.85, 12: 3.08} → {1: 4.09, 6: 3.83, 12: 3.06}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: on_demand 2.77 → 2.76  [REVIEW: pricing]; committed {1: 2.62, 6: 2.47, 12: 2.31} → {1: 2.6, 6: 2.45, 12: 2.3}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: on_demand 2.77 → 2.76  [REVIEW: pricing]; committed {1: 2.62, 6: 2.47, 12: 2.31} → {1: 2.6, 6: 2.45, 12: 2.3}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: on_demand 2.77 → 2.76  [REVIEW: pricing]; committed {1: 2.62, 6: 2.47, 12: 2.31} → {1: 2.6, 6: 2.45, 12: 2.3}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: on_demand 2.77 → 2.76  [REVIEW: pricing]; committed {1: 2.62, 6: 2.47, 12: 2.31} → {1: 2.6, 6: 2.45, 12: 2.3}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/1x/standard`: on_demand 1.34 → 1.33  [REVIEW: pricing]; committed {1: 0.8, 6: 0.74, 12: 0.66} → {1: 0.8, 6: 0.73, 12: 0.66}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/2x/standard`: on_demand 1.33 → 1.32  [REVIEW: pricing]; committed {1: 0.78, 6: 0.71, 12: 0.64} → {1: 0.78, 6: 0.7, 12: 0.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/4x/standard`: on_demand 1.31 → 1.3  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: on_demand 1.3 → 1.29  [REVIEW: pricing]; committed {1: 0.77, 6: 0.69, 12: 0.62} → {1: 0.76, 6: 0.69, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: on_demand 2.96 → 2.95  [REVIEW: pricing]; committed {1: 2.37, 6: 2.13, 12: 1.77} → {1: 2.35, 6: 2.12, 12: 1.76}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: on_demand 2.93 → 2.91  [REVIEW: pricing]; committed {1: 2.32, 6: 2.07, 12: 1.7} → {1: 2.31, 6: 2.05, 12: 1.69}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: on_demand 2.9 → 2.89  [REVIEW: pricing]; committed {1: 2.3, 6: 2.04, 12: 1.68} → {1: 2.28, 6: 2.03, 12: 1.67}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: on_demand 2.87 → 2.86  [REVIEW: pricing]; committed {1: 2.27, 6: 2.02, 12: 1.67} → {1: 2.26, 6: 2.01, 12: 1.66}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.56 → 3.54  [REVIEW: pricing]; committed {1: 3.2, 6: 2.84, 12: 2.37} → {1: 3.18, 6: 2.83, 12: 2.35}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: on_demand 3.52 → 3.5  [REVIEW: pricing]; committed {1: 3.14, 6: 2.76, 12: 2.27} → {1: 3.12, 6: 2.74, 12: 2.26}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: on_demand 3.49 → 3.46  [REVIEW: pricing]; committed {1: 3.1, 6: 2.73, 12: 2.25} → {1: 3.09, 6: 2.71, 12: 2.24}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: on_demand 3.45 → 3.43  [REVIEW: pricing]; committed {1: 3.07, 6: 2.7, 12: 2.23} → {1: 3.05, 6: 2.69, 12: 2.21}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: committed {1: 0.52, 6: 0.47, 12: 0.42} → {1: 0.52, 6: 0.46, 12: 0.42}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/4x/standard`: committed {1: 0.51, 6: 0.45, 12: 0.39} → {1: 0.51, 6: 0.44, 12: 0.39}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/8x/standard`: on_demand 0.57 → 0.56  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: on_demand 2.14 → 2.13  [REVIEW: pricing]; committed {1: 2.12, 6: 2.1, 12: 2.02} → {1: 2.11, 6: 2.09, 12: 2.01}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: on_demand 2.12 → 2.11  [REVIEW: pricing]; committed {1: 2.08, 6: 2.03, 12: 1.94} → {1: 2.06, 6: 2.02, 12: 1.93}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: on_demand 2.1 → 2.09  [REVIEW: pricing]; committed {1: 2.06, 6: 2.01, 12: 1.92} → {1: 2.04, 6: 2.0, 12: 1.91}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: on_demand 2.08 → 2.06  [REVIEW: pricing]; committed {1: 2.03, 6: 1.99, 12: 1.9} → {1: 2.02, 6: 1.98, 12: 1.89}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: committed {1: 0.88, 6: 0.75, 12: 0.64} → {1: 0.87, 6: 0.74, 12: 0.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: committed {1: 0.87, 6: 0.72, 12: 0.62} → {1: 0.86, 6: 0.72, 12: 0.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/8x/standard`: committed {1: 0.85, 6: 0.71, 12: 0.6} → {1: 0.84, 6: 0.71, 12: 0.6}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: on_demand 3.22 → 3.2  [REVIEW: pricing]; committed {1: 2.35, 6: 1.96, 12: 1.62} → {1: 2.33, 6: 1.95, 12: 1.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: on_demand 3.19 → 3.17  [REVIEW: pricing]; committed {1: 2.3, 6: 1.89, 12: 1.56} → {1: 2.28, 6: 1.88, 12: 1.55}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: on_demand 3.16 → 3.14  [REVIEW: pricing]; committed {1: 2.28, 6: 1.87, 12: 1.55} → {1: 2.26, 6: 1.86, 12: 1.54}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: on_demand 3.12 → 3.11  [REVIEW: pricing]; committed {1: 2.25, 6: 1.86, 12: 1.53} → {1: 2.24, 6: 1.84, 12: 1.52}  [REVIEW: pricing]
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review
- Price history: 36 changed observation(s) appended to `data/price-history/cyfuture-ai.jsonl`

## tata-communications

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: on_demand 5.28 → 5.25  [REVIEW: pricing]; committed {3: 5.13, 6: 4.55, 12: 4.05, 36: 3.83, 48: 3.64} → {3: 5.1, 6: 4.53, 12: 4.02, 36: 3.81, 48: 3.62}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: on_demand 5.74 → 5.71  [REVIEW: pricing]; committed {3: 5.58, 6: 4.95, 12: 4.4, 36: 4.17, 48: 3.96} → {3: 5.55, 6: 4.92, 12: 4.38, 36: 4.15, 48: 3.94}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: on_demand 5.57 → 5.54  [REVIEW: pricing]; committed {3: 5.42, 6: 4.81, 12: 4.27, 36: 4.05, 48: 3.85} → {3: 5.38, 6: 4.78, 12: 4.25, 36: 4.02, 48: 3.82}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: on_demand 3.17 → 3.16  [REVIEW: pricing]; committed {3: 3.09, 6: 2.74, 12: 2.43, 36: 2.31, 48: 2.19} → {3: 3.07, 6: 2.72, 12: 2.42, 36: 2.29, 48: 2.18}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: on_demand 4.35 → 4.32  [REVIEW: pricing]; committed {3: 4.23, 6: 3.75, 12: 3.33, 36: 3.16, 48: 3.01} → {3: 4.2, 6: 3.73, 12: 3.31, 36: 3.14, 48: 2.99}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: on_demand 4.72 → 4.69  [REVIEW: pricing]; committed {3: 4.59, 6: 4.07, 12: 3.61, 36: 3.43, 48: 3.26} → {3: 4.56, 6: 4.04, 12: 3.59, 36: 3.41, 48: 3.24}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: on_demand 4.88 → 4.85  [REVIEW: pricing]; committed {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.55, 48: 3.36} → {3: 4.71, 6: 4.18, 12: 3.72, 36: 3.53, 48: 3.34}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: on_demand 4.35 → 4.33  [REVIEW: pricing]; committed {3: 4.23, 6: 3.75, 12: 3.34, 36: 3.16, 48: 3.0} → {3: 4.2, 6: 3.73, 12: 3.32, 36: 3.14, 48: 2.98}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: on_demand 4.72 → 4.69  [REVIEW: pricing]; committed {3: 4.59, 6: 4.07, 12: 3.62, 36: 3.43, 48: 3.26} → {3: 4.56, 6: 4.04, 12: 3.6, 36: 3.41, 48: 3.24}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: on_demand 4.88 → 4.85  [REVIEW: pricing]; committed {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.54, 48: 3.37} → {3: 4.71, 6: 4.18, 12: 3.72, 36: 3.52, 48: 3.35}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: on_demand 5.14 → 5.11  [REVIEW: pricing]; committed {3: 5.0, 6: 4.43, 12: 3.94, 36: 3.73, 48: 3.55} → {3: 4.97, 6: 4.41, 12: 3.92, 36: 3.71, 48: 3.53}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: on_demand 5.87 → 5.84  [REVIEW: pricing]; committed {3: 5.71, 6: 5.06, 12: 4.5, 36: 4.27, 48: 4.05} → {3: 5.67, 6: 5.03, 12: 4.47, 36: 4.24, 48: 4.03}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: on_demand 4.88 → 4.85  [REVIEW: pricing]; committed {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.55, 48: 3.37} → {3: 4.71, 6: 4.18, 12: 3.72, 36: 3.52, 48: 3.35}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: on_demand 2.16 → 2.15  [REVIEW: pricing]; committed {3: 2.1, 6: 1.87, 12: 1.65, 36: 1.57, 48: 1.49} → {3: 2.09, 6: 1.86, 12: 1.65, 36: 1.56, 48: 1.48}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: on_demand 2.36 → 2.34  [REVIEW: pricing]; committed {3: 2.29, 6: 2.03, 12: 1.81, 36: 1.71, 48: 1.62} → {3: 2.28, 6: 2.02, 12: 1.8, 36: 1.7, 48: 1.61}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: on_demand 2.44 → 2.43  [REVIEW: pricing]; committed {3: 2.37, 6: 2.11, 12: 1.87, 36: 1.77, 48: 1.69} → {3: 2.35, 6: 2.1, 12: 1.86, 36: 1.76, 48: 1.68}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: on_demand 2.52 → 2.51  [REVIEW: pricing]; committed {3: 2.46, 6: 2.17, 12: 1.94, 36: 1.84, 48: 1.74} → {3: 2.44, 6: 2.16, 12: 1.92, 36: 1.83, 48: 1.73}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: on_demand 2.16 → 2.15  [REVIEW: pricing]; committed {3: 2.1, 6: 1.87, 12: 1.66, 36: 1.57, 48: 1.49} → {3: 2.09, 6: 1.85, 12: 1.65, 36: 1.56, 48: 1.48}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: on_demand 2.36 → 2.34  [REVIEW: pricing]; committed {3: 2.29, 6: 2.03, 12: 1.81, 36: 1.71, 48: 1.63} → {3: 2.28, 6: 2.02, 12: 1.8, 36: 1.7, 48: 1.62}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: on_demand 2.53 → 2.51  [REVIEW: pricing]; committed {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.83, 48: 1.74} → {3: 2.44, 6: 2.17, 12: 1.92, 36: 1.82, 48: 1.73}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: committed {3: 0.94, 6: 0.84, 12: 0.75, 36: 0.7, 48: 0.67} → {3: 0.94, 6: 0.84, 12: 0.74, 36: 0.7, 48: 0.67}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: on_demand 1.05 → 1.04  [REVIEW: pricing]; committed {3: 1.02, 6: 0.91, 12: 0.8, 36: 0.76, 48: 0.72} → {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.75, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: committed {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.76}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: on_demand 1.27 → 1.26  [REVIEW: pricing]; committed {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.92, 48: 0.88} → {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.91, 48: 0.87}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: on_demand 1.05 → 1.04  [REVIEW: pricing]; committed {3: 1.02, 6: 0.9, 12: 0.81, 36: 0.76, 48: 0.72} → {3: 1.02, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: committed {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.76}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: on_demand 1.27 → 1.26  [REVIEW: pricing]; committed {3: 1.23, 6: 1.1, 12: 0.97, 36: 0.92, 48: 0.88} → {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.92, 48: 0.87}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: committed {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72} → {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.75, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu`: on_demand 1.16 → 1.15  [REVIEW: pricing]; committed {3: 1.13, 6: 1.0, 12: 0.89, 36: 0.84, 48: 0.8} → {3: 1.12, 6: 0.99, 12: 0.88, 36: 0.84, 48: 0.8}  [REVIEW: pricing]
- Price history: 29 changed observation(s) appended to `data/price-history/tata-communications.jsonl`

## yotta-shakti

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 4.63 → 4.6  [REVIEW: pricing]; committed {6: 4.11, 12: 3.81, 24: 3.4} → {6: 4.09, 12: 3.78, 24: 3.38}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: on_demand 2.57 → 2.56  [REVIEW: pricing]; committed {6: 2.16, 12: 1.96, 24: 1.75} → {6: 2.15, 12: 1.95, 24: 1.74}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 5.12 → 5.09  [REVIEW: pricing]; committed {6: 5.12, 12: 5.12, 24: 5.12, 36: 4.09, 48: 3.42, 60: 3.02} → {6: 5.09, 12: 5.09, 24: 5.09, 36: 4.06, 48: 3.4, 60: 3.0}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: committed {12: 11.42, 24: 9.35, 36: 7.27, 48: 5.19, 60: 4.11} → {12: 11.35, 24: 9.29, 36: 7.23, 48: 5.16, 60: 4.09}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 6.45 → 6.41  [REVIEW: pricing]; committed {1: 5.82, 3: 5.64, 6: 5.53, 12: 5.35} → {1: 5.78, 3: 5.61, 6: 5.5, 12: 5.32}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 6.35 → 6.32  [REVIEW: pricing]; committed {1: 5.73, 3: 5.56, 6: 5.44, 12: 5.27} → {1: 5.69, 3: 5.52, 6: 5.41, 12: 5.24}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 6.33 → 6.29  [REVIEW: pricing]; committed {1: 5.7, 3: 5.53, 6: 5.41, 12: 5.24} → {1: 5.66, 3: 5.49, 6: 5.38, 12: 5.21}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: on_demand 3.27 → 3.25  [REVIEW: pricing]; committed {1: 2.64, 3: 2.56, 6: 2.51, 12: 2.43} → {1: 2.62, 3: 2.54, 6: 2.49, 12: 2.41}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: on_demand 3.21 → 3.19  [REVIEW: pricing]; committed {1: 2.58, 3: 2.5, 6: 2.45, 12: 2.37} → {1: 2.56, 3: 2.49, 6: 2.44, 12: 2.36}  [REVIEW: pricing]
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

- FX: USD/INR 93.0036 (2026-11-27, ECB reference rate)
- CHANGED `ovhcloud/EU-FR/A100/1x/a100-180`: on_demand 3.02 → 3.01  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/2x/a100-360`: on_demand 3.02 → 3.01  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/4x/a100-720`: on_demand 3.02 → 3.01  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/1x/h100-380`: committed {1: 2.92} → {1: 2.91}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/2x/h100-760`: committed {1: 2.92} → {1: 2.91}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920`: on_demand 5.76 → 5.75  [REVIEW: pricing]; committed {1: 5.76} → {1: 5.75}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920-eph`: on_demand 5.76 → 5.75  [REVIEW: pricing]; committed {1: 5.76} → {1: 5.75}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/win-l4-90`: on_demand 1.66 → 1.65  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/2x/l40s-180`: on_demand 1.54 → 1.53  [REVIEW: pricing]; committed {1: 1.52} → {1: 1.51}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/4x/l40s-360`: on_demand 1.54 → 1.53  [REVIEW: pricing]; committed {1: 1.52} → {1: 1.51}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/1x/l40s-90`: on_demand 1.54 → 1.53  [REVIEW: pricing]; committed {1: 1.52} → {1: 1.51}  [REVIEW: pricing]
- Price history: 13 changed observation(s) appended to `data/price-history/ovhcloud.jsonl`
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

- CHANGED `nebius/EU-WEST2/B300/1x/hgx-b300-1x`: spot 4.7 → 3.5  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST2/B300/8x/hgx-b300-8x`: spot 4.7 → 3.5  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/1x/hgx-b300-1x`: spot 4.9 → 1.9  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/8x/hgx-b300-8x`: spot 4.9 → 1.9  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/1x/hgx-b300-1x`: spot 5.3 → 2.0  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/8x/hgx-b300-8x`: spot 5.3 → 2.0  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/1x/hgx-b200-1x`: spot 3.5 → 4.1  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/8x/hgx-b200-8x`: spot 3.5 → 4.1  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/1x/hgx-b200-1x`: spot 3.1 → 2.5  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/8x/hgx-b200-8x`: spot 3.1 → 2.5  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/1x/hgx-h200-1x`: spot 2.0 → 1.4  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/8x/hgx-h200-8x`: spot 2.0 → 1.4  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/1x/hgx-h200-1x`: spot 2.8 → 1.69  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/8x/hgx-h200-8x`: spot 2.8 → 1.69  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 0.9 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 0.9 → 0.79  [REVIEW: pricing]
- Price history: 16 changed observation(s) appended to `data/price-history/nebius.jsonl`
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

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 6e4b69489e4c
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 6473 B sha1 61dfcc8e15ad
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4966 B sha1 63ad48a7bc99
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 3fd0881fb571
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 8263461944d3
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 722f6d318930
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 1a2e75c4e9c2
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 dd864049e427
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 6811938088dd
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 aa1f93271b1e
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 05213895f3ce
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 c4db5b2466aa
- `jl gpus --json` 3240 B sha1 9ff818df09af
- `https://jarvislabs.ai/pricing` 156217 B sha1 e9bb3cf6c886
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 114366 B sha1 f700b9c67942
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 113700 B sha1 05db68535fb5
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 113389 B sha1 6379571b5fac
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 114019 B sha1 04e59cc6d197
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 113954 B sha1 ccc577d1ba96
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 113633 B sha1 5e39031e0950
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 113041 B sha1 5017576610cc
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 114063 B sha1 1c62b151f899
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 114354 B sha1 36054ce759f4
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 113462 B sha1 f7dbe83c1c84
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 113416 B sha1 a2be84094375
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 114352 B sha1 c89eed413db6
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 113734 B sha1 523d1cb6e34e
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 113396 B sha1 a20c4520a6a4
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 114038 B sha1 ba02e811de82
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 113982 B sha1 8573c0fc3834
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 113658 B sha1 caa9dac152ee
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 113057 B sha1 6c6051d3c13f
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 114069 B sha1 361ddeedace0
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 114376 B sha1 d60bb9c985b5
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 113484 B sha1 aa75cfaaccda
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 113415 B sha1 373c5c30c265
- `https://neysa.ai/pricing/` 12104 B sha1 8059d95ef436
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 131248 B sha1 7b0df72d94e8
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145741 B sha1 6a002322f066
- `https://cyfuture.ai/pricing` 523485 B sha1 aae7779bcd63
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301291 B sha1 9ae5c13b49bb
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1508 B sha1 f8e4c0633daf
- `https://www.olakrutrim.com/gpu-services` 47035 B sha1 5ffe869b08de
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 104579 B sha1 0f2cc3885d5b
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45958 B sha1 e054072629de
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35940 B sha1 46028dc0f1e1
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21634 B sha1 8757aa67352f
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7991523 B sha1 199fc022c34a
- `https://nebius.com/prices` 280525 B sha1 5835c3399987
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3527 B sha1 2339c59c5edc
- `https://api.verda.com/v1/instance-types` 188477 B sha1 f603022ce992
- `https://www.hyperstack.cloud/gpu-pricing` 148668 B sha1 c8c5e365d7c4

