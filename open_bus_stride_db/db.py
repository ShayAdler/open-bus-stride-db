import os
from typing import ContextManager
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine(os.environ.get('SQLALCHEMY_URL', 'postgresql://postgres:123456@localhost'), future=True)
_sessionmaker = sessionmaker(bind=engine, future=True)


@contextmanager
def get_session() -> ContextManager[Session]:
    session: Session = _sessionmaker()
    try:
        yield session
    finally:
        session.close()


def session_decorator(func):

    def _func(*args, **kwargs):
        with get_session() as session:
            return func(session, *args, **kwargs)

    return _func
