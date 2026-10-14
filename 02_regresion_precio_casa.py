from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


carpeta_proyecto = Path(__file__).resolve().parent
datos = pd.DataFrame(
    {
        "tamano_m2": [50, 60, 80, 100, 120, 150],
        "precio_usd": [120000, 135000, 180000, 210000, 250000, 300000],
    }
)

x = datos[["tamano_m2"]]
y = datos["precio_usd"]
modelo = LinearRegression()
modelo.fit(x, y)
precio_estimado = modelo.predict(pd.DataFrame({"tamano_m2": [90]}))[0]

plt.figure(figsize=(8, 5))
plt.scatter(datos["tamano_m2"], datos["precio_usd"], color="royalblue", label="Datos históricos")
plt.plot(datos["tamano_m2"], modelo.predict(x), color="crimson", label="Línea de regresión")
plt.scatter(90, precio_estimado, color="darkgreen", label="Predicción para 90 m²")
plt.title("Precio de casa según tamaño")
plt.xlabel("Tamaño (m²)")
plt.ylabel("Precio (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(carpeta_proyecto / "grafico_regresion_casas.png", dpi=150)

print(f"Precio estimado para una casa de 90 m²: ${precio_estimado:,.2f}")

if plt.get_backend().lower() != "agg":
    plt.show()
