import pymongo

# for insert one data
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["customers"]


#searching for data
