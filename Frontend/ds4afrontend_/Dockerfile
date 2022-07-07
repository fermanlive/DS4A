FROM node:lts-alpine

WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY yarn.lock ./
COPY ./ ./

RUN yarn add node-sass
RUN yarn

CMD ["yarn", "start"]