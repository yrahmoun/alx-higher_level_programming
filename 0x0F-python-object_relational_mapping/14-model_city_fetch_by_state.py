#!/usr/bin/python3
"""  prints all City objects from the database """

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    cities = session.query(City, State).join(State).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
