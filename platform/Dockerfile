FROM python:3.12-slim
WORKDIR /app
COPY platform/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY platform/app.py ./
COPY platform/static ./static
COPY library /data/library
COPY addon /data/addon
ENV OPENACADEMY_LIBRARY=/data/library OPENACADEMY_ADDON=/data/addon
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
