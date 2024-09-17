from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///test.db")
sessionmaker_obj = sessionmaker(bind=engine)


def get_session():
    while True:
        try:
            session = sessionmaker_obj()
            print("opened")
            yield session
        finally:
            print("closed")
            session.close()

session_generator = get_session()