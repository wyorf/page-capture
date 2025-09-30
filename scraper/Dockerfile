FROM python:3.11

WORKDIR /app

# Installing Chromium та ChromeDriver
RUN apt-get update && apt-get install -y \
      chromium chromium-driver ca-certificates curl wget unzip \
    && update-ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Installing Python-libraries
# ignoring ssl certs.. not for prod!
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org selenium==4.13.0

COPY app.py .

RUN mkdir -p /output

CMD ["sh", "-c", "python /app/app.py \"$URL\""]
