import sys
from collections import Counter

def count_words(filename):
    try:
        with open(filename,'r', encoding='utf-8') as file_handle:
            text= file_handle.read()
    except FileNotFoundError:
        print(f"El archivo '{text}' no se encontró.")
        return
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return

    # Procesar el texto
    palabras = text.lower().split()
    conteo = Counter(palabras)

    # Mostrar los resultados
    print("\nConteo de palabras:")
    for palabra, frecuencia in conteo.most_common():
        print(f"{palabra}: {frecuencia}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f'Uso: python contador_palabras.py <archivo.txt>')
    else:
        count_words(sys.argv[1])