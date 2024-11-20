#arm compatatible 
FROM python:3.9-slim

WORKDIR /app

COPY . /app

COPY . /converted_data/data

COPY . /csv_to_json

# dependancies 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
