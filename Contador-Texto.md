# README - Contador de Palabras en un Archivo de Texto

Este proyecto contiene un script en Python que permite contar las palabras más frecuentes de un archivo de texto. Utiliza el módulo `Counter` de la librería `collections` para realizar un análisis y mostrar las palabras más comunes, junto con su frecuencia de aparición. El archivo de texto debe ser proporcionado por el usuario y la función procesará el contenido de dicho archivo.

## Descripción del Código

El script contiene la siguiente lógica principal:

1. **Abrir y leer el archivo de texto**: El código intenta abrir el archivo especificado y leer su contenido.
2. **Procesar el texto**: Convierte todo el texto a minúsculas y lo divide en palabras individuales.
3. **Contar las palabras**: Utiliza `Counter` para contar la frecuencia de cada palabra en el texto.
4. **Mostrar las palabras más frecuentes**: Se muestran las 10 palabras más comunes con su respectiva frecuencia de aparición.

## Requisitos

- Python 3.x o superior.
- El archivo de texto debe estar en formato `.txt` y debe contener texto legible.
- La ruta al archivo debe ser correcta y debe tener permisos de lectura.

## Cómo usar el archivo

1. **Preparar el archivo de texto**:
   - Asegúrate de tener un archivo de texto (`archivo.txt` o cualquier otro nombre de archivo `.txt`) que quieras analizar.
   - Coloca el archivo en una ubicación accesible en tu sistema (en el ejemplo, el archivo está ubicado en el escritorio del usuario).

2. **Actualizar la ruta del archivo**:
   - Dentro del archivo `script.py`, actualiza la ruta del archivo en la variable `files`:
     ```python
     files = "C:/ruta/al/archivo.txt"
     ```
     Asegúrate de que la ruta sea correcta según el sistema operativo.

3. **Ejecutar el script**:
   - Una vez que hayas configurado la ruta correctamente, abre una terminal o consola y navega al directorio donde se encuentra el archivo `script.py`.
   - Ejecuta el script con el siguiente comando:
     ```bash
     python script.py
     ```

4. **Resultados**:
   - El script intentará abrir el archivo y leer su contenido. Si todo es correcto, mostrará las 10 palabras más frecuentes junto con su cantidad de ocurrencias.
   - Si el archivo no se encuentra o hay algún error, el script mostrará un mensaje adecuado.

## Ejemplo de Salida

Supongamos que el archivo contiene el siguiente texto:


### Notas

- El script maneja los errores de forma que si el archivo no se encuentra o hay problemas al leerlo, se informará adecuadamente.
- El conteo se realiza sin distinguir entre mayúsculas y minúsculas (es decir, no diferencia "Texto" de "texto").

## Modificaciones

Si deseas ajustar el número de palabras más frecuentes mostradas, puedes modificar el número en el siguiente fragmento de código:

```python
for palabra, frecuencia in conteo.most_common(10):
