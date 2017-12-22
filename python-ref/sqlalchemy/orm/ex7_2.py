#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime,
                        ForeignKey, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from datetime import datetime

engine = create_engine("sqlite:///:memory:", echo=False)

# This line should only be used ONCE in an application's global scope
# and thereafter be treated like a configuration setting.
Session = sessionmaker(bind=engine)

# Then, make a session from this Session. Presumably, this can be done
# many times in different parts (threads?) of an application.
session = Session()

Base = declarative_base()

class Cookie(Base):
    __tablename__ = "cookies"

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))  # 12 numbers (I think?), two decimal places

    # Not required - only for demonstration.
    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
            "cookie_recipe_url='{self.cookie_recipe_url}', " \
            "cookie_sku='{self.cookie_sku}', " \
            "quantity={self.quantity}, " \
            "unit_cost={self.unit_cost})".format(self=self)


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)  # Set it to auto-update

    # Not required - only for demonstration.
    def __repr__(self):
        return "User(username='{self.username}', " \
            "email_address='{self.email_address}', " \
            "phone='{self.phone}', " \
            "password='{self.password}')".format(self.self)
    

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"))
    shipped = Column(Boolean(), default=False)

    # Establish a one-to-many relationship. This also establishes an
    # "orders" property the User class via the backref keyword argument,
    # which is ordered by order_id
    user = relationship("User", backref=backref("orders",
                                                order_by=order_id))

    # Not required - only for demonstration.
    def __repr__(self):
        return "Order(user_id={self.user_id}, " \
            "shipped={self.shipped})".format(self=self)


class LineItem(Base):
    __tablename__ = "line_item"

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("orders.order_id"))
    cookie_id = Column(Integer(), ForeignKey("cookies.cookie_id"))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    # One-to-many relationship:
    order = relationship("Order", backref=backref("line_items",
                                                  order_by=line_item_id))

    # One-to-one relationship:
    cookie = relationship("Cookie", uselist=False, order_by=cookie_id)

    # Not required - only for demonstration.
    def __repr__(self):
        return "LineItems(order_id={self.order_id}, " \
            "cookie_id={self.cookie_id}, " \
            "quantity={self.quantity}, " \
            "extended_cost={self.extended_cost})".format(self=self)
                        

Base.metadata.create_all(engine)

## Inserting data

# Inserting a single object
cc_cookie = Cookie(cookie_name="chocolate chip",
                   cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
                   cookie_sku="CC01",
                   quantity=12,
                   unit_cost=0.50)
session.add(cc_cookie)
# session.commit() also sets the Cookie.cookie_id in the object, which
# was created in the database.
session.commit()

print(cc_cookie.cookie_id)

# Inserting many objects

dcc = Cookie(cookie_name="dark chocolate chip",
             cookie_recipe_url="http://some.asweso.me/cookie/recipe_dark.html",
             cookie_sku="CC02",
             quantity=1,
             unit_cost=0.75)

mol = Cookie(cookie_name="molasses",
             cookie_recipe_url="http://some.aweso.me/cookie/recipe_mol.html",
             cookie_sku="MOL01",
             quantity=1,
             unit_cost=0.80)
session.add(dcc)
session.add(mol)

# Flush is like commit, but it doesn't perform an actual database commit.
# Because of this, dcc and mol are still connected to the session and can
# be used to perform additional database tasks without triggering
# additional database queries.
session.flush()

print(dcc.cookie_id)
print(mol.cookie_id)
