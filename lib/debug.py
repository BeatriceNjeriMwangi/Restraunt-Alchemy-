from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.restaurant import Restaurant
from models.review import Review
from models.customer import Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///Restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()


# printing session
# all_customers = session.query(Customer).all()
# for customer in all_customers:
#     print(f"{customer.full_name()}")
 
for list_customers in session.query(Review).all():
    customers = list_customers.get_customer()
    print(f"{customers.first_name} {customers.last_name}")

for list_restraunts in session.query(Review).all():
    restraunts = list_restraunts.get_restaurant()
    print(restraunts.name)

list_rest = session.query(Restaurant).first()
all_reviews= list_rest.get_reviews()

for review in all_reviews:
    print(f"{review.star_rating} {list_rest.name}")


all_customers = session.query(Restaurant).first()
customers = all_customers.get_customers()
print(customers)

list_customers = session.query(Customer).first()
list_reviews = list_customers.get_reviews()

for review in list_reviews:
    print(f"{review.star_rating} {list_customers.full_name()}")

collection =session.query(Customer).first()
restaurants =collection.get_restaurants()
print(restaurants)

add_reviews= Customer.add_review(Customer,5,4)

full_reviews= Review.full_review()