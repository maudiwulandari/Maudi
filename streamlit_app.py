import streamlit as st

st.title("🎈My new app ")
st.write(
   "HI THERE! [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("Screenshot_2025-04-17-13-05-08-19_b86672daa061159f52c1a3195c773d05.jpg")
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
