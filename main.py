
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import io
import os
import numpy as np
import requests


def registration():
    Fullname = StringVar()
    Email = StringVar()
    dob = StringVar()
    Phone = StringVar()
    Address = StringVar()
    relpho1 = StringVar()
    relpho2 = StringVar()
    bg = StringVar()
    registration = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    registration.title("Registration")

    # sets the geometry of toplevel
    registration.geometry("1200x700")

    canvas1 = Canvas(registration, width=700, height=100, relief='raised', bg="white")
    canvas1.pack()

    label1 = Label(registration, text='REGISTRAION')
    label1.config(font=("bold", 40), bg="white")
    canvas1.create_window(350, 50, window=label1)

    canvas2 = Canvas(registration, width=1000, height=500, relief='raised', bg="white")
    canvas2.pack()

    label2 = Label(registration, text='Fullname :')
    label2.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(65, 30, window=label2)

    entry1 = Entry(registration, textvar=Fullname, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 30, window=entry1)

    label3 = Label(registration, text='E-mail :')
    label3.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(52, 70, window=label3)

    entry2 = Entry(registration, textvar=Email, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 70, window=entry2)

    label4 = Label(registration, text='D. O. B :')
    label4.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(52, 110, window=label4)

    entry3 = Entry(registration, textvar=dob, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 110, window=entry3)

    label5 = Label(registration, text='Gender :')
    label5.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(54, 150, window=label5)

    var = StringVar()
    rd1 = Radiobutton(registration, text="Male", padx=5, variable=var, value="Male")
    rd1.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(200, 150, window=rd1)

    rd2 = Radiobutton(registration, text="Female", padx=20, variable=var, value="Female")
    rd2.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(300, 150, window=rd2)

    label6 = Label(registration, text='Phone No. :')
    label6.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(65, 190, window=label6)

    entry4 = Entry(registration, textvar=Phone, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 190, window=entry4)

    label7 = Label(registration, text='Address :')
    label7.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(60, 240, window=label7)

    entry5 = Entry(registration, textvar=Address, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 240, window=entry5)

    label8 = Label(registration, text='Blood Group :')
    label8.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(65, 290, window=label8)

    bgap = Radiobutton(registration, text="A+", padx=5, variable=bg, value="A+")
    bgap.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(200, 275, window=bgap)

    bgan = Radiobutton(registration, text="A-", padx=5, variable=bg, value="A-")
    bgan.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(250, 275, window=bgan)

    bgbp = Radiobutton(registration, text="B+", padx=5, variable=bg, value="B+")
    bgbp.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(300, 275, window=bgbp)

    bgbn = Radiobutton(registration, text="B-", padx=5, variable=bg, value="B-")
    bgbn.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(350, 275, window=bgbn)

    bgop = Radiobutton(registration, text="O+", padx=5, variable=bg, value="O+")
    bgop.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(200, 308, window=bgop)

    bgon = Radiobutton(registration, text="O-", padx=5, variable=bg, value="O-")
    bgon.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(255, 308, window=bgon)

    bgabp = Radiobutton(registration, text="AB+", padx=5, variable=bg, value="AB+")
    bgabp.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(315, 308, window=bgabp)

    bgabn = Radiobutton(registration, text="AB-", padx=5, variable=bg, value="AB-")
    bgabn.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(380, 308, window=bgabn)

    label9 = Label(registration, text='Relative Phone 1 :')
    label9.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(85, 335, window=label9)

    entry6 = Entry(registration, textvar=relpho1, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 335, window=entry6)

    label10 = Label(registration, text='Relative Phone 2 :')
    label10.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(85, 375, window=label10)

    entry7 = Entry(registration, textvar=relpho2, font=(14), borderwidth=2, width=30)
    canvas2.create_window(320, 375, window=entry7)

    def upload():
        global filename, img
        f_types = [('All Files', '*.*'),
                   ('JPG', '*.jpg'),
                   ('PNG', '*.png')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        if (filename):
            img = Image.open(filename)
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            label = Label(registration, image=img, width=100, height=100)
            canvas2.create_window(900, 60, window=label)

    uploadb = Button(registration, text='UPLOAD YOUR FINGERPRINT', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(650, 60, window=uploadb)

    def submit():
        fb = open(filename, 'rb')  # filename from upload_file()
        fb = fb.read()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ankit",
                database="demo"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO people (name,email,dob,gender,phone,aadhar,address,bloodgroup,relaphone1,relaphone2,finger) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"
            val = [(Fullname.get(), Email.get(), dob.get(), var.get(), Phone.get(), 0, Address.get(), bg.get(),
                    relpho1.get(), relpho2.get(), fb)]
            mycursor.executemany(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted successfuly.")
        except mysql.connector.Error as error:
            print("Failed to insert into customer table {}".format(error))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")

    register = Button(registration, text='REGISTER', command=submit, bg='red', fg='white',
                      font=('helvetica', 25, 'bold'))
    canvas2.create_window(500, 450, window=register)


def fetch():
    relp1 = 0
    relp2 = 0
    aadhaarno = StringVar()
    Fullname = StringVar()
    fetch = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    fetch.title("Fetch")

    # sets the geometry of toplevel
    fetch.geometry("1200x700")

    canvas1 = Canvas(fetch, width=700, height=100, relief='raised', bg="white")
    canvas1.pack()

    label1 = Label(fetch, text='FETCH')
    label1.config(font=("bold", 40), bg="white")
    canvas1.create_window(350, 50, window=label1)

    canvas2 = Canvas(fetch, width=1000, height=520, relief='raised', bg="white")
    canvas2.pack()

    label2 = Label(fetch, text='Fullname :')
    label2.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(65, 30, window=label2)

    label3 = Label(fetch, text='E-mail :')
    label3.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(52, 70, window=label3)

    label4 = Label(fetch, text='D. O. B :')
    label4.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(54, 110, window=label4)

    label5 = Label(fetch, text='Gender :')
    label5.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(54, 150, window=label5)

    label6 = Label(fetch, text='Phone No. :')
    label6.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(65, 190, window=label6)

    label7 = Label(fetch, text='Aadhaar No. :')
    label7.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(72, 230, window=label7)

    label8 = Label(fetch, text='Address :')
    label8.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(56, 270, window=label8)

    label9 = Label(fetch, text='Blood Group :')
    label9.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(72, 310, window=label9)

    label10 = Label(fetch, text='Relative Phone 1 :')
    label10.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(89, 350, window=label10)

    label11 = Label(fetch, text='Relative Phone 2 :')
    label11.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(89, 390, window=label11)

    label12 = Label(fetch, text='Aadhaar No. :')
    label12.config(font=('helvetica', 14), bg="white")
    canvas2.create_window(570, 30, window=label12)

    entry8 = Entry(fetch, textvar=aadhaarno, font=(14), borderwidth=2, width=30)
    canvas2.create_window(800, 30, window=entry8)

    def submitaadhaar():
        global img
        # trying to make a connection to database, here i am using mysql
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ankit",
                database="demo"
            )
            mycursor = mydb.cursor()
            # a basic sql query to retrieve image from database
            # images are stored as BLOB file in database
            mycursor.execute("SELECT name FROM people WHERE aadhar='%s'" % aadhaarno.get())
            name1 = mycursor.fetchone()

            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str

            name = convertTuple(name1)
            namelabel = Label(fetch, text='' + str(name))
            namelabel.config(font=('helvetica', 14), bg="white", fg="red")
            canvas2.create_window(170, 30, window=namelabel)

            mycursor.execute("SELECT email FROM people WHERE aadhar='%s'"%aadhaarno.get())
            email1 = mycursor.fetchone()
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            email = convertTuple(email1)
            emaillabel = Label(fetch, text=''+str(email))
            emaillabel.config(font=('helvetica',14),bg="white",fg="red")
            canvas2.create_window(205, 70, window=emaillabel)

            mycursor.execute("SELECT dob FROM people WHERE aadhar='%s'"%aadhaarno.get())
            dob1 = mycursor.fetchone()
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            dob = convertTuple(dob1)
            doblabel = Label(fetch, text=''+str(dob))
            doblabel.config(font=('helvetica',14),bg="white",fg="red")
            canvas2.create_window(142, 110, window=doblabel)

            mycursor.execute("SELECT gender FROM people WHERE aadhar='%s'"%aadhaarno.get())
            gender1 = mycursor.fetchone()
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            gender = convertTuple(gender1)
            genderlabel = Label(fetch, text=''+str(gender))
            genderlabel.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(112, 150, window=genderlabel)

            mycursor.execute("SELECT phone from people WHERE aadhar='%s'"%aadhaarno.get())
            phone1 = mycursor.fetchone()
            phone1 = tuple(map(str, phone1))
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            phone = convertTuple(phone1)
            phonelabel = Label(fetch, text=''+str(phone))
            phonelabel.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(174, 190, window=phonelabel)

            mycursor.execute("SELECT aadhar from people WHERE aadhar='%s'"%aadhaarno.get())
            aadhaar1 = mycursor.fetchone()
            aadhaar1 = tuple(map(str, aadhaar1))
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            aadhaar = convertTuple(aadhaar1)
            aadhaarlabel = Label(fetch, text=''+str(aadhaar))
            aadhaarlabel.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(205, 230, window=aadhaarlabel)

            mycursor.execute("SELECT address from people WHERE aadhar='%s'"%aadhaarno.get())
            address1 = mycursor.fetchone()
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            address = convertTuple(address1)
            addresslabel = Label(fetch, text=''+str(address))
            addresslabel.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(165, 270, window=addresslabel)

            mycursor.execute("SELECT bloodgroup from people WHERE aadhar='%s'"%aadhaarno.get())
            bloodgroup1 = mycursor.fetchone()
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            bloodgroup = convertTuple(bloodgroup1)
            bloodgrouplabel = Label(fetch, text=''+str(bloodgroup))
            bloodgrouplabel.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(145, 310, window=bloodgrouplabel)

            mycursor.execute("SELECT relaphone1 from people WHERE aadhar='%s'"%aadhaarno.get())
            relaphone11 = mycursor.fetchone()
            relaphone11 = tuple(map(str, relaphone11))
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            relaphone1 = convertTuple(relaphone11)
            relaphonelabel1 = Label(fetch, text=''+str(relaphone1))
            relaphonelabel1.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(225, 350, window=relaphonelabel1)

            mycursor.execute("SELECT relaphone2 from people WHERE aadhar='%s'"%aadhaarno.get())
            relaphone21 = mycursor.fetchone()
            relaphone21 = tuple(map(str, relaphone21))
            def convertTuple(tup):
                str = ''
                for item in tup:
                    str = str + item
                return str
            relaphone2 = convertTuple(relaphone21)
            relaphonelabel2 = Label(fetch, text=''+str(relaphone2))
            relaphonelabel2.config(font=('helvetica',14,),bg="white",fg="red")
            canvas2.create_window(225, 390, window=relaphonelabel2)

            mycursor.execute("SELECT finger FROM people WHERE aadhar='%s'"%aadhaarno.get())
            myresult = mycursor.fetchone()
            img = Image.open(io.BytesIO(myresult[0]))
            img=img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            label = Label(fetch, image=img,width=100,height=100)
            canvas2.create_window(65, 460, window=label)

        except mysql.connector.Error as error:
            print("Failed to get from customer table {}".format(error))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed")

    uploadaadhaar = Button(fetch, text='Get Detail By Aadhaar', command=submitaadhaar, font=('helvetica', 14, 'bold'))
    canvas2.create_window(750, 70, window=uploadaadhaar)

    def upload():
        global filename, img
        newpath = r'C:\Users\ankit\PycharmProjects\SpeedyLine\Upload'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        f_types = [('BMP', '*.bmp')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        if (filename):
            img = Image.open(filename)
            img = img.resize((100, 100))
            img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Upload\\sample.bmp', 'BMP')
            img = ImageTk.PhotoImage(img)
            label = Label(fetch, image=img, width=100, height=100, bg = "white")
            canvas2.create_window(750, 160, window=label)

    uploadfinger = Button(fetch, text='Upload Finger', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(750, 250, window=uploadfinger)


    def scorecheck(img1, img2):
        # Open the two images

        # Convert the images to numpy arrays
        arr1 = np.array(img1)
        arr2 = np.array(img2)

        # Calculate the mean squared error between the two arrays
        mse = np.square(np.subtract((arr1), arr2)).mean()

        # Convert the MSE to a similarity score (the lower the MSE, the higher the similarity)
        score = 1 / (1 + mse)
        return score



    def submitfinger():
        global img
        newpath = r'C:\Users\ankit\PycharmProjects\SpeedyLine\Download'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        st = 200000000001
        for i in range(st, 200000000010):
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ankit",
                    database="demo"
                )
                # a basic sql query to retrieve image from database
                # images are stored as BLOB file in database
                mycursor = mydb.cursor()
                mycursor.execute("SELECT finger FROM people WHERE aadhar='%s'" %i)
                myresult = mycursor.fetchone()
                img = Image.open(io.BytesIO(myresult[0]))
                img = img.resize((100, 100))
                img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Download\\Check.bmp', 'BMP')
                img1 = Image.open("Download\Check.bmp")
                img2 = Image.open("Upload\Sample.bmp")
                score = scorecheck(img1,img2)
                if (score>=1.0):
                    mycursor.execute("SELECT name FROM people WHERE aadhar='%s'" %i)
                    name1 = mycursor.fetchone()
                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str
                    name = convertTuple(name1)
                    namelabel = Label(fetch, text='' + str(name))
                    namelabel.config(font=('helvetica', 14), bg="white", fg="red")
                    canvas2.create_window(170, 30, window=namelabel)

                    mycursor.execute("SELECT email FROM people WHERE aadhar='%s'" %i)
                    email1 = mycursor.fetchone()

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    email = convertTuple(email1)
                    emaillabel = Label(fetch, text='' + str(email))
                    emaillabel.config(font=('helvetica', 14), bg="white", fg="red")
                    canvas2.create_window(205, 70, window=emaillabel)

                    mycursor.execute("SELECT dob FROM people WHERE aadhar='%s'" %i)
                    dob1 = mycursor.fetchone()

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    dob = convertTuple(dob1)
                    doblabel = Label(fetch, text='' + str(dob))
                    doblabel.config(font=('helvetica', 14), bg="white", fg="red")
                    canvas2.create_window(142, 110, window=doblabel)

                    mycursor.execute("SELECT gender FROM people WHERE aadhar='%s'" %i)
                    gender1 = mycursor.fetchone()

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    gender = convertTuple(gender1)
                    genderlabel = Label(fetch, text='' + str(gender))
                    genderlabel.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(112, 150, window=genderlabel)

                    mycursor.execute("SELECT phone from people WHERE aadhar='%s'" %i)
                    phone1 = mycursor.fetchone()
                    phone1 = tuple(map(str, phone1))

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    phone = convertTuple(phone1)
                    phonelabel = Label(fetch, text='' + str(phone))
                    phonelabel.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(174, 190, window=phonelabel)

                    mycursor.execute("SELECT aadhar from people WHERE aadhar='%s'" %i)
                    aadhaar1 = mycursor.fetchone()
                    aadhaar1 = tuple(map(str, aadhaar1))

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    aadhaar = convertTuple(aadhaar1)
                    aadhaarlabel = Label(fetch, text='' + str(aadhaar))
                    aadhaarlabel.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(205, 230, window=aadhaarlabel)

                    mycursor.execute("SELECT address from people WHERE aadhar='%s'" %i)
                    address1 = mycursor.fetchone()

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    address = convertTuple(address1)
                    addresslabel = Label(fetch, text='' + str(address))
                    addresslabel.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(165, 270, window=addresslabel)

                    mycursor.execute("SELECT bloodgroup from people WHERE aadhar='%s'" %i)
                    bloodgroup1 = mycursor.fetchone()

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    bloodgroup = convertTuple(bloodgroup1)
                    bloodgrouplabel = Label(fetch, text='' + str(bloodgroup))
                    bloodgrouplabel.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(145, 310, window=bloodgrouplabel)

                    mycursor.execute("SELECT relaphone1 from people WHERE aadhar='%s'" %i)
                    relaphone11 = mycursor.fetchone()
                    relaphone11 = tuple(map(str, relaphone11))

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str
                    relaphone1 = convertTuple(relaphone11)
                    relp1 = str(relaphone1)
                    relaphonelabel1 = Label(fetch, text='' + str(relaphone1))
                    relaphonelabel1.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(225, 350, window=relaphonelabel1)

                    mycursor.execute("SELECT relaphone2 from people WHERE aadhar='%s'" %i)
                    relaphone21 = mycursor.fetchone()
                    relaphone21 = tuple(map(str, relaphone21))

                    def convertTuple(tup):
                        str = ''
                        for item in tup:
                            str = str + item
                        return str

                    relaphone2 = convertTuple(relaphone21)
                    relp2 = str(relaphone2)
                    relaphonelabel2 = Label(fetch, text='' + str(relaphone2))
                    relaphonelabel2.config(font=('helvetica', 14,), bg="white", fg="red")
                    canvas2.create_window(225, 390, window=relaphonelabel2)
                    break
            except mysql.connector.Error as error:
                print("Failed to get from customer table {}".format(error))

            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
                    # print("Fetching Information, Please Wait....")

            def sendsms():
                url = "https://www.fast2sms.com/dev/bulkV2"

                querystring = {
                    "authorization": "ISn9AoN5DT4cYshMUKa7Zu0L6Et2degjXRF8PWx3fmkbQVJzOGX5eDox3Vzkv2pjn6B0ICuFE7MbHAQg",
                    "message": "This is test message", "language": "english", "route": "q", "numbers":""+str(relp1)+","+str(relp2)}

                headers = {
                    'cache-control': "no-cache"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)

                print(response.text)
                print(relp1)
                print(relp2)

            sendsms = Button(fetch, text='Send SMS', command=sendsms, font=('helvetica', 14, 'bold'))
            canvas2.create_window(750, 450, window=sendsms)

    fetchfinger = Button(fetch, text='Get Detail By Finger', command=submitfinger, font=('helvetica', 14, 'bold'))
    canvas2.create_window(750, 310, window=fetchfinger)




def exit():
    root.destroy()


# Create the main window
root = Tk()
root.geometry("1200x700")
root.title("SPEEDY LINE")
root.resizable(False, False)

canvas1 = Canvas(root, width=700, height=100, relief='raised', bg="white")
canvas1.pack()

label1 = Label(root, text='SPEEDY LINE')
label1.config(font=("bold", 40), bg="white")
canvas1.create_window(350, 50, window=label1)

canvas2 = Canvas(root, width=1000, height=500, relief='raised', bg="white")
canvas2.pack()

registration = Button(root, text='Registration', command=registration, bg='black', fg='white',
                      font=('helvetica', 25, 'bold'))
canvas2.create_window(150, 150, window=registration)

fetch = Button(root, text='      Fetch      ', command=fetch, bg='black', fg='white', font=('helvetica', 25, 'bold'))
canvas2.create_window(850, 150, window=fetch)

exit = Button(root, text='      Exit      ', command=exit, bg='red', fg='white', font=('helvetica', 25, 'bold'))
canvas2.create_window(500, 450, window=exit)

# # Create labels and entry fields for the form
# name_label = tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0)
# name_entry = tk.Entry(root)
# name_entry.grid(row=0, column=1)

# email_label = tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0)
# email_entry = tk.Entry(root)
# email_entry.grid(row=1, column=1)

# phone_label = tk.Label(root, text="Phone:")
# phone_label.grid(row=2, column=0)
# phone_entry = tk.Entry(root)
# phone_entry.grid(row=2, column=1)

# checkin_label = tk.Label(root, text="Check-in Date:")
# checkin_label.grid(row=3, column=0)
# checkin_entry = tk.Entry(root)
# checkin_entry.grid(row=3, column=1)

# checkout_label = tk.Label(root, text="Check-out Date:")
# checkout_label.grid(row=4, column=0)
# checkout_entry = tk.Entry(root)
# checkout_entry.grid(row=4, column=1)

# # Create a button to save the registration
# save_button = tk.Button(root, text="Save", command=save_registration)
# save_button.grid(row=5, column=1, pady=10)

root.mainloop()
