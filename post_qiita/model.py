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


@dataclass
class User:
    description: Optional[str] = None
    facebook_id: Optional[str] = None
    followees_count: int
    followers_count: int
    github_login_name: Optional[str] = None
    id: str
    items_count: int
    linkedin_id: Optional[str] = None
    location: Optional[str] = None
    name: Optional[str] = None
    organization: Optional[str] = None
    permanent_id: int
    profile_image_url: str
    team_only: bool
    twitter_screen_name: Optional[str] = None
    website_url: Optional[str] = None


