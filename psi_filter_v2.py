import numpy as np

class PsiFilter:
    def __init__(self, dim=128, omega=2*np.pi*0.4, gamma=0.35, hurst=0.8, variance=0.05, attraction_strength=0.8):
        self.dim = dim
        self.omega = omega
        self.gamma = gamma
        self.hurst = hurst
        self.variance = variance
        self.attraction_strength = attraction_strength
        self.a_i = np.random.uniform(0.5, 1.5, dim)
        self.target = 0.0

    def evolve(self, features_scaled, t):
        psi = np.zeros((len(t), self.dim))
        for i in range(self.dim):
            oscillatory = (np.cos(self.omega * t) + 1j * np.sin(self.omega * t)) * np.exp(-self.gamma * t)
            turbulence = self.hurst * features_scaled[:, 0] * np.random.normal(0, self.variance, len(t))
            base = self.a_i[i] * np.real(oscillatory) * features_scaled[:, i % features_scaled.shape[1]] + turbulence
            attraction = self.attraction_strength * (self.target - base) * (1 - np.exp(-self.gamma * t))
            psi[:, i] = base + attraction
        return psi

    def reduce(self, psi):
        return psi.mean(axis=1)

# For direct import in benchmark
if __name__ == "__main__":
    print("PsiFilter v2.0 loaded successfully")
