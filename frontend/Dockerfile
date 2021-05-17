FROM node:12

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . /app

CMD ["npm", "start"]
