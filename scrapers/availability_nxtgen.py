"""NxtGen SpeedCloud availability — "SOLD OUT" badges on the public homepage.

The homepage product cards are the only public stock signal. A SOLD OUT card
means zero rentable instances of that plan (0 GPUs / 0 VMs). A card without the
badge says the plan can be ordered but not how many are free, so counts stay
null. NxtGen has no spot market (spot is null).
"""
from __future__ import annotations

from pricing_common import Context
from pricing_nxtgen import HOME, MODELS, cards

PROVIDER = "nxtgen"
REGION = "IN"


def collect(ctx: Context) -> list[dict]:
    from pricing_common import accel
    obs = []
    for (model, n), card in sorted(cards(ctx).items()):
        if model not in MODELS or n not in (1, 2, 4, 8):
            continue
        a = accel(MODELS[model])
        sold = card["sold_out"]
        obs.append({
            "provider": PROVIDER, "region": REGION, "gpu": a.gpu, "shape": f"{n}x", "variant": "standard",
            "available_gpus": 0 if sold else None, "available_vms": 0 if sold else None,
            "spot_available_gpus": None, "spot_available_vms": None, "total_gpus": None,
            "vms_derived": False, "observed_via": "page",
            "source": f"{HOME} (plan {card['name']}: {'SOLD OUT' if sold else 'orderable, count not shown'})",
            "confidence": "medium",
        })
    return obs
