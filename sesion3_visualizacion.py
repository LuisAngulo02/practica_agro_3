# sesion3_visualizacion.py
import matplotlib.pyplot as plt
from Bio import SeqIO

ids = []
longitudes = []
secuencia_ejemplo = ""

# Leer datos del archivo
for i, record in enumerate(SeqIO.parse("ls_orchid.fasta", "fasta")):
    ids.append(record.id)
    longitudes.append(len(record.seq))
    if i == 0:  # Guardamos la primera secuencia para el gráfico de pastel
        secuencia_ejemplo = str(record.seq)

# 1. Gráfico de barras (Primeras 10 secuencias)
plt.figure(figsize=(10, 5))
plt.bar(ids[:10], longitudes[:10], color='skyblue')
plt.xticks(rotation=90)
plt.ylabel("Longitud (pares de bases)")
plt.title("Longitud de las primeras 10 secuencias")
plt.tight_layout()
plt.savefig("barras_longitud.png") # Guardamos como imagen
plt.show()

# 2. Gráfico de pastel
conteo_A = secuencia_ejemplo.count("A")
conteo_T = secuencia_ejemplo.count("T")
conteo_G = secuencia_ejemplo.count("G")
conteo_C = secuencia_ejemplo.count("C")

proporciones = [conteo_A, conteo_T, conteo_G, conteo_C]
etiquetas = ["Adenina (A)", "Timina (T)", "Guanina (G)", "Citosina (C)"]
colores = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

plt.figure(figsize=(7, 7))
plt.pie(proporciones, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=140)
plt.title(f"Proporciones de Bases Genéticas\n(Secuencia: {ids[0]})")
plt.tight_layout()
plt.savefig("pastel_proporciones.png")
plt.show()