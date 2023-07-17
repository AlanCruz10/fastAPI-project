import sqlalchemy
from sqlalchemy.exc import InvalidRequestError

metadata = sqlalchemy.MetaData()


def __init__():
    statistic = sqlalchemy.Table(
        "statistics",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BIGINT, primary_key=True),
        sqlalchemy.Column("median", sqlalchemy.FLOAT),
        sqlalchemy.Column("parameter_id", sqlalchemy.BIGINT, sqlalchemy.ForeignKey("parameters.id")),
    )
    return statistic


def statistic_entity():
    try:
        return __init__()
    except InvalidRequestError:
        user = metadata.tables["statistics"]
        return user


