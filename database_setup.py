from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
import pytz

Base = declarative_base()

# Creating Catalogs Table


class Catalog(Base):
    __tablename__ = "catalog"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }

# Creating Items Table


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now(
        tz=pytz.UTC).astimezone(pytz.timezone('Africa/Maputo')))
    description = Column(String, nullable=False)

    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date,
            'description': self.description,
        }


engine = create_engine('sqlite:///itemcatalogs.db')
Base.metadata.create_all(engine)
