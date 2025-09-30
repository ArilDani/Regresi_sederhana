import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Simulasi Regresi Linear Sederhana")

# =============================
#data frame sederhana
data = {
    "bulan": [1, 2, 3, 4, 5, 6],
    "penjualan": [120, 135, 150, 160, 175, 190]
}
df = pd.DataFrame(data)

st.subheader("Data Penjualan")
st.write(df)

# =============================
#Regresi Linear menggunakan numpy
X = df["bulan"].values
y = df["penjualan"].values

m, b = np.polyfit(X, y, 1)  # slope dan intercept
st.write(f"Persamaan regresi: **Penjualan = {m:.2f} * bulan + {b:.2f}**")

#Prediksi bulan berikutnya
bulan_baru = X.max() + 1
prediksi = m * bulan_baru + b
st.success(f"Prediksi penjualan bulan ke-{bulan_baru}: **{prediksi:.2f}**")

# =============================
#Visualisasi menggunakan seaborn
fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(x=X, y=y, color="blue", s=100, ax=ax, label="Data Penjualan")
sns.lineplot(x=X, y=m*X+b, color="red", linestyle="--", ax=ax, label="Garis Regresi")
ax.scatter(bulan_baru, prediksi, color="green", s=120, label=f"Prediksi Bulan {bulan_baru}")

ax.set_xlabel("Bulan")
ax.set_ylabel("Penjualan")
ax.set_title("Simulasi Regresi Linear Sederhana")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# =============================
#Kesimpulan
st.subheader("Kesimpulan")
trend = "meningkat" if m > 0 else "menurun" if m < 0 else "stabil"
st.write(
    f"Berdasarkan hasil regresi linear, penjualan cenderung **{trend}** setiap bulan "
    f"dengan rata-rata perubahan sekitar **{m:.2f} unit per bulan**. "
    f"Prediksi penjualan pada bulan ke-{bulan_baru} adalah **{prediksi:.2f}**, "
    f"menunjukkan tren {trend} dari data sebelumnya."
)

# =============================
# Link Source Code
st.markdown("**Source Code:** [Lihat di GitHub](https://github.com/ArilDani/Regresi_sederhana)")
