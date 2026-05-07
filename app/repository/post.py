from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate , PostUpdate

def create_post(db : Session , post: PostCreate, user_id : int):

    new_post = Post(
        title = post.title,
        content = post.content,
        user_id = user_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return(new_post)

def update_post(db : Session, post_id : int, post_data : PostUpdate):

    post = db.query(Post).filter(Post.id == post_id).first()

    if not Post:
        return None
    
    post.title = post_data.title
    post.content = post_data.content

    db.commit()
    db.refresh(post)

    return post

def delete_post(db: Session, post_id: int):

    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        return None

    db.delete(post)
    db.commit()

    return post