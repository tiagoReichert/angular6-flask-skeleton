LABEL maintainer "tiago@reichert.eti.br"

# Stage 0, based on Node.js, to build and compile Angular
FROM node:10.4.1 as build
WORKDIR /app
COPY ./ /app/
RUN npm install
RUN npm run build --prod

# Stage 1, based on Nginx, to have only the compiled frontend, ready for production with Nginx
FROM nginx:1.15
COPY --from=build /app/dist/frontend/* /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
