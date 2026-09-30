from sqlmodel import *
import os

engine = create_engine('sqlite:///elements.db')


class Element(SQLModel, table=True):
  path:str  = Field(max_length=100, primary_key=True)
  

  

SQLModel.metadata.create_all(engine)

def add_to_db(path_:str):

  with Session(engine) as session:
    element1 = Element(path=path_)

    session.add(element1)
    session.commit()

    statement = select(Element).where(Element.path==path_)
    res = session.exec(statement)
    # print(res.all())

def search_element(param: str):
  with Session(engine) as session:
    statment = select(Element)
    res = session.exec(statment)

    for i in res.fetchall():
      print(i.path+'\\'+param)


search_element('cursor.png')


