from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1111@localhost:5432/qwer")

Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    idd = Column("idd", Integer, primary_key=True)
    name = Column("name", String)
    email = Column("email", String)
    password = Column("password", String)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)


class Tickets(Base):
    __tablename__ = "ticketss"

    ticketid = Column("ticketid", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Integer)
    status = Column("status", Integer)
    owner_id = Column("owner_idd", Integer, ForeignKey(User.idd))
