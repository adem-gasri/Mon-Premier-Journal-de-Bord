import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 🌟 CONFIG PAGE
st.set_page_config(
    page_title="Dashboard Ventes",
    page_icon="📊",
    layout="wide"
)

# 🎨 TITRE STYLE
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📊 Analyse des Ventes</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# 📂 CHARGEMENT DONNÉES
uploaded_file = st.file_uploader("📂 Importer un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("⚠️ Veuillez uploader un fichier CSV pour continuer.")
    st.stop()

# ⚙️ CALCULS
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.2

# 💰 KPIs (cartes)
col1, col2, col3 = st.columns(3)

col1.metric("💰 CA Total", f"{df['CA_Net'].sum():.2f}")
col2.metric("📦 Produits", len(df))
col3.metric("🏆 Meilleur ID", df.loc[df["CA_Net"].idxmax(), "ID"])

st.markdown("---")

# 📊 TABLEAU
st.subheader("📋 Données détaillées")
st.dataframe(df, use_container_width=True)

# 📈 GRAPHIQUE
st.subheader("📊 CA par produit")

fig, ax = plt.subplots()
ax.bar(df["ID"], df["CA_Net"])
ax.set_title("Chiffre d'affaires net")
ax.set_xlabel("ID Produit")
ax.set_ylabel("CA Net")

st.pyplot(fig)

st.markdown("---")

# ✨ FOOTER
st.markdown(
    "<p style='text-align: center; color: grey;'>Dashboard créé avec Streamlit 🚀</p>",
    unsafe_allow_html=True
)