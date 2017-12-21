#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


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


class SomeDataClass(Base):
    __tablename__ = "somedatatable"
    __table_args__ = (ForeignKeyConstraint(["id"], ["other_table.id"]),
                      CheckConstraint("unit_cost >= 0.00",
                                      name="unit_cost_positive"))
