# Pulled April 26, 2021
FROM python:3.8@sha256:ff2d0720243a476aae42e4594527661b3647c98cbf5c1735e2bb0311374521f4
RUN pip install --upgrade pip
WORKDIR /srv
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY setup.py ./
COPY open_bus_stride_db ./open_bus_stride_db
COPY alembic ./alembic
COPY alembic.ini ./
RUN pip install -e .
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["alembic", "upgrade", "head"]
