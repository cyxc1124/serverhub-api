from datetime import datetime

from pydantic import BaseModel


class ServerBase(BaseModel):
    name: str
    host: str
    port: int = 22
    description: str | None = None


class ServerCreate(ServerBase):
    pass


class ServerUpdate(BaseModel):
    name: str | None = None
    host: str | None = None
    port: int | None = None
    description: str | None = None
    status: str | None = None


class ServerRead(ServerBase):
    id: int
    status: str
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
