from conecctions import ConnectDataBase
from entitites import Parametric
from models import ParametricModel
from services import UserService

database = ConnectDataBase.connect_to_database()


async def get_all_parametric(date, user_id):
    await database.connect()
    parameter = Parametric.parameter_entity()
    user = await UserService.get_user(user_id)

    list_parameters = parameter.select().where(parameter.c.user_id == user.id)
    list_parameters_found = await database.fetch_all(query=list_parameters)
    list_parameters_filter = [list_parameter for list_parameter in list_parameters_found if
                              list_parameter[1].startswith(date)]

    list_parameter_model = [ParametricModel.Parametric(**dict(filter_list_parameter)) for filter_list_parameter in
                            list_parameters_filter]
    await database.disconnect()
    return list_parameter_model
