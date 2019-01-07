FROM        smallbee3/trello:base
MAINTAINER  smallbee3@gmail.com

ENV         BUILD_MODE  prod
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

# Frontend
# 1) git clone
WORKDIR     /srv
RUN         rm -rf      /srv/frontend
RUN         git clone https://github.com/smallbeehive/trello-frontend.git frontend
WORKDIR     /srv/frontend
# 2) git pull
#WORKDIR    /srv/frontend
#RUN        git pull origin master

RUN         npm install

# Backend
COPY        .   /srv/project
RUN         cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf      /etc/nginx/nginx.conf
RUN         cp -f   /srv/project/.config/${BUILD_MODE}/nginx-app.conf  /etc/nginx/sites-available/
RUN         rm -f   /etc/nginx/sites-enalbed/*
RUN         ln -sf  /etc/nginx/sites-available/nginx-app.conf          /etc/nginx/sites-enabled/
RUN         cp -f   /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/
CMD         pkill nginx; supervisord -n
EXPOSE      80
