from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

from .Base import Base, session
class Restaurant(Base):
    __tablename__="restaurants"
    id=Column(Integer, primary_key=True)
    name=Column(String)
    price=Column(Integer)
    reviews=relationship("Review", back_populates="restaurants")

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name={self.name}, price={self.price})>"

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return [review.customers.full_name() for review in self.reviews]
    
    @classmethod
    def fanciest(cls, session):
        
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [ review.full_review() for review in self.reviews]