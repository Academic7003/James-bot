from sqlalchemy import (Column, Integer, String, Sequence)
from sqlalchemy import sql
from utils.db_api.database import db


class TruthOrDare(db.Model):
    
    __tablename__ = 'truthordare'


    id = Column(Integer, primary_key=True)
    category = Column(String(20))
    text =  Column(String(20))
    query: sql.Select

    
    def __repr__(self):
        return f'{self.text}--{self.category}'
