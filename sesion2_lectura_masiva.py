# sesion2_lectura_masiva.py
from Bio import SeqIO

longitudes = []

# 1. Leer automáticamente todas las secuencias y guardar longitudes
print("ID y Longitud de las secuencias encontradas:")
for record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(f"ID: {record.id} | Longitud: {len(record.seq)}")
    longitudes.append(len(record.seq))

print("-" * 50)

# 2. Mostrar estadísticas generales
numero_total = len(longitudes)
longitud_promedio = sum(longitudes) / numero_total if numero_total > 0 else 0
secuencia_mas_larga = max(longitudes) if numero_total > 0 else 0

print(f"Número total de secuencias: {numero_total}")
print(f"Longitud promedio: {longitud_promedio:.2f} pares de bases")
print(f"Secuencia más larga: {secuencia_mas_larga} pares de bases")