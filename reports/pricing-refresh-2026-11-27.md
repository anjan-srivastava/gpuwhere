# Pricing refresh 2026-11-27 00:02 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=151, unchanged=269, stale=30, retired=0, failed=0, price_rows=146

## e2e-networks

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {3: 7.41} → {3: 7.39}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: committed {3: 5.02} → {3: 5.0}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: committed {3: 3.77} → {3: 3.76}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {3: 2.36} → {3: 2.35}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/A100/1x/standard`: spot 0.72 → 0.71  [REVIEW: pricing]
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

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.09 → 3.08  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H200/8x/standard`: committed {1: 2.47, 6: 2.47, 12: 1.97} → {1: 2.46, 6: 2.46, 12: 1.97}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.68 → 2.67  [REVIEW: pricing]; committed {1: 2.15, 6: 2.15, 12: 1.71} → {1: 2.14, 6: 2.14, 12: 1.71}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.72 → 2.71  [REVIEW: pricing]; committed {1: 2.18, 6: 2.18, 12: 1.75} → {1: 2.17, 6: 2.17, 12: 1.74}  [REVIEW: pricing]
- CHANGED `nxtgen/IN/MI325X/8x/standard`: committed {1: 2.18, 6: 2.18, 12: 1.74} → {1: 2.17, 6: 2.17, 12: 1.74}  [REVIEW: pricing]
- Price history: 4 changed observation(s) appended to `data/price-history/nxtgen.jsonl`

## leapswitch

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.38 → 4.37  [REVIEW: pricing]
- CHANGED `leapswitch/IN/RTX A4000/1x/standard`: on_demand 0.22 → 0.21  [REVIEW: pricing]

