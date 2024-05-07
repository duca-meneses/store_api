from datetime import datetime, timezone
from typing import Annotated
import uuid

from pydantic import UUID4, BaseModel, Field


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: Annotated[datetime, Field(default_factory=datetime_now)]
    updated_at: Annotated[datetime, Field(default_factory=datetime_now)]
