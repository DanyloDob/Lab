from sqlalchemy import or_

from models import Session, User, Tickets

def list_of_users(email=None, first_name=None, last_name=None):
    session=Session()
    filters = []
    if email:
        filters.append(User.email.like(email))
    if first_name:
        filters.append(User.first_name.like(first_name))
    if last_name:
        filters.append(User.last_name.like(last_name))
    return session.query(User).filter(*filters).all()

def list_of_Tickets():
    session = Session()
    return session.query(Tickets).all()

def list_of_Users():
    session = Session()
    return session.query(User).all()

def create_entry(model_class, *, commit=True, **kwargs):
    session = Session()
    entry = model_class(**kwargs)
    session.add(entry)
    if commit:
        session.commit()
    return entry


def get_entry_by_idd(model_class, idd):
    session = Session()
    return session.query(model_class).filter_by(idd=idd).one()


def update_entry(entry, *, commit=True, **kwargs):
    session = Session()
    for key, value in kwargs.items():
        setattr(entry, key, value)
    if commit:
        session.commit()
    return entry


def delete_entry(model_class, idd, *, commit=True):
    session = Session()
    session.query(model_class).filter_by(idd=idd).delete()
    if commit:
        session.commit()