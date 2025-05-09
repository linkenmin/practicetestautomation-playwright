FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--headless", "-n", "auto"]
