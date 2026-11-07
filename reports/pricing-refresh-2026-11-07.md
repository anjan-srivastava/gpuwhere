# Pricing refresh 2026-11-07 (all providers) — reconstructed

> The original write-mode report of this run was overwritten by a later single-provider run. Below is the dry-run output captured immediately before the write. The write itself reported: new=199, changed=57, unchanged=8, stale=3, retired=15, failed=0 (the dry run had 2 E2E fetch resets, fixed before writing, and listed superseded files as STALE instead of RETIRED).


Mode: dry-run. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=198, changed=57, unchanged=8, stale=18, retired=0, failed=0

## e2e-networks

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: committed {} → {3: 7.27}  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- CHANGED `e2e-networks/IN-DEL/B200/8x/standard`: on_demand 7.99 → None  [REVIEW: pricing]; pricing_status None → quote_only
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: spot 0.93 → 0.94  [REVIEW: pricing]; committed {3: 4.87} → {3: 4.93}  [REVIEW: pricing]; pricing_status None → published
- NEW `e2e-networks/IN-DEL/H200/8x/standard` — quote_only, None vCPU, None GB RAM
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: spot 0.74 → 0.75  [REVIEW: pricing]; committed {3: 3.66} → {3: 3.7}  [REVIEW: pricing]; pricing_status None → published
- NEW `e2e-networks/IN-DEL/H100/8x/standard` — quote_only, None vCPU, None GB RAM
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: committed {} → {3: 2.32}  [REVIEW: pricing]
- CHANGED `e2e-networks/IN-DEL/A100/1x/standard`: spot None → 0.7  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- NEW `e2e-networks/IN-DEL/A100/8x/standard` — quote_only, None vCPU, None GB RAM
- NEW `e2e-networks/IN-DEL/A100/8x/a100-40gb` — quote_only, None vCPU, None GB RAM
- NEW `e2e-networks/IN-DEL/A40/8x/standard` — quote_only, None vCPU, None GB RAM
- CHANGED `e2e-networks/IN-DEL/L40S/1x/standard`: confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- NEW `e2e-networks/IN-DEL/L40S/8x/standard` — quote_only, None vCPU, None GB RAM
- STALE `skus/e2e-networks/IN-DEL/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/e2e-networks/IN-DEL/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- WARNING: [Errno 54] Connection reset by peer for https://www.e2enetworks.com/gpus/nvidia-a30.md
- WARNING: [Errno 54] Connection reset by peer for https://www.e2enetworks.com/gpus/nvidia-l4.md
- Listed but not a SKU: Monthly/annual GPU plans: 'Contact Sales' (feed termPricing).

## jarvislabs

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- NEW `jarvislabs/EU1/H100/1x/standard` — $3.02/GPU-hr, 16 vCPU, 200 GB RAM
- NEW `jarvislabs/EU1/H100/2x/standard` — $3.02/GPU-hr, 32 vCPU, 400 GB RAM
- NEW `jarvislabs/EU1/H100/4x/standard` — $3.02/GPU-hr, 64 vCPU, 800 GB RAM
- NEW `jarvislabs/EU1/H100/8x/standard` — $3.02/GPU-hr, 128 vCPU, 1600 GB RAM
- NEW `jarvislabs/EU1/H200/1x/standard` — $4.02/GPU-hr, 16 vCPU, 200 GB RAM
- NEW `jarvislabs/EU1/H200/2x/standard` — $4.02/GPU-hr, 32 vCPU, 400 GB RAM
- NEW `jarvislabs/EU1/H200/4x/standard` — $4.02/GPU-hr, 64 vCPU, 800 GB RAM
- NEW `jarvislabs/EU1/H200/8x/standard` — $4.02/GPU-hr, 128 vCPU, 1600 GB RAM
- NEW `jarvislabs/IN1/RTX PRO 6000/2x/standard` — $2.19/GPU-hr, 56 vCPU, 320 GB RAM
- NEW `jarvislabs/IN1/RTX PRO 6000/4x/standard` — $2.19/GPU-hr, 112 vCPU, 640 GB RAM
- NEW `jarvislabs/IN1/RTX PRO 6000/8x/standard` — $2.19/GPU-hr, 224 vCPU, 1280 GB RAM
- CHANGED `jarvislabs/IN2/A100/1x/standard`: vcpus 16 → 28
- NEW `jarvislabs/IN2/A100/2x/a100-40gb` — $0.89/GPU-hr, 32 vCPU, 224 GB RAM
- NEW `jarvislabs/IN2/A100/2x/standard` — $1.49/GPU-hr, 56 vCPU, 224 GB RAM
- NEW `jarvislabs/IN2/A100/4x/a100-40gb` — $0.89/GPU-hr, 64 vCPU, 448 GB RAM
- NEW `jarvislabs/IN2/A100/4x/standard` — $1.49/GPU-hr, 112 vCPU, 448 GB RAM
- NEW `jarvislabs/IN2/A100/8x/a100-40gb` — $0.89/GPU-hr, 128 vCPU, 896 GB RAM
- NEW `jarvislabs/IN2/A100/8x/standard` — $1.49/GPU-hr, 224 vCPU, 896 GB RAM
- CHANGED `jarvislabs/IN2/A30/1x/standard`: ram_gb 112 → 64
- NEW `jarvislabs/IN2/A30/2x/standard` — $0.41/GPU-hr, 32 vCPU, 128 GB RAM
- NEW `jarvislabs/IN2/A30/4x/standard` — $0.41/GPU-hr, 64 vCPU, 256 GB RAM
- NEW `jarvislabs/IN2/A30/8x/standard` — $0.41/GPU-hr, 128 vCPU, 512 GB RAM
- CHANGED `jarvislabs/IN2/H100/1x/standard`: vcpus 16 → 24; pricing_status None → published
- NEW `jarvislabs/IN2/H100/2x/standard` — $3.49/GPU-hr, 48 vCPU, 400 GB RAM
- CHANGED `jarvislabs/IN2/H100/4x/standard`: vcpus 64 → 96; pricing_status None → published
- NEW `jarvislabs/IN2/H100/8x/standard` — $3.49/GPU-hr, 192 vCPU, 1600 GB RAM
- CHANGED `jarvislabs/IN2/H200/1x/standard`: pricing_status None → published
- NEW `jarvislabs/IN2/H200/2x/standard` — $4.59/GPU-hr, 56 vCPU, 600 GB RAM
- CHANGED `jarvislabs/IN2/H200/4x/standard`: pricing_status None → published
- NEW `jarvislabs/IN2/H200/8x/standard` — $4.59/GPU-hr, 224 vCPU, 2400 GB RAM
- CHANGED `jarvislabs/IN2/L4/1x/standard`: vcpus 32 → 28
- NEW `jarvislabs/IN2/L4/2x/standard` — $0.44/GPU-hr, 56 vCPU, 248 GB RAM
- NEW `jarvislabs/IN2/L4/4x/standard` — $0.44/GPU-hr, 112 vCPU, 496 GB RAM
- NEW `jarvislabs/IN2/L4/8x/standard` — $0.44/GPU-hr, 224 vCPU, 992 GB RAM

## acecloud

- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-16-128`: committed {12: 3.25} → {1: 3.61, 6: 3.43, 12: 3.25}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-24-192`: committed {12: 3.51} → {1: 3.9, 6: 3.7, 12: 3.51}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-28-282`: committed {12: 3.87} → {1: 4.3, 6: 4.08, 12: 3.87}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- NEW `acecloud/IN-NOI/H200/2x/n-h200-48-384` — $4.88/GPU-hr, 48 vCPU, 384 GB RAM
- NEW `acecloud/IN-NOI/H200/2x/n-h200-56-564` — $5.37/GPU-hr, 56 vCPU, 564 GB RAM
- CHANGED `acecloud/IN-NOI/H200/4x/n-h200-96-768`: committed {12: 3.51} → {1: 3.9, 6: 3.7, 12: 3.51}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- CHANGED `acecloud/IN-NOI/H100/1x/n-hgxh100-250`: committed {12: 3.26} → {6: 3.44, 12: 3.26}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- NEW `acecloud/IN-NOI/H100/2x/n-hgxh100-500` — $3.63/GPU-hr, 52 vCPU, 500 GB RAM
- CHANGED `acecloud/IN-NOI/H100/4x/n-hgxh100-1000`: committed {12: 3.26} → {6: 3.44, 12: 3.26}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- NEW `acecloud/IN-NOI/H100/8x/n-hgxh100-2000` — $3.63/GPU-hr, 208 vCPU, 2000 GB RAM
- CHANGED `acecloud/IN-NOI/A100/1x/n-a100-128`: on_demand 1.3 → 1.81  [REVIEW: pricing]; committed {} → {6: 1.72, 12: 1.63}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/A100/2x/n-a100-256` — $1.81/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-NOI/A100/4x/n-a100-512` — $1.81/GPU-hr, 64 vCPU, 512 GB RAM
- CHANGED `acecloud/IN-NOI/L40S/1x/n-l40s-64`: on_demand 1.2 → 1.5  [REVIEW: pricing]; committed {} → {6: 1.42, 12: 1.35}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/L40S/1x/n-l40s-128` — $1.82/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `acecloud/IN-NOI/L40S/2x/n-l40s-192` — $1.65/GPU-hr, 24 vCPU, 192 GB RAM
- NEW `acecloud/IN-NOI/L40S/2x/n-l40s-256` — $1.82/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-NOI/L40S/4x/n-l40s-512` — $1.82/GPU-hr, 64 vCPU, 512 GB RAM
- CHANGED `acecloud/IN-NOI/L4/1x/n-l4-32`: on_demand 0.53 → 0.66  [REVIEW: pricing]; committed {} → {6: 0.63, 12: 0.6}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/L4/1x/n-l4-64` — $0.87/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-NOI/L4/2x/n-l4-96` — $0.77/GPU-hr, 24 vCPU, 96 GB RAM
- NEW `acecloud/IN-NOI/L4/2x/n-l4-128` — $0.87/GPU-hr, 32 vCPU, 128 GB RAM
- NEW `acecloud/IN-NOI/L4/4x/n-l4-192` — $0.76/GPU-hr, 48 vCPU, 192 GB RAM
- CHANGED `acecloud/IN-NOI/A30/1x/n-a30-32`: on_demand 0.59 → 0.73  [REVIEW: pricing]; committed {} → {6: 0.7, 12: 0.66}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/A30/1x/n-a30-48` — $0.78/GPU-hr, 12 vCPU, 48 GB RAM
- NEW `acecloud/IN-NOI/A30/2x/n-a30-64` — $0.73/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-NOI/A30/2x/n-a30-96` — $0.78/GPU-hr, 24 vCPU, 96 GB RAM
- CHANGED `acecloud/IN-NOI/A2/1x/n-a2-32`: on_demand 0.23 → 0.28  [REVIEW: pricing]; committed {} → {6: 0.27, 12: 0.25}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/A2/2x/n-a2-64` — $0.28/GPU-hr, 16 vCPU, 64 GB RAM
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-16-128`: on_demand 1.75 → 2.19  [REVIEW: pricing]; committed {} → {6: 2.08, 12: 1.97}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-24-192` — $2.58/GPU-hr, 24 vCPU, 192 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-32-256` — $2.98/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 6000/2x/n-pro6000-48-384` — $2.58/GPU-hr, 48 vCPU, 384 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 6000/2x/n-pro6000-64-512` — $2.98/GPU-hr, 64 vCPU, 512 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 6000/4x/n-pro6000-96-768` — $2.58/GPU-hr, 96 vCPU, 768 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 6000/4x/n-pro6000-128-1024` — $2.98/GPU-hr, 128 vCPU, 1024 GB RAM
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-8-32`: on_demand 0.62 → 0.78  [REVIEW: pricing]; committed {} → {6: 0.74, 12: 0.7}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-16-48` — $0.88/GPU-hr, 16 vCPU, 48 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-24-64` — $0.99/GPU-hr, 24 vCPU, 64 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/2x/n-pro4500-32-96` — $0.88/GPU-hr, 32 vCPU, 96 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/2x/n-pro4500-48-128` — $0.99/GPU-hr, 48 vCPU, 128 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/4x/n-pro4500-64-192` — $0.88/GPU-hr, 64 vCPU, 192 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/4x/n-pro4500-96-256` — $0.99/GPU-hr, 96 vCPU, 256 GB RAM
- NEW `acecloud/IN-NOI/RTX PRO 4500/8x/n-pro4500-192-512` — $0.99/GPU-hr, 192 vCPU, 512 GB RAM
- CHANGED `acecloud/IN-NOI/RTX 6000 Ada/1x/n-rtx6000ada-64`: on_demand 0.91 → 1.14  [REVIEW: pricing]; committed {} → {6: 1.08, 12: 1.02}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/RTX 6000 Ada/1x/n-rtx6000ada-128` — $1.47/GPU-hr, 24 vCPU, 128 GB RAM
- NEW `acecloud/IN-NOI/RTX 6000 Ada/2x/n-rtx6000ada-192` — $1.3/GPU-hr, 32 vCPU, 192 GB RAM
- CHANGED `acecloud/IN-NOI/RTX A6000/1x/n-rtxa6000-64`: on_demand 0.74 → 0.93  [REVIEW: pricing]; committed {} → {6: 0.88, 12: 0.83}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- NEW `acecloud/IN-NOI/RTX A6000/1x/n-rtxa6000-128` — $1.26/GPU-hr, 24 vCPU, 128 GB RAM
- NEW `acecloud/IN-NOI/RTX A6000/2x/n-rtxa6000-192` — $1.09/GPU-hr, 32 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/H200/1x/n-h200-16-128` — $3.61/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/H200/1x/n-h200-24-192` — $3.9/GPU-hr, 24 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/H200/1x/n-h200-28-282` — $4.3/GPU-hr, 28 vCPU, 282 GB RAM
- NEW `acecloud/IN-BOM/H200/2x/n-h200-48-384` — $3.9/GPU-hr, 48 vCPU, 384 GB RAM
- NEW `acecloud/IN-BOM/H200/2x/n-h200-56-564` — $4.3/GPU-hr, 56 vCPU, 564 GB RAM
- NEW `acecloud/IN-BOM/H200/4x/n-h200-96-768` — $3.9/GPU-hr, 96 vCPU, 768 GB RAM
- NEW `acecloud/IN-BOM/H100/1x/n-hgxh100-250` — $3.63/GPU-hr, 26 vCPU, 250 GB RAM
- NEW `acecloud/IN-BOM/H100/2x/n-hgxh100-500` — $3.63/GPU-hr, 52 vCPU, 500 GB RAM
- NEW `acecloud/IN-BOM/H100/4x/n-hgxh100-1000` — $3.63/GPU-hr, 104 vCPU, 1000 GB RAM
- NEW `acecloud/IN-BOM/H100/8x/n-hgxh100-2000` — $3.63/GPU-hr, 208 vCPU, 2000 GB RAM
- NEW `acecloud/IN-BOM/A100/1x/n-a100-128` — $1.81/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/A100/2x/n-a100-256` — $1.81/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-BOM/A100/4x/n-a100-512` — $1.81/GPU-hr, 64 vCPU, 512 GB RAM
- NEW `acecloud/IN-BOM/L40S/1x/n-l40s-64` — $1.87/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/L40S/1x/n-l40s-128` — $2.27/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/L40S/2x/n-l40s-192` — $2.06/GPU-hr, 24 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/L40S/2x/n-l40s-256` — $2.27/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-BOM/L40S/4x/n-l40s-512` — $2.27/GPU-hr, 64 vCPU, 512 GB RAM
- NEW `acecloud/IN-BOM/L4/1x/n-l4-32` — $0.66/GPU-hr, 8 vCPU, 32 GB RAM
- NEW `acecloud/IN-BOM/L4/1x/n-l4-64` — $0.87/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/L4/2x/n-l4-96` — $0.77/GPU-hr, 24 vCPU, 96 GB RAM
- NEW `acecloud/IN-BOM/L4/2x/n-l4-128` — $0.87/GPU-hr, 32 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/L4/4x/n-l4-192` — $0.76/GPU-hr, 48 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/A30/1x/n-a30-32` — $0.73/GPU-hr, 8 vCPU, 32 GB RAM
- NEW `acecloud/IN-BOM/A30/1x/n-a30-48` — $0.78/GPU-hr, 12 vCPU, 48 GB RAM
- NEW `acecloud/IN-BOM/A30/2x/n-a30-64` — $0.73/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/A30/2x/n-a30-96` — $0.78/GPU-hr, 24 vCPU, 96 GB RAM
- NEW `acecloud/IN-BOM/A2/1x/n-a2-32` — $0.28/GPU-hr, 8 vCPU, 32 GB RAM
- NEW `acecloud/IN-BOM/A2/2x/n-a2-64` — $0.28/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-16-128` — $2.19/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-24-192` — $2.58/GPU-hr, 24 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-32-256` — $2.98/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/2x/n-pro6000-48-384` — $2.58/GPU-hr, 48 vCPU, 384 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/2x/n-pro6000-64-512` — $2.98/GPU-hr, 64 vCPU, 512 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/4x/n-pro6000-96-768` — $2.58/GPU-hr, 96 vCPU, 768 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 6000/4x/n-pro6000-128-1024` — $2.98/GPU-hr, 128 vCPU, 1024 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-8-32` — $0.97/GPU-hr, 8 vCPU, 32 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-16-48` — $1.1/GPU-hr, 16 vCPU, 48 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-24-64` — $1.24/GPU-hr, 24 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/2x/n-pro4500-32-96` — $1.1/GPU-hr, 32 vCPU, 96 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/2x/n-pro4500-48-128` — $1.24/GPU-hr, 48 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/4x/n-pro4500-64-192` — $1.1/GPU-hr, 64 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/4x/n-pro4500-96-256` — $1.24/GPU-hr, 96 vCPU, 256 GB RAM
- NEW `acecloud/IN-BOM/RTX PRO 4500/8x/n-pro4500-192-512` — $1.24/GPU-hr, 192 vCPU, 512 GB RAM
- NEW `acecloud/IN-BOM/RTX 6000 Ada/1x/n-rtx6000ada-64` — $1.14/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/RTX 6000 Ada/1x/n-rtx6000ada-128` — $1.47/GPU-hr, 24 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/RTX 6000 Ada/2x/n-rtx6000ada-192` — $1.3/GPU-hr, 32 vCPU, 192 GB RAM
- NEW `acecloud/IN-BOM/RTX A6000/1x/n-rtxa6000-64` — $1.16/GPU-hr, 16 vCPU, 64 GB RAM
- NEW `acecloud/IN-BOM/RTX A6000/1x/n-rtxa6000-128` — $1.57/GPU-hr, 24 vCPU, 128 GB RAM
- NEW `acecloud/IN-BOM/RTX A6000/2x/n-rtxa6000-192` — $1.09/GPU-hr, 32 vCPU, 192 GB RAM
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- CHANGED `neysa/IN-BOM/H200/1x/standard`: committed {36: 2.56} → {36: 2.55}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- NEW `neysa/IN-BOM/H200/2x/standard` — $4.72/GPU-hr, None vCPU, None GB RAM
- CHANGED `neysa/IN-BOM/H200/4x/standard`: committed {36: 2.56} → {36: 2.55}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- CHANGED `neysa/IN-BOM/H100/1x/standard`: confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- NEW `neysa/IN-BOM/H100/2x/standard` — $4.39/GPU-hr, None vCPU, None GB RAM
- CHANGED `neysa/IN-BOM/H100/4x/standard`: confidence high → medium  [REVIEW: confidence]; pricing_status None → published
- CHANGED `neysa/IN-BOM/L40S/1x/standard`: committed {} → {36: 0.98}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; disk_gb None → 100
- NEW `neysa/IN-BOM/L40S/2x/standard` — $1.95/GPU-hr, None vCPU, None GB RAM
- NEW `neysa/IN-BOM/L40S/4x/standard` — $1.95/GPU-hr, None vCPU, None GB RAM
- CHANGED `neysa/IN-BOM/L4/1x/standard`: committed {} → {36: 0.59}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; disk_gb None → 100
- NEW `neysa/IN-BOM/L4/2x/standard` — $1.17/GPU-hr, None vCPU, None GB RAM
- NEW `neysa/IN-BOM/L4/4x/standard` — $1.17/GPU-hr, None vCPU, None GB RAM
- CHANGED `neysa/IN-BOM/RTX PRO 6000/1x/quote`: confidence high → medium  [REVIEW: confidence]; disk_gb None → 100
- CHANGED `neysa/IN-BOM/B300/8x/bare-metal-quote`: confidence high → medium  [REVIEW: confidence]
- NEW `neysa/IN-BOM/RTX PRO 6000/8x/bare-metal-quote` — quote_only, None vCPU, None GB RAM
- CHANGED `neysa/IN-BOM/MI300X/8x/bare-metal-reserved`: committed {} → {36: 2.22}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `neysa/IN-BOM/H200/8x/bare-metal-reserved`: committed {} → {36: 2.36}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `neysa/IN-BOM/H100/8x/bare-metal-reserved`: committed {} → {36: 2.13}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `neysa/IN-BOM/L40S/8x/bare-metal-reserved`: committed {} → {36: 0.74}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]

## nxtgen

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: on_demand 3.0 → 3.03  [REVIEW: pricing]; committed {1: 2.4, 6: 2.4, 12: 1.92} → {1: 2.43, 6: 2.43, 12: 1.94}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/H200/8x/standard`: on_demand 2.99 → 3.03  [REVIEW: pricing]; committed {1: 2.4, 6: 2.4, 12: 1.92} → {1: 2.42, 6: 2.42, 12: 1.94}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/H100/1x/standard`: on_demand 2.6 → 2.63  [REVIEW: pricing]; committed {1: 2.08, 6: 2.08, 12: 1.66} → {1: 2.11, 6: 2.11, 12: 1.68}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/L40S/1x/standard`: on_demand 1.55 → 1.57  [REVIEW: pricing]; committed {1: 1.24, 6: 1.24, 12: 0.99} → {1: 1.26, 6: 1.26, 12: 1.0}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/MI325X/1x/standard`: on_demand 2.64 → 2.67  [REVIEW: pricing]; committed {1: 2.12, 6: 2.12, 12: 1.69} → {1: 2.14, 6: 2.14, 12: 1.71}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/MI325X/8x/standard`: on_demand 2.64 → 2.68  [REVIEW: pricing]; committed {1: 2.12, 6: 2.12, 12: 1.69} → {1: 2.14, 6: 2.14, 12: 1.71}  [REVIEW: pricing]; pricing_status None → published
- CHANGED `nxtgen/IN/B200/8x/cluster-quote`: confidence high → medium  [REVIEW: confidence]; vram_gb_per_gpu 192 → 180

