# Usa una imagen base de Python
FROM python:3.10

RUN adduser --disabled-password --gecos '' appuser

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY main.py .

USER appuser

# Expone el puerto (ajústalo si es necesario)
EXPOSE 5000

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]
