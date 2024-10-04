import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.title("Proyek Analisis Data: Bike Sharing Dataset")

# Fungsi untuk memuat data
def load_data():
    df = pd.read_csv("all_data.csv")
    return df

# Memuat data
data = load_data()

# Tampilkan tabel data
st.subheader("Tabel Data Penyewa Sepeda")
st.dataframe(data)

# Pilihan untuk menampilkan grafik berdasarkan kolom tertentu
st.subheader("Visualisasi Data")
visualization_type = st.selectbox("Pilih tipe visualisasi", ["Line Plot", "Bar Plot", "Pie Chart", "Heatmap", "Boxplot"])
selected_column = st.selectbox("Pilih kolom untuk visualisasi", options=data.columns)

# Buat visualisasi berdasarkan tipe yang dipilih
fig, ax = plt.subplots()

# Line Plot
if visualization_type == "Line Plot":
    ax.plot(data[selected_column], label=selected_column)
    ax.set_xlabel("Index")
    ax.set_ylabel(selected_column)
    ax.set_title(f"Grafik {selected_column}")
    ax.legend()

# Bar Plot
elif visualization_type == "Bar Plot":
    sns.barplot(x=data.index, y=selected_column, data=data, ax=ax)
    ax.set_title(f"Bar Plot {selected_column}")
    ax.set_xlabel("Index")
    ax.set_ylabel(selected_column)

# Pie Chart
elif visualization_type == "Pie Chart":
    # Pastikan kolom yang dipilih kategorikal atau memiliki beberapa kategori
    pie_data = data[selected_column].value_counts()  # Menghitung distribusi nilai
    ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    ax.set_title(f"Pie Chart {selected_column}")

# Heatmap
elif visualization_type == "Heatmap":
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Heatmap Korelasi")

# Boxplot
elif visualization_type == "Boxplot":
    sns.boxplot(y=selected_column, data=data, ax=ax)
    ax.set_title(f"Boxplot {selected_column}")

# Tampilkan grafik di Streamlit
st.pyplot(fig)