## leapswitch

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `leapswitch/IN/L4/1x/cloudpe-quote`: confidence high → medium  [REVIEW: confidence]; disk_gb None → 30
- CHANGED `leapswitch/IN/H200/1x/standard`: on_demand 4.26 → 4.31  [REVIEW: pricing]; disk_gb None → 30; pricing_status None → published
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: on_demand 1.93 → 1.95  [REVIEW: pricing]; disk_gb None → 30; pricing_status None → published
- NEW `leapswitch/IN/RTX A4000/1x/standard` — $0.21/GPU-hr, 8 vCPU, 16 GB RAM
- NEW `leapswitch/IN/RTX A5000/1x/standard` — $0.29/GPU-hr, 8 vCPU, 16 GB RAM
- NEW `leapswitch/IN/RTX A6000/1x/standard` — $0.46/GPU-hr, 8 vCPU, 16 GB RAM
- CHANGED `leapswitch/IN/A100/1x/standard`: on_demand 1.61 → 1.62  [REVIEW: pricing]; disk_gb None → 500; pricing_status None → published
- NEW `leapswitch/IN/A40/1x/standard` — $0.48/GPU-hr, 8 vCPU, 16 GB RAM

## cyfuture-ai

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- NEW `cyfuture-ai/IN/B300/1x/standard` — quote_only, 32 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/B300/2x/standard` — quote_only, 64 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/B300/4x/standard` — quote_only, 128 vCPU, 1024 GB RAM
- NEW `cyfuture-ai/IN/B300/8x/standard` — quote_only, 256 vCPU, 2048 GB RAM
- NEW `cyfuture-ai/IN/RTX PRO 6000/1x/standard` — $2.73/GPU-hr, 32 vCPU, 64 GB RAM
- NEW `cyfuture-ai/IN/RTX PRO 6000/2x/standard` — $2.73/GPU-hr, 64 vCPU, 128 GB RAM
- NEW `cyfuture-ai/IN/RTX PRO 6000/4x/standard` — $2.73/GPU-hr, 128 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/RTX PRO 6000/8x/standard` — $2.73/GPU-hr, 256 vCPU, 512 GB RAM
- CHANGED `cyfuture-ai/IN/L40S/1x/standard`: on_demand 2.88 → 1.32  [REVIEW: pricing]; committed {} → {1: 0.79, 6: 0.72, 12: 0.65}  [REVIEW: pricing]; vcpus None → 16; ram_gb None → 256; pricing_status None → published
- NEW `cyfuture-ai/IN/L40S/2x/standard` — $1.3/GPU-hr, 32 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/L40S/4x/standard` — $1.29/GPU-hr, 64 vCPU, 768 GB RAM
- NEW `cyfuture-ai/IN/L40S/8x/standard` — $1.28/GPU-hr, 64 vCPU, 1536 GB RAM
- NEW `cyfuture-ai/IN/MI300X/1x/standard` — $2.92/GPU-hr, 16 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/MI300X/2x/standard` — $2.89/GPU-hr, 32 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/MI300X/4x/standard` — $2.86/GPU-hr, 64 vCPU, 768 GB RAM
- NEW `cyfuture-ai/IN/MI300X/8x/standard` — $2.83/GPU-hr, 128 vCPU, 1536 GB RAM
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: on_demand 3.46 → 3.5  [REVIEW: pricing]; committed {1: 3.12, 6: 2.77, 12: 2.31} → {1: 3.15, 6: 2.8, 12: 2.33}  [REVIEW: pricing]; vcpus None → 16; ram_gb None → 256; pricing_status None → published
- NEW `cyfuture-ai/IN/H100/2x/standard` — $3.47/GPU-hr, 32 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/H100/4x/standard` — $3.43/GPU-hr, 64 vCPU, 768 GB RAM
- NEW `cyfuture-ai/IN/H100/8x/standard` — $3.4/GPU-hr, 128 vCPU, 1536 GB RAM
- NEW `cyfuture-ai/IN/V100/1x/standard` — $0.57/GPU-hr, 16 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/V100/2x/standard` — $0.57/GPU-hr, 32 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/V100/4x/standard` — $0.56/GPU-hr, 64 vCPU, 1024 GB RAM
- NEW `cyfuture-ai/IN/V100/8x/standard` — $0.56/GPU-hr, 128 vCPU, 2048 GB RAM
- NEW `cyfuture-ai/IN/A100/1x/standard` — $2.11/GPU-hr, 8 vCPU, 64 GB RAM
- NEW `cyfuture-ai/IN/A100/2x/standard` — $2.09/GPU-hr, 16 vCPU, 128 GB RAM
- NEW `cyfuture-ai/IN/A100/4x/standard` — $2.07/GPU-hr, 32 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/A100/8x/standard` — $2.04/GPU-hr, 64 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/Gaudi 2/1x/standard` — $1.08/GPU-hr, 19 vCPU, 288 GB RAM
- NEW `cyfuture-ai/IN/Gaudi 2/2x/standard` — $1.06/GPU-hr, 38 vCPU, 576 GB RAM
- NEW `cyfuture-ai/IN/Gaudi 2/4x/standard` — $1.06/GPU-hr, 76 vCPU, 1152 GB RAM
- NEW `cyfuture-ai/IN/Gaudi 2/8x/standard` — $1.04/GPU-hr, 152 vCPU, 2304 GB RAM
- NEW `cyfuture-ai/IN/MI325X/1x/standard` — $3.17/GPU-hr, 16 vCPU, 256 GB RAM
- NEW `cyfuture-ai/IN/MI325X/2x/standard` — $3.14/GPU-hr, 32 vCPU, 512 GB RAM
- NEW `cyfuture-ai/IN/MI325X/4x/standard` — $3.11/GPU-hr, 64 vCPU, 768 GB RAM
- NEW `cyfuture-ai/IN/MI325X/8x/standard` — $3.08/GPU-hr, 128 vCPU, 1536 GB RAM
- STALE (superseded) `skus/cyfuture-ai/IN/A100/1x/quote.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/cyfuture-ai/IN/B300/1x/quote.json` — retire with --write --retire-superseded
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review

## tata-communications

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- NEW `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu` — $5.2/GPU-hr, 224 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu` — $5.65/GPU-hr, 224 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu` — $5.49/GPU-hr, 192 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu` — $3.12/GPU-hr, 128 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu` — $4.28/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu` — $4.64/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu` — $4.8/GPU-hr, 24 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu` — $4.29/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu` — $4.64/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu` — $4.8/GPU-hr, 48 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu` — $5.06/GPU-hr, 64 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu` — $5.78/GPU-hr, 64 vCPU, None GB RAM
- NEW `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu` — $4.8/GPU-hr, 96 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu` — $2.13/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu` — $2.32/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu` — $2.41/GPU-hr, 24 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu` — $2.48/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu` — $2.13/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu` — $2.32/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu` — $2.49/GPU-hr, 64 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu` — $0.96/GPU-hr, 8 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu` — $1.03/GPU-hr, 8 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu` — $1.1/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu` — $1.25/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu` — $1.03/GPU-hr, 16 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu` — $1.1/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu` — $1.25/GPU-hr, 32 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu` — $1.03/GPU-hr, 48 vCPU, None GB RAM
- NEW `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu` — $1.14/GPU-hr, 48 vCPU, None GB RAM
- STALE (superseded) `skus/tata-communications/IN/H100/8x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/H200/1x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/H200/2x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/H200/4x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/H200/8x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L4/1x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L4/2x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L4/4x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L40S/1x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L40S/2x/standard.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/tata-communications/IN/L40S/4x/standard.json` — retire with --write --retire-superseded

## yotta-shakti

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 2.77 → 2.72  [REVIEW: pricing]; committed {} → {3: 2.64, 6: 2.58, 12: 2.5}  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 2.83 → 2.78  [REVIEW: pricing]; committed {} → {3: 2.7, 6: 2.64, 12: 2.56}  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 2.83 → 2.78  [REVIEW: pricing]; committed {} → {3: 2.7, 6: 2.64, 12: 2.56}  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]; pricing_status None → published
- NEW `yotta-shakti/IN/L40S/1x/standard` — $1.08/GPU-hr, 28 vCPU, 240 GB RAM
- NEW `yotta-shakti/IN/L40S/2x/standard` — $1.08/GPU-hr, 56 vCPU, 480 GB RAM
- NEW `yotta-shakti/IN/H100/8x/bare-metal` — $2.13/GPU-hr, 224 vCPU, 2048 GB RAM
- NEW `yotta-shakti/IN/L40S/4x/bare-metal` — $1.04/GPU-hr, 128 vCPU, 1024 GB RAM
- NEW `yotta-shakti/IN/B200/8x/bare-metal` — $2.06/GPU-hr, 224 vCPU, 2048 GB RAM
- NEW `yotta-shakti/IN/B300/8x/bare-metal` — $2.06/GPU-hr, 256 vCPU, 2048 GB RAM
- STALE (superseded) `skus/yotta-shakti/IN/H100/8x/bare-metal-quote.json` — retire with --write --retire-superseded
- STALE (superseded) `skus/yotta-shakti/IN/L40S/1x/quote.json` — retire with --write --retire-superseded

## Fetched

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 a7b9b6c14514
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 5066 B sha1 d2d962906fc6
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4950 B sha1 e622ad027280
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 b001604ec838
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 720215bd4c48
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 e1c4db3099d2
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 4f3ddb3ee93b
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 d4ab5aa902c0
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 d49fab965f4d
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 9e425fccd34d
- `jl gpus --json` 4211 B sha1 2ec2b924c105
- `https://jarvislabs.ai/pricing` 165382 B sha1 ff0c3de72673
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 120239 B sha1 b607f567ceea
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 119558 B sha1 7956d28302b7
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 119250 B sha1 0ca0dbd51ced
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 119869 B sha1 d84212a7858b
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 119810 B sha1 6d8b1185d319
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 119491 B sha1 baee0ef949a6
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 118897 B sha1 99eeb2f7dd5c
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 119925 B sha1 f71dd4a5f73b
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 120207 B sha1 55031e5d999b
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 119339 B sha1 c1a3b7c3e5cf
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 119272 B sha1 19cd21c43900
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 120213 B sha1 872f45f31a7e
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 119594 B sha1 b11de54b680d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 119259 B sha1 a99a32f3468c
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 119900 B sha1 bce395b82c5b
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 119841 B sha1 d56fc8ba6234
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 119518 B sha1 cc6fb5e5c95b
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 118916 B sha1 acecb7d086a3
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 119933 B sha1 4246df7cc04b
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 120230 B sha1 2cf04eda4859
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 119363 B sha1 4c78c2a310b5
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 119274 B sha1 b691e6e78168
- `https://neysa.ai/pricing/` 335141 B sha1 515b8862b932
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 120727 B sha1 befdc0b756e4
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145850 B sha1 4aeae3463540
- `https://cyfuture.ai/pricing` 504246 B sha1 a72805a9c745
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3



