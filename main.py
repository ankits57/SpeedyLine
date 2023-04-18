import shutil
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import io
import os
import numpy as np
import requests
import subprocess
import cv2
import math
import fingerprint_enhancer
from skimage.morphology import skeletonize
from scipy.spatial import distance
from collections import Counter

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

    label1 = Label(registration, text='REGISTRTAION')
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
        os.system("C:\\Users\\ankit\\OneDrive\\Desktop\\Demo_Software\\DotNet\\CgtFpAccessCSD200Dotnet_Test.exe")
        global filename1, img1
        f_types = [('BMP', '*.bmp')]
        filename1 = filedialog.askopenfilename(filetypes=f_types)
        if (filename1):
            img1 = Image.open(filename1)
            img1 = ImageTk.PhotoImage(img1)
            label = Label(registration, image=img1, width=100, height=100)
            canvas2.create_window(900, 60, window=label)

    uploadb = Button(registration, text='UPLOAD YOUR FINGERPRINT 1', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(650, 60, window=uploadb)

    def upload():
        os.system("C:\\Users\\ankit\\OneDrive\\Desktop\\Demo_Software\\DotNet\\CgtFpAccessCSD200Dotnet_Test.exe")
        global filename2, img2
        f_types = [('BMP', '*.bmp')]
        filename2 = filedialog.askopenfilename(filetypes=f_types)
        if (filename2):
            img2 = Image.open(filename2)
            img2 = ImageTk.PhotoImage(img2)
            label = Label(registration, image=img2, width=100, height=100)
            canvas2.create_window(900, 170, window=label)

    uploadb = Button(registration, text='UPLOAD YOUR FINGERPRINT 2', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(650, 150, window=uploadb)

    def upload():
        os.system("C:\\Users\\ankit\\OneDrive\\Desktop\\Demo_Software\\DotNet\\CgtFpAccessCSD200Dotnet_Test.exe")
        global filename3, img3
        f_types = [('BMP', '*.bmp')]
        filename3 = filedialog.askopenfilename(filetypes=f_types)
        if (filename3):
            img3 = Image.open(filename3)
            img3 = ImageTk.PhotoImage(img3)
            label = Label(registration, image=img3, width=100, height=100)
            canvas2.create_window(900, 280, window=label)

    uploadb = Button(registration, text='UPLOAD YOUR FINGERPRINT 3', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(650, 240, window=uploadb)

    def upload():
        os.system("C:\\Users\\ankit\\OneDrive\\Desktop\\Demo_Software\\DotNet\\CgtFpAccessCSD200Dotnet_Test.exe")
        global filename4, img4
        f_types = [('BMP', '*.bmp')]
        filename4 = filedialog.askopenfilename(filetypes=f_types)
        if (filename4):
            img4 = Image.open(filename4)
            img4 = ImageTk.PhotoImage(img4)
            label = Label(registration, image=img4, width=100, height=100)
            canvas2.create_window(900, 390, window=label)

    uploadb = Button(registration, text='UPLOAD YOUR FINGERPRINT 4', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(650, 320, window=uploadb)

    def submit():
        fb1 = open(filename1, 'rb')  # filename from upload_file()
        fb1 = fb1.read()
        fb2 = open(filename2, 'rb')  # filename from upload_file()
        fb2 = fb2.read()
        fb3 = open(filename3, 'rb')  # filename from upload_file()
        fb3 = fb3.read()
        fb4 = open(filename4, 'rb')  # filename from upload_file()
        fb4 = fb4.read()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ankit",
                database="demo"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO people (name,email,dob,gender,phone,aadhar,address,bloodgroup,relaphone1,relaphone2,finger1,finger2,finger3,finger4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = [(Fullname.get(), Email.get(), dob.get(), var.get(), Phone.get(), 0, Address.get(), bg.get(),
                    relpho1.get(), relpho2.get(), fb1, fb2, fb3, fb4)]
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

            mycursor.execute("SELECT finger1 FROM people WHERE aadhar='%s'"%aadhaarno.get())
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
        os.system("C:\\Users\\ankit\\OneDrive\\Desktop\\Demo_Software\\DotNet\\CgtFpAccessCSD200Dotnet_Test.exe")
        global filename, img
        newpath = r'C:\Users\ankit\PycharmProjects\SpeedyLine\Upload'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        f_types = [('BMP', '*.bmp')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        if (filename):
            img = Image.open(filename)
            img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Upload\\101.bmp', 'BMP')
            img = ImageTk.PhotoImage(img)
            label = Label(fetch, image=img, width=100, height=100, bg = "white")
            canvas2.create_window(750, 160, window=label)

    uploadfinger = Button(fetch, text='Upload Finger', command=upload, font=('helvetica', 14, 'bold'))
    canvas2.create_window(750, 250, window=uploadfinger)



    # def scorecheck(img1, img2):
    #     # Open the two images
    #
    #     img_1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    #     img_2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
    #
    #     # Create an instance of the ORB feature detector
    #     orb = cv2.ORB_create()
    #
    #     # Detect keypoints and compute descriptors for each fingerprint image
    #     kp1, des1 = orb.detectAndCompute(img_1, None)
    #     kp2, des2 = orb.detectAndCompute(img_2, None)
    #
    #     # Create a Brute-Force Matcher object
    #     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    #
    #     # Match the descriptors of the two fingerprint images
    #     matches = bf.match(des1, des2)
    #
    #     # Sort the matches by their distance
    #     matches = sorted(matches, key=lambda x: x.distance)
    #
    #     # Calculate the similarity score
    #     score = sum([match.distance for match in matches]) / len(matches)
    #     return score
    def scorecheck():
        def segmentation(original_img, block_size=15):

            shp = original_img.shape
            segmentation_mask = np.ones(shp)
            global_threshold = np.var(original_img, axis=None) * 0.1
            row, col = original_img.shape[0], original_img.shape[1]
            i = 0
            j = 0
            while i < row:
                while j < col:
                    a = i + block_size
                    b = j + block_size
                    y = min(col, b)
                    x = min(row, a)
                    local_grayscale_variance = np.var(original_img[i: x, j: y])
                    if local_grayscale_variance <= global_threshold:
                        segmentation_mask[i: x, j: y] = 0
                    j += block_size
                i += block_size
            return segmentation_mask
            # print(original_img.shape[0])
            # print(original_img.shape[1])
            # print(global_threshold)

        def erosion(img, kernel):
            ero = cv2.erode(img, kernel, iterations=1)
            return ero

        def dilation(img, kernel):
            dil = cv2.dilate(img, kernel, iterations=1)
            return dil

        def seg_masking(original_img, segmentation_mask, block_size=15):
            # Apply Segmentation mask
            segmented_image = original_img.copy()
            # Removing unnecessary noise in the image
            doub = 2 * block_size
            kernel_open_close = cv2.getStructuringElement(cv2.MORPH_RECT, (doub, doub))
            # segmentation_mask = cv2.morphologyEx(segmentation_mask, cv2.MORPH_CLOSE, kernel_open_close)
            # segmentation_mask = cv2.morphologyEx(segmentation_mask, cv2.MORPH_OPEN, kernel_open_close)
            # Opening is the operation of erosion followed by dilation to remove noise
            segmentation_mask = erosion(segmentation_mask, kernel_open_close)
            segmentation_mask = dilation(segmentation_mask, kernel_open_close)
            # Closing Dilation is the operation of followed by Erosion to remove noise
            segmentation_mask = dilation(segmentation_mask, kernel_open_close)
            segmentation_mask = erosion(segmentation_mask, kernel_open_close)
            # print(segmented_image)
            row, col = segmentation_mask.shape[0], segmentation_mask.shape[1]
            for i in range(row):
                for j in range(col):
                    if segmentation_mask[i][j] == 0:
                        segmented_image[i][j] = 255

            return segmented_image

        def normalization(segmented_image):
            desired_mean = 128.0
            desired_variance = 7500.0
            current_variance, current_mean = np.var(segmented_image), np.mean(segmented_image)
            row, col = segmented_image.shape[0], segmented_image.shape[1]
            normalized_image = np.empty([row, col], dtype=float)
            for i in range(row):
                for j in range(col):
                    aux = (math.sqrt(
                        math.pow(segmented_image[i][j] - current_mean, 2) * (desired_variance / current_variance)))
                    if segmented_image[i][j] > current_mean:
                        normalized_image[i][j] = desired_mean + aux
                    else:
                        normalized_image[i][j] = desired_mean - aux
            return normalized_image

        def crop_image(normalized_image):
            im = Image.open(normalized_image)
            left = 20
            top = 10
            right = 280
            bottom = 380
            cropped_image = im.crop((left, top, right, bottom))
            return cropped_image

        def enhancement(cropped_image):
            enhanced_image = fingerprint_enhancer.enhance_Fingerprint(cropped_image)
            return enhanced_image

        def thinning(enhanced_image):
            thinned_image = np.where(skeletonize(enhanced_image / 255), 0.0, 1.0)
            return thinned_image

        def get_line_ends(i, j, W, tangent):
            temp = W / 2

            if -1 <= tangent and tangent <= 1:
                start = (int((temp) * tangent + j + temp), i)
                end = (int((temp) * tangent + j + temp), i + W)
            else:
                start = (j + math.floor(temp), int(i + temp + W / (2 * tangent)))
                end = (j - math.floor(temp), int(i + temp - W / (2 * tangent)))
            return (start, end)

        def ridge_orientation_field(original_img, normalized_image, block_size=15):
            scale, delta = 1, 0
            grad_x = cv2.Sobel(normalized_image / 255, cv2.CV_64F, 0, 1, ksize=3, scale=scale, delta=delta,
                               borderType=cv2.BORDER_DEFAULT)
            grad_y = cv2.Sobel(normalized_image / 255, cv2.CV_64F, 1, 0, ksize=3, scale=scale, delta=delta,
                               borderType=cv2.BORDER_DEFAULT)
            local_directions_x = np.zeros(original_img.shape)
            local_directions_y = local_directions_x
            row, col = original_img.shape[0], original_img.shape[1]
            for i in range(0, row, 1):
                for j in range(0, col, 1):
                    temp = block_size // 2
                    start_j = max(0, j - temp)
                    end_j = min(j + temp, col)
                    end_i = min(i + temp, row)
                    start_i = max(0, i - temp)
                    y = grad_y[start_i: end_i, start_j: end_j]
                    x = grad_x[start_i: end_i, start_j: end_j]
                    G_a = x ** 2 - y ** 2
                    local_directions_y[i, j] = np.sum(G_a)
                    G_b = 2 * x * y
                    local_directions_x[i, j] = np.sum(G_b)

            siz = 2 * block_size + 1
            kernel_size = (siz, siz)
            gaussian_directions_x = cv2.GaussianBlur(local_directions_x, kernel_size, 1.0)
            gaussian_directions_y = cv2.GaussianBlur(local_directions_y, kernel_size, 1.0)

            orientation_map = 0.5 * (np.arctan2(gaussian_directions_x, gaussian_directions_y)) + 0.5 * np.pi

            orientation_image = cv2.cvtColor((normalized_image).astype(np.uint8), cv2.COLOR_GRAY2RGB)

            return orientation_image, orientation_map

        # Feature extraction using crossing number technique
        def crossing_number(i, j, img):
            if img[i, j] != 0.0:
                return 2.0
            else:
                row_a = [(-1, -1), (-1, 0), (-1, 1)]
                row_b = [(0, 1), (1, 1), (1, 0)]
                row_c = [(1, -1), (0, -1), (-1, -1)]
                offsets = row_a + row_b + row_c
                pixel_values = []
                for x, y in offsets:
                    pixel_values.append(img[i + x, j + y])
                a = 0
                sum_cn = 0.0
                while a < 8:
                    sum_cn += abs(pixel_values[a] - pixel_values[a + 1])
                    a += 1

                return sum_cn // 2

        # False minutiae removal close to the boundary case
        def minutiae_removal(original_img, thinned_image, block_size=15):
            segment_mask_min = np.ones(original_img.shape)
            global_greyscale_variance = np.var(thinned_image) * 0.1
            i, j = 0, 0
            row, col = original_img.shape[0], original_img.shape[1]
            while i < row:
                while j < col:
                    siz_a = i + block_size
                    end_i = min(row, siz_a)
                    siz_b = j + block_size
                    end_j = min(col, siz_b)
                    local_grayscale_variance = np.var(thinned_image[i: end_i, j: end_j])
                    test = lambda x: True if (local_grayscale_variance > global_greyscale_variance) else False
                    if test:
                        segment_mask_min[i: end_i, j: end_j] = 1
                    else:
                        segment_mask_min[i: end_i, j: end_j] = 0.0
                    j += block_size
                i += block_size

            return segment_mask_min

        # Removing outermost strip
        def remove_outer_strip(original_img, minutiae, segment_mask_min, block_size=15):

            i = 0
            j = 0
            row, col = original_img.shape[0], original_img.shape[1]

            while j < col:
                start = 0
                siz = j + block_size
                end_j = min(col, siz)
                segment_mask_min[start: block_size, j: end_j] = 0.0
                segment_mask_min[row - block_size:  row, j:end_j] = 0.0
                j += block_size

            while i < row:
                start = 0
                temp1 = i + block_size
                end_i = min(row, temp1)
                segment_mask_min[i: end_i, start: block_size] = 0.0
                segment_mask_min[i: end_i, col - block_size:  col] = 0.0
                i += block_size

            new_minutiae = {}
            neighbourhood = [(0, 1), (0, -1), (0, 0), (1, 0), (-1, 0)]
            for j in minutiae:
                x = j[0]
                y = j[1]

                to_append = False
                for i in range(5):
                    direction_x, direction_y = neighbourhood[i][0] * block_size, neighbourhood[i][1] * block_size
                    try:
                        var_x = x + direction_x
                        var_y = y + direction_y
                        if segment_mask_min[var_x, var_y] == 0.0:
                            to_append = True
                            break
                    except IndexError:
                        to_append = True
                        break
                if to_append == False:
                    new_minutiae[(x, y)] = minutiae[(x, y)]

            return new_minutiae

        # Removal of cluster
        def Remove_cluster(minutiae, block_size=15):
            minutiae_list = list(minutiae.items())
            dist_thresh = block_size / 2
            cluster_found = False
            cluster_list = set()
            i = 1
            while i < len(minutiae_list):
                j = 0
                while j < i:
                    (x2, y2), (_, _) = minutiae_list[j]
                    aux1 = 0
                    (x1, y1), (_, _) = minutiae_list[i]
                    if distance.euclidean((x1, y1), (x2, y2)) <= dist_thresh:
                        cluster_list.add((x1, y1))
                        cluster_list.add((x2, y2))
                        cluster_found = True
                    j += 1
                i += 1

            if cluster_found == False:
                return False, minutiae
            j = 0
            while j < 10:
                i = 0
                while i < len(minutiae_list):
                    if (x1, y1) not in cluster_list:
                        for (x2, y2) in cluster_list:
                            aux2 = 0
                            (x1, y1), _ = minutiae_list[i]
                            if distance.euclidean((x1, y1), (x2, y2)) <= dist_thresh:
                                cluster_list.add((x1, y1))
                    i += 1
                j += 1

            for (x1, y1) in cluster_list:
                del minutiae[(x1, y1)]

            return True, minutiae

        def fingerprint_recognition(path_fp_img):
            original_img = cv2.imread(path_fp_img, cv2.IMREAD_GRAYSCALE)
            segmentation_mask = segmentation(original_img)
            block_size = 15
            # cv2.imshow("seg_mask", segmentation_mask)
            # cv2.waitKey(0)
            segmented_image = seg_masking(original_img, segmentation_mask)
            # cv2.imshow("seg_image", segmented_image)
            # cv2.waitKey(0)
            normalized_image = normalization(segmented_image)
            # cv2.imshow("norm_image", normalized_image)
            # cv2.waitKey(0)
            enhanced_image = enhancement(normalized_image)
            # cv2.imshow("enh_image", enhanced_image)
            # cv2.waitKey(0)
            thinned_image = thinning(enhanced_image)
            # cv2.imshow("thin_image", thinned_image)
            # cv2.waitKey(0)
            orientation, map = ridge_orientation_field(original_img, normalized_image)
            # cv2.imshow("orient_imag",orientation)
            # cv2.waitKey(0)

            minutiae = {}
            minutiae_img = cv2.cvtColor((255 * thinned_image).astype(np.uint8), cv2.COLOR_GRAY2RGB)
            row, col = original_img.shape[0], original_img.shape[1]
            i = 1
            while i < row - 1:
                j = 1
                while j < col - 1:
                    current_cn = crossing_number(i, j, thinned_image)
                    if current_cn == 1:
                        minutiae[(i, j)] = (current_cn, map[i, j])
                    elif current_cn == 3:
                        minutiae[(i, j)] = (current_cn, map[i, j])
                    j += 1
                i += 1

            segment_mask_min = minutiae_removal(original_img, thinned_image)
            # cv2.imshow("minuate_removal",segment_mask_min)
            # cv2.waitKey(0)

            doub = 2 * block_size
            kernel_open_close = cv2.getStructuringElement(cv2.MORPH_RECT, (doub, doub))
            segment_mask_min = erosion(segment_mask_min, kernel_open_close)
            segment_mask_min = dilation(segment_mask_min, kernel_open_close)
            segment_mask_min = dilation(segment_mask_min, kernel_open_close)
            segment_mask_min = erosion(segment_mask_min, kernel_open_close)

            new_minutiae = remove_outer_strip(original_img, minutiae, segment_mask_min)
            # print(new_minutiae)

            cluster_remain = True
            while cluster_remain:
                cluster_remain, new_minutiae = Remove_cluster(new_minutiae)
            # Draw minutiae on image
            for (x, y) in new_minutiae:
                c_n, _ = new_minutiae[(x, y)]
                # if ridge end color pink them
                temp = [1, 3]
                if c_n == temp[0]:
                    cv2.circle(minutiae_img, (y, x), radius=3, color=(255, 0, 255), thickness=2)
                # if ridge bifurication color green them
                if c_n == temp[1]:
                    cv2.circle(minutiae_img, (y, x), radius=3, color=(0, 255, 0), thickness=2)
            # cv2.imshow("minutiae_cluster_rem",minutiae_img)
            # cv2.waitKey(0)
            return minutiae_img, new_minutiae

        def round5(x, base=5):
            return base * round(x / base)

        def alignment_using_hough_transform(first, second, block_size=15):
            # Generalized Hough Transform
            # It is assumed both fingerprint have same size
            accumulator = dict()

            for (x_first, y_first) in second.keys():
                (_, theta_t) = second[(x_first, y_first)]
                for (x_second, y_second) in first.keys():
                    (_, theta_q) = first[(x_second, y_second)]
                    d_theta = theta_t - theta_q
                    d_theta = min(d_theta, 2 * np.pi - d_theta)
                    cos_dtheta, sin_dtheta = math.cos(d_theta), math.sin(d_theta)
                    d_x = x_first - x_second * cos_dtheta + y_second * sin_dtheta
                    d_y = y_first - x_second * sin_dtheta - y_second * cos_dtheta
                    lis = []
                    lis.append(round5(180 * d_theta / np.pi, 5))
                    lis.append(round5(d_x, block_size // 4))
                    lis.append(round5(d_y, block_size // 4))
                    conf = tuple(lis)
                    if accumulator.get(conf):
                        accumulator[conf] = accumulator[conf] + 1

                    else:
                        accumulator[conf] = 1
            temp = max(accumulator, key=accumulator.get)
            theta = temp[0]
            x = temp[1]
            y = temp[2]

            return np.pi * theta / 180, x, y

        def pairing(first, second, transform_config, block_size=15):
            # Calculate which minutiae match to which minutiae in other fingerprint
            # Looser condition for matched minutiae than that during alignment
            flag_first, flag_second = np.zeros(len(first), ), np.zeros(len(second), )
            angle_thresh = 10 * np.pi / 180
            distance_thresh = block_size / 2
            count_matched = 0
            matched_minutiae = []

            i = 0
            ht_theta, _, _ = transform_config
            _, ht_x, _ = transform_config
            _, _, ht_y = transform_config
            for (x_first, y_first) in second.keys():
                j = 0
                (_, theta_t) = second[(x_first, y_first)]
                for (x_second, y_second) in first.keys():
                    (_, theta_q) = first[(x_second, y_second)]
                    d_theta = theta_t - theta_q - ht_theta
                    d_theta = min(d_theta, 2 * np.pi - d_theta)
                    cos_theta, sin_theta = math.cos(ht_theta), math.sin(ht_theta)
                    x_y_first = [x_first, y_first]
                    x_y_second = [- x_second * cos_theta + y_second * sin_theta - ht_x,
                                  -x_second * sin_theta - y_second * cos_theta - ht_y]
                    d_x = x_y_first[0] + x_y_second[0]
                    d_y = x_y_first[1] + x_y_second[1]
                    aux1 = distance.euclidean((0, 0,), (d_x, d_y)) <= distance_thresh
                    aux2 = abs(d_theta) <= abs(angle_thresh)
                    if flag_second[i] == 0.0 and flag_first[j] == 0.0 and aux1 and aux2:
                        flag_second[i] = 1.0
                        count_matched = count_matched + 1
                        matched_minutiae.append(((x_first, y_first), (x_second, y_second)))
                    j = j + 1
                i = i + 1

            return count_matched, i

        def interactive_display(window_label, image):
            cv2.imshow(window_label, image)
            while True:
                key = cv2.waitKey(0) & 0xFF
                # wait for enter key to exit
                if key == 13:
                    cv2.destroyAllWindows()
                    break
            cv2.destroyAllWindows()

        def match(first, second, img_1, img_2):
            matches, _ = pairing(first, second, alignment_using_hough_transform(first, second))
            len1 = len(first)
            len2 = len(second)
            #         print("Fingerprint 1 has {} minutiae points".format(len1))
            #         print("Fingerprint 2 has {} minutiae points".format(len2))
            #         print("{} out of those match in between them".format(matches))
            #         print("{:.2f} percentage of minutiae matched".format(100*matches/min(len1, len2)))
            #         interactive_display("Fingerprint 1 Minutiae", img_1)
            #         interactive_display("Fingerprint 2 Minutiae", img_2)
            var = 100 * matches / min(len1, len2)
            return var

        path_d = os.getcwd() + "/Download/"
        path_u = os.getcwd() + "/Upload/"
        path_fp_img_1 = path_u +"101.bmp"
        path_fp_img_2 = path_d +"101_1.bmp"
        path_fp_img_3 = path_d +"101_2.bmp"
        path_fp_img_4 = path_d +"101_3.bmp"
        path_fp_img_5 = path_d +"101_4.bmp"
        img_1, minuate_1 = fingerprint_recognition(path_fp_img_1)
        img_2, minuate_2 = fingerprint_recognition(path_fp_img_2)
        img_3, minuate_3 = fingerprint_recognition(path_fp_img_3)
        img_4, minuate_4 = fingerprint_recognition(path_fp_img_4)
        img_5, minuate_5 = fingerprint_recognition(path_fp_img_5)
        var1 = match(minuate_1, minuate_2, img_1, img_2)
        var2 = match(minuate_1, minuate_3, img_1, img_3)
        var3 = match(minuate_1, minuate_4, img_1, img_4)
        var4 = match(minuate_1, minuate_5, img_1, img_5)
        final_score = (var1 + var2 + var3 + var4) / 4
        return final_score

    def submitfinger():
        global img
        newpath = r'C:\Users\ankit\PycharmProjects\SpeedyLine\Download'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        st = 1
        for i in range(st, 100):
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
                mycursor.execute("SELECT finger1 FROM people WHERE aadhar='%s'" %i)
                myresult1 = mycursor.fetchone()
                img = Image.open(io.BytesIO(myresult1[0]))
                img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Download\\101_1.bmp', 'BMP')
                mycursor.execute("SELECT finger2 FROM people WHERE aadhar='%s'" % i)
                myresult2 = mycursor.fetchone()
                img = Image.open(io.BytesIO(myresult2[0]))
                img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Download\\101_2.bmp', 'BMP')
                mycursor.execute("SELECT finger3 FROM people WHERE aadhar='%s'" % i)
                myresult3 = mycursor.fetchone()
                img = Image.open(io.BytesIO(myresult3[0]))
                img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Download\\101_3.bmp', 'BMP')
                mycursor.execute("SELECT finger4 FROM people WHERE aadhar='%s'" % i)
                myresult4 = mycursor.fetchone()
                img = Image.open(io.BytesIO(myresult4[0]))
                img.save('C:\\Users\\ankit\\PycharmProjects\\SpeedyLine\\Download\\101_4.bmp', 'BMP')
                score = scorecheck()
                print(score)
                if (score>=30.0):
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

                    shutil.rmtree(newpath)

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
