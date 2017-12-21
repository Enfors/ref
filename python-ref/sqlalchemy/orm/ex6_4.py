#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import DateTime

from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


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
                        
