#!/usr/bin/env bash

cd `mktemp -d` &&\
pg_dump -d $DB -h $HOSTNAME -U $USER -n $SCHEMA --no-privileges -f ./stride_db.sql &&\
gzip ./stride_db.sql &&\
mv ./stride_db.sql.gz $FILENAME
