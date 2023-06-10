from sqlalchemy import Column, Integer, String
from models.database import Base

class ConvContent(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(8), nullable=False)
    text = Column(String(128), nullable=False)

    def __init__(self, name=None, text=None):
        self.name = name
        self.text = text
        
    def __repr__(self):
        return '<Text %r>' % (self.text)