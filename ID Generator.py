from time import sleep 

import random

import os 

def Check():

    path = "Dir Path"                         #Directory Path 

    if os.path.isdir('Dir Path') == True:      #Check if Path is correct or No 

        print("Available Directory")

    else:

        try:

            os.mkdir(path)

            sleep(2)

        except OSError:

            print ("Creation of the directory %s failed" % path)

            sleep(2)

        else:

            print ("Successfully created the directory %s " % path)

            sleep(2)

    if os.path.isfile('add your file path'):       #Check if file path Exist or No 

        print('Available File')                                       
  
    else:                                                                #Creating txt File into custom path 

        print("unavailable File We Should Create One")

        sleep(1)

        print("Creating ... ")

        sleep(2)

        f = open("","x")                #Path of file

        print("IDHex.txt Is Available Now ")

Check()

def Generator():

    f = open("File Full Path","a")

    Decimal = []

    number_id = int(input(" Number of IDs to generate : \n" ))

    for flist in range(number_id):                                        #Fill List of Decimal Codes 
        
        n = random.randint(1000000,9999999)

        Decimal.append(n)

        Decimal = list(dict.fromkeys(Decimal))

    print(Decimal)

    for i in range (len(Decimal)):                                       #Put ID in File 

        x = Decimal[i]

        x = hex(x)[2:]                                                   #Convert Decimal To Hex without 0x

        x = str(x)

        f.write(x)

        f.write("\n")
          
    f.close()



Generator()
