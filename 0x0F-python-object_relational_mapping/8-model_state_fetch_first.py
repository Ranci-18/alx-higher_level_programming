#!/usr/bin/python3
"""script to list all states in hbtn_0e_6_usa using sqlalchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    first_state = sess.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    sess.close()