---

# Pricing refresh 2026-11-07 (yotta-shakti)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=9, unchanged=0, stale=0, retired=0, failed=0

## yotta-shakti

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: on_demand 2.13 → 4.56  [REVIEW: pricing]; committed {6: 2.05, 12: 1.6, 24: 1.53} → {6: 4.05, 12: 3.75, 24: 3.34}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; disk_gb None → 61440
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: on_demand 1.04 → 2.53  [REVIEW: pricing]; committed {6: 0.93, 12: 0.84, 24: 0.77} → {6: 2.13, 12: 1.93, 24: 1.72}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]; disk_gb None → 7680
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: on_demand 2.06 → 5.04  [REVIEW: pricing]; committed {6: 2.06, 12: 2.06, 24: 2.06, 36: 1.65, 48: 1.38, 60: 1.22} → {6: 5.04, 12: 5.04, 24: 5.04, 36: 4.02, 48: 3.36, 60: 2.97}  [REVIEW: pricing]; confidence low → medium  [REVIEW: confidence]; disk_gb None → 30400
- CHANGED `yotta-shakti/IN/B300/8x/bare-metal`: on_demand 2.06 → None  [REVIEW: pricing]; committed {6: 2.06, 12: 2.06, 24: 1.69, 36: 1.31, 48: 0.94, 60: 0.74} → {12: 11.24, 24: 9.2, 36: 7.15, 48: 5.11, 60: 4.05}  [REVIEW: pricing]; confidence low → medium  [REVIEW: confidence]; disk_gb None → 30720; pricing_status published → quote_only
- CHANGED `yotta-shakti/IN/H100/1x/standard`: on_demand 2.72 → 3.79  [REVIEW: pricing]; committed {3: 2.64, 6: 2.58, 12: 2.5} → {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `yotta-shakti/IN/H100/2x/standard`: on_demand 2.78 → 3.79  [REVIEW: pricing]; committed {3: 2.7, 6: 2.64, 12: 2.56} → {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `yotta-shakti/IN/H100/4x/standard`: on_demand 2.78 → 3.79  [REVIEW: pricing]; committed {3: 2.7, 6: 2.64, 12: 2.56} → {1: 3.03, 3: 2.94, 6: 2.88, 12: 2.79}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: on_demand 1.08 → 1.46  [REVIEW: pricing]; committed {3: 1.05, 6: 1.03, 12: 0.99} → {1: 1.17, 3: 1.13, 6: 1.11, 12: 1.08}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: on_demand 1.08 → 1.46  [REVIEW: pricing]; committed {3: 1.05, 6: 1.03, 12: 0.99} → {1: 1.14, 3: 1.11, 6: 1.08, 12: 1.05}  [REVIEW: pricing]; confidence high → medium  [REVIEW: confidence]

## Fetched

- `https://shakticloud.ai/pricing/` 301313 B sha1 bd994fee576b
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 9e425fccd34d

---

# Pricing refresh 2026-11-07 18:10 UTC (nxtgen)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=5, unchanged=2, stale=0, retired=0, failed=0

## nxtgen

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: status active → unavailable
- CHANGED `nxtgen/IN/H200/8x/standard`: status active → unavailable
- CHANGED `nxtgen/IN/H100/1x/standard`: status active → unavailable
- CHANGED `nxtgen/IN/MI325X/1x/standard`: status active → unavailable
- CHANGED `nxtgen/IN/MI325X/8x/standard`: status active → unavailable

## Fetched

- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 9e425fccd34d


---

# Pricing refresh 2026-11-07 18:39 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=242, unchanged=22, stale=3, retired=0, failed=0

## e2e-networks

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `e2e-networks/IN-DEL/B200/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/H200/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/H100/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/RTX PRO 6000/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/A100/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/A100/1x/a100-40gb`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/A40/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/L40S/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/V100/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/A30/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/L4/1x/standard`: billing_model None → hourly
- CHANGED `e2e-networks/IN-DEL/T4/1x/standard`: billing_model None → hourly
- STALE `skus/e2e-networks/IN-DEL/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/e2e-networks/IN-DEL/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- Listed but not a SKU: Monthly/annual GPU plans: 'Contact Sales' (feed termPricing).

## jarvislabs

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `jarvislabs/EU1/H100/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H100/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H100/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H100/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H200/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H200/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H200/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/EU1/H200/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN1/RTX PRO 6000/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN1/RTX PRO 6000/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN1/RTX PRO 6000/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN1/RTX PRO 6000/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/1x/a100-40gb`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/2x/a100-40gb`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/4x/a100-40gb`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/8x/a100-40gb`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A100/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A30/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A30/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A30/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/A30/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H100/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H100/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H100/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H100/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H200/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H200/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H200/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/H200/8x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/L4/1x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/L4/2x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/L4/4x/standard`: billing_model None → hourly
- CHANGED `jarvislabs/IN2/L4/8x/standard`: billing_model None → hourly

## acecloud

- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-16-128`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-24-192`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H200/1x/n-h200-28-282`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H200/2x/n-h200-48-384`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H200/2x/n-h200-56-564`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H200/4x/n-h200-96-768`: billing_model None → hourly
- CHANGED `acecloud/IN-NOI/H100/1x/n-hgxh100-250`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/H100/2x/n-hgxh100-500`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/H100/4x/n-hgxh100-1000`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/H100/8x/n-hgxh100-2000`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A100/1x/n-a100-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A100/2x/n-a100-256`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A100/4x/n-a100-512`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L40S/1x/n-l40s-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L40S/1x/n-l40s-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L40S/2x/n-l40s-192`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L40S/2x/n-l40s-256`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L40S/4x/n-l40s-512`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L4/1x/n-l4-32`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L4/1x/n-l4-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L4/2x/n-l4-96`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L4/2x/n-l4-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/L4/4x/n-l4-192`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A30/1x/n-a30-32`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A30/1x/n-a30-48`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A30/2x/n-a30-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A30/2x/n-a30-96`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A2/1x/n-a2-32`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/A2/2x/n-a2-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-16-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-24-192`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/1x/n-pro6000-32-256`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/2x/n-pro6000-48-384`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/2x/n-pro6000-64-512`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/4x/n-pro6000-96-768`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 6000/4x/n-pro6000-128-1024`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-8-32`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-16-48`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/1x/n-pro4500-24-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/2x/n-pro4500-32-96`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/2x/n-pro4500-48-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/4x/n-pro4500-64-192`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/4x/n-pro4500-96-256`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX PRO 4500/8x/n-pro4500-192-512`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX 6000 Ada/1x/n-rtx6000ada-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX 6000 Ada/1x/n-rtx6000ada-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX 6000 Ada/2x/n-rtx6000ada-192`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX A6000/1x/n-rtxa6000-64`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX A6000/1x/n-rtxa6000-128`: billing_model None → monthly
- CHANGED `acecloud/IN-NOI/RTX A6000/2x/n-rtxa6000-192`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/1x/n-h200-16-128`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/1x/n-h200-24-192`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/1x/n-h200-28-282`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/2x/n-h200-48-384`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/2x/n-h200-56-564`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H200/4x/n-h200-96-768`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H100/1x/n-hgxh100-250`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H100/2x/n-hgxh100-500`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H100/4x/n-hgxh100-1000`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/H100/8x/n-hgxh100-2000`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A100/1x/n-a100-128`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A100/2x/n-a100-256`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A100/4x/n-a100-512`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/L40S/1x/n-l40s-64`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/L40S/1x/n-l40s-128`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/L40S/2x/n-l40s-192`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/L40S/2x/n-l40s-256`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/L40S/4x/n-l40s-512`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/L4/1x/n-l4-32`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/L4/1x/n-l4-64`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/L4/2x/n-l4-96`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/L4/2x/n-l4-128`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/L4/4x/n-l4-192`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A30/1x/n-a30-32`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A30/1x/n-a30-48`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A30/2x/n-a30-64`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A30/2x/n-a30-96`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A2/1x/n-a2-32`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/A2/2x/n-a2-64`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-16-128`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-24-192`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/1x/n-pro6000-32-256`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/2x/n-pro6000-48-384`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/2x/n-pro6000-64-512`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/4x/n-pro6000-96-768`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 6000/4x/n-pro6000-128-1024`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-8-32`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-16-48`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/1x/n-pro4500-24-64`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/2x/n-pro4500-32-96`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/2x/n-pro4500-48-128`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/4x/n-pro4500-64-192`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/4x/n-pro4500-96-256`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX PRO 4500/8x/n-pro4500-192-512`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX 6000 Ada/1x/n-rtx6000ada-64`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX 6000 Ada/1x/n-rtx6000ada-128`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX 6000 Ada/2x/n-rtx6000ada-192`: billing_model None → monthly
- CHANGED `acecloud/IN-BOM/RTX A6000/1x/n-rtxa6000-64`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX A6000/1x/n-rtxa6000-128`: billing_model None → hourly
- CHANGED `acecloud/IN-BOM/RTX A6000/2x/n-rtxa6000-192`: billing_model None → monthly
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- CHANGED `neysa/IN-BOM/H200/1x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/H200/2x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/H200/4x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/H100/1x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/H100/2x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/H100/4x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L40S/1x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L40S/2x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L40S/4x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L4/1x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L4/2x/standard`: billing_model None → hourly
- CHANGED `neysa/IN-BOM/L4/4x/standard`: billing_model None → hourly

## nxtgen

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `nxtgen/IN/H200/1x/standard`: billing_model None → hourly
- CHANGED `nxtgen/IN/H200/8x/standard`: billing_model None → hourly
- CHANGED `nxtgen/IN/H100/1x/standard`: billing_model None → hourly
- CHANGED `nxtgen/IN/L40S/1x/standard`: billing_model None → hourly
- CHANGED `nxtgen/IN/MI325X/1x/standard`: billing_model None → hourly
- CHANGED `nxtgen/IN/MI325X/8x/standard`: billing_model None → hourly

## leapswitch

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `leapswitch/IN/H200/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/RTX PRO 6000/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/RTX A4000/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/RTX A5000/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/RTX A6000/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/A100/1x/standard`: billing_model None → monthly
- CHANGED `leapswitch/IN/A40/1x/standard`: billing_model None → monthly

## cyfuture-ai

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/RTX PRO 6000/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/L40S/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/L40S/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/L40S/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/L40S/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI300X/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI300X/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI300X/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI300X/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/H100/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/H100/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/H100/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/H100/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/V100/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/V100/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/V100/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/V100/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/A100/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/A100/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/A100/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/A100/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/Gaudi 2/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/Gaudi 2/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/Gaudi 2/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/Gaudi 2/8x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI325X/1x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI325X/2x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI325X/4x/standard`: billing_model None → hourly
- CHANGED `cyfuture-ai/IN/MI325X/8x/standard`: billing_model None → hourly
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review

## tata-communications

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `tata-communications/IN/H100/8x/gpu-bm-d224-h100sxm-8x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d224-h200sxm-8x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/8x/gpu-bm-d192-h200nvl-8x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/4x/gpu-bm-d128-l40s-4x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/1x/gpu-d16-h200nvl-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/1x/gpu-h16-h200nvl-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/1x/gpu-e24-h200nvl-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/2x/gpu-d32-h200nvl-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/2x/gpu-h32-h200nvl-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/2x/gpu-e48-h200nvl-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/2x/gpu-d64-h200nvl-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/2x/gpu-h64-h200nvl-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/H200/4x/gpu-e96-h200nvl-4x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/1x/gpu-d16-l40s-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/1x/gpu-h16-l40s-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/1x/gpu-e24-l40s-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/1x/gpu-d32-l40s-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/2x/gpu-d32-l40s-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/2x/gpu-h32-l40s-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L40S/2x/gpu-d64-l40s-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/1x/gpu-d8-l4-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/1x/gpu-h8-l4-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/1x/gpu-d16-l4-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/1x/gpu-h16-l4-1x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/2x/gpu-h16-l4-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/2x/gpu-d32-l4-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/2x/gpu-h32-l4-2x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/4x/gpu-d48-l4-4x-olu`: billing_model None → hourly
- CHANGED `tata-communications/IN/L4/4x/gpu-h48-l4-4x-olu`: billing_model None → hourly

## yotta-shakti

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- CHANGED `yotta-shakti/IN/H100/8x/bare-metal`: billing_model None → monthly
- CHANGED `yotta-shakti/IN/L40S/4x/bare-metal`: billing_model None → monthly
- CHANGED `yotta-shakti/IN/B200/8x/bare-metal`: billing_model None → monthly
- CHANGED `yotta-shakti/IN/H100/1x/standard`: billing_model None → hourly
- CHANGED `yotta-shakti/IN/H100/2x/standard`: billing_model None → hourly
- CHANGED `yotta-shakti/IN/H100/4x/standard`: billing_model None → hourly
- CHANGED `yotta-shakti/IN/L40S/1x/standard`: billing_model None → hourly
- CHANGED `yotta-shakti/IN/L40S/2x/standard`: billing_model None → hourly

## Fetched

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 00c74ac93ccb
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 5066 B sha1 d2d962906fc6
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4950 B sha1 e622ad027280
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 b001604ec838
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 720215bd4c48
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 e1c4db3099d2
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 4f3ddb3ee93b
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 d4ab5aa902c0
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 d49fab965f4d
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 05708c9418a1
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 d5593c8e2cb7
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 9e425fccd34d
- `jl gpus --json` 4211 B sha1 4b278f7da068
- `https://jarvislabs.ai/pricing` 165382 B sha1 ff0c3de72673
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 120238 B sha1 0889ad317a27
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 119559 B sha1 4bfa96ec06a2
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 119249 B sha1 7155f0b5c7a0
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 119870 B sha1 c5482397873c
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 119810 B sha1 da8b3f991f92
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 119492 B sha1 a4cd815c0040
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 118898 B sha1 56b41b768f84
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 119925 B sha1 e5863dee3e8a
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 120206 B sha1 fef45ec9f30a
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 119339 B sha1 8b0be1aa3406
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 119273 B sha1 e5dca441bd27
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 120213 B sha1 9a7e59fdf2e5
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 119594 B sha1 84a288b011c4
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 119258 B sha1 2dcc2efc67c6
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 119900 B sha1 c2826ddda3a7
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 119841 B sha1 74b955a84faf
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 119519 B sha1 e5b576a7f401
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 118915 B sha1 4f329ef1720a
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 119933 B sha1 fbd917bea481
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 120231 B sha1 1562a7ce98b6
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 119363 B sha1 7c07584abd5d
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 119273 B sha1 e6181c733607
- `https://neysa.ai/pricing/` 335140 B sha1 281c247c2f7f
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 120727 B sha1 befdc0b756e4
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145850 B sha1 84700d1403b9
- `https://cyfuture.ai/pricing` 504246 B sha1 5e9d0cb4cbcf
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301313 B sha1 bd994fee576b
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3


---

# Pricing refresh 2026-11-07 19:38 UTC (krutrim-cloud, microsoft-azure)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=27, changed=0, unchanged=0, stale=0, retired=0, failed=0

## krutrim-cloud

- NEW `krutrim-cloud/IN/H100/1x/console-price` — quote_only, None vCPU, None GB RAM
- NEW `krutrim-cloud/IN/A100/1x/console-price` — quote_only, None vCPU, None GB RAM
- Listed but not a SKU: Spliced (fractional) GPUs: not a whole-GPU shape

## microsoft-azure

- NEW `microsoft-azure/IN-PNQ/T4/1x/nc16as-t4-v3` — $1.32/GPU-hr, 16 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/T4/1x/nc4as-t4-v3` — $0.58/GPU-hr, 4 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/T4/1x/nc8as-t4-v3` — $0.83/GPU-hr, 8 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/A100/1x/nc24ads-a100-v4` — $5.14/GPU-hr, 24 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/H100/1x/nc40ads-h100-v5` — $9.77/GPU-hr, 40 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/A100/2x/nc48ads-a100-v4` — $5.14/GPU-hr, 48 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/T4/4x/nc64as-t4-v3` — $1.2/GPU-hr, 64 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/H100/2x/nc80adis-h100-v5` — $9.77/GPU-hr, 80 vCPU, None GB RAM
- NEW `microsoft-azure/IN-PNQ/A100/4x/nc96ads-a100-v4` — $5.14/GPU-hr, 96 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/T4/1x/nc16as-t4-v3` — $1.7/GPU-hr, 16 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/T4/1x/nc4as-t4-v3` — $0.74/GPU-hr, 4 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/T4/1x/nc8as-t4-v3` — $1.06/GPU-hr, 8 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/T4/4x/nc64as-t4-v3` — $1.53/GPU-hr, 64 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/A100/8x/nd96ams-a100-v4` — $6.19/GPU-hr, 96 vCPU, None GB RAM
- NEW `microsoft-azure/IN-MAA/A100/8x/nd96amsr-a100-v4` — $6.19/GPU-hr, 96 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-W/A100/1x/nc24ads-a100-v4` — $5.14/GPU-hr, 24 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-W/H100/1x/nc40ads-h100-v5` — $9.77/GPU-hr, 40 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-W/A100/2x/nc48ads-a100-v4` — $5.14/GPU-hr, 48 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-W/H100/2x/nc80adis-h100-v5` — $9.77/GPU-hr, 80 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-W/A100/4x/nc96ads-a100-v4` — $5.14/GPU-hr, 96 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-C/A100/1x/nc24ads-a100-v4` — $5.14/GPU-hr, 24 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-C/H100/1x/nc40ads-h100-v5` — $9.77/GPU-hr, 40 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-C/A100/2x/nc48ads-a100-v4` — $5.14/GPU-hr, 48 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-C/H100/2x/nc80adis-h100-v5` — $9.77/GPU-hr, 80 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JIO-C/A100/4x/nc96ads-a100-v4` — $5.14/GPU-hr, 96 vCPU, None GB RAM
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

## Fetched

- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1383 B sha1 abc68ea42e0a
- `https://www.olakrutrim.com/gpu-services` 46359 B sha1 c2044bdc66ed
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344


---

# Pricing refresh 2026-11-07 19:49 UTC (aws)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=48, changed=0, unchanged=0, stale=0, retired=0, failed=0

## aws

- NEW `aws/IN-BOM/T4/1x/g4dn-16xlarge` — $4.79/GPU-hr, 64 vCPU, 274.9 GB RAM
- NEW `aws/IN-BOM/T4/1x/g4dn-4xlarge` — $1.32/GPU-hr, 16 vCPU, 68.7 GB RAM
- NEW `aws/IN-BOM/T4/1x/g4dn-xlarge` — $0.58/GPU-hr, 4 vCPU, 17.2 GB RAM
- NEW `aws/IN-BOM/T4/1x/g4dn-8xlarge` — $2.4/GPU-hr, 32 vCPU, 137.4 GB RAM
- NEW `aws/IN-BOM/T4/1x/g4dn-2xlarge` — $0.83/GPU-hr, 8 vCPU, 34.4 GB RAM
- NEW `aws/IN-BOM/L40S/1x/g6e-4xlarge` — $3.61/GPU-hr, 16 vCPU, 137.4 GB RAM
- NEW `aws/IN-BOM/L40S/1x/g6e-xlarge` — $2.23/GPU-hr, 4 vCPU, 34.4 GB RAM
- NEW `aws/IN-BOM/L40S/1x/g6e-16xlarge` — $9.1/GPU-hr, 64 vCPU, 549.8 GB RAM
- NEW `aws/IN-BOM/L40S/1x/g6e-8xlarge` — $5.44/GPU-hr, 32 vCPU, 274.9 GB RAM
- NEW `aws/IN-BOM/L40S/1x/g6e-2xlarge` — $2.69/GPU-hr, 8 vCPU, 68.7 GB RAM
- NEW `aws/IN-BOM/H100/1x/p5-4xlarge` — $8.26/GPU-hr, 16 vCPU, 274.9 GB RAM
- NEW `aws/IN-BOM/L4/1x/g6-8xlarge` — $2.42/GPU-hr, 32 vCPU, 137.4 GB RAM
- NEW `aws/IN-BOM/L4/1x/gr6-4xlarge` — $1.85/GPU-hr, 16 vCPU, 137.4 GB RAM
- NEW `aws/IN-BOM/L4/1x/g6-xlarge` — $0.97/GPU-hr, 4 vCPU, 17.2 GB RAM
- NEW `aws/IN-BOM/L4/1x/g6-16xlarge` — $4.08/GPU-hr, 64 vCPU, 274.9 GB RAM
- NEW `aws/IN-BOM/L4/1x/g6-4xlarge` — $1.59/GPU-hr, 16 vCPU, 68.7 GB RAM
- NEW `aws/IN-BOM/L4/1x/g6-2xlarge` — $1.17/GPU-hr, 8 vCPU, 34.4 GB RAM
- NEW `aws/IN-BOM/L4/1x/gr6-8xlarge` — $2.94/GPU-hr, 32 vCPU, 274.9 GB RAM
- NEW `aws/IN-BOM/T4/4x/g4dn-12xlarge` — $1.08/GPU-hr, 48 vCPU, 206.2 GB RAM
- NEW `aws/IN-BOM/L4/4x/g6-12xlarge` — $1.38/GPU-hr, 48 vCPU, 206.2 GB RAM
- NEW `aws/IN-BOM/L4/4x/g6-24xlarge` — $2.0/GPU-hr, 96 vCPU, 412.3 GB RAM
- NEW `aws/IN-BOM/H100/8x/p5-48xlarge` — $8.26/GPU-hr, 192 vCPU, 2199 GB RAM
- NEW `aws/IN-BOM/T4/8x/g4dn-metal` — $1.08/GPU-hr, 96 vCPU, 412.3 GB RAM
- NEW `aws/IN-BOM/H200/8x/p5en-48xlarge` — $9.49/GPU-hr, 192 vCPU, 2199 GB RAM
- NEW `aws/IN-BOM/L40S/4x/g6e-24xlarge` — $4.52/GPU-hr, 96 vCPU, 824.6 GB RAM
- NEW `aws/IN-BOM/L40S/4x/g6e-12xlarge` — $3.15/GPU-hr, 48 vCPU, 412.3 GB RAM
- NEW `aws/IN-BOM/A100/8x/p4d-24xlarge` — $3.29/GPU-hr, 96 vCPU, 1237 GB RAM
- NEW `aws/IN-BOM/B200/8x/p6-b200-48xlarge` — $20.08/GPU-hr, 192 vCPU, 2199 GB RAM
- NEW `aws/IN-BOM/L40S/8x/g6e-48xlarge` — $4.52/GPU-hr, 192 vCPU, 1649.3 GB RAM
- NEW `aws/IN-BOM/L4/8x/g6-48xlarge` — $2.0/GPU-hr, 192 vCPU, 824.6 GB RAM
- NEW `aws/IN-HYD/L4/1x/g6-xlarge` — $0.97/GPU-hr, 4 vCPU, 17.2 GB RAM
- NEW `aws/IN-HYD/L4/1x/g6-8xlarge` — $2.42/GPU-hr, 32 vCPU, 137.4 GB RAM
- NEW `aws/IN-HYD/L4/1x/g6-2xlarge` — $1.17/GPU-hr, 8 vCPU, 34.4 GB RAM
- NEW `aws/IN-HYD/L4/1x/g6-16xlarge` — $4.08/GPU-hr, 64 vCPU, 274.9 GB RAM
- NEW `aws/IN-HYD/L4/1x/g6-4xlarge` — $1.59/GPU-hr, 16 vCPU, 68.7 GB RAM
- NEW `aws/IN-HYD/L4/4x/g6-12xlarge` — $1.38/GPU-hr, 48 vCPU, 206.2 GB RAM
- NEW `aws/IN-HYD/L4/4x/g6-24xlarge` — $2.0/GPU-hr, 96 vCPU, 412.3 GB RAM
- NEW `aws/IN-HYD/B200/8x/p6-b200-48xlarge` — $20.08/GPU-hr, 192 vCPU, 2199 GB RAM
- NEW `aws/IN-HYD/L40S/4x/g6e-24xlarge` — $4.52/GPU-hr, 96 vCPU, 824.6 GB RAM
- NEW `aws/IN-HYD/L40S/4x/g6e-12xlarge` — $3.15/GPU-hr, 48 vCPU, 412.3 GB RAM
- NEW `aws/IN-HYD/L40S/1x/g6e-xlarge` — $2.23/GPU-hr, 4 vCPU, 34.4 GB RAM
- NEW `aws/IN-HYD/L40S/1x/g6e-4xlarge` — $3.61/GPU-hr, 16 vCPU, 137.4 GB RAM
- NEW `aws/IN-HYD/L40S/1x/g6e-8xlarge` — $5.44/GPU-hr, 32 vCPU, 274.9 GB RAM
- NEW `aws/IN-HYD/L40S/1x/g6e-2xlarge` — $2.69/GPU-hr, 8 vCPU, 68.7 GB RAM
- NEW `aws/IN-HYD/L40S/1x/g6e-16xlarge` — $9.1/GPU-hr, 64 vCPU, 549.8 GB RAM
- NEW `aws/IN-HYD/L40S/8x/g6e-48xlarge` — $4.52/GPU-hr, 192 vCPU, 1649.3 GB RAM
- NEW `aws/IN-HYD/L4/8x/g6-48xlarge` — $2.0/GPU-hr, 192 vCPU, 824.6 GB RAM
- NEW `aws/IN-HYD/B300/8x/p6-b300-48xlarge` — $25.1/GPU-hr, 192 vCPU, 4398 GB RAM
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## Fetched

- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35561 B sha1 887ec242f2a4
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21633 B sha1 85ef5435e002


---

# Pricing refresh 2026-11-07 19:54 UTC (microsoft-azure)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=10, changed=0, unchanged=15, stale=0, retired=0, failed=0

## microsoft-azure

- NEW `microsoft-azure/IN-JAM/A100/1x/nc24ads-a100-v4` — $5.14/GPU-hr, 24 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JAM/H100/1x/nc40ads-h100-v5` — $9.77/GPU-hr, 40 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JAM/A100/2x/nc48ads-a100-v4` — $5.14/GPU-hr, 48 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JAM/H100/2x/nc80adis-h100-v5` — $9.77/GPU-hr, 80 vCPU, None GB RAM
- NEW `microsoft-azure/IN-JAM/A100/4x/nc96ads-a100-v4` — $5.14/GPU-hr, 96 vCPU, None GB RAM
- NEW `microsoft-azure/IN-NAG/A100/1x/nc24ads-a100-v4` — $5.14/GPU-hr, 24 vCPU, None GB RAM
- NEW `microsoft-azure/IN-NAG/H100/1x/nc40ads-h100-v5` — $9.77/GPU-hr, 40 vCPU, None GB RAM
- NEW `microsoft-azure/IN-NAG/A100/2x/nc48ads-a100-v4` — $5.14/GPU-hr, 48 vCPU, None GB RAM
- NEW `microsoft-azure/IN-NAG/H100/2x/nc80adis-h100-v5` — $9.77/GPU-hr, 80 vCPU, None GB RAM
- NEW `microsoft-azure/IN-NAG/A100/4x/nc96ads-a100-v4` — $5.14/GPU-hr, 96 vCPU, None GB RAM
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

## Fetched

- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344


---

# Pricing refresh 2026-11-07 19:59 UTC (all providers)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=32, changed=0, unchanged=339, stale=3, retired=0, failed=0

## e2e-networks

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- STALE `skus/e2e-networks/IN-DEL/H100/4x/standard.json` — no current source covers H100 4x; left for human review
- STALE `skus/e2e-networks/IN-DEL/H200/4x/standard.json` — no current source covers H200 4x; left for human review
- Listed but not a SKU: Monthly/annual GPU plans: 'Contact Sales' (feed termPricing).

## jarvislabs

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)

## acecloud

- no changes
- Listed but not a SKU: RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; no accelerator file, so not modelled.

## neysa

- no changes

## nxtgen

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)

## leapswitch

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)

## cyfuture-ai

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- STALE `skus/cyfuture-ai/IN/H200/1x/quote.json` — no current source covers H200 1x; left for human review

## tata-communications

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)

## yotta-shakti

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)

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
- WARNING: unmapped AWS accelerated type g7e.2xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.8xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.4xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.48xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.12xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- WARNING: unmapped AWS accelerated type g7e.24xlarge in Asia Pacific (Mumbai); add it to _gpu_map
- Listed but not a SKU: inf1.6xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.24xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.16xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.8xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.4xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.24xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf1.2xlarge (IN-BOM): inf1 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.16xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.4xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.24xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.2xlarge (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g6f.large (IN-BOM): g6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: p2.8xlarge (IN-BOM): p2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.8xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: gr6f.4xlarge (IN-BOM): gr6f (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.2xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: inf2.48xlarge (IN-BOM): inf2 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.48xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: g5.12xlarge (IN-BOM): g5 (A10G/fractional/Trainium/Inferentia) not modelled
- Listed but not a SKU: trn2.48xlarge (IN-HYD): trn2 (A10G/fractional/Trainium/Inferentia) not modelled

## ovhcloud

- FX: USD/INR 93.9225 (2026-11-06, ECB reference rate)
- NEW `ovhcloud/EU-FR/A100/1x/a100-180` — $3.07/GPU-hr, 15 vCPU, 180 GB RAM
- NEW `ovhcloud/EU-FR/A100/2x/a100-360` — $3.07/GPU-hr, 30 vCPU, 360 GB RAM
- NEW `ovhcloud/EU-FR/A100/4x/a100-720` — $3.07/GPU-hr, 60 vCPU, 720 GB RAM
- NEW `ovhcloud/EU-FR/H100/4x/h100-1520` — $3.13/GPU-hr, 120 vCPU, 1520 GB RAM
- NEW `ovhcloud/EU-FR/H100/1x/h100-380` — $3.13/GPU-hr, 30 vCPU, 380 GB RAM
- NEW `ovhcloud/EU-FR/H100/2x/h100-760` — $3.13/GPU-hr, 60 vCPU, 760 GB RAM
- NEW `ovhcloud/EU-FR/H200/8x/h200-1920` — $5.86/GPU-hr, 224 vCPU, 1920 GB RAM
- NEW `ovhcloud/EU-FR/L4/2x/l4-180` — $0.84/GPU-hr, 45 vCPU, 180 GB RAM
- NEW `ovhcloud/EU-FR/L4/2x/win-l4-180` — $1.71/GPU-hr, 45 vCPU, 180 GB RAM
- NEW `ovhcloud/EU-FR/L4/4x/l4-360` — $0.84/GPU-hr, 90 vCPU, 360 GB RAM
- NEW `ovhcloud/EU-FR/L4/4x/win-l4-360` — $1.71/GPU-hr, 90 vCPU, 360 GB RAM
- NEW `ovhcloud/EU-FR/L4/1x/l4-90` — $0.84/GPU-hr, 22 vCPU, 90 GB RAM
- NEW `ovhcloud/EU-FR/L4/1x/win-l4-90` — $1.69/GPU-hr, 22 vCPU, 90 GB RAM
- NEW `ovhcloud/EU-FR/L40S/2x/l40s-180` — $1.56/GPU-hr, 30 vCPU, 180 GB RAM
- NEW `ovhcloud/EU-FR/L40S/4x/l40s-360` — $1.56/GPU-hr, 60 vCPU, 360 GB RAM
- NEW `ovhcloud/EU-FR/L40S/1x/l40s-90` — $1.56/GPU-hr, 15 vCPU, 90 GB RAM
- Listed but not a SKU: a10-180: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-45: A10 has no accelerator spec in the catalogue
- Listed but not a SKU: a10-90: A10 has no accelerator spec in the catalogue
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

- NEW `nebius/EU-FI/B300/1x/standard` — $9.5/GPU-hr, 24 vCPU, 346 GB RAM
- NEW `nebius/EU-FI/B200/1x/standard` — $8.5/GPU-hr, 20 vCPU, 224 GB RAM
- NEW `nebius/EU-FI/H200/1x/standard` — $5.4/GPU-hr, 16 vCPU, 200 GB RAM
- NEW `nebius/EU-FI/H100/1x/standard` — $4.5/GPU-hr, 16 vCPU, 200 GB RAM
- NEW `nebius/EU-FI/RTX PRO 6000/1x/standard` — $1.8/GPU-hr, 24 vCPU, 218 GB RAM
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## verda

- no changes

## hyperstack

- NEW `hyperstack/EU-NO/H200/1x/h200-sxm` — $3.99/GPU-hr, 22 vCPU, 225 GB RAM
- NEW `hyperstack/EU-NO/H100/1x/h100-sxm` — $3.2/GPU-hr, 24 vCPU, 240 GB RAM
- NEW `hyperstack/EU-NO/H100/1x/h100-nvlink` — $2.6/GPU-hr, 31 vCPU, 180 GB RAM
- NEW `hyperstack/EU-NO/H100/1x/h100` — $2.5/GPU-hr, 28 vCPU, 180 GB RAM
- NEW `hyperstack/EU-NO/RTX PRO 6000/1x/rtx-pro-6000-se` — $1.85/GPU-hr, 31 vCPU, 180 GB RAM
- NEW `hyperstack/EU-NO/A100/1x/a100-sxm` — $1.6/GPU-hr, 24 vCPU, 120 GB RAM
- NEW `hyperstack/EU-NO/A100/1x/a100-nvlink` — $1.4/GPU-hr, 31 vCPU, 240 GB RAM
- NEW `hyperstack/EU-NO/A100/1x/a100` — $1.35/GPU-hr, 28 vCPU, 120 GB RAM
- NEW `hyperstack/EU-NO/RTX A6000/1x/a6000` — $0.5/GPU-hr, 28 vCPU, 58 GB RAM
- NEW `hyperstack/EU-NO/RTX A4000/1x/a4000` — $0.15/GPU-hr, 6 vCPU, 24 GB RAM
- NEW `hyperstack/EU-NO/B200/1x/b200` — $6.0/GPU-hr, 31 vCPU, 256 GB RAM

## Fetched

- `https://www.e2enetworks.com/pricing.json` 21772 B sha1 5d398638f21a
- `https://www.e2enetworks.com/gpus/nvidia-b200.md` 5066 B sha1 d2d962906fc6
- `https://www.e2enetworks.com/gpus/nvidia-h200.md` 4950 B sha1 e622ad027280
- `https://www.e2enetworks.com/gpus/nvidia-h100.md` 5014 B sha1 b001604ec838
- `https://www.e2enetworks.com/gpus/nvidia-rtx-pro-6000.md` 8357 B sha1 720215bd4c48
- `https://www.e2enetworks.com/gpus/nvidia-a100-80gb.md` 4890 B sha1 e1c4db3099d2
- `https://www.e2enetworks.com/gpus/nvidia-a100-40gb.md` 4975 B sha1 4f3ddb3ee93b
- `https://www.e2enetworks.com/gpus/nvidia-a40.md` 4822 B sha1 d4ab5aa902c0
- `https://www.e2enetworks.com/gpus/nvidia-l40s.md` 4795 B sha1 d49fab965f4d
- `https://www.e2enetworks.com/gpus/nvidia-a30.md` 4787 B sha1 05708c9418a1
- `https://www.e2enetworks.com/gpus/nvidia-l4.md` 4789 B sha1 d5593c8e2cb7
- `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` 1547 B sha1 9e425fccd34d
- `jl gpus --json` 4211 B sha1 c0d5dcd086e5
- `https://jarvislabs.ai/pricing` 165382 B sha1 ff0c3de72673
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h200-nvl/` 120239 B sha1 78e506093936
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-h100-hgx/` 119557 B sha1 97c1fbec0aba
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a100-80gb/` 119250 B sha1 1551a8e0b3b5
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l40s-48gb/` 119870 B sha1 bb4ac996a906
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-l4-24gb/` 119811 B sha1 51d8f30f988a
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a30-24gb/` 119491 B sha1 23f1bb29b471
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-a2-16gb/` 118898 B sha1 b21ec17a7ee3
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-6000-96gb/` 119926 B sha1 a92b11fac7df
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-pro-4500/` 120207 B sha1 59fa273740bb
- `https://acecloud.ai/pricing/linux/usd/noida/nvidia-rtx-6000-ada-48gb/` 119339 B sha1 939a5b59f5e3
- `https://acecloud.ai/pricing/linux/usd/noida/rtx-a6000-48gb/` 119271 B sha1 830c7546086d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h200-nvl/` 120212 B sha1 772c859c7c4d
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-h100-hgx/` 119594 B sha1 1a062dc99bb7
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a100-80gb/` 119259 B sha1 4163ef7a7dff
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l40s-48gb/` 119901 B sha1 a3b7e07f7cc7
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-l4-24gb/` 119841 B sha1 75aab233d6cb
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a30-24gb/` 119519 B sha1 4bd0a026b665
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-a2-16gb/` 118915 B sha1 c706c8de7b40
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-6000-96gb/` 119933 B sha1 610ba11633f0
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-pro-4500/` 120229 B sha1 8a8b620d2312
- `https://acecloud.ai/pricing/linux/usd/mumbai/nvidia-rtx-6000-ada-48gb/` 119363 B sha1 50f2ecee1e0b
- `https://acecloud.ai/pricing/linux/usd/mumbai/rtx-a6000-48gb/` 119274 B sha1 3c000947214a
- `https://neysa.ai/pricing/` 335140 B sha1 b80da56aefd3
- `https://speedcloud.nxtgen.com/` 166358 B sha1 eb2fea440b64
- `https://speedcloud.nxtgen.com/aiinstances.html` 63867 B sha1 be68dcfe5ab3
- `https://leapswitch.com/gpu-cloud/` 120727 B sha1 befdc0b756e4
- `https://service.leapswitch.com/cart/gpu-cloud-servers-inr` 145850 B sha1 e5f596bf8141
- `https://cyfuture.ai/pricing` 504246 B sha1 3ab8510140e7
- `https://www.tatacommunications.com/hubfs/library/documents/Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf` 340526 B sha1 3d6f3325be33
- `https://shakticloud.ai/pricing/` 301313 B sha1 bd994fee576b
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json` 13169 B sha1 a85c4ef5649d
- `https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json` 14030 B sha1 faa4276b8dd3
- `https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md` 1383 B sha1 abc68ea42e0a
- `https://www.olakrutrim.com/gpu-services` 46359 B sha1 acd61f2829a2
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27centralindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 103823 B sha1 df5a687f4d05
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27southindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 45454 B sha1 e705c0d6e076
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27westindia%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 125 B sha1 a4147d566ea9
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiawest%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26375 B sha1 f4c72afdfe06
- `https://prices.azure.com/api/retail/prices?$filter=armRegionName%20eq%20%27jioindiacentral%27%20and%20serviceName%20eq%20%27Virtual%20Machines%27%20and%20%28contains%28armSkuName%2C%27H100%27%29%20or%20contains%28armSkuName%2C%27H200%27%29%20or%20contains%28armSkuName%2C%27A100%27%29%20or%20contains%28armSkuName%2C%27MI300%27%29%20or%20contains%28armSkuName%2C%27T4%27%29%20or%20contains%28armSkuName%2C%27A10%27%29%20or%20contains%28armSkuName%2C%27L40%27%29%20or%20contains%28armSkuName%2C%27B200%27%29%20or%20contains%28armSkuName%2C%27GB200%27%29%20or%20contains%28armSkuName%2C%27V100%27%29%29` 26633 B sha1 9ed1a7837344
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Mumbai%29/Linux/index.json` 35561 B sha1 887ec242f2a4
- `https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/Asia%20Pacific%20%28Hyderabad%29/Linux/index.json` 21633 B sha1 85ef5435e002
- `https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE` 8322930 B sha1 e29e06230f6e
- `https://nebius.com/prices` 274339 B sha1 5fbef6687421
- `https://verda.com/pricing` 461521 B sha1 2cda23bff3f0
- `https://www.hyperstack.cloud/gpu-pricing` 156963 B sha1 4ef9470a1a54


---

# Pricing refresh 2026-11-07 19:59 UTC (verda)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=0, unchanged=0, stale=0, retired=0, failed=0

## verda

- no changes

## Fetched

- `https://verda.com/pricing` 461521 B sha1 2cda23bff3f0


---

# Pricing refresh 2026-11-07 20:00 UTC (verda)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=10, changed=0, unchanged=0, stale=0, retired=0, failed=0

## verda

- NEW `verda/EU-FI/B300/1x/30cpu-255gb` — $11.69/GPU-hr, 30 vCPU, 255 GB RAM
- NEW `verda/EU-FI/B200/1x/30cpu-170gb` — $9.14/GPU-hr, 30 vCPU, 170 GB RAM
- NEW `verda/EU-FI/H200/1x/44cpu-170gb` — $6.44/GPU-hr, 44 vCPU, 170 GB RAM
- NEW `verda/EU-FI/H100/1x/30cpu-120gb` — $4.94/GPU-hr, 30 vCPU, 120 GB RAM
- NEW `verda/EU-FI/H100/1x/32cpu-170gb` — $4.94/GPU-hr, 32 vCPU, 170 GB RAM
- NEW `verda/EU-FI/A100/1x/22cpu-120gb` — $2.32/GPU-hr, 22 vCPU, 120 GB RAM
- NEW `verda/EU-FI/RTX PRO 6000/1x/30cpu-90gb` — $2.73/GPU-hr, 30 vCPU, 90 GB RAM
- NEW `verda/EU-FI/L40S/1x/20cpu-60gb` — $1.94/GPU-hr, 20 vCPU, 60 GB RAM
- NEW `verda/EU-FI/RTX 6000 Ada/1x/10cpu-60gb` — $1.54/GPU-hr, 10 vCPU, 60 GB RAM
- NEW `verda/EU-FI/RTX A6000/1x/10cpu-60gb` — $0.85/GPU-hr, 10 vCPU, 60 GB RAM
- Listed but not a SKU: 1x GB300 SXM6 288GB: no accelerator spec or unsupported shape
- Listed but not a SKU: 1x Tesla V100 16GB: no accelerator spec or unsupported shape

## Fetched

- `https://verda.com/pricing` 461521 B sha1 2cda23bff3f0


---

# Pricing refresh 2026-11-07 20:33 UTC (nebius)

Mode: write. Pricing and confidence changes need human review (AGENTS.md).
Summary: new=0, changed=2, unchanged=3, stale=0, retired=0, failed=0

## nebius

- CHANGED `nebius/EU-FI/H200/1x/standard`: spot None → 2.9  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]
- CHANGED `nebius/EU-FI/H100/1x/standard`: spot None → 0.8  [REVIEW: pricing]; confidence medium → high  [REVIEW: confidence]
- Listed but not a SKU: NVIDIA L40S with Intel CPU: on-demand published only as a 'from' range
- Listed but not a SKU: NVIDIA L40S with AMD CPU: on-demand published only as a 'from' range

## Fetched

- `https://nebius.com/prices` 274339 B sha1 5fbef6687421
- `https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100` 3252 B sha1 04525cb6c682

