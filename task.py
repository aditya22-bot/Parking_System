import mysql.connector
import datetime as t

conn = mysql.connector.connect(host='localhost', database='parking_system', user='root', password='')
cursor = conn.cursor()
def recored():
    cursor.execute('select * from parking_id;')
    records = cursor.fetchall()
    for row in records:
        print("Parking_ID=>", row[0], "Car_Type=>", row[1], "Number_plet=>", row[2], "Floor=>", row[3], "price=>",
              row[4], "car_in=>", row[5], "car_out=>", row[6])
def login():
    while True:
        userName = input("Enter User Name")
        Password = input("Enter Your Password")
        cursor.execute(
            'select * from login_details where login_id="{}" and password ="{}"'.format(userName, Password))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows != 1:
            print('Invalid Login details..... Try again')
        else:
            print('Welcome To Car Parking System')
            break
def add_details():
    print("Enter Details")
    car_Type = input('Enter Parking Type( 1. Two wheelar 2. Car 3. Bus 4. Truck ')
    number = input("Enter Number plet ")
    floor = int(input("Enter Floor"))
    price = int(input("Enter Car Price Bases On Critetia of car"))
    date_time_in = t.datetime.now().isoformat()
    sql = f"INSERT INTO parking_id (car_Type,Number_plet,floor,Price,car_in) VALUES {car_Type, number, floor, price, date_time_in}"
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record inserted.")


# add_details()
def out_time():
    print("Enter Details")
    # numbers=input("Enter Your Car Number pleat")
    parking_id = int(input("enter Your parking id"))
    tim = t.datetime.now().isoformat()
    sql = f"update parking_id set car_Out=(%s) where parking_id=(%s)"
    val = (tim, parking_id)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "Record Updated")

# out_time()
def find_record():
    print("Enter Details To Find Where Your car is")
    input1 = int(input("Enter Parking ID For Finding a Record"))

    cursor.execute(f'SELECT Number_plet,floor FROM parking_id WHERE parking_id IN ({input1});')
    records = cursor.fetchall()
    for i in records:
        print("Floor is=",i[1],"Number IS=>",i[0])

if __name__ == '__main__':
    login()
    s=True
    while s:
        print("Welcome User")
        print("1.Add Record 2. Out_Time 3. Record_history 4. Find 5. log_out")
        choice=int(input("Enter Your Choice"))
        if choice==1:
            add_details()
        elif choice==2:
            out_time()
        elif choice==3:
            recored()
        elif choice==4:
            find_record()
        elif choice==5:
            s=False
            print("Thank You")

        else:
            print("Wrong Choice Please Enter Correct Choice")

