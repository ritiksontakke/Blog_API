from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.schemas.comment import CommentCreate


class CommentRepository:

    def create_comment(
        self,
        db: Session,
        comment: CommentCreate,
        user_id: int,
        post_id: int
    ):

        new_comment = Comment(
            content=comment.content,
            user_id=user_id,
            post_id=post_id
        )

        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)

        return new_comment

    def get_comment(
        self,
        db: Session,
        comment_id: int
    ):

        return db.query(Comment).filter(
            Comment.id == comment_id
        ).first()

    def get_all_comments(self, db: Session):

        return db.query(Comment).all()

    def delete_comment(
        self,
        db: Session,
        comment_id: int
    ):

        comment = db.query(Comment).filter(
            Comment.id == comment_id
        ).first()

        if not comment:
            return None

        db.delete(comment)
        db.commit()

        return comment