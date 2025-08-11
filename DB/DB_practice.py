# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
#     def __repr__(self):
#         return f"<User(id={self.id}, username={self.username}, email={self.email})>)"
#
#
from sqlalchemy import create_engine, Boolean
from sqlalchemy.util.preloaded import engine_url

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Text

from Homeworks.HW2.exception_HW import divide

#
# engine = create_engine('sqlite:///european_database.sqlite')
# conn = engine.connect()
#
# metadate = MetaData()
# division = Table('divisions', metadate, autoload_with=engine)
#
# # print(repr(metadate.tables['divisions']))
# #
# # print(division.columns.keys())
# query = division.select()
# print(query)
#
# execution = conn.execute(query)
# # print(execution.fetchone())
# print(execution.fetchmany(5))
# # print(execution.fetchall())

engine = create_engine("sqlite:///datacamp.sqlite")

conn = engine.connect()
metadate = MetaData()

Student = Table("Student", metadate,
          Column('Id', Integer(), primary_key=True),
                Column('Name', String(255), nullable=False),
                Column('Major', String(255), default="Math"),
                Column('Pass', Boolean(), default=True)
                )

metadate.create_all(engine)
from sqlalchemy import insert
# query = insert(Student).values(Id=1, Name="Mattew", Major="Math", Pass= True)
# print(query)

# execution = conn.execute(query)
# conn.commit()

# query1 = Student.select()
# execution1 = conn.execute(query1) #чтобы достать элемент который добавил
# print(execution1.fetchone())

# values_list = [
#     {'Id':'2', 'Name':'Nisha', 'Major':"Science", 'Pass':False},
#     {'Id':'3', 'Name':'Natasha', 'Major':"Math", 'Pass':True},
#     {'Id':'4', 'Name':'Ben', 'Major':"English", 'Pass':False}
# ]
#
# query = insert(Student).values(values_list)
# print(query)
# execution = conn.execute(query)
# conn.commit()

# query = Student.select().where(Student.columns.Major == "English")
# print(query)
#
# execution = conn.execute(query)
# print(execution.fetchall())

# queryu = Student.select().where(Student.columns.Pass == True)
# print(queryu)
# print(conn.execute(queryu).fetchall())

from sqlalchemy import and_

# query = Student.select().where(and_(Student.columns.Major == "Math",
#                                     Student.columns.Pass == True))
#
# print(conn.execute(query).fetchall())
# from sqlalchemy import desc
# query = Student.select().order_by(desc(Student.columns.Name)) # сортировка, с desc сортировка в обратном порядке
# print(query)
# print(conn.execute(query).fetchall())
from sqlalchemy import func

# query = Student.select([func.count(Student.columns.Id), func.sum(Student.columns.Id)])
# print(query)

# query = Student.select().where(Student.columns.Major.in_(["English", "Math"]))
#
# result = conn.execute(query).fetchall()
# print(result)
#
# import pandas as pd
#
# data = pd.DataFrame(result)
# print(data)

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Text, Boolean

engine = create_engine("sqlite:///european_database.sqlite")
conn = engine.connect()

metadata = MetaData()
division = Table("divisions", metadata, autoload_with=engine)
matches = Table("matchs", metadata, autoload_with=engine)

# query = division.select()
# excution = conn.execute(query)
# print(excution.fetchmany(10))

query = matches.select().where(and_(matches.columns.Div == "E0",
                                    matches.columns.season == 2012))
execution = conn.execute(query)
# print(execution.fetchmany(10))

import pandas as pd
league_2012 = pd.DataFrame(execution.fetchall())
print(league_2012.head(5))