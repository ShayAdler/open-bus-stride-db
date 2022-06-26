# Pulled April 26, 2021
FROM --platform=linux/amd64 python:3.8@sha256:ff2d0720243a476aae42e4594527661b3647c98cbf5c1735e2bb0311374521f4
RUN pip install --upgrade pip
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&\
    echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list &&\
    apt-get update && apt-get install -y postgresql-client-13
WORKDIR /srv
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY setup.py ./
COPY open_bus_stride_db ./open_bus_stride_db
COPY alembic ./alembic
COPY alembic.ini ./
RUN pip install -e .
ENV PYTHONUNBUFFERED=1
COPY entrypoint.sh ./
ENTRYPOINT ["/srv/entrypoint.sh"]
