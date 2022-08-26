
from sqlalchemy import create_engine

# Engine parameters
dialect = 'postgresql'
driver = 'psycopg2'
username = 'root'
password = 'root'
host = 'localhost'
port = '5432'
database = 'test_db'

# Engine URL
url = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"

print(url)

# Creating the engine
engine = create_engine(url)

