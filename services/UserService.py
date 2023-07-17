from conecctions import ConnectDataBase
from entitites import User
from models import UserModel
database = ConnectDataBase.connect_to_database()


async def get_user(user_id):
    await database.connect()
    user = User.user_entity()

    find_user = user.select().where(user.c.id == user_id)

    user_found = await database.fetch_one(query=find_user)

    model_user = UserModel.User(**dict(user_found))
    await database.disconnect()
    return model_user
