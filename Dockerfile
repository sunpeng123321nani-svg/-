FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

ENV PORT=9000
ENV WSGI_SERVER=waitress

CMD ["python", "server.py"]
