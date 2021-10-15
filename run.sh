#!/bin/bash

cleanup () { 
    clear
    echo "[*] Application stopped."
    rm -rf venv/
    return 0
}

run () { 
    source venv/bin/activate && \
        clear && \
        echo "[*] Application running..." && \
        if [ $STAGE == "d" ]; then 
            python3 __main__.py "d" &
        else
            gunicorn3 -w 4 -b 127.0.0.1:5000 wsgi:app &
        fi
    return 0
}
install () {
        python3 -m venv venv && \
            source venv/bin/activate && \
            pip3 install -r requirements.txt
        return 0
}


DIRECTORY="venv"

if [ "$1" == "d" ]; then
    STAGE="d"
elif [ "$1" == "p" ]; then
    STAGE="p"
elif [ "$1" == "c" ]; then
    cleanup
else
    echo "Usage ./run.sh <stage>"
    exit
fi

if [ -d "$DIRECTORY" ]; then
    run
else
    install && run
fi
