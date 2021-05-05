# Open Bus Stride DB

Open Bus Stride database schema, migrations and related code

* [Alembic](https://alembic.sqlalchemy.org/) is used for migrations
* [SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/) is used for the ORM


## Local development


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


### Local Development

Start a Postgresql DB

```
docker run --name stride-db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -v `pwd`/.data/db:/var/lib/postgresql/data -d postgres:13
```

Set DB connection env var

```
export SQLALCHEMY_URL=postgresql://postgres:123456@localhost
```

Update DB to latest migration

```
alembic upgrade head
```

Start an interpreter and run some ORM code

```
python
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


### Tests

Follow all the steps for local development

Install test requirements

```
pip install -r tests/requirements.txt
```

Run tests

```
pytest
```


### Using the Docker image

The Docker image is used to run DB migrations

Build and run on the local DB:

```
docker build -t open_bus_stride_db . &&\
docker run --rm --network host -e SQLALCHEMY_URL open_bus_stride_db
```
