import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("chitchat.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://chitchat-ad935-default-rtdb.firebaseio.com/"
})
ref=db.reference('sender')
data={
"Chat":{
"Enter":" "
}}

for key,value in data.items():
    ref.child(key).set(value)

revdata=" "
chedata=" "
print("enter text:")
while True:

    txt=input()
    if txt=="exit":
        ref.delete()
        break
    else:
        if txt!='.':
            ref=db.reference('reciever')
            data={
            "reply":{
                "Enter":f"{txt}"
            }}

            for key,value in data.items():
                ref.child(key).set(value)

        ref=db.reference('sender/Chat')
        Mydata=ref.get()
        for key,val in Mydata.items():
            chedata=val
        if chedata!=revdata:
            for key,val in Mydata.items():
                print("\t",val)
                revdata=val
        else:
            print(end="")



