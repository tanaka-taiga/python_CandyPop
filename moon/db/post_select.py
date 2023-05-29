from database import session
from post_table import Post

posts = session.query(Post).all()

for i in posts:
    print(f"ID : {i.id}, Title : {i.title}, Content : {i.content}, Date : {i.created_at}")
    
session.close()
