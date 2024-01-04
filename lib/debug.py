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


list_review = session.query(Restaurant).first()
reviews = list_review.get_review()
print(reviews) 
    
# list_review = session.query(Restaurant).all()
# for review in list_review:
#     reviews=review.get_reviews()
#     print(reviews)

