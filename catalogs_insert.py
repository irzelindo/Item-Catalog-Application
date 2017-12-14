from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Catalog, Item

engine = create_engine('sqlite:///itemcatalogs.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

catalogs = ['Soccer', 'Basketball', 'Baseball', 'Frisbee',
            'Snowboarding', 'Rock Climbing', 'Foosball', 'Skating', 'Hockey']

for catalog in catalogs:
    catalog_name = Catalog(name=catalog)
    session.add(catalog_name)
    session.commit()
