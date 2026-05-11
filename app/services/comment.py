from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.comment import CommentCreate
from app.repository.comment import CommentRepository


class CommentService:

    def __init__(self, db: Session):

        self.db = db
        self.comment_repository = CommentRepository()

    def create_comment(
        self,
        comment: CommentCreate,
        user_id: int,
        post_id: int
    ):

        return self.comment_repository.create_comment(
            self.db,
            comment,
            user_id,
            post_id
        )

    def get_comment(self, comment_id: int):

        comment = self.comment_repository.get_comment(
            self.db,
            comment_id
        )

        if not comment:
            raise HTTPException(
                status_code=404,
                detail="Comment not found"
            )

        return comment

    def get_all_comments(self):

        return self.comment_repository.get_all_comments(
            self.db
        )

    def delete_comment(self, comment_id: int):

        comment = self.comment_repository.delete_comment(
            self.db,
            comment_id
        )

        if not comment:
            raise HTTPException(
                status_code=404,
                detail="Comment not found"
            )

        return {
            "message": "Comment deleted successfully"
        }