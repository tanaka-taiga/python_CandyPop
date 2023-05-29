from database import session
from post_table import Post

update_post = session.query(Post).filter_by(title="Hello").first()

update_post.title = "Hello World"

session.add(update_post)

session.commit()

session.close()
