from tkinter import *
import socket
import hashlib
import threading
import getpass


mainframe = Tk()
mainframe_weight = "475"
mainframe_height = "250"
mainframe.geometry(mainframe_weight + "x" + mainframe_height)
mainframe.resizable(0, 0)
headline = "arial 20 bold"
mainframe.overrideredirect(0)
backgroundcolor = "#212224"
addingbackgroundcolor = "#313236"
foregroundcolor = "#bababf"
errorcolor = "#ad3e3e"
buttonbarfont = "Arial 12 bold"
headlinelabelfont = "Arial 14 bold"
mainframe.configure(bg=backgroundcolor)
standardlabelfont = "Arial 12"

Login = Frame(mainframe, width=1000, height=800, bg=backgroundcolor, bd=0)

autologin_path = "C:/Users/" + getpass.getuser() + "/AppData/Local/Temp/mym-autologin.txt"
userdata_path = "C:/Users/" + getpass.getuser() + "/AppData/Local/Temp/mym-user_datas.txt"


def login_thread():
    loginthread = threading.Thread(target=login)
    loginthread.start()


Label(mainframe, text="Login - MYM", font=headline, bg=backgroundcolor, fg=foregroundcolor).place(x=153, y=40)
Label(mainframe, text="Benutzername", font="Arial 10 bold", bg=backgroundcolor, fg=foregroundcolor).place(x=20, y=100)
Label(mainframe, text="Passwort", font="Arial 10 bold", bg=backgroundcolor, fg=foregroundcolor).place(x=55, y=150)
username_entry = Entry(mainframe, font="Arial 10", fg=foregroundcolor, bg=backgroundcolor)
username_entry.place(x=150, y=105, height=15, width=300)
password_entry = Entry(mainframe, font="Arial 10", show="*", fg=foregroundcolor, bg=backgroundcolor)
password_entry.place(x=150, y=155, height=15, width=300)
save_logindatavar = StringVar()
save_logindata = Checkbutton(mainframe, text="Anmeldedaten speichern", variable=save_logindatavar, bg=backgroundcolor,
                             fg=foregroundcolor, onvalue="save", offvalue="dont_save")
save_logindata.deselect()
save_logindata.place(x=145, y=185, height=15)
Button(mainframe, text="anmelden", command=login_thread, font="Arial 10 bold", bg=backgroundcolor, fg=foregroundcolor,
       borderwidth=0).place(x=375, y=215)
Button(mainframe, text="abbrechen", command=mainframe.destroy, font="Arial 10 bold", bg=backgroundcolor, borderwidth=0,
       fg=foregroundcolor).place(x=275, y=215)


def hide_screen():
    mainframe.overrideredirect(0)
    mainframe.iconify()


def screen_appear(event):
    mainframe.overrideredirect(1)


def titlebar_login():
    def callback(event):
        mainframe.geometry("+{0}+{1}".format(event.x_root, event.y_root))

    titlebar = Frame(mainframe, bg="yellow", relief=SUNKEN, bd=0)
    titlebar.place(width=475, height=30)
    titlebartext = Label(titlebar, text="Login - MYM", font="Times 8 bold", bg=backgroundcolor, fg=foregroundcolor)
    titlebartext.place(x=10, y=5)
    titlebarclose = Button(titlebar, text="x", bg=backgroundcolor, highlightcolor="white",
                           command=lambda: [mainframe.destroy()],
                           fg=foregroundcolor, bd=0)
    titlebarclose.place(x=458, y=0)
    titlebarminimize = Button(titlebar, bg=backgroundcolor, text="-", highlightcolor="white", command=hide_screen,
                              fg=foregroundcolor, bd=0)
    titlebarminimize.place(x=443, y=0)
    titlebar.bind("<B1-Motion>", callback)
    titlebar.bind("<Map>", screen_appear)


def login():
    username = username_entry.get()
    password = password_entry.get()
    usernamehash = hashlib.sha512()
    usernamehash.update(username.encode("UTF-8"))
    usernamehash = usernamehash.hexdigest()
    passwordhash = hashlib.sha512()
    passwordhash.update(password.encode("UTF-8"))
    passwordhash = passwordhash.hexdigest()
    save_loginstatus = save_logindatavar.get()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    login_host = "45.10.24.152"
    login_port = 61483

    try:
        try:
            s.connect((login_host, login_port))
        except:
            no_connection = Label(text="Verbindung zum Server fehlgeschlagen", font="Arial 10 bold", bg=backgroundcolor,
                                  fg=errorcolor)
            no_connection.place(x=10, y=220)
            s.close()

        c_messg = usernamehash
        s.send(c_messg.encode())
        s_messg = s.recv(1024)

        if s_messg != "no file":
            pass
            if passwordhash == s_messg.decode():
                if save_loginstatus == "save":
                    save_login = open(autologin_path, "w+")
                    save_login.write(usernamehash + "\n" + passwordhash)
                    save_login.close()
                login_success()
            else:
                wrong_login = Label(text="Benutzername oder Passwort ist falsch", font="Arial 10 bold",
                                    bg=backgroundcolor,
                                    fg=errorcolor)
                wrong_login.place(x=10, y=220)
        else:
            wrong_login = Label(text="Benutzername oder Passwort ist falsch", font="Arial 10 bold", bg=backgroundcolor,
                                fg=errorcolor)
            wrong_login.place(x=10, y=220)
    except:
        no_connection = Label(text="Verbindung zum Server fehlgeschlagen", font="Arial 10 bold", bg=backgroundcolor,
                              fg=errorcolor)
        no_connection.place(x=10, y=220)


def login_success():
    print("login success")

mainframe.mainloop()
