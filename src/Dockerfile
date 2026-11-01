FROM python:3.12-slim
WORKDIR /app
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/app.py ./
COPY src/static ./static
COPY content /data/content
COPY plugins/cognitive-sparring-partner /data/plugin
ENV OPENACADEMY_CONTENT=/data/content OPENACADEMY_PLUGIN=/data/plugin
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
