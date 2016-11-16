#!/usr/bin/env bash

NAME='politikon'
DB_NAME='politikon_db'
PSQL_VER='postgres:latest'
NODE_NAME='politikon_instance'
CELERY_NAME='politikon_celery'
CELERY_REDIS_NAME='politikon_celery_redis'
DOCKER_RUN='./docker_run.sh'

function pri {
    echo " [${1}] $2"
}

echo " Please be patient..."

if   ! docker ps -a | grep $DB_NAME >/dev/null; then
    pri 'db' "$DB_NAME do not exist - did you run $DOCKER_RUN ?"
elif ! docker ps -a | grep $DB_NAME | grep Up >/dev/null; then
    pri 'db' "nothing to do - $DB_NAME not running"
else
    pri 'db' "stopping $DB_NAME..."
    docker stop $DB_NAME
fi

##
#docker run --name some-redis -d redis
## persistance mode
#docker run --name some-redis -d redis redis-server --appendonly yes

#docker run --link some-redis:redis -e CELERY_BROKER_URL=redis://redis --name some-celery -d celery

docker run --name some-app --link some-redis:redis -d application-that-uses-redis



if   ! docker ps -a | grep $NODE_NAME >/dev/null; then
    pri 'vm' "$NODE_NAME do not exist - did you run $DOCKER_RUN ?"
elif ! docker ps -a | grep $NODE_NAME | grep Up >/dev/null; then
    pri 'vm' "nothing to do - $NODE_NAME not running"
else
    pri 'vm' "stopping $NODE_NAME..."
    docker stop $NODE_NAME
fi

echo " bye, bye, bye..."

