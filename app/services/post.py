from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.post import PostCreate, PostUpdate
from app.repository.post import (
    create_post,
    update_post,
    delete_post,
    get_all_posts,
    get_post

)


def create_post_service(
    db: Session,
    post: PostCreate,
    user_id: int
):

    return create_post(db, post, user_id)


def get_post_service(db: Session, post_id: int):

     post = get_post(db, post_id)

     if not post:
         raise HTTPException(
             status_code=404,
             detail="Post not found"
         )

     return post


def get_all_posts_service(db: Session):

     return get_all_posts(db)


def update_post_service(
     db: Session,
     post_id: int,
     post_data: PostUpdate
 ):

    post = update_post(db, post_id, post_data)

    if not post:
        raise HTTPException(
             status_code=404,
             detail="Post not found"
        )

    return post


def delete_post_service(db: Session, post_id: int):

    post = delete_post(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return {
        "message": "Post deleted successfully"
    }
