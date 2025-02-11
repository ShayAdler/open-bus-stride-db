# Open Bus Stride DB

Open Bus Stride database schema, migrations and related code

* [Alembic](https://alembic.sqlalchemy.org/) is used for migrations
* [SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/) is used for the ORM

See [our contributing docs](https://github.com/hasadna/open-bus-pipelines/blob/main/CONTRIBUTING.md) if you want to suggest changes to this repository.

## Development using the Docker Compose environment

This is the easiest option to start development, follow these instructions: https://github.com/hasadna/open-bus-pipelines/blob/main/README.md#stride-db

For local development, see the additional functionality section: `Develop stride-db migrations from a local clone of stride-db`

## Development using local Python interpreter

It's much easier to use the Docker Compose environment, but the following can be
refferd to for more details regarding the internal processes and for development
using your local Python interpreter. 

### Install

Create virtualenv (Python 3.8)

```
python3.8 -m venv venv
```

Install dependencies

```
venv/bin/python -m pip install -r requirements.txt
```

Install the Python module

```
venv/bin/python -m pip install -e .
```

Create a `.env` file with the following contents (don't change anything, it's only a local DB)

```
. venv/bin/activate
export SQLALCHEMY_URL=postgresql://postgres:123456@localhost
```

### Use

Start a Postgresql DB by running the following from `constru.pipelines` repository:

```
docker-compose up -d stride-db
```

### Update DB to latest migration

```
. .env && alembic upgrade head
```

### Make changes to the DB model

* Make code changes in open_bus_stride_db.model
* Create an alembic autogenerated revision: `. .env && alembic revision --autogenerate -m "describe the change here"`
* Update DB to latest migration

### Run ORM code

```
. .env && python
>>> from open_bus_stride_db.db import Session
>>> from open_bus_stride_db.model import Route
>>> session = Session()
>>> session.query(Route).all()
[]
>>> session.add(Route())
>>> session.query(Route).all()
[<open_bus_stride_db.model.route.Route object at 0x7f690b889a00>]
>>> session.commit()
```

See [Alembic](https://alembic.sqlalchemy.org/) and [SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/) docs for more details


### Using the Docker image

The Docker image is used to initialize the DB

Run DB migrations:

```
docker build -t open_bus_stride_db . &&\
docker run --rm --network host -e SQLALCHEMY_URL open_bus_stride_db
```

Restore DB from local production backup (Make sure DB is empty beforehand):

```
docker build -t open_bus_stride_db . &&\
docker run --rm --network host \
    -e PGPASSWORD=123456 \
    -e HOSTNAME=localhost \
    -e USER=postgres \
    -e DB=postgres \
    -e DB_RESTORE_FILENAME=/mnt/stride_db.sql \
    -v `pwd`/.data/backup:/mnt \
    open_bus_stride_db
```

Restore DB from remote production backup (Make sure DB is empty beforehand):

```
docker build -t open_bus_stride_db . &&\
docker run --rm --network host \
    -e PGPASSWORD=123456 \
    -e HOSTNAME=localhost \
    -e USER=postgres \
    -e DB=postgres \
    -e DB_RESTORE_FROM_URL=yes \
    -v `pwd`/.data/backup:/mnt \
    open_bus_stride_db
```

### Using the backup Docker image

The backup Docker image is used to create a DB backup which provides developers with a 
copy of the DB for local developmnet.

Build the DB backup image and create a local backup:

```
docker build -t open_bus_stride_db_backup backup &&\
docker run \
    -e PGPASSWORD=123456 \
    -e HOSTNAME=localhost \
    -e USER=postgres \
    -e DB=postgres \
    -e SCHEMA=public \
    -e FILENAME=/mnt/stride_db.sql.gz \
    -v `pwd`/.data/backup:/mnt \
    --network host \
    open_bus_stride_db_backup
```

Backup file is available at .data/backup/stride_db.sql.gz

## Generating documenation

Install dependencies

```
pip install -r requirements-docgen.txt
sudo apt install graphviz
```

Generate docs

```
python bin/docgen.py .
```

Created files:

* `dbschema.png`
* `DATA_MODEL.md`
