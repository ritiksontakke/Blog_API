from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.post import (
    PostCreate,
    PostUpdate
)

from app.repository.post import PostRepository


class PostService:

    def __init__(self, db: Session):

        self.db = db
        self.post_repository = PostRepository()

    def create_post(
        self,
        post: PostCreate,
        user_id: int
    ):

        return self.post_repository.create_post(
            self.db,
            post,
            user_id
        )

    def get_post(self, post_id: int):

        post = self.post_repository.get_post(
            self.db,
            post_id
        )

        if not post:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )

        return post

    def get_all_posts(self):

        return self.post_repository.get_all_posts(
            self.db
        )

    def update_post(
        self,
        post_id: int,
        post_data: PostUpdate,
        current_user
    ):

        # Get Post
        post = self.post_repository.get_post(
            self.db,
            post_id
        )

        if not post:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )

        # Authorization Check
        if post.user_id != current_user.id:

            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        return self.post_repository.update_post(
            self.db,
            post_id,
            post_data
        )

    def delete_post(
        self,
        post_id: int,
        current_user
    ):

        # Get Post
        post = self.post_repository.get_post(
            self.db,
            post_id
        )

        if not post:
            raise HTTPException(
                status_code=404,
                detail="Post not found"
            )

        # Authorization Check
        if post.user_id != current_user.id:

            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        self.post_repository.delete_post(
            self.db,
            post_id
        )

        return {
            "message": "Post deleted successfully"
        }