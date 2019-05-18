#!/usr/bin/env python3

# import all modules needed for configuration
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# base instance inherit all features of SQLAlchemy
Base = declarative_base()


# add Admin class definition code for admin table
class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'picture': self.picture,
        }


# add class definition code and mapper for downloads table
class Downloads(Base):
    __tablename__ = 'downloads'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(250), nullable=False)
    file_path = Column(String(250), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship(Admin)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'file_name': self.file_name,
            'file_path': self.file_path,
            'id': self.id,
        }


# add class definition code and mapper for departments table
class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    dept_name = Column(String(250), nullable=False)
    srt_name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'dept_name': self.dept_name,
            'srt_name': self.srt_name,
        }


# add class definition code and mapper for facaulties table
class Facaulties(Base):
    __tablename__ = 'facaulties'

    id = Column(Integer, primary_key=True)
    fac_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    picture = Column(String(250))
    ac_rank = Column(String(250))
    edu = Column(String(250))
    dept_id = Column(Integer, ForeignKey('departments.id'))
    departments = relationship(Departments)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship(Admin)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'fac_name': self.fac_name,
            'picture': self.picture,
            'ac_rank': self.ac_rank,
            'email': self.email,
            'password': self.password,
            'edu': self.edu,
            'id': self.id,
        }


# add class definition code and mapper for students table
class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    st_name = Column(String(250), nullable=False)
    roll_no = Column(String(250), nullable=False)
    picture = Column(String(250))
    mob_no = Column(String(250), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship(Admin)
    dept_id = Column(Integer, ForeignKey('departments.id'))
    departments = relationship(Departments)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'st_name': self.st_name,
            'roll_no': self.roll_no,
            'picture': self.picture,
            'mob_no': self.mob_no,
            'id': self.id,
        }


# === to connect to an existing db or create a new one ===
engine = create_engine('sqlite:///collegedemo.db')

Base.metadata.create_all(engine)
