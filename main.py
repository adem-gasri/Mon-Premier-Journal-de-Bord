import pandas as pd

# Lire le fichier
df = pd.read_csv("vente.csv")

# CA Brut
df["CA_Brut"] = df["Prix"] * df["Quantite"]

# CA Net
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)

# TVA
df["TVA"] = df["CA_Net"] * 0.2

# CA Total
ca_total = df["CA_Net"].sum()
print("CA Total =", ca_total)

# Produit le plus rentable
produit_max = df.loc[df["CA_Net"].idxmax(), "ID"]
print("Produit le plus rentable ID =", produit_max)

# Export fichier final
df.to_csv("resultats_final.csv", index=False)

print("Export terminé")
import matplotlib.pyplot as plt

plt.bar(df["ID"], df["CA_Net"])
plt.title("CA par produit")
plt.xlabel("ID")
plt.ylabel("CA Net")
plt.show()