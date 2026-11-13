import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from psi_filter_v2 import PsiFilter   # ← the file above

# Load your real EAST data
df = pd.read_csv('east_ip.txt', sep=r'\s+', header=None, names=['time_s', 'ip_ma'])
t = df['time_s'].values
signal = df['ip_ma'].values

# Add real plasma effects
np.random.seed(42)
noise = np.random.normal(0, 0.03, len(t))
spikes = np.random.choice([0, 1], len(t), p=[0.98, 0.02]) * np.random.normal(0, 0.4, len(t))
wall_drift = 0.02 * np.cumsum(np.random.normal(0, 0.01, len(t)))
wall_signal = signal + noise + spikes + wall_drift
delayed_signal = np.roll(wall_signal, 2)
delayed_signal[:2] = wall_signal[:2]

features_scaled = (delayed_signal.reshape(-1, 1) - delayed_signal.mean()) / delayed_signal.std()

# Run Psi v2 only. The baseline attractors used in an earlier, unpublished
# comparison are not included in this repository, so no ranking is claimed here.
psi_filter = PsiFilter(gamma=0.35, attraction_strength=0.8)
psi_output = psi_filter.reduce(psi_filter.evolve(features_scaled, t))

print(f"Psi v2 output std: {np.std(psi_output):.3f}")
print("Note: std of the output rewards shrinkage toward zero; it is not a tracking-error metric.")
print("Baseline comparison not included; see README 'Status of Results'.")
