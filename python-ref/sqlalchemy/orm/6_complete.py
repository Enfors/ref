#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import DateTime

from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine

Base = declarative_base()


class Cookie(Base):
    __tablename__ = "cookies"

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))  # 12 numbers (I think?), two decimal places


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
    

class LineItem(Base):
    __tablename__ = "line_item"

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("users.user_id"))
    cookie_id = Column(Integer(), ForeignKey("cookies.cookie_id"))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    # One-to-many relationship:
    order = relationship("Order", backref=backref("line_items",
                                                  order_by=line_item_id))

    # One-to-one relationship:
    cookie = relationship("Cookie", uselist=False)
                        

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
