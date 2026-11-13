# Psi Universe Attractor Library v2.0

**Toroidal Path-Integral Attractor Filter with a Lyapunov Stability Sketch**  
Exploratory research code. Tested on **one** EAST discharge (#41195) with synthetic noise added; not validated.

---

## Overview

This library implements the **Ψ_universe attractor** derived from the closed toroidal path-integral equation:

```
∫_γ (d|ψ⟩⟨ψ| + H(X,Y) + E(ρ_AB) + Φ · r · e^{b0}) dω = Ψ_universe
```

**v2.0** adds a strong explicit attraction term to the fixed point **Ψ_universe**, intended to make it tighter and more robust than classical negative attractors under simulated plasma disturbances (diagnostic noise, wall drift, actuator delay). This has not yet been established by a reproducible benchmark.

---

## What's New in v2.0

- Strong centering force to **Ψ_universe** (direct from `d|ψ⟩⟨ψ|` term)
- **Lyapunov stability sketch** (argument outline for ultimate boundedness; not a complete proof)
- Robustness test with simulated disturbances (noise + wall drift + actuator delay) added to a real signal
- Exploratory test on the plasma current trace of **one** EAST discharge (#41195)

---

## Status of Results (please read)

An earlier version of this README listed a comparison table (Ψ v2 std 0.274 vs. classical attractors). That table is **withdrawn** until it can be reproduced, because:

- It comes from **one** EAST discharge (#41195), with synthetic noise, spikes, wall drift and a 2-sample delay added to the real plasma-current trace.
- The script and data needed to regenerate it are **not in this repository** (`east_ip.txt` is not included, and the comparison filters were never committed).
- The metric (standard deviation of the filter output) rewards a filter that simply shrinks its output toward zero; it does not measure tracking error against the true signal, so a lower number is not evidence of better control.

A reproducible benchmark (multiple discharges, tracking-error metrics, all baselines in code) is in preparation. Until then, treat this library as exploratory research code.

---

## Quick Start

```python
from psi_filter_v2 import PsiFilter
import numpy as np

filter = PsiFilter(gamma=0.35, attraction_strength=0.8)
psi = filter.reduce(filter.evolve(features_scaled, t))
```

---

## Citation (please use this)

Quiroz, N. B. (2026).  
*Psi Universe Attractor Library v2.0 — Toroidal Path-Integral Filter with Lyapunov Stability (Tested on Real EAST #41195 Data)* — title of the archived v2.0 record; see Status of Results above. [Software].  
Zenodo. https://doi.org/10.5281/zenodo.18939068

---

## License

Copyright (C) 2026 Nicolas B. Quiroz, MD  

Licensed under the **Apache License, Version 2.0**  
(see the `LICENSE` file for full text).

---

## Preprint Note

This is an open-source research artifact. A full technical preprint with detailed derivations, multi-shot analysis, and additional EAST discharges will be linked in future versions. Feedback and real-shot collaborations are welcome.

## Keywords:
tokamak
fusion energy
plasma physics
toroidal plasma
magnetic confinement
plasma attractor dynamics
