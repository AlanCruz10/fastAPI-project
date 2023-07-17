from fastapi import FastAPI
from typing import List
from conecctions import ConnectDataBase
from services import StatisticService
from models import RecordModel
from configurations import configuration_cors

database = ConnectDataBase.connect_to_database()
app = FastAPI()

configuration_cors.cors(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/get/all/history/{date}/user/{user_id}", response_model=List[RecordModel.Record])
async def get_record_by_date(date: str, user_id: int):
    return await StatisticService.get_record_by_date(date, user_id)


if __name__ == "__main__":
    import uvicorn
    # configuration_cors.cors(app)
    uvicorn.run(app, host="127.0.0.1", port=8000)
