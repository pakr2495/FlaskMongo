from pymongo import MongoClient

class DB:
    def __init__(self):
        self.client = MongoClient('my-mongo',27017)
        self.db = self.client['TaskDB']
        self.collection = self.db['TaskCollection']


    def insertData(self,id,task_name,task_descrition,task_status,task_duedate):
        self.collection.insert_one({
            "Id":id,
            "Task_Name": task_name,
            "Task_Descrition": task_descrition,
            "Task_Status":task_status,
            "Task_Duedate":task_duedate
        })
        self.collection.count_documents


if __name__ =="__main__":
    db = DB()
    db.insertData(1,"Learn Python","Start from basic to end","Not Completed","30/07/2021")