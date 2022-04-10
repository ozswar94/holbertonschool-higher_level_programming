#!/usr/bin/python3
"""
Update table states from the database hbtn_0e_0_usa using ORM

Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
    name of state sys.argv[4]
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sqlalchemy import delete

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        pool_pre_ping=True
        ))
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    s1 = session.query(State).filter(State.name.like("%a%"))
    s1.delete(synchronize_session=False)
    session.commit()
    session.close()
