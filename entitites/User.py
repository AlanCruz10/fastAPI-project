import sqlalchemy
from sqlalchemy.exc import InvalidRequestError

metadata = sqlalchemy.MetaData()


def __init__():
    user = sqlalchemy.Table(
        "users",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BIGINT, primary_key=True),
        sqlalchemy.Column("email", sqlalchemy.String(length=255)),
        sqlalchemy.Column("name", sqlalchemy.String(length=255)),
        sqlalchemy.Column("password", sqlalchemy.String(length=255)),
        sqlalchemy.Column("product_key", sqlalchemy.String(length=255)),
    )
    return user


def user_entity():
    try:
        return __init__()
    except InvalidRequestError:
        user = metadata.tables["users"]
        return user
