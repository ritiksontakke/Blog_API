# services/comment.py

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.comment import CommentCreate
from app.repository.comment import (
    create_comment,
    get_comment,
    get_all_comments,
    delete_comment
)


def create_comment_service(
    db: Session,
    comment: CommentCreate,
    user_id: int,
    post_id: int
):

    return create_comment(
        db,
        comment,
        user_id,
        post_id
    )


def get_comment_service(db: Session, comment_id: int):

    comment = get_comment(db, comment_id)

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    return comment


def get_all_comments_service(db: Session):

    return get_all_comments(db)


def delete_comment_service(
    db: Session,
    comment_id: int
):

    comment = delete_comment(db, comment_id)

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    return {
        "message": "Comment deleted successfully"
    }