#!/usr/bin/env bash

if [ "${DB_RESTORE_FILENAME}" != "" ]; then
  echo attempting DB restore from file, checking if DB already contains data &&\
  if ! psql -h $HOSTNAME -U $USER -d $DB -qtc "select 1;"; then
    echo DB is not ready
    exit 1
  elif ! psql -h $HOSTNAME -U $USER -d $DB -qtc "select version_num from alembic_version;"; then
    echo restoring DB from backup file &&\
    cd `mktemp -d` &&\
    gzip -cd "${DB_RESTORE_FILENAME}.gz" > ./stride_db.sql &&\
    psql -h $HOSTNAME -U $USER -d $DB -f ./stride_db.sql
  else
    echo DB already restored, running migrations
    exec alembic upgrade head
  fi
elif [ "${DB_RESTORE_FROM_URL}" == "yes" ]; then
  echo attempting DB restore from URL, checking if DB already contains data &&\
  if ! psql -h $HOSTNAME -U $USER -d $DB -qtc "select 1;"; then
    echo DB is not ready
    exit 1
  elif ! psql -h $HOSTNAME -U $USER -d $DB -qtc "select version_num from alembic_version;"; then
    echo restoring DB from URL &&\
    cd `mktemp -d` &&\
    curl https://open-bus-siri-requester.hasadna.org.il/stride_db_backup/stride_db.sql.gz \
      -o stride_db.sql.gz &&\
    gzip -cd stride_db.sql.gz > stride_db.sql &&\
    psql -h $HOSTNAME -U $USER -d $DB -f stride_db.sql
  else
    echo DB already restored, running migrations
    exec alembic upgrade head
  fi
else
  exec alembic upgrade head
fi
