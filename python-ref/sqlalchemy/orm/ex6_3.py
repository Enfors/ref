#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import DateTime

from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

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
