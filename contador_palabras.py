
from collections import Counter

def count_words(filename):
    try:
        print(f"Intentando abrir el archivo: {filename}")
        with open(filename, 'r', encoding='utf-8') as file_handle:
            text = file_handle.read()
        print("Archivo leído exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encontró.")
        return
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return

    # Procesar el texto
    palabras = text.lower().split()
    conteo = Counter(palabras)

    # Mostrar los resultados
    print("\nConteo de palabras:")
    for palabra, frecuencia in conteo.most_common(10):  # Mostrar las 10 palabras más frecuentes
        print(f"{palabra}: {frecuencia}")

# Ruta al archivo definida como variable
files = "C:/Users/User/Desktop/project_python/archivo.txt"

if __name__ == "__main__":
    # Llamar directamente a la función con la ruta predeterminada
    count_words(files)
