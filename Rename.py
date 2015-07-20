__author__ = 'Pri'

import os


def rename_filename():
    global file_name, file_name, path
   # path = r"E:\Python Projects\prank\prank"
    file_list = os.listdir(r"C:\Users\Pri\Desktop\CD 1 - Latest DJ-Mixes (Jan-February 2015) [DJMaza ExclusivE]")
    print (file_list)
    saved_path = os.getcwd()

    print(saved_path)
    os.chdir(r"C:\Users\Pri\Desktop\CD 1 - Latest DJ-Mixes (Jan-February 2015) [DJMaza ExclusivE]")

    for file_name in file_list:
        print("Old Name - " + file_name)
        # print("New Name - " + (file_name, file_name.translate(None, "0123456789")))
        # file_name.replace("D","")
        # print(file_name.strip('D'))
        os.rename(file_name, file_name.translate(None, "DMaza incfo www[]IL."))

    os.chdir(saved_path)


rename_filename()


# r stands for raw path take as it
