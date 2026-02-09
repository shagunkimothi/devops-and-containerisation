FROM alpine:3.19

RUN apk add --no-cache nginx \
    && mkdir -p /run/nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
