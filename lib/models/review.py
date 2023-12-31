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
    restaurants=relationship("Restaurant", back_populates="reviews")
    customers=relationship("Customer", back_populates="reviews")
    
    def __repr__(self):
        return f"<Review(id={self.id}, star_rating={self.star_rating}, restraunt_id={self.restaurant_id}, customer_id={self.customer_id})>"
    def get_customer(self):
        return self.customers
    
    def get_restaurant(self):
        return self.restaurants
    def full_review(self):
        return f"Review for {self.restaurants.name} by {self.customers.full_name()}: {self.star_rating} stars."
