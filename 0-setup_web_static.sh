#!/usr/bin/env bash

# updates the list of available packages and their versions
sudo apt-get update

# install nginx if no exist
sudo apt-get install nginx -y

# make dir: /data
# -p flag: no error if existing
sudo mkdir -p /data/

# make dir: /data/web_static/
# -p flag: no error if existing
sudo mkdir -p /data/web_static/

#make dir: /data/web_static/releases/
# -p flag: no error if existing
sudo mkdir -p /data/web_static/releases/

# make dir: /data/web_static/shared/
# -p flag: no error if existing
sudo mkdir -p /data/web_static/shared/

#make dir: /data/web_static/releases/test/
# -p flag: no error if existing
sudo mkdir -p /data/web_static/releases/test

#make file HTML
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

# make simboloic link: /data/web_static/releases/test/ /data/web_static/current
# ln -sf [Specific file/directory] [symlink name]
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
# owner
sudo chown -R ubuntu /data/
# group
sudo chgrp -R ubuntu /data/

# Update the Nginx configuration to serve the content
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.holbertonschool.com/co;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    add_header X-Served-By $HOSTNAME;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" > /etc/nginx/sites-available/default

# restart Nginx server
sudo nginx -s reload
