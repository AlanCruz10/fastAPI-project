from conecctions import ConnectDataBase
from entitites import Statistic
from models import StatisticModel, RecordModel
from services import ParametricService
from services import UserService

database = ConnectDataBase.connect_to_database()


async def get_record_by_date(date, user_id):
    await database.connect()
    statistic = Statistic.statistic_entity()
    parametric_list = await ParametricService.get_all_parametric(date, user_id)
    user = await UserService.get_user(user_id)
    list_statistic_model = []
    for parameter in parametric_list:
        find_statistic = statistic.select().where(statistic.c.parameter_id == parameter.id)
        statistic_found = await database.fetch_one(query=find_statistic)
        model_statistic = StatisticModel.Statistic(**dict(statistic_found))
        list_statistic_model.append(model_statistic)

    if len(parametric_list) == len(list_statistic_model):
        record_by_date = []
        for parameter_filter, statistic_filer in zip(parametric_list, list_statistic_model):
            record = dict(RecordModel.Record(id=parameter_filter.id, date=parameter_filter.date,
                                             humidity_above=parameter_filter.humidity_above,
                                             humidity_below=parameter_filter.humidity_below, lux=parameter_filter.lux,
                                             temperature=parameter_filter.temperature, status=parameter_filter.status,
                                             user_id=user.id, product_key=user.product_key,
                                             statistic_id=statistic_filer.id, median=statistic_filer.median))
            record_by_date.append(record)
        await database.disconnect()
        return record_by_date
    else:
        record_by_date = []
        for parameter_filter in parametric_list:
            record = dict(RecordModel.Record(id=parameter_filter.id, date=parameter_filter.date,
                                             humidity_above=parameter_filter.humidity_above,
                                             humidity_below=parameter_filter.humidity_below, lux=parameter_filter.lux,
                                             temperature=parameter_filter.temperature, status=parameter_filter.status,
                                             user_id=user.id, product_key=user.product_key,
                                             statistic_id=None, median=None))
            record_by_date.append(record)
        await database.disconnect()
        return record_by_date
