from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import Integer,VARCHAR
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker,declarative_base



SQLALCHEMY_DATABASE_URL="mysql+pymysql://root@localhost/emp_info"
engine=create_engine(   
    SQLALCHEMY_DATABASE_URL,connect_args={}
)

Session=sessionmaker(bind=engine,autocommit=False, autoflush=False,)
session=Session()

Base=declarative_base()

#_________________creating table _________________
class Empinfo(Base):
    __tablename__='detail'
    id=Column(Integer ,primary_key=True,autoincrement=True)
    emp_name=Column(VARCHAR(50))
    DOJ=Column(VARCHAR(30))
    MOnumber=Column(VARCHAR(23))
    
Base.metadata.create_all(engine)

    

def get_db():
    db=Session()
    try:
        yield db
    finally:
        print("done")
        db.close()
        

