#!/usr/bin/env bash

# usage:
#   run a single backup: /srv/entrypoint.sh
#   run backups on a schedule: /srv/entrypoint.sh --cron "min hour day month weekday"
# CRON_SCHEDULE: min hour day month weekday

if [ "${1}" == "--cron" ]; then
  mkdir -p /srv/crontab &&\
  echo "${2} /srv/entrypoint.sh" > /srv/crontab/root
  echo >> /srv/crontab/root
  exec crond -f -L /dev/stdout -c /srv/crontab
else
  cd `mktemp -d` &&\
  pg_dump -d $DB -h $HOSTNAME -U $USER -n $SCHEMA --no-privileges -f ./stride_db.sql &&\
  gzip ./stride_db.sql &&\
  mv ./stride_db.sql.gz $FILENAME
fi
