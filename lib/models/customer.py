from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .Base import Base


class Customer(Base):
    __tablename__ = 'customers'
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    reviews=relationship("Review", back_populates="customer", cascade = "all")

    def __repr__(self):
        return f"<Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>"
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    
    def get_reviews(self):
        return self.reviews
    def get_restaurants(self):
        return [review.restaurant for review in self.review]