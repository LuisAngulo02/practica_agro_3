# sesion1_analisis_basico.py

# 1. Abrir y leer el archivo
with open("ls_orchid.fasta", "r") as archivo:
    contenido = archivo.read()
    print("Primeros 500 caracteres del archivo:")
    print(contenido[:500])
    print("-" * 50)

# 2. Trabajar una secuencia como cadena

secuencia = "ATGCGTACGTAGCTAGCTAGCTA"

# 3. Funciones simples
longitud = len(secuencia)
conteo_A = secuencia.count("A")
conteo_T = secuencia.count("T")
conteo_C = secuencia.count("C")
conteo_G = secuencia.count("G")

# Calcular porcentaje GC
porcentaje_GC = ((conteo_G + conteo_C) / longitud) * 100 if longitud > 0 else 0

# 4. Imprimir resultados
print(f"Secuencia analizada: {secuencia}")
print(f"Longitud de la secuencia: {longitud}")
print(f"Bases -> A: {conteo_A}, T: {conteo_T}, C: {conteo_C}, G: {conteo_G}")
print(f"Porcentaje GC: {porcentaje_GC:.2f}%")