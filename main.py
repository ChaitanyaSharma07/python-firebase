import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json


databaseURL = "<database url>"

cred_obj = credentials.Certificate('<path to service account file>')  
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': databaseURL
})


#functions to set data to database
def user_update():
    user_name = input("Enter your user name: ")
    user_password = input("Enter your password: ")

    data_set = {
        "user": {
            "user_name": user_name,
            "password": user_password
        
        }
    }


    with open("users.json", "r+") as file:
        data = json.load(file)

        data["allUsers"].append(data_set)
        

        file.seek(0)
        json.dump(data, file, indent=4)



        ref = db.reference("/")

        ref.set({
            "Users": {
                "allUsers": len(data["allUsers"])
            }   
        })

        ref = db.reference("/Users/")

        file_content = data["allUsers"]

        for key, value in enumerate(file_content):
            ref.push().set(value)


user_update()