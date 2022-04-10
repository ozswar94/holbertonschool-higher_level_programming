#!/usr/bin/python3
"""
lists all state from the database hbtn_0e_0_usa contains 'a' using ORM

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

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        pool_pre_ping=True
        ))
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    s1 = State(name="Louisiana")
    session.add(s1)
    session.commit()

    print(s1.id)
    session.close()
