import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongo_pass = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = os.getenv("MONGO_PORT", "27017")
mongo_db = os.getenv("MONGO_DB", "student_db")

# MongoDB connection URI
uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"
client = MongoClient(uri)

# Select database and collection
db = client[mongo_db]
students = db["students"]

def create_account():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if students.find_one({"username": username}):
        print("❌ Username already exists!")
        return

    students.insert_one({"username": username, "password": password})
    print("✅ Account created successfully!")

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user = students.find_one({"username": username, "password": password})
    if user:
        print(f"✅ Login successful! Welcome, {username}!")
    else:
        print("❌ Invalid username or password.")

def main():
    print("=== Student Login System ===")
    print("1. Create Account")
    print("2. Login")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
