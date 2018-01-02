#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from datetime import datetime

engine = create_engine("sqlite:///:memory:", echo=False)

Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now())

    def __str__(self):
        output = "User: name: %s" % self.name

        for data_item in self.user_data:
            output += "\n- " + str(data_item)

        return output


class UserData(Base):
    __tablename__ = "userdata"

    data_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"))
    data_key = Column(String(64), nullable=False)
    data_val = Column(String(256))

    user = relationship("User", backref=backref("user_data",
                                                order_by=data_id))

    def __str__(self):
        return "UserData: User: %s, key='%s', val='%s'" % (self.user.name, self.data_key,
                                                       self.data_val)

    
if __name__ == '__main__':
    enfors = User(name="Enfors")
    data = UserData(user=enfors,
                    data_key="bukai",
                    data_val="shodan")
    print(enfors)

    
