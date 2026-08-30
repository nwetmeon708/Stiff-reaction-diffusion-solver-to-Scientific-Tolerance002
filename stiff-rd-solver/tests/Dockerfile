FROM python:3.13-slim-bookworm

# Pre-install everything the verifier needs — test.sh must never apt-get /
# curl / pip install at verify time
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
RUN pip install pytest==9.1.1 pytest-json-ctrf==0.5.2

# Bake tests into the image — harbor does NOT upload tests/ at verify time
COPY . /tests/

# Pre-create the parent dir of every declared artifact
RUN mkdir -p /app
