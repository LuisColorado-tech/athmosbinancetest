from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime


class Coin(BaseModel, Base):
    __tablename__ = 'coin'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    E = Column(DateTime)
    t = Column(String(50))
    T = Column(String(50))
    s = Column(String(50))
    i = Column(String(50))
    f = Column(String(50))
    L = Column(String(50))
    o = Column(String(50))
    c = Column(String(50))
    h = Column(String(50))
    l = Column(String(50))
    v = Column(String(50))
    n = Column(String(50))
    x = Column(String(50))
    q = Column(String(50))
    V = Column(String(50))
    Q = Column(String(50))
    B = Column(String(50))
