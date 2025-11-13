# Usa imagem base do Python
FROM python:3.11-slim

# Evita geração de arquivos .pyc e força logs no console
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema necessárias para o WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    libjpeg-dev \
    libpng-dev \
    fonts-liberation \
    fonts-dejavu-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Atualiza o pip e instala as dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define a porta que o Render vai usar
ENV PORT=5000

# Comando padrão para iniciar o app com Gunicorn
CMD gunicorn run:app --bind 0.0.0.0:$PORT
