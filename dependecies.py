from models.db import SessionLocal


def get_db():
    """
    Method for obtaining a database session.
     :return: DB session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
