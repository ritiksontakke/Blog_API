# app/routers/post.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.post import (
    PostCreate,
    PostUpdate,
    PostResponse
)

from app.db.dependency import get_db

from app.services.post import (
    create_post_service,
    get_post_service,
    get_all_posts_service,
    update_post_service,
    delete_post_service
)


PostRouter = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@PostRouter.post(
    "/create-post",
    response_model=PostResponse
)
def create_post(
    post: PostCreate,
    user_id: int,
    db: Session = Depends(get_db)
):

    return create_post_service(
        db,
        post,
        user_id
    )


@PostRouter.get("/{post_id}")
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):

    return get_post_service(db, post_id)


@PostRouter.get("/")
def get_all_posts(
    db: Session = Depends(get_db)
):

    return get_all_posts_service(db)


@PostRouter.put("/{post_id}")
def update_post(
    post_id: int,
    post_data: PostUpdate,
    db: Session = Depends(get_db)
):

    return update_post_service(
        db,
        post_id,
        post_data
    )


@PostRouter.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db)
):

    return delete_post_service(db, post_id)