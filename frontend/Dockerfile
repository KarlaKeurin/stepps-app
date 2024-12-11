# Usando a imagem oficial do Node
FROM node:18.19.1

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar o restante dos arquivos
COPY . .

# Build do projeto Angular
RUN npm run build

# Expor a porta 4200
EXPOSE 4200

# Rodar o servidor para exibir a aplicação
CMD ["npm", "start"]
