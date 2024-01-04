# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# import sqlalchemy.orm
# from sqlalchemy.orm import relationship
# from models.customer import Customer
# from models.restaurant import Restaurant
# from models.review import Review
# from models.Base import Base
# from faker import Faker



# engine = create_engine("sqlite:///Restaurant.db") 

# Base.metadata.create_all(bind=engine)
# Session= sessionmaker(bind=engine)
# session = Session()

# session.query(Customer).delete()
# session.query(Review).delete()
# session.query(Restaurant).delete()


# # customer1 = Customer(first_name="Beatrice", last_name="Njeri")
# # customer2 = Customer(first_name="John", last_name=" Ndungu")
# # customer3 = Customer(first_name="Ian", last_name="Njuguna")
# # customer4 = Customer(first_name="Susan", last_name="Njoki")
# # customer5 = Customer(first_name="Ellie", last_name="Kimani")
# # customer6 = Customer(first_name="Joy", last_name="Wanjiku")





# # restaurant1 = Restaurant(name="Cafe", price=50)
# # restaurant2 = Restaurant(name="Deli", price=100)
# # restaurant3 = Restaurant(name="pork", price=150)
# # restaurant4 = Restaurant(name="Haza", price=200)
# # restaurant5 = Restaurant(name="posty", price=250)
# # restaurant6 = Restaurant(name="heri", price=500)



# # review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
# # review2 = Review(restaurant=restaurant2, customer=customer3, star_rating=4)
# # review3 = Review(restaurant=restaurant3, customer=customer2, star_rating=4)
# # review4 = Review(restaurant=restaurant4, customer=customer4, star_rating=2)
# # review5 = Review(restaurant=restaurant1, customer=customer4, star_rating=5)
# # review6 = Review(restaurant=restaurant5, customer=customer6, star_rating=3)
# # review7 = Review(restaurant=restaurant5, customer=customer5, star_rating=1)
# # review8 = Review(restaurant=restaurant6, customer=customer2, star_rating=3)






# # adding objects to session
# session.add(restaurant1)
# session.add(restaurant2)
# session.add(restaurant3)
# session.add(restaurant4)
# session.add(restaurant5)
# session.add(restaurant6)



# session.add(customer1)
# session.add(customer2)
# session.add(customer3)
# session.add(customer4)
# session.add(customer5)
# session.add(customer6)

# session.add(review1)

# # commit session
# session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from models import Restaurant, Customer, Review, Base
from faker import Faker
from models.restaurant import Restaurant
from models.customer import Customer
from models.review import Review
from models.Base import Base


# Replace 'your_database_url' with the actual URL of your database.
engine = create_engine('sqlite:///Restaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(Customer).delete()
session.query(Review).delete()
session.query(Restaurant).delete()

fake = Faker()

def seed_data():
    # Create Restaurants
    restaurants = []
    for _ in range(5):
        restaurant = Restaurant(name=fake.company(), price=fake.random_int(1, 5))
        restaurants.append(restaurant)
        session.add(restaurant)

    # Create Customers
    customers = []
    for _ in range(10):
        customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())
        customers.append(customer)
        session.add(customer)

    session.commit()

    # Create Reviews
    for _ in range(30):
        review = Review(
            star_rating=fake.random_int(1, 5),
            restaurants=fake.random_element(restaurants),
            customers=fake.random_element(customers)
        )
        session.add(review)

    session.commit()

if __name__ == '__main__':
    seed_data()
print("done")