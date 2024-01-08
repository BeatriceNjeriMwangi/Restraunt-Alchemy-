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

# customer = session.query(Customer).first()
# restaurant = session.query(Restaurant).first()

# add_newreview = customer.add_review(restaurant=restaurant,rating=5)
  

# session.add(add_newreview)
# # print (f"Added review for customer:{customer.full_name()}")
# for review in customer.reviews:
#             print (f"Review id:{review.id}, rating:{review.star_rating}")

restraunt_id =3
all_reviews= session.query(Restaurant).filter_by(id=restraunt_id).first()
if all_reviews:
    reviews = all_reviews.all_reviews()
    print(f"all reviews for {all_reviews.name}")
    for review in reviews:
        print (review)
fanciest = Restaurant.fanciest(session)
if fanciest :
    print(f"fanciest restaurant is: {fanciest.name}")

