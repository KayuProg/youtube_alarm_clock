#!/bin/bash
cd /home/kayu/Desktop/youtube_alarm_clock/
echo 0>a.txt
source .venv/bin/activate
export PYTHONPATH=$VIRTUAL_ENV/lib/python3.11/site-packages

#export PYTHONPATH=$PYTHONPATH:/home/kayu/.local/lib/python3.12/site-packages
#LOG_FILE="/home/kayu/Desktop/log.txt"
#python3 /home/kayu/Desktop/youtube_alarm_clock/main.py >> "$LOG_FILE" 2>&1

python3 /home/kayu/Desktop/youtube_alarm_clock/main.py

exit