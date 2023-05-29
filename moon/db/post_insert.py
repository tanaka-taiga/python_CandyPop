from database import session
from post_table import Post

new_post = Post(title='Hello', content='Hello World!')
session.add(new_post)
session.commit()   
session.close()
