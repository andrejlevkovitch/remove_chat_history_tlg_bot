#!/bin/bash

CRED_FILE=$1
CHAT_NAME=$2
WORK_DIR=$(dirname $CRED_FILE)
LOG_FILE=/var/log/clear_bot.log

echo "chat for clearing: $CHAT_NAME"


# scripts uses session files, which must be in cred dir, so it is our working directiory
cd $WORK_DIR


check_user_authorization $CRED_FILE


# need for using variables in cron
printenv | sed 's/^\(.*\)$$/export \1/g' > /root/project_env.sh



touch $LOG_FILE
cron
crontab /etc/cron.d/periodic_chat_clear
tail -f $LOG_FILE
