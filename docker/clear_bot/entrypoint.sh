#!/bin/bash

CRED_FILE=$1
WORK_DIR=$(dirname $CRED_FILE)
LOG_FILE=/var/log/clear_bot.log


# scripts uses session files, which must be in cred dir, so it is our working directiory
cd $WORK_DIR


check_user_authorization $CRED_FILE


touch $LOG_FILE
clear_bot $CRED_FILE &>> $LOG_FILE &
tail -f $LOG_FILE
