#!/usr/bin/python3
"""script to list all states with the
letter 'a' in hbtn_0e_6_usa using sqlalchemy"""
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
    for state in sess.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    sess.close()
