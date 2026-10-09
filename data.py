from sqlmodel import *
import os


engine = create_engine('sqlite:///elements.db')


class Element(SQLModel, table=True):
  path:str = Field(max_length=100, primary_key=True)
  
SQLModel.metadata.create_all(engine)


def add_to_db(path_list:list[str]) -> None:

  with Session(engine) as session:
    element_list: list[Element] = []

    for path in path_list:
      element_list.append(Element(path=path))

    session.add_all(element_list)
    session.commit()

def search_element(param: str) -> Sequence:
  with Session(engine) as session:
    statment = select(Element)
    res = session.exec(statment)

    return res.fetchall()
      




