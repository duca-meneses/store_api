from datetime import datetime, timezone
import uuid
from pydantic import UUID4, BaseModel, Field


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime_now)
    updated_at: datetime = Field(default_factory=datetime_now)
