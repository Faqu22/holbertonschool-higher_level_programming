#!/usr/bin/python3
"""
    Write a script that prints the first \
        State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    row = session.query(State).first()
    if row is None:
        print("Nothing")
    print(f"{row.id}: {row.name}")
