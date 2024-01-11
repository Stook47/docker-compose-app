FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY visualization.py /app
COPY templates /app/templates

RUN ls -l /app
COPY ../static /app/static/

CMD ["python", "visualization.py"]
