# sesion4_traduccion_patrones.py
from Bio.Seq import Seq

# Secuencia de prueba
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# 1. Traducción a proteínas
proteina = dna.translate()

# 2. Búsqueda de un motivo
motivo = "ATG"
secuencia_str = str(dna)
posiciones = []

pos = secuencia_str.find(motivo)
while pos != -1:
    posiciones.append(pos)
    pos = secuencia_str.find(motivo, pos + 1)

# Imprimir en consola
print(f"Secuencia DNA: {dna}")
print(f"Proteína traducida: {proteina}")
print(f"El motivo '{motivo}' se encuentra en los índices: {posiciones}")

# 3. Guardar resultados en un archivo .txt
with open("resultados_sesion4.txt", "w") as archivo_txt:
    archivo_txt.write("--- Análisis de Secuencia ---\n")
    archivo_txt.write(f"Secuencia DNA Original: {dna}\n")
    archivo_txt.write(f"Proteína Traducida: {proteina}\n")
    archivo_txt.write(f"Índices del motivo '{motivo}': {posiciones}\n")

print("\nResultados guardados exitosamente en 'resultados_sesion4.txt'.")