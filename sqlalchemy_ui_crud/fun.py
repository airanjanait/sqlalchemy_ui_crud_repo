from database import Empinfo,session
from sqlalchemy import update

#____________insert data_____________

class crud:
    def insert(self,data):
        insert_data=Empinfo(emp_name=data[0],DOJ=data[1],MOnumber=data[2])
        print(insert_data,"==========")
        session.add(insert_data)
        return "data inserted"
    
#_____________fetching all data____________
    
    def fetch_data(self):
        data_list=[]
        fetch=session.query(Empinfo).filter(Empinfo.emp_name==self.)
        print(fetch,"######################")
        for f in fetch:
            id=f.id
            emp_name=f.emp_name
            DOJ=f.DOJ
            Monumber=f.MOnumber
            data=emp_name,DOJ,Monumber,id
            data_list.append(data)  
            print(data_list,"======================")
            return data_list
    
#_______________deleting data ______________
    
    def delete_data(self,id):
        delete_data=session.query(Empinfo).filter(Empinfo.id==id).first()
        session.delete(delete_data)
        return "deleted"
    
#__________________fetching one data to update__________________
    
    def fetchonedata(self,id):
        data=""
        fetchone=session.query(Empinfo).filter(Empinfo.id==id)
        for fe in fetchone:
            id=fe.id
            name=fe.emp_name
            DOJ=fe.DOJ
            MOnumber=fe.MOnumber
            data=name,DOJ,MOnumber,id
        return data
    
    
    def update(self,emp_name,DOJ,MOnumber,id):
        update_data=update(Empinfo).where(Empinfo.id==id).values(emp_name=emp_name,DOJ=DOJ,MOnumber=MOnumber)
        s=session.execute(update_data)
        print(s)
        return update_data     