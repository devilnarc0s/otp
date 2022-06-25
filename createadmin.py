import sqlite3
from dbase import *

def main():
    # adminid = input("Enter telegram userid to be made admin:")
    # check = check_admin(adminid)
    # if check == True:
    #     print("Admin already exists")
    # else:
    #     try:
    #         create_admin(adminid)
    #         create_user_lifetime(adminid)
    #     except:
    #         print('something went wrong')
    #     else:
    #         print('Admin created...')
    #        create_admin(1631961416)
    james = fetch_UserData_table()
    print(james)
if __name__ == '__main__':
    main()