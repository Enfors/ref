#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime,
                        ForeignKey, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from sqlalchemy import desc, func

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

# Getting objects from the database
cookies = session.query(Cookie).all()
for cookie in cookies:
    print(cookie)

# Instead of all(), you can also use first() to get just the first row.
# If you want to make sure there is only one match, use one() which raises
# an exception is there is not exactly one.
    
# We can also do it this way. Note that we don't use all() this time. This
# method is better for production code.
for cookie in session.query(Cookie):
    print(cookie.cookie_name)

# We can also just get the specific columns we want:
print("\n=== Getting specific columns")
print(session.query(Cookie.cookie_name, Cookie.quantity).first())

# Ordering
print("\n=== Ordering")
for cookie in session.query(Cookie).order_by(Cookie.quantity):
    print("{:3} - {}".format(cookie.quantity, cookie.cookie_name))

# Ordering in reverse
print("\n=== Ordering in reverse")
for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
    print("{:3} - {}".format(cookie.quantity, cookie.cookie_name))

# Using limit
print("\n=== Using limit")
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
print([result.cookie_name for result in query])

# Summing
print("\n=== Summing")
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
# Note: scalar() raises an exception if it doesn't get just one value.
print(inv_count)

# Counting rows
print("\n=== Counting rows")
rec_count = session.query(func.count(Cookie.cookie_name)).first()
print(rec_count)

# Using label to get better column labels
print("\n=== Using label")
rec_count = session.query(func.count(Cookie.cookie_name) \
                          .label("inventory_count")).first()
print(rec_count.keys())
print(rec_count.inventory_count)

# Filtering
print("\n=== Filtering")
record = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip")  \
                              .first()
print(record)

# Using where
print("\n=== Using where")
query = session.query(Cookie).filter(Cookie.cookie_name.like("%chocolate%"))
for record in query:
    print(record.cookie_name)

# Updating
print("\n=== Updating")
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "chocolate chip").first()
cc_cookie.quantity = cc_cookie.quantity + 120
session.commit()
print(cc_cookie.quantity)

# Updating data in place
print("\n=== Updating data in place")
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "chocolate chip")
query.update({Cookie.quantity: Cookie.quantity - 20})

cc_cookie = query.first()
print(cc_cookie.quantity)

# Deleting data
print("\n=== Deleting data")
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "dark chocolate chip")
dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()
dcc_cookie = query.first()
print(dcc_cookie)

# Deleting data in place
print("\n=== Deleting data in place without having an object")
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "molasses")
query.delete()
mol_cookie = query.first()
print(mol_cookie)

# Add more data
cookiemon = User(username="cookiemon",
                 email_address="mon@cookie.com",
                 phone="111-111-1111",
                 password="password")
cakeeater = User(username="cakeeater",
                 email_address="cakeeater@cake.com",
                 phone="222-222-2222",
                 password="password")
pieperson = User(username="pieperson",
                 email_address="person@pie.com",
                 phone="333-333-3333",
                 password="password")
for user in [cookiemon, cakeeater, pieperson]:
    session.add(user)
session.commit()

# Add related data
o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").one()
line1 = LineItem(cookie=cc, quantity=2, extended_cost=1.00)

pb = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").one()
line2 = LineItem(quantity=12, extended_cost=3.00)
line2.cookie = pb
line2.order = o1

o1.line_items.append(line1)
o1.line_items.append(line2)

session.commit()

o2 = Order()
o2.user = cakeeater

cc = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").one()
line1 = LineItem(cookie=cc, quantity=24, extended_cost=12.00)

oat = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").one()
line2 = LineItem(cookie=oat, quantity=24, extended_cost=6.00)

o2.line_items.append(line1)
o2.line_items.append(line2)

session.add(o2)
session.commit()

# Using join to select from multiple tables
print("\n=== Using join to select from multiple tables")
query = session.query(Order.order_id, User.username, User.phone,
                      Cookie.cookie_name, LineItem.quantity,
                      LineItem.extended_cost)
query = query.join(User).join(LineItem).join(Cookie)
for result in query.filter(User.username == "cookiemon").all():
    print(result)

# Using outerjoin to select from multiple tables
print("\n=== Using outerjoin to select from multiple tables")
# Show how many orders each user has
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
for row in query:
    print(row)

# Self-referencing tables
print("\n=== Self-referencing tables")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer(), primary_key=True)
    manager_id = Column(Integer(), ForeignKey("employees.id"))
    name = Column(String(255), nullable=False)

    manager = relationship("Employee", backref=backref("reports"),
                           remote_side=[id])

Base.metadata.create_all(engine)

# Boss
marsha = Employee(name="Marsha")

# Employee
fred = Employee(name="Fred")

marsha.reports.append(fred)

session.add(marsha)
session.commit()

print("Emplyees who report to Marsha:")
for report in marsha.reports:
    print("-", report.name)

# Grouping data
print("\n=== Grouping data")
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
print("How many orders each user has:")
for row in query:
    print(row)

# Chaining
print("\n=== Chaining")

def get_orders_by_customer(cust_name):
    query = session.query(Order.order_id, User.username, User.phone,
                          Cookie.cookie_name, LineItem.quantity,
                          LineItem.extended_cost)
    query = query.join(User).join(LineItem).join(Cookie)
    results = query.filter(User.username == cust_name).all()
    return results

print("Orders by customer cakeeater:")
for row in get_orders_by_customer("cakeeater"):
    print("-", row)

print("\n=== Conditional chaining")

def get_orders_by_customer2(cust_name, shipped=None, details=False):
    query = session.query(Order.order_id, User.username, User.phone)
    query = query.join(User)
    if details:
        query = query.add_columns(Cookie.cookie_name, LineItem.quantity,
                                  LineItem.extended_cost)
        query = query.join(LineItem).join(Cookie)

    if shipped is not None:
        query = query.filter(Order.shipped == shipped)

    results = query.filter(User.username == cust_name).all()
    return results

print(get_orders_by_customer2("cakeeater"))
print(get_orders_by_customer2("cakeeater", details=True))
print(get_orders_by_customer2("cakeeater", shipped=False))
print(get_orders_by_customer2("cakeeater", shipped=False, details=True))

