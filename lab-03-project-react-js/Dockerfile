FROM node:18-alpine as build

WORKDIR /react_app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

FROM docker.io/node:18-alpine as product

WORKDIR /react_app/app

COPY --from=build /react_app/dist/ /react_app/app/dist/

COPY package.json .
COPY vite.config.ts .

RUN npm install typescript

EXPOSE 8080
CMD ["npm", "run", "preview"]