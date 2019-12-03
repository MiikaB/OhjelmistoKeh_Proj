import subprocess
from pyngrok import ngrok

feed = 0

#Command to open putty through powershell and set connetion address with credentials
tunnel = ("powershell putty.exe ""mariadb.haaga-helia.fi"" -l <USERNAME> -pw <PASSWORD>")

while True :
    try:
        print(":::MariaDB Tunnel Script:::")
        print("::1:: Establish tunnel\n::2:: Terminate tunnel\n::3:: Quit\n")
        feed = input("Select an action: ")
        if int(feed) == 1:
            print("Attempting to login..")
            try:

                #Command to open tunnel with subprocess -module and giving previosly set credentials
                pid = subprocess.Popen(tunnel).pid

                #Command to run ngrok -module to create sertificate for localhost in order to access https
                localhost = ngrok.connect(port=8080, proto="http")

                #Manually inserting string s after http, for easy copy-paste and printing it to console
                localhostsecure = localhost[:4] + "s" + localhost[4:]
            
                print("Success!\nLocalhost http running at: " + localhost + "/recipebook_miika/recipes" + "\nLocalhost https running at: " + localhostsecure + "/recipebook_miika/recipes")
            except Exception:
                print("Error happened during login :(")
        elif int(feed) == 2:

            #Taskkill to stop putty process in order to kill the tunnel connection
            try:
                subprocess.call(["taskkill","/F","/IM","putty.exe"])
                print("MariaDB Tunnel succesfully terminated")
                print("Ngrok localhost terminates automatically when script is closed")
            except Exception:
                print("Error happened during tunnel closing")
        elif int(feed) == 3:

            #Breaking loop and ending the script with user feed 3
            break

        #Incorrect feed catch
        elif int(feed) != 1 & int(feed) != 2 & int(feed) != 3:
            print("Invalid action")
        elif str(feed) is str:
            print("Invalid action")

    #Error catching
    except TypeError:
        print("Check input!")
    except Exception:
        print("Something went wrong!")