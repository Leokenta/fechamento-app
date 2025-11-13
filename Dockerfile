FROM python:3.11-slim


# Dependências do sistema para WeasyPrint
RUN apt-get update && apt-get install -y \
build-essential libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev share