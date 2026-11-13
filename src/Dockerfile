FROM python:3.12-slim
WORKDIR /app
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/app.py ./
COPY src/static ./static
COPY content /data/content
ENV OPENAKADEMEIA_CONTENT=/data/content DATABASE_URL=sqlite:////data/db/openakademeia.db
RUN mkdir -p /data/db
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
