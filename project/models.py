from sqlalchemy.orm import DeclarativeBase, Mapped

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

class Teacher(Base):
    __tablename__ = "teachers"
