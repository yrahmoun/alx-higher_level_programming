#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
that contain the letter a """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
