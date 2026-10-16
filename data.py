from sqlmodel import *
import os
from schemas import Element


engine = create_engine('sqlite:///elements.db')
SQLModel.metadata.create_all(engine)


def add_to_db(skin_folder: str, element: str, ) -> None:
  """
  path_list: a list of osu skin paths 

  Meant to scrape a list of skin paths
  """
  path_list: list[str] = os.listdir(skin_folder)

  with Session(engine) as session:
    element_list:list[Element] = []
    for path in path_list:
      element_list.append(Element(root_path= skin_folder+path+element))
    session.add_all(element_list)
    session.commit()

def search_element(table: object) -> Sequence:
  with Session(engine) as session:

    res = session.exec(select(table))
    return res.all()

print(search_element())




