#!/usr/bin/python3
""" Lists all state objevts from database using sqlalchemy"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    usr = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

# dialect+driver://username:password@host:port/database
    c_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(usr, pswd, db_name)
    engine = create_engine(c_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).\
        filter(City.state_id == State.id).\
        order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
