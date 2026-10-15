from sqlmodel import *


class Element(SQLModel, table=True):
  root_path:str = Field(max_length=100, primary_key=True)


