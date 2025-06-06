FROM python:3.9-slim

WORKDIR /app

# Install build tools required to compile pandas and other packages
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

# Upgrade pip before installing requirements
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "etl_analysis.py"]

