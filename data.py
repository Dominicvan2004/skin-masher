from sqlmodel import Session
from sqlalchemy import Engine
from os import listdir
from schemas import *
from pathlib import Path
from classes import Image


#scrape files then add then to db 

class db_connection():
  def __init__(self, engine: Engine, skin_folder_path: str):
      """    
        Args:
          engine: SQLAlchemy engine to establish a connection with the db
          skin_folder_path: Path to your OSU! skin folder
        """
      self.engine = engine
      self.skin_folder_path = skin_folder_path


  def scrape_add_element(self, table: Element, element: str):
    """    
    Args:
      table: The SQLmodel table you want to add to
      element: The element you want to add
    """
      
    with Session(self.engine) as session: 
      list_of_entries: list[Element] = []
      for skin in listdir(self.skin_folder_path):

        skin_path = self.skin_folder_path + "\\" + skin
        element_in_bytes = Path(skin+"element")

        inst = Cursor(
          skin_origin=skin,
          element_id= skin_path,
          element= element_in_bytes.read_bytes()
        )

        list_of_entries.append(inst)

      session.add_all(list_of_entries)
      session.commit()

  def get_element_img_list(self) -> list[Image]:

    with Session(self.engine) as session:
      statement = select(Cursor)
      return [Image(i.element,i.skin_origin) for i in list(session.exec(statement).all())]
  
