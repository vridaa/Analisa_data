import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

 
st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('Belajar analisa data ')
all_df = pd.read_csv('alldata.csv')


col1, col2 = st.columns(2)
 
with col1:
    average_review_score_by_category = all_df.groupby('product_category_name')['review_score'].mean().reset_index()
    average_review_score_by_category.columns = ['product_category_name', 'average_review_score']

    st.write("Rata-rata Skor Ulasan per Kategori Produk:")
    st.dataframe(average_review_score_by_category)
 
with col2:
    st.write("Dataframe all_df:")
    st.dataframe(all_df) 

st.write("Statistik Deskriptif untuk all_df:")
st.write(all_df.describe(include="all"))


sorted_df = all_df.groupby('product_category_name')['review_score'].mean().sort_values(ascending=False).reset_index()

st.title('Rata-rata Skor Ulasan per Kategori Produk')

plt.figure(figsize=(6, 12))
sn.barplot(x='review_score', y='product_category_name', data=sorted_df)
plt.xticks(rotation=90)
plt.title('Rata-rata Skor Ulasan per Kategori Produk')

st.pyplot(plt)


correlation_estimasi = all_df[['selisih_estimasi_penerimaan', 'review_score']].corr()

plt.figure(figsize=(6, 6))
sn.heatmap(correlation_estimasi, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Heatmap Korelasi antara Selisih Estimasi Penerimaan dan Skor Ulasan')
st.pyplot(plt)  

numeric_df = all_df.select_dtypes(include=[np.number])
correlation_all = numeric_df.corr()

review_correlation = correlation_all[['review_score']]

st.write("Korelasi antara Semua Kolom dan Skor Ulasan:")
st.write(review_correlation)

plt.figure(figsize=(6, 6))
sn.heatmap(review_correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Heatmap Korelasi antara Semua Kolom dan Skor Ulasan')
st.pyplot(plt)
