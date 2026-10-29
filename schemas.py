from sqlmodel import *


class Element(SQLModel, table=True):
    skin_origin: str = Field(max_length=100)
    element_id: str = Field(primary_key=True)
    element: bytes

class Cursor(Element, table=true):
    __tablename__ = "Cursors"



