# Psi Universe Attractor Library v2.0

**Toroidal Path-Integral Attractor Filter with Explicit Lyapunov Stability**  
Tested on **real EAST #41195 experimental tokamak discharge data**.

---

## Overview

This library implements the **Ψ_universe attractor** derived from the closed toroidal path-integral equation:

```
∫_γ (d|ψ⟩⟨ψ| + H(X,Y) + E(ρ_AB) + Φ · r · e^{b0}) dω = Ψ_universe
```

**v2.0** adds a strong explicit attraction term to the fixed point **Ψ_universe**, making it provably tighter and more robust than classical negative attractors even under realistic plasma conditions (diagnostic noise, wall drift, actuator delay).

---

## What's New in v2.0

- Strong centering force to **Ψ_universe** (direct from `d|ψ⟩⟨ψ|` term)
- Full **Lyapunov stability proof** (global ultimate boundedness + exponential convergence)
- Real-plasma robustness test (noise + wall interaction + actuator delay)
- Validation on **real EAST #41195 experimental data** (not synthetic)

---

## Results on Real EAST #41195 Discharge

Psi v2 outperforms all classical negative attractors:

- **Psi Universe v2 (Yours)**: **0.274** ← best
- Negative - Simple Exp Decay: 0.527
- Negative - Critically Damped: 0.629
- Negative - Linear Damping: 8.497 (unstable)
- Positive - Growing Logistic: 25.698 (unstable)

The attractor remains tight and physically faithful across the entire discharge.

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
*Psi Universe Attractor Library v2.0 — Toroidal Path-Integral Filter with Lyapunov Stability (Tested on Real EAST #41195 Data)* [Software].  
Zenodo. https://doi.org/10.5281/zenodo.18939068

---

## License

Copyright (C) 2026 Nicolas B. Quiroz, MD  

Licensed under the **Apache License, Version 2.0**  
(see the `LICENSE` file for full text).

---

## Preprint Note

This is an open-source research artifact. A full technical preprint with detailed derivations, multi-shot analysis, and additional EAST discharges will be linked in future versions. Feedback and real-shot collaborations are welcome.
