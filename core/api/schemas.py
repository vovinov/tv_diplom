from pydantic import BaseModel


class PingResponceSchema(BaseModel):
    result: bool
