#!/usr/bin/python3
"""
lists the first state from the database hbtn_0e_0_usa using ORM

Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        pool_pre_ping=True
        ))
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
