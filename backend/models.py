from pydantic import BaseModel

class YellEntry(BaseModel):
    who_yelled: str
    reason: str
    count:int