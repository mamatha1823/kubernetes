FROM almalinux:9
RUN dnf install nginx -y
RUN rm -f /usr/share/nginx/html/index.html
COPY index.html /usr/share/nginx/html/index.html