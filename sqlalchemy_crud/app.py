from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer,VARCHAR
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker,declarative_base,query


engine=create_engine("mysql+pymysql://root@localhost/emnfo",echo=False)

Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base()

#________________creating table in emp_info database____________

class Empinfo(Base):
    __tablename__='empinfo'
    id=Column(Integer ,primary_key=True,autoincrement=True)
    emp_name=Column(VARCHAR(50))
    DOJ=Column(VARCHAR(30))
    MOnumber=Column(VARCHAR(23))
    
# Base.metadata.create_all(engine)

#____________insert data into table _______________________

insert_data=Empinfo(emp_name="ranjana",DOJ="06/12/2022",MOnumber="+91 29832839989")
session.add(insert_data)
session.commit()

#______________get data from table_________________________

data=session.query(Empinfo)
for d in data:
    emp_name=d.emp_name
    DOJ=d.DOJ
    MOnumber=d.MOnumber
    
    print(emp_name,DOJ,MOnumber)
   
#________________________update data ___________________________

update_data=session.query(Empinfo).filter(Empinfo.emp_name=='ranjana').first()
if update_data:
    update_data.emp_name="rohit"
    # session.commit()
    print("updated")
else :
    print("record not found")
    
#____________________delete data___________________________________

delete_data=session.query(Empinfo).filter(Empinfo.emp_name=="rohit").first()
session.delete(delete_data)
session.commit()
print("data deleted ")