## cyfuture-ai

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `cyfuture-ai/IN/B300/1x/standard`: committed {1: 8.24, 6: 7.72, 12: 6.18} → {1: 8.22, 6: 7.71, 12: 6.17}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/2x/standard`: committed {1: 8.24, 6: 7.72, 12: 6.18} → {1: 8.22, 6: 7.71, 12: 6.17}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/4x/standard`: committed {1: 6.18, 6: 5.79, 12: 4.63} → {1: 6.17, 6: 5.78, 12: 4.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/B300/8x/standard`: committed {1: 4.12, 6: 3.86, 12: 3.09} → {1: 4.11, 6: 3.85, 12: 3.08}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: on_demand 2.78 → 2.77  [REVIEW: pricing]; committed {1: 2.63, 6: 2.47, 12: 2.32} → {1: 2.62, 6: 2.47, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: on_demand 2.78 → 2.77  [REVIEW: pricing]; committed {1: 2.63, 6: 2.47, 12: 2.32} → {1: 2.62, 6: 2.47, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: on_demand 2.78 → 2.77  [REVIEW: pricing]; committed {1: 2.63, 6: 2.47, 12: 2.32} → {1: 2.62, 6: 2.47, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: on_demand 2.78 → 2.77  [REVIEW: pricing]; committed {1: 2.63, 6: 2.47, 12: 2.32} → {1: 2.62, 6: 2.47, 12: 2.31}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/2x/standard`: committed {1: 0.79, 6: 0.71, 12: 0.64} → {1: 0.78, 6: 0.71, 12: 0.64}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/4x/standard`: committed {1: 0.78, 6: 0.7, 12: 0.63} → {1: 0.77, 6: 0.7, 12: 0.63}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: committed {1: 0.77, 6: 0.7, 12: 0.62} → {1: 0.77, 6: 0.69, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: on_demand 2.97 → 2.96  [REVIEW: pricing]; committed {1: 2.37, 6: 2.14, 12: 1.78} → {1: 2.37, 6: 2.13, 12: 1.77}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: on_demand 2.94 → 2.93  [REVIEW: pricing]; committed {1: 2.33, 6: 2.07, 12: 1.71} → {1: 2.32, 6: 2.07, 12: 1.7}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: on_demand 2.91 → 2.9  [REVIEW: pricing]; committed {1: 2.3, 6: 2.05, 12: 1.69} → {1: 2.3, 6: 2.04, 12: 1.68}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: on_demand 2.88 → 2.87  [REVIEW: pricing]; committed {1: 2.28, 6: 2.03, 12: 1.67} → {1: 2.27, 6: 2.02, 12: 1.67}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.57 → 3.56  [REVIEW: pricing]; committed {1: 3.21, 6: 2.85, 12: 2.37} → {1: 3.2, 6: 2.84, 12: 2.37}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: on_demand 3.53 → 3.52  [REVIEW: pricing]; committed {1: 3.14, 6: 2.76, 12: 2.28} → {1: 3.14, 6: 2.76, 12: 2.27}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: committed {1: 3.11, 6: 2.74, 12: 2.26} → {1: 3.1, 6: 2.73, 12: 2.25}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: on_demand 3.46 → 3.45  [REVIEW: pricing]; committed {1: 3.08, 6: 2.71, 12: 2.23} → {1: 3.07, 6: 2.7, 12: 2.23}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: on_demand 0.59 → 0.58  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/V100/4x/standard`: committed {1: 0.51, 6: 0.45, 12: 0.4} → {1: 0.51, 6: 0.45, 12: 0.39}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: on_demand 2.15 → 2.14  [REVIEW: pricing]; committed {1: 2.13, 6: 2.1, 12: 2.03} → {1: 2.12, 6: 2.1, 12: 2.02}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: on_demand 2.13 → 2.12  [REVIEW: pricing]; committed {1: 2.08, 6: 2.04, 12: 1.95} → {1: 2.08, 6: 2.03, 12: 1.94}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: committed {1: 2.06, 6: 2.01, 12: 1.93} → {1: 2.06, 6: 2.01, 12: 1.92}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: committed {1: 2.04, 6: 1.99, 12: 1.91} → {1: 2.03, 6: 1.99, 12: 1.9}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: on_demand 1.1 → 1.09  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: committed {1: 0.87, 6: 0.73, 12: 0.62} → {1: 0.87, 6: 0.72, 12: 0.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/4x/standard`: on_demand 1.08 → 1.07  [REVIEW: pricing]; committed {1: 0.86, 6: 0.72, 12: 0.61} → {1: 0.85, 6: 0.72, 12: 0.61}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/Gaudi 2/8x/standard`: committed {1: 0.85, 6: 0.71, 12: 0.61} → {1: 0.85, 6: 0.71, 12: 0.6}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: on_demand 3.23 → 3.22  [REVIEW: pricing]; committed {1: 2.35, 6: 1.96, 12: 1.63} → {1: 2.35, 6: 1.96, 12: 1.62}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: on_demand 3.2 → 3.19  [REVIEW: pricing]; committed {1: 2.3, 6: 1.9, 12: 1.57} → {1: 2.3, 6: 1.89, 12: 1.56}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: committed {1: 2.28, 6: 1.88, 12: 1.55} → {1: 2.28, 6: 1.87, 12: 1.55}  [REVIEW: pricing]
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: on_demand 3.13 → 3.12  [REVIEW: pricing]; committed {1: 2.26, 6: 1.86, 12: 1.53} → {1: 2.25, 6: 1.86, 12: 1.53}  [REVIEW: pricing]
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review
- Price history: 32 changed observation(s) appended to `data/price-history/cyfuture-ai.jsonl`

## tata-communications

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: on_demand 5.29 → 5.28  [REVIEW: pricing]; committed {3: 5.14, 6: 4.56, 12: 4.06, 36: 3.84, 48: 3.65} → {3: 5.13, 6: 4.55, 12: 4.05, 36: 3.83, 48: 3.64}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: on_demand 5.76 → 5.74  [REVIEW: pricing]; committed {3: 5.59, 6: 4.96, 12: 4.41, 36: 4.18, 48: 3.97} → {3: 5.58, 6: 4.95, 12: 4.4, 36: 4.17, 48: 3.96}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: on_demand 5.59 → 5.57  [REVIEW: pricing]; committed {3: 5.43, 6: 4.82, 12: 4.28, 36: 4.06, 48: 3.85} → {3: 5.42, 6: 4.81, 12: 4.27, 36: 4.05, 48: 3.85}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: on_demand 3.18 → 3.17  [REVIEW: pricing]; committed {3: 3.09, 6: 2.74, 12: 2.44, 36: 2.31, 48: 2.2} → {3: 3.09, 6: 2.74, 12: 2.43, 36: 2.31, 48: 2.19}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: on_demand 4.36 → 4.35  [REVIEW: pricing]; committed {3: 4.24, 6: 3.76, 12: 3.34, 36: 3.17, 48: 3.01} → {3: 4.23, 6: 3.75, 12: 3.33, 36: 3.16, 48: 3.01}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: on_demand 4.73 → 4.72  [REVIEW: pricing]; committed {3: 4.6, 6: 4.08, 12: 3.62, 36: 3.44, 48: 3.26} → {3: 4.59, 6: 4.07, 12: 3.61, 36: 3.43, 48: 3.26}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: on_demand 4.89 → 4.88  [REVIEW: pricing]; committed {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.56, 48: 3.37} → {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.55, 48: 3.36}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: on_demand 4.36 → 4.35  [REVIEW: pricing]; committed {3: 4.24, 6: 3.76, 12: 3.34, 36: 3.17, 48: 3.01} → {3: 4.23, 6: 3.75, 12: 3.34, 36: 3.16, 48: 3.0}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: on_demand 4.73 → 4.72  [REVIEW: pricing]; committed {3: 4.6, 6: 4.08, 12: 3.63, 36: 3.44, 48: 3.26} → {3: 4.59, 6: 4.07, 12: 3.62, 36: 3.43, 48: 3.26}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: on_demand 4.89 → 4.88  [REVIEW: pricing]; committed {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.55, 48: 3.38} → {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.54, 48: 3.37}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: on_demand 5.15 → 5.14  [REVIEW: pricing]; committed {3: 5.01, 6: 4.45, 12: 3.95, 36: 3.74, 48: 3.56} → {3: 5.0, 6: 4.43, 12: 3.94, 36: 3.73, 48: 3.55}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: on_demand 5.89 → 5.87  [REVIEW: pricing]; committed {3: 5.72, 6: 5.07, 12: 4.51, 36: 4.28, 48: 4.06} → {3: 5.71, 6: 5.06, 12: 4.5, 36: 4.27, 48: 4.05}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: on_demand 4.89 → 4.88  [REVIEW: pricing]; committed {3: 4.75, 6: 4.22, 12: 3.75, 36: 3.55, 48: 3.37} → {3: 4.74, 6: 4.21, 12: 3.74, 36: 3.55, 48: 3.37}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: on_demand 2.17 → 2.16  [REVIEW: pricing]; committed {3: 2.1, 6: 1.88, 12: 1.66, 36: 1.57, 48: 1.5} → {3: 2.1, 6: 1.87, 12: 1.65, 36: 1.57, 48: 1.49}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: committed {3: 2.3, 6: 2.04, 12: 1.81, 36: 1.71, 48: 1.63} → {3: 2.29, 6: 2.03, 12: 1.81, 36: 1.71, 48: 1.62}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: on_demand 2.45 → 2.44  [REVIEW: pricing]; committed {3: 2.37, 6: 2.11, 12: 1.88, 36: 1.78, 48: 1.69} → {3: 2.37, 6: 2.11, 12: 1.87, 36: 1.77, 48: 1.69}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: on_demand 2.53 → 2.52  [REVIEW: pricing]; committed {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.84, 48: 1.75} → {3: 2.46, 6: 2.17, 12: 1.94, 36: 1.84, 48: 1.74}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: on_demand 2.17 → 2.16  [REVIEW: pricing]; committed {3: 2.11, 6: 1.87, 12: 1.66, 36: 1.58, 48: 1.5} → {3: 2.1, 6: 1.87, 12: 1.66, 36: 1.57, 48: 1.49}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: committed {3: 2.3, 6: 2.04, 12: 1.81, 36: 1.72, 48: 1.63} → {3: 2.29, 6: 2.03, 12: 1.81, 36: 1.71, 48: 1.63}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: committed {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.84, 48: 1.75} → {3: 2.46, 6: 2.18, 12: 1.94, 36: 1.83, 48: 1.74}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: on_demand 0.98 → 0.97  [REVIEW: pricing]; committed {3: 0.94, 6: 0.85, 12: 0.75, 36: 0.7, 48: 0.67} → {3: 0.94, 6: 0.84, 12: 0.75, 36: 0.7, 48: 0.67}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: committed {3: 1.02, 6: 0.91, 12: 0.8, 36: 0.76, 48: 0.73} → {3: 1.02, 6: 0.91, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: on_demand 1.12 → 1.11  [REVIEW: pricing]; committed {3: 1.08, 6: 0.96, 12: 0.86, 36: 0.81, 48: 0.77} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: committed {3: 1.24, 6: 1.1, 12: 0.98, 36: 0.92, 48: 0.88} → {3: 1.23, 6: 1.09, 12: 0.97, 36: 0.92, 48: 0.88}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: committed {3: 1.02, 6: 0.91, 12: 0.81, 36: 0.76, 48: 0.73} → {3: 1.02, 6: 0.9, 12: 0.81, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: on_demand 1.12 → 1.11  [REVIEW: pricing]; committed {3: 1.08, 6: 0.96, 12: 0.86, 36: 0.81, 48: 0.77} → {3: 1.08, 6: 0.96, 12: 0.85, 36: 0.81, 48: 0.77}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: committed {3: 1.24, 6: 1.1, 12: 0.98, 36: 0.93, 48: 0.88} → {3: 1.23, 6: 1.1, 12: 0.97, 36: 0.92, 48: 0.88}  [REVIEW: pricing]
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: on_demand 1.05 → 1.04  [REVIEW: pricing]; committed {3: 1.02, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72} → {3: 1.01, 6: 0.9, 12: 0.8, 36: 0.76, 48: 0.72}  [REVIEW: pricing]
- Price history: 29 changed observation(s) appended to `data/price-history/tata-communications.jsonl`

## yotta-shakti

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 4.64 → 4.63  [REVIEW: pricing]; committed {6: 4.12, 12: 3.82, 24: 3.4} → {6: 4.11, 12: 3.81, 24: 3.4}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: on_demand 2.58 → 2.57  [REVIEW: pricing]; committed {6: 2.17, 12: 1.96, 24: 1.76} → {6: 2.16, 12: 1.96, 24: 1.75}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 5.13 → 5.12  [REVIEW: pricing]; committed {6: 5.13, 12: 5.13, 24: 5.13, 36: 4.1, 48: 3.43, 60: 3.02} → {6: 5.12, 12: 5.12, 24: 5.12, 36: 4.09, 48: 3.42, 60: 3.02}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: committed {12: 11.45, 24: 9.37, 36: 7.29, 48: 5.2, 60: 4.12} → {12: 11.42, 24: 9.35, 36: 7.27, 48: 5.19, 60: 4.11}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 6.46 → 6.45  [REVIEW: pricing]; committed {1: 5.83, 3: 5.66, 6: 5.54, 12: 5.37} → {1: 5.82, 3: 5.64, 6: 5.53, 12: 5.35}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 6.37 → 6.35  [REVIEW: pricing]; committed {1: 5.74, 3: 5.57, 6: 5.45, 12: 5.28} → {1: 5.73, 3: 5.56, 6: 5.44, 12: 5.27}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 6.34 → 6.33  [REVIEW: pricing]; committed {1: 5.71, 3: 5.54, 6: 5.43, 12: 5.25} → {1: 5.7, 3: 5.53, 6: 5.41, 12: 5.24}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: committed {1: 2.65, 3: 2.57, 6: 2.51, 12: 2.43} → {1: 2.64, 3: 2.56, 6: 2.51, 12: 2.43}  [REVIEW: pricing]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: committed {1: 2.59, 3: 2.51, 6: 2.46, 12: 2.38} → {1: 2.58, 3: 2.5, 6: 2.45, 12: 2.37}  [REVIEW: pricing]
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

- FX: USD/INR 92.4501 (2026-11-26, ECB reference rate)
- CHANGED `ovhcloud/EU-FR/A100/1x/a100-180`: on_demand 3.01 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/2x/a100-360`: on_demand 3.01 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/A100/4x/a100-720`: on_demand 3.01 → 3.02  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/4x/h100-1520`: on_demand 3.06 → 3.07  [REVIEW: pricing]; committed {1: 2.91} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/1x/h100-380`: on_demand 3.06 → 3.07  [REVIEW: pricing]; committed {1: 2.91} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H100/2x/h100-760`: on_demand 3.06 → 3.07  [REVIEW: pricing]; committed {1: 2.91} → {1: 2.92}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920`: on_demand 5.74 → 5.76  [REVIEW: pricing]; committed {1: 5.74} → {1: 5.76}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/H200/8x/h200-1920-eph`: on_demand 5.74 → 5.76  [REVIEW: pricing]; committed {1: 5.74} → {1: 5.76}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/2x/win-l4-180`: on_demand 1.67 → 1.68  [REVIEW: pricing]; committed {1: 1.67} → {1: 1.68}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/4x/win-l4-360`: on_demand 1.67 → 1.68  [REVIEW: pricing]; committed {1: 1.67} → {1: 1.68}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L4/1x/win-l4-90`: on_demand 1.65 → 1.66  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/2x/l40s-180`: on_demand 1.53 → 1.54  [REVIEW: pricing]; committed {1: 1.51} → {1: 1.52}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/4x/l40s-360`: on_demand 1.53 → 1.54  [REVIEW: pricing]; committed {1: 1.51} → {1: 1.52}  [REVIEW: pricing]
- CHANGED `ovhcloud/EU-FR/L40S/1x/l40s-90`: on_demand 1.53 → 1.54  [REVIEW: pricing]; committed {1: 1.51} → {1: 1.52}  [REVIEW: pricing]
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

- CHANGED `nebius/EU-WEST2/B300/1x/hgx-b300-1x`: spot 3.6 → 4.7  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST2/B300/8x/hgx-b300-8x`: spot 3.6 → 4.7  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/1x/hgx-b300-1x`: spot 1.99 → 4.9  [REVIEW: pricing]
- CHANGED `nebius/UK-SOUTH1/B300/8x/hgx-b300-8x`: spot 1.99 → 4.9  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/1x/hgx-b300-1x`: spot 2.59 → 5.3  [REVIEW: pricing]
- CHANGED `nebius/US-NORTH1/B300/8x/hgx-b300-8x`: spot 2.59 → 5.3  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/1x/hgx-b200-1x`: spot 2.8 → 3.5  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/B200/8x/hgx-b200-8x`: spot 2.8 → 3.5  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/1x/hgx-b200-1x`: spot 3.9 → 3.1  [REVIEW: pricing]
- CHANGED `nebius/ME-WEST1/B200/8x/hgx-b200-8x`: spot 3.9 → 3.1  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/1x/hgx-h200-1x`: spot 1.4 → 2.0  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H200/8x/hgx-h200-8x`: spot 1.4 → 2.0  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/1x/hgx-h200-1x`: spot 0.79 → 1.7  [REVIEW: pricing]
- CHANGED `nebius/EU-WEST1/H200/8x/hgx-h200-8x`: spot 0.79 → 1.7  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/1x/hgx-h200-1x`: spot 0.79 → 2.8  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/H200/8x/hgx-h200-8x`: spot 0.79 → 2.8  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/1x/hgx-h100-1x`: spot 1.05 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/EU-NORTH1/H100/8x/hgx-h100-8x`: spot 1.05 → 0.79  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 0.89 → 0.9  [REVIEW: pricing]
- CHANGED `nebius/US-CENTRAL1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 0.89 → 0.9  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/1x/rtx-pro-6000-1x`: spot 1.09 → 1.38  [REVIEW: pricing]
- CHANGED `nebius/EU-SOUTH1/RTX PRO 6000/8x/rtx-pro-6000-8x`: spot 1.09 → 1.38  [REVIEW: pricing]
- Price history: 22 changed observation(s) appended to `data/price-history/nebius.jsonl`
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## verda

- CHANGED `verda/EU-FI/B300/1x/30cpu-255gb-268gb`: on_demand 13.31 → 12.53  [REVIEW: pricing]; spot 6.66 → 6.26  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/2x/60cpu-510gb-536gb`: on_demand 13.31 → 12.53  [REVIEW: pricing]; spot 6.66 → 6.26  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/4x/120cpu-1020gb-1072gb`: on_demand 13.31 → 12.53  [REVIEW: pricing]; spot 6.66 → 6.26  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B300/8x/240cpu-2040gb-2144gb`: on_demand 13.31 → 12.53  [REVIEW: pricing]; spot 6.66 → 6.26  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/1x/30cpu-170gb-180gb`: on_demand 9.84 → 9.6  [REVIEW: pricing]; spot 4.92 → 4.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/2x/60cpu-340gb-360gb`: on_demand 9.85 → 9.61  [REVIEW: pricing]; spot 4.92 → 4.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/4x/120cpu-680gb-720gb`: on_demand 9.85 → 9.6  [REVIEW: pricing]; spot 4.92 → 4.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/B200/8x/240cpu-1360gb-1440gb`: on_demand 9.84 → 9.6  [REVIEW: pricing]; spot 4.92 → 4.8  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/1x/44cpu-170gb-141gb`: on_demand 7.18 → 6.77  [REVIEW: pricing]; spot 3.59 → 3.38  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/2x/88cpu-340gb-282gb`: on_demand 7.18 → 6.77  [REVIEW: pricing]; spot 3.59 → 3.38  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/4x/176cpu-680gb-564gb`: on_demand 7.18 → 6.77  [REVIEW: pricing]; spot 3.59 → 3.38  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H200/8x/176cpu-1360gb-1128gb`: on_demand 7.18 → 6.77  [REVIEW: pricing]; spot 3.59 → 3.38  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/30cpu-120gb-80gb`: on_demand 5.62 → 5.29  [REVIEW: pricing]; spot 2.81 → 2.65  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/1x/32cpu-170gb-80gb`: on_demand 5.62 → 5.29  [REVIEW: pricing]; spot 2.81 → 2.65  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/2x/80cpu-340gb-160gb`: on_demand 5.62 → 5.29  [REVIEW: pricing]; spot 2.81 → 2.65  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/4x/176cpu-680gb-320gb`: on_demand 5.62 → 5.29  [REVIEW: pricing]; spot 2.81 → 2.65  [REVIEW: pricing]
- CHANGED `verda/EU-FI/H100/8x/176cpu-1360gb-640gb`: on_demand 5.62 → 5.29  [REVIEW: pricing]; spot 2.81 → 2.65  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/1x/22cpu-120gb-80gb`: on_demand 2.48 → 2.41  [REVIEW: pricing]; spot 1.24 → 1.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/2x/44cpu-240gb-160gb`: on_demand 2.48 → 2.41  [REVIEW: pricing]; spot 1.24 → 1.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/4x/88cpu-480gb-320gb`: on_demand 2.48 → 2.41  [REVIEW: pricing]; spot 1.24 → 1.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/A100/8x/176cpu-960gb-640gb`: on_demand 2.48 → 2.41  [REVIEW: pricing]; spot 1.24 → 1.21  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/1x/30cpu-90gb-96gb`: on_demand 3.04 → 2.86  [REVIEW: pricing]; spot 1.52 → 1.43  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/2x/60cpu-180gb-192gb`: on_demand 3.04 → 2.86  [REVIEW: pricing]; spot 1.52 → 1.43  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/4x/120cpu-360gb-384gb`: on_demand 3.04 → 2.87  [REVIEW: pricing]; spot 1.52 → 1.43  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX PRO 6000/8x/240cpu-720gb-768gb`: on_demand 3.04 → 2.86  [REVIEW: pricing]; spot 1.52 → 1.43  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/1x/10cpu-60gb-48gb`: on_demand 1.7 → 1.62  [REVIEW: pricing]; spot 0.85 → 0.81  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/2x/20cpu-120gb-96gb`: on_demand 1.7 → 1.62  [REVIEW: pricing]; spot 0.85 → 0.81  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/4x/40cpu-240gb-192gb`: on_demand 1.7 → 1.62  [REVIEW: pricing]; spot 0.85 → 0.81  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX 6000 Ada/8x/80cpu-480gb-384gb`: on_demand 1.7 → 1.62  [REVIEW: pricing]; spot 0.85 → 0.81  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/1x/10cpu-60gb-48gb`: on_demand 0.94 → 0.9  [REVIEW: pricing]; spot 0.47 → 0.45  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/2x/20cpu-120gb-96gb`: on_demand 0.94 → 0.9  [REVIEW: pricing]; spot 0.47 → 0.45  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/4x/40cpu-240gb-192gb`: on_demand 0.94 → 0.9  [REVIEW: pricing]; spot 0.47 → 0.45  [REVIEW: pricing]
- CHANGED `verda/EU-FI/RTX A6000/8x/80cpu-480gb-384gb`: on_demand 0.94 → 0.9  [REVIEW: pricing]; spot 0.47 → 0.45  [REVIEW: pricing]
- Price history: 33 changed observation(s) appended to `data/price-history/verda.jsonl`
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

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 8ab54b8833af
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
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 f5fa9737254c
- `jl gpus --json` 3240 B sha1 4a1a8fbf78b8
- `https://jarvislabs.ai/pricing` 156217 B sha1 e9bb3cf6c886
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 114366 B sha1 f6460d365293
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 113700 B sha1 57139bb6926e
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 113389 B sha1 c3abbfe9dd17
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 114019 B sha1 497490f94423
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 113954 B sha1 02d4f8043253
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 113633 B sha1 299cdd6d5c33
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 113041 B sha1 b58964e5f0fc
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 114063 B sha1 16a4d5ab1a0c
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 114354 B sha1 7588f87b3aaa
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 113462 B sha1 bd7881bc7c8a
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 113416 B sha1 cf1d9f3f4148
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 114352 B sha1 2b6701803a15
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 113734 B sha1 e9f06f50cd4b
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 113396 B sha1 50d2a43bc097
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 114038 B sha1 8d3882e71515
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 113982 B sha1 155ab326a7b5
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 113658 B sha1 0e25c1d4e014
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 113057 B sha1 e0e68c0e4c06
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 114069 B sha1 bdbc5abf8293
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 114376 B sha1 969212cf4b6a
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 113484 B sha1 5fe6c70b0458
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 113415 B sha1 920dc6fd363a
- `https://neysa.ai/pricing/` 11997 B sha1 f18c1e9a8ec2
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 131248 B sha1 7b0df72d94e8
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145743 B sha1 4f7bbe099155
- `https://cyfuture.ai/pricing` 523485 B sha1 7131439051d2
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301291 B sha1 9ae5c13b49bb
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1508 B sha1 f8e4c0633daf
- `https://www.olakrutrim.com/gpu-services` 47036 B sha1 2d88cd8ca22f
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 104579 B sha1 0f2cc3885d5b
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45958 B sha1 e054072629de
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35940 B sha1 46028dc0f1e1
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21634 B sha1 8757aa67352f
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 7991523 B sha1 199fc022c34a
- `https://nebius.com/prices` 280525 B sha1 576ba8cd1fe4
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3525 B sha1 875faa7a8eeb
- `https://api.verda.com/v1/instance-types` 187757 B sha1 d3bf347e9026
- `https://www.hyperstack.cloud/gpu-pricing` 148668 B sha1 c8c5e365d7c4

