from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="radioactive", email="radioactive@gmail.com")
session.add(User1)
session.commit()

category1 = Categories(user_id=1, name="Science Fiction")
session.add(category1)
session.commit()

category2 = Categories(user_id=1, name="Satire")
session.add(category2)
session.commit()

category3 = Categories(user_id=1, name="Drama")
session.add(category3)
session.commit()

category4 = Categories(user_id=1, name="Action and Adventure")
session.add(category4)
session.commit()

category5 = Categories(user_id=1, name="Romance")
session.add(category5)
session.commit()

category6 = Categories(user_id=1, name="Poetry")
session.add(category6)
session.commit()

category7 = Categories(user_id=1, name="Encyclopedia")
session.add(category7)
session.commit()

category8 = Categories(user_id=1, name="Comics")
session.add(category8)
session.commit()

category9 = Categories(user_id=1, name="Series")
session.add(category9)
session.commit()

category10 = Categories(user_id=1, name="Autobiographies")
session.add(category10)
session.commit()

category11 = Categories(user_id=1, name="Cookbooks")
session.add(category11)
session.commit()

# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="Maus",
                             description="Maus is a graphic novel by American\
                             cartoonist Art Spiegelman, serialized from 1980\
                             to 1991. It depicts Spiegelman interviewing his\
                             father about his experiences as a Polish Jew and\
                             Holocaust survivor.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Encyclopedia Britannica",
                             description="The Encyclopedia Britannica,\
                             formerly published by Encyclopedia Britannica, In\
                             c., is a general knowledge English-language\
                             encyclopaedia. It was written by about 100 fu\
                             ll-time editors and more than 4000\
                             contributors.", categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="A Song of Ice and Fire",
                             description="A Song of Ice and Fire is a series of\
                             epic fantasy novels by the American novelist and\
                             screenwriter George R. R. Martin. He began the\
                             first volume of the series, A Game of Thrones,\
                             in 1991, and it was published in 1996.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Macbeth",
                             description="Macbeth is a tragedy by William\
                             Shakespeare it is thought to have been first\
                             performed in 1606. It dramatises the damaging\
                             physical and psychological effects of political\
                             ambition on those who seek power for its own\
                             sake.", categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Scooby-Doo Team-Up",
                             description="The Dynamic Duo Batman and Robin team\
                             up with Scooby-Doo and his mystery busting\
                             friends the Mystery Inc.!", categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Fahrenheit 451",
                             description="Fahrenheit 451 is a dystopian novel\
                             by American writer Ray Bradbury, first published\
                             in 1953. It is regarded as one of his best works.\
                             The novel presents a future American society\
                             where books are outlawed and firemen burn any\
                             that are found", categories=category1)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Run Fast Eat Slow",
                             description="New York Times bestseller Run Fast.\
                             Eat Slow. taught runners of all ages that healthy\
                             food could be both indulgent and incredibly\
                             nourishing.", categories=category11)
session.add(categoryItem1)
session.commit()
print "added category items!"
