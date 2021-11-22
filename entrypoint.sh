#!/usr/bin/env bash

if [ "${DB_RESTORE_FILENAME}" != "" ]; then
  echo attempeting DB restore, checking if DB already contains data &&\
  if ! psql -h $HOSTNAME -U $USER -d $DB -qtc "select version_num from alembic_version;"; then
    echo restoring DB from backup file &&\
    cd `mktemp -d` &&\
    gzip -cd "${DB_RESTORE_FILENAME}.gz" > ./stride_db.sql &&\
    psql -h $HOSTNAME -U $USER -d $DB -f ./stride_db.sql
  else
    echo DB already restored, running migrations
    exec alembic upgrade head
  fi
else
  exec alembic upgrade head
fi
