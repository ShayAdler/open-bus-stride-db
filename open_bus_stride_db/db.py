import os
from typing import ContextManager
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine(os.environ.get('SQLALCHEMY_URL', 'postgresql://postgres:123456@localhost'),
                       future=True,
                       connect_args={"options": "-c timezone=utc"},
                       echo=bool(os.environ.get('SQLALCHEMY_ECHO')))
_sessionmaker = sessionmaker(bind=engine, future=True, autoflush=False, autocommit=False)


@contextmanager
def get_session(session=None) -> ContextManager[Session]:
    if session:
        # this supports a use-case for functions to work with or without an existing session
        yield session
    else:
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
