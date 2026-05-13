from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.current_user import get_current_user

from app.schemas.post import (
    PostCreate,
    PostUpdate,
    PostResponse
)

from app.db.dependency import get_db
from app.services.post import PostService


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
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    post_service = PostService(db)

    return post_service.create_post(
        post,
        current_user.id
    )


@PostRouter.get("/{post_id}")
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    post_service = PostService(db)

    return post_service.get_post(post_id, current_user)

@PostRouter.put("/{post_id}")
def update_post(
    post_id: int,
    post_data: PostUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    post_service = PostService(db)

    return post_service.update_post(
        post_id,
        post_data,
        current_user
    )


@PostRouter.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)

):

    post_service = PostService(db)

    return post_service.delete_post(post_id , current_user)