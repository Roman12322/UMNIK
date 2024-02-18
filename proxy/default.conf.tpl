server {
    listen ${LISTEN_PORT};

    location /static {
        alias /aiforce/static;
    }

    location /media {
        alias /aiforce/media;
    }

    location / {
        proxy_pass http://${APP_HOST}:${APP_PORT};
        include    /etc/nginx/proxy_params;
    }
}