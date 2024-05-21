from datetime import datetime
from pydantic import BaseModel


class NewsSchema(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime | None = None


NewsListSchema = list[NewsSchema]
