#!/bin/bash

function startworker {
    echo "start hawk worker..."
    celery multi start w1 w2 w3 w4 w5 w6 w7 w8 -A hawk -l info --pidfile=./logs/%n.pid --logfile=./logs/%n%I.log
}

function stopworker {
    echo "stop hawk worker..."
    celery multi stopwait w1 w2 w3 w4 w5 w6 w7 w8 -A hawk -l info --pidfile=./logs/%n.pid
}

function restartworker {
    echo "restart hawk worker..."
    celery multi restart w1 w2 w3 w4 w5 w6 w7 w8 -A hawk -l info --pidfile=./logs/%n.pid --logfile=./logs/%n%I.log
}

function startflower {
    echo "start flower server..."
    celery -A hawk flower --port=5555 &    
}

function stopflower {
    echo "stop flower server..."
    python3 ./toolkit/killflower.py
}

function startweb {
    echo "start web server..."
    sudo python3 app.py --port=80 &
}

function usage {
    echo "usage:"
    echo "      start: start hawk worker"
    echo "      stop: stop hawk worker"
    echo "      restart: restart hawk worker"
    echo "      startd: start dispatch worker"
    echo "      stopd: stop dispatch worker"
    echo "      restartd: restart dispatch worker"
    echo "      startall: start all worker"
    echo "      restartall: restart all worker"
    echo "      stop all: stop all worker"
    echo "      flower: start flower server"
    echo "      web: start web server"
    echo "      status: use ps show status"    
    echo "      clearlog: clear all log"    
}

function startd {
    echo "start dispatch worker..."
    python3 dispatch.py start
}

function restartd {
    echo "restart dispatch worker..."
    python3 dispatch.py restart
}

function stopd {
    echo "stop dispatch worker..."
    python3 dispatch.py stop
}

action=$1
case $action in
    start) 
        startworker
        ;;
    stop) 
        stopworker
        ;;
    restart) 
        restartworker
        ;;
    flower) 
        startflower
        ;;
    web) 
        startweb
        ;;
    startd) 
        startd
        ;;
    restartd) 
        restartd
        ;;
    stopd) 
        stopd
        ;;
    status)
        python3 ./toolkit/status.py
        python3 ./toolkit/manage.py
        # service redis status
        ;;
    startall) 
        startworker
        startd
        startflower
        ;;
    stopall)
        stopd
        stopworker
        stopflower
        ;;
    reall)
        restartworker
        restartd
        stopflower
        startflower
        ;;
    clearlog)
        rm -f ./logs/*.log
        ;;
    dump)
        mysqldump -uroot -p hawk > /home/hawk/backup/$(date +'%Y_%m_%d').sql
        ;;
    *) 
        usage
        ;;
esac