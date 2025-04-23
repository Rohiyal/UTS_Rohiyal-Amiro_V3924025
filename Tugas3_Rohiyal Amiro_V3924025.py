import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_pasien2.csv", sep=";")

Jumlah_Pasien = pd.crosstab(df["Hasil_Tes"], df["Menderita_Penyakit"], margins=True)
print("Jumlah Pasien:")
print(Jumlah_Pasien)

TP = Jumlah_Pasien.loc["Positif", "Ya"]
FP = Jumlah_Pasien.loc["Positif", "Tidak"]
TN = Jumlah_Pasien.loc["Negatif", "Tidak"]
FN = Jumlah_Pasien.loc["Negatif", "Ya"]

PPV = TP / (TP + FP)  
NPV = TN / (TN + FN)  

print("\nHasil Perhitungan:")
print(f"a. P(Sakit | Positif) = {PPV:.4f}")
print(f"b. P(Tidak Sakit | Negatif) = {NPV:.4f}")

plt.figure(figsize=(8, 5))
df["Hasil_Tes"].value_counts().plot(kind="bar", color=["#4CAF50", "#FF5722"])
plt.title("Distribusi Hasil Tes Positif dan Negatif")
plt.xlabel("Hasil Tes")
plt.ylabel("Jumlah Pasien")
plt.xticks(rotation=0)
plt.show()
