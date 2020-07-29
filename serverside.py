import socket
print("-----------------------------------------------------------------------------------------------------------------------")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "45.10.24.152"
port = 61483

serversocket.bind((host, port))
serversocket.listen(1)


while True:
    con, addr = serversocket.accept()
    print("Anmeldeversuch von", addr)
    c_data = con.recv(1024)
    print("Benutzernamehash vom Client:", c_data.decode())
    dc_data = c_data.decode()
    try:
        with open("login_datas/" + dc_data + ".txt") as check_data:
            x = check_data.read()
            con.send(bytes(str(x), "utf-8"))
            print("Passwordhash vom Server:", x)
            print("-----------------------------------------------------------------------------------------------------------------------")
    except socket.error:
        y = "no file"
        con.send(bytes(str(y), "utf-8"))
        print("Den Benutzernamehash ist kein Passwordhash zugeordnet")
        print("-----------------------------------------------------------------------------------------------------------------------")
