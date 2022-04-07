from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime as dt
import csv

engine = create_engine('sqlite:///dbms.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Integer)
    date_updated = Column(DateTime)

    def __repr__(self):
        attributes = '' + \
                     f'product_id="{self.product_id}", ' + \
                     f'product_name="{self.product_name}", ' + \
                     f'product_quantity={self.product_quantity}, ' + \
                     f'product_price={self.product_price}, ' + \
                     f'date_updated="{self.date_updated}"'
        return f'<Product({attributes})>'

    def save(self):
        session.add(self)
        session.commit()
        return f'{self.__repr__} saved!'


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class User(Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    openid = Column('openid', String(200))
    name = Column(String(200))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    def to_json(self):
        return dict(name=self.name, is_admin=self.is_admin)

    @property
    def is_admin(self):
        return self.openid in app.config['ADMINS']

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Category(Model):
    __tablename__ = 'categories'
    id = Column('category_id', Integer, primary_key=True)
    name = Column(String(50))
    slug = Column(String(50))

    def __init__(self, name):
        self.name = name
        self.slug = '-'.join(name.split()).lower()

    def to_json(self):
        return dict(name=self.name, slug=self.slug, count=self.count)

    @cached_property
    def count(self):
        return self.snippets.count()

    @property
    def url(self):
        return url_for('snippets.category', slug=self.slug)
