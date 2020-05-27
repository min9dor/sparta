from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({"title":"매트릭스"})

db.movies.update_many({"star":9.39},{"$set":{"star":0}})