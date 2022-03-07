#!/usr/bin/python3
""" Lists all state objevts from database using sqlalchemy"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

# dialect+driver://username:password@host:port/database
    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.
    format(username, password, database_name)
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
