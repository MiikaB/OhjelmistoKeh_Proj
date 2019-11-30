import subprocess

feed = 0
cmd = ("powershell putty.exe ""mariadb.haaga-helia.fi"" -l <USERNAME> -pw <PASSWORD>")


while feed != "exit" :
    try:
        print(":::MariaDB Tunnel Script:::")
        print("::1:: Establish tunnel\n::2:: Terminate tunnel\n::3:: Quit")
        feed = input("Select an action: ")
        if int(feed) == 1:
            print("Attempting to login..")
            try:
                pid = subprocess.Popen(cmd).pid
                print("Success! Tunnel established")
            except Exception:
                print("Error happened during login :(")
        elif int(feed) == 2:
            try:
                subprocess.call(["taskkill","/F","/IM","putty.exe"])
                print("MariaDB Tunnel succesfully terminated")
            except Exception:
                print("Error happened during tunnel closing")
        elif int(feed) == 3:
            print("Bye bye!")
            break
        elif int(feed) != 1 & int(feed) != 2 & int(feed) != 3:
            print("Invalid action")
    except TypeError:
        print("Check input!")
    except Exception:
        print("Something went wrong!")