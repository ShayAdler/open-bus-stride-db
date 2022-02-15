#!/usr/bin/env bash

# usage:
#   run a single backup: /srv/entrypoint.sh
#   run backups on a schedule: /srv/entrypoint.sh --cron "min hour day month weekday"
# CRON_SCHEDULE: min hour day month weekday

if [ "${1}" == "--cron" ]; then
  mkdir -p /srv/crontab &&\
  echo "${2} /srv/entrypoint.sh --from-cron 2>&1" > /srv/crontab/root
  echo >> /srv/crontab/root
  exec crond -f -L /dev/stdout -c /srv/crontab
elif [ "${1}" == "--health-daemon" ]; then
  exec python3 /srv/health_daemon.py
else
  mkdir -p /srv/backup &&\
  cd /srv/backup &&\
  echo Running pg_dump from hostname $PG_BACKUP_HOSTNAME schema $PG_BACKUP_CRON_SCHEDULE db $PG_PG_BACKUP_DB to $PG_BACKUP_FILENAME &&\
  pg_dump -d $PG_BACKUP_DB -h $PG_BACKUP_HOSTNAME -U $PG_BACKUP_USER -n $PG_BACKUP_SCHEMA --no-privileges -f ./stride_db.sql &&\
  du -h ./stride_db.sql &&\
  gzip -kf ./stride_db.sql &&\
  du -h ./stride_db.sql.gz &&\
  cp -f ./stride_db.sql.gz "${PG_BACKUP_FILENAME}_temp" &&\
  du -h "${PG_BACKUP_FILENAME}_temp" &&\
  mv "${PG_BACKUP_FILENAME}_temp" "${PG_BACKUP_FILENAME}" &&\
  du -h "${PG_BACKUP_FILENAME}"
  if [ "$?" != "0" ]; then
    echo "Disappointing failure"
    if [ "${1}" == "--from-cron" ]; then
      echo terminating the crond process
      rm -rf /srv/crontab
    fi
    exit 1
  else
    echo "Great success"
    exit 0
  fi
fi
