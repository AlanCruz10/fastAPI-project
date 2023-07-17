import sqlalchemy
from sqlalchemy.exc import InvalidRequestError

metadata = sqlalchemy.MetaData()


def __init__():
    parameter = sqlalchemy.Table(
        "parameters",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BIGINT, primary_key=True),
        sqlalchemy.Column("date", sqlalchemy.String(length=255)),
        sqlalchemy.Column("humidity_above", sqlalchemy.FLOAT),
        sqlalchemy.Column("humidity_below", sqlalchemy.FLOAT),
        sqlalchemy.Column("lux", sqlalchemy.FLOAT),
        sqlalchemy.Column("temperature", sqlalchemy.FLOAT),
        sqlalchemy.Column("status", sqlalchemy.String(length=255)),
        sqlalchemy.Column("user_id", sqlalchemy.BIGINT, sqlalchemy.ForeignKey("users.id")),
        sqlalchemy.Column("statistic_id", sqlalchemy.BIGINT, sqlalchemy.ForeignKey("statistics.id")),
    )
    return parameter


def parameter_entity():
    try:
        return __init__()
    except InvalidRequestError:
        parameter = metadata.tables["parameters"]
        return parameter
