#!/bin/bash -e

BASEDIR=`dirname $0`/..
VENV="$BASEDIR/env"

if [ ! -d "$VENV" ]; then
    echo "Create virtualenv ${VENV}."
    python3 -m venv $VENV
    echo "${VENV} virtualenv created."
else
    echo "Skipping virtualenv creation."
fi

source $VENV/bin/activate
echo `python3 --version`

pip3 install -U pip
echo `pip3 --version`

if [ ! -f "$VENV/updated" -o $BASEDIR/requirements.txt -nt $VENV/updated ]; then
    source $VENV/bin/activate
    pip3 install --upgrade setuptools pip
    pip3 install -r $BASEDIR/requirements.txt
    touch $VENV/updated
    echo "Requirements installed."
else
    echo "Skipping requirements install."
fi

echo `pip3 freeze`