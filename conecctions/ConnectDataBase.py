import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
DATABASE_URL = "mysql://admin:adminamili@amilidb.ctlqdwf7wjsv.us-east-1.rds.amazonaws.com:3306/users_db"
# DATABASE_URL = "mysql://root:Corazon666@localhost:3306/test-statistic"


def connect_to_database():
    database = databases.Database(DATABASE_URL)

    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)

    return database
