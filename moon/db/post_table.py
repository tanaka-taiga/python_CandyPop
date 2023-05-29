import sys
from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from database import Base
from database import ENGINE
import datetime

# テーブル：postsの定義
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def __init__():
    print('postsのTableを定義')

# テーブルを作成
Base.metadata.create_all(bind=ENGINE)






