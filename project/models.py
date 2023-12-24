from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey,Text

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(Text,nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(Text,nullable=False)



class Teacher(Base):
    __tablename__ = "teachers"
    id:Mapped[int] = mapped_column(primary_key=True)
    subject_id:Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    name:Mapped[str] = mapped_column(Text,nullable=False)


