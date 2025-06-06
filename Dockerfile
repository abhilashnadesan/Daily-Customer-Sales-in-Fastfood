FROM python:3.9-slim

WORKDIR /app

# Install system dependencies needed for some Python packages (like pandas)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade pip before installing requirements
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "etl_analysis.py"]

