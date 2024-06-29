# Usar a imagem oficial do Python 3.11.5 baseada em Alpine
FROM python:3.11.5-alpine

# Atualizar e instalar dependências necessárias
RUN apk add --no-cache bash build-base python3-dev libffi-dev

# Definir o diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos da aplicação para o diretório de trabalho
COPY . .

# Instalar as dependências do projeto
RUN pip install .

# Expor a porta que o servidor usará
EXPOSE 4333

# Comando para rodar a aplicação
CMD ["python", "simple_chat/server.py"]
