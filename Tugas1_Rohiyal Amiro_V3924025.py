import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lambda_ = 8  
total_jam = 12 * 30  

np.random.seed(42)  
simulasi_kedatangan = np.random.poisson(lambda_, total_jam)

plt.figure(figsize=(10, 6))
plt.hist(simulasi_kedatangan, bins=range(0, 21), density=True, alpha=0.7, label="Simulasi")
x = np.arange(0, 21)
plt.plot(x, poisson.pmf(x, lambda_), 'ro-', label="Teoritis Poisson")
plt.xlabel("Jumlah Kedatangan per Jam")
plt.ylabel("Probabilitas")
plt.title("Distribusi Kedatangan Pelanggan")
plt.legend()
plt.show()

prob_a_sim = np.mean(simulasi_kedatangan == 0)  
prob_b_sim = np.mean(simulasi_kedatangan > 10)  

prob_a_teori = poisson.pmf(0, lambda_)
prob_b_teori = 1 - poisson.cdf(10, lambda_)

print("Hasil Perbandingan:")
print(f"a. P(Kedatangan = 0): Simulasi = {prob_a_sim:.4f}, Teori = {prob_a_teori:.4f}")
print(f"b. P(Kedatangan > 10): Simulasi = {prob_b_sim:.4f}, Teori = {prob_b_teori:.4f}")
