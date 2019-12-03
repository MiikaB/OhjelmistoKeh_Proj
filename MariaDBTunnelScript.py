import subprocess
from pyngrok import ngrok

feed = 0
tunnel = ("powershell putty.exe -load ""mariadbtunnel"" -l <USERNAME> -pw <PASSWORD>")

while True :
    try:
        print(":::MariaDB Tunnel Script:::")
        print("::1:: Establish tunnel\n::2:: Terminate tunnel\n::3:: Quit\n")
        feed = input("Select an action: ")
        if int(feed) == 1:
            print("Attempting to login..")
            try:
                pid = subprocess.Popen(tunnel).pid
                localhost = ngrok.connect(port=8080, proto="http")
                localhostsecure = localhost[:4] + "s" + localhost[4:]
                print("Success!\nLocalhost http running at: " + localhost + "/recipebook_miika/recipes" + "\nLocalhost https running at: " + localhostsecure + "/recipebook_miika/recipes")
            except Exception:
                print("Error happened during login :(")
        elif int(feed) == 2:
            try:
                subprocess.call(["taskkill","/F","/IM","putty.exe"])
                print("MariaDB Tunnel succesfully terminated")
                print("Ngrok localhost terminates automatically when script is closed")
            except Exception:
                print("Error happened during tunnel closing")
        elif int(feed) == 3:
            break
        elif int(feed) != 1 & int(feed) != 2 & int(feed) != 3:
            print("Invalid action")
        elif str(feed) is str:
            print("Invalid action")
    except TypeError:
        print("Check input!")
    except Exception:
        print("Something went wrong!")