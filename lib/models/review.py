from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from .Base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id=Column(Integer, primary_key=True)
    star_rating=Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant=relationship("Restaurant", back_populates="reviews")
    customer=relationship("Customer", back_populates="reviews")
    
    def __repr__(self):
        return f"<Review(id={self.id}, star_rating={self.star_rating}, restraunt_id={self.restaurant_id}, customer_id={self.customer_id})>"
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    