from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))


if __name__ == "__main__":
    engine = create_engine('sqlite:///orm.sqlite')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)

    d = Department(name="IT")
    emp1 = Employee(name="John", department=d)
    s = session()
    s.add(d)
    s.add(emp1)
    s.commit()
    s.delete(d)
    s.commit()

    d = Department(name="Accounting")
    emp2 = Employee(name="Fred", department=d)
    s = session()
    s.add(d)
    s.add(emp2)
    s.commit()

    with open('/home/andy/data/drivers_s.csv', 'r') as f:
        contents = f.readlines()
        for line in contents:
            row = line.split(',')
            print(row)
            # add employee by pulling from row[n]
