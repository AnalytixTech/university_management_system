from pymongo import MongoClient, errors

try:
    client = MongoClient(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=5000
    )
    # Force connection on server_info() call.
    client.server_info()
except errors.ServerSelectionTimeoutError as err:
    print("Failed to connect to MongoDB:", err)
    exit(1)

# Use (or create) a database named 'university_system'
db = client["university_system"]
users_col      = db["users"]
students_col   = db["students"]
professors_col = db["professors"]
courses_col    = db["courses"]
