from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.comment import (
    CommentCreate,
    CommentResponse
)

from app.db.dependency import get_db

from app.services.comment import CommentService


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

    comment_service = CommentService(db)

    return comment_service.create_comment(
        comment,
        user_id,
        post_id
    )


@CommentRouter.get("/{comment_id}")
def get_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):

    comment_service = CommentService(db)

    return comment_service.get_comment(comment_id)

@CommentRouter.delete("/{comment_id}")
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):

    comment_service = CommentService(db)

    return comment_service.delete_comment(comment_id)