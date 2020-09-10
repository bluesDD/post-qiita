from typing import Optional
from dataclasses import dataclass


@dataclass
class Post:
    rendered_body: str
    body: str
    coediting: Optional[bool] = None
    comments_count: int
    created_at: datetime
    group: str
    id: str
    likes_count: Optional[int] = None
    private: Optional[bool] = None
    reactions_count: Optional[bool] = None
    tags: list
    title: str
    updated_at: datetime
    url: str
    user: User
    page_views_count: Optional[int] = None



    
    
