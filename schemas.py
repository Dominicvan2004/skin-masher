from sqlmodel import *


class Element(SQLModel, table=True):
  root_path:str = Field(max_length=100, primary_key=True)

class FolderPath(SQLModel, table=True):
  folder_path: str  = Field(max_length=100, primary_key=true)



