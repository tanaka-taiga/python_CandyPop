from database import session
from post_table import Post

result = session.query(Post).filter_by(title="Hello World").delete()

print(result) # 1 = success, 0 = fail

session.commit()

session.close()
