from pydantic import BaseModel


class Record(BaseModel):
    id: int
    date: str
    humidity_above: float
    humidity_below: float
    lux: float
    temperature: float
    status: str
    user_id: int
    product_key: str
    statistic_id: int | None = None
    median: float | None = None
