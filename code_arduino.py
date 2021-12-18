from os import device_encoding
import serial
import sqlite3
from time import *
db=sqlite3.connect("database.db")
while True:
    device="COM18"
    try:
        print("trying....to conect with",device)
        arduino=serial.Serial(device,9600)
    except:
        print("failed to connect on",device)
    try:
        time.sleep(1)
        data=arduino.readline()
        print(data)
        id=data.split(" ")
        try:
            db.row_factory = sqlite3.Row
            cursor = db.execute("select * from employee")
            a=False
            for row in cursor:
                if str(row["id"])==id:
                    s=row
                    a=True
            if a:
                db.row_factory = sqlite3.Row
                cursor = db.execute("select * from hours")
                a=False
                for row in cursor:
                    if str(row["id"])==id:
                        a=True
                if not a:
                    sr=strftime("%H:%M:%S", gmtime())
                    db.execute("insert into hours(name,id,clock_in,clock_out) values(?,?,?,?)",(a["full_name"],id,strftime("%H:%M:%S", gmtime()),''))
                else:
                    db.execute("update hours set clock_out='{strftime("%H:%M:%S", gmtime()}' where id={id}")
                db.commit()
                db.close()
            else:
                print("this ",id,"employee doesnt exist in our database")
        except:
            print("failed to insert")
    except:
        print("failed to get data from arduino")