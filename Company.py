from sqlalchemy import Column, Integer, String, DateTime, REAL
from db_config import Base

'''
CREATE TABLE COMPANY(
 ID INT PRIMARY KEY NOT NULL [auto-increment],
 NAME String (50) NOT NULL unique,
 AGE INT NOT NULL [default = 0],
 ADDRESS String(50) not null,
 SALARY REAL
);
'''
class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    age = Column(Integer(), nullable=False, default=0)
    address = Column(String(50), nullable=False)
    salary = Column(REAL())

    def __repr__(self):
        return f'\n<Company id={self.id} name={self.name} age={self.age} address={self.address} salary={self.salary}>'

    def __str__(self):
        return f'\n<Company id={self.id} name={self.name} age={self.age} address={self.address} salary={self.salary}>'