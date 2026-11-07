"""JarvisLabs live availability — official CLI `jl gpus --json`.

The CLI reports free GPUs per (region, GPU type, workload). Shapes are slices
of the same pool, so for an n-GPU shape: usable GPUs = floor(free / n) * n,
VMs = floor(free / n) (derived). Rows exist for VM and/or container workloads;
the VM row is used when present, otherwise the container row, and the
observation's source names which one.
"""
from __future__ import annotations

import json

from pricing_common import Context
from pricing_jarvislabs import COUNTS, VARIANTS
from pricing_common import accel

PROVIDER = "jarvislabs"
CLI = "jl gpus --json"


def collect(ctx: Context) -> list[dict]:
    rows = json.loads(ctx.run(PROVIDER, CLI, ["jl", "gpus", "--json"]))
    chosen: dict[tuple, dict] = {}
    for r in rows:
        key = (r["region"], r["gpu_type"])
        if key in chosen and r.get("workload_type") != "vm":
            continue
        chosen[key] = r
    obs = []
    for (region, gpu_type), r in sorted(chosen.items()):
        if gpu_type not in VARIANTS or r.get("num_free_devices") is None:
            continue
        a = accel(VARIANTS[gpu_type])
        variant = ("a100-40gb" if a.variant == "a100-sxm4-40gb" else "standard") if a.gpu == "A100" else "standard"
        free, spot = r["num_free_devices"], r.get("spot_num_free_devices")
        workload = r.get("workload_type") or "unspecified"
        for n in COUNTS:
            obs.append({
                "provider": PROVIDER, "region": region, "gpu": a.gpu, "shape": f"{n}x", "variant": variant,
                "available_gpus": (free // n) * n, "available_vms": free // n,
                "spot_available_gpus": None if spot is None else (spot // n) * n,
                "spot_available_vms": None if spot is None else spot // n,
                "total_gpus": None, "vms_derived": True, "observed_via": "api",
                "source": f"{CLI} (workload={workload})", "confidence": "high",
            })
    return obs
