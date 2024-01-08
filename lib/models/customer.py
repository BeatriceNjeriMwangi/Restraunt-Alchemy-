from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .Base import Base, session
from models.review import Review


class Customer(Base):
    __tablename__ = 'customers'
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    reviews=relationship("Review", back_populates="customers", cascade = "all")

    def __repr__(self):
        return f"<Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>"
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    
    def get_reviews(self):
        return self.reviews
    def get_restaurants(self):
        return [review.restaurants.name for review in self.reviews]
    def favorite_restaurant(self):
        if not self.reviews:
            return  None
        else:
            return max (self.review(),key=lambda review: review.star_rating).restaurant()
    # def add_review(self, restaurant, rating):
    #     review = Review(star_rating=rating,restaurant_id=restaurant, customer_id=1)
    #     session.add(review)
    #     session.commit()
    def add_review(self, restaurant, rating):
        rev = Review(star_rating=rating,restaurant_id=restaurant, customer_id=self)
        self.reviews.append(rev)
        session.commit()
        return rev


    def delete_reviews(self, restaurant):
        session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).delete()
        session.commit()
        