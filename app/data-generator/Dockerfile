FROM python:3.8-slim


WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY data_generator.py /app/
RUN ls -l /app   # Debugging line
COPY ../static /app/static/

CMD ["python", "data_generator.py"]