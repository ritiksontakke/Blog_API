# app/routers/comment.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.comment import (
    CommentCreate,
    CommentResponse
)

from app.db.dependency import get_db

from app.services.comment import (
    create_comment_service,
    get_comment_service,
    get_all_comments_service,
    delete_comment_service
)


CommentRouter = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@CommentRouter.post(
    "/create-comment",
    response_model=CommentResponse
)
def create_comment(
    comment: CommentCreate,
    user_id: int,
    post_id: int,
    db: Session = Depends(get_db)
):

    return create_comment_service(
        db,
        comment,
        user_id,
        post_id
    )


@CommentRouter.get("/{comment_id}")
def get_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):

    return get_comment_service(db, comment_id)


@CommentRouter.get("/")
def get_all_comments(
    db: Session = Depends(get_db)
):

    return get_all_comments_service(db)


@CommentRouter.delete("/{comment_id}")
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):

    return delete_comment_service(
        db,
        comment_id
    )