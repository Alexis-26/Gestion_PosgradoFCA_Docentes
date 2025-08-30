# Usa la imagen base de Python 3.11
FROM python:3.11-slim

# Instala unzip y curl
RUN apt-get update && apt-get install -y unzip curl

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt ./

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el resto del proyecto
COPY . .

# Expone el puerto dinámico que Railway asigna
EXPOSE 8000

# Arranca backend + frontend usando el PORT de Railway
CMD ["sh", "-c", "reflex run --env prod --backend-only --host 0.0.0.0 --port ${PORT:-8080}"]