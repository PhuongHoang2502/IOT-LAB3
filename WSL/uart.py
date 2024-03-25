import serial.tools.list_ports


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
    # return commPort
    # return "COM4"
    return "/dev/pts/9"


if getPort() != "None":
    # ser = serial.Serial(port=getPort(), baudrate=115200)
    ser = serial.Serial("/dev/pts/9")
    print(ser)


def processData(client, data):
    data = data.replace("(", "")
    data = data.replace(")", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        client.publish("cambien1", splitData[2])
    elif splitData[1] == "L":
        client.publish("cambien2", splitData[2])
    elif splitData[1] == "H":
        client.publish("cambien3", splitData[2])


mess = ""


def readSerial(client):
    bytesToRead = ser.inWaiting()
    # print(bytesToRead)
    if bytesToRead > 0:
        global mess
        new_mess = ser.read(bytesToRead).decode("UTF-8")
        # mess = mess + ser.read(bytesToRead).decode("UTF-8")
        mess = mess + new_mess
        # print(mess)
        # new_mess = ser.read(bytesToRead).decode("UTF-8")
        print(new_mess)
        while ("(" in mess) and (")" in mess):
            start = mess.find("(")
            end = mess.find(")")
            processData(client, mess[start : end + 1])
            if end == len(mess):
                mess = ""
            else:
                mess = mess[end + 1 :]


def writeData(data):
    ser.write(str(data).encode())


# https://unix.stackexchange.com/questions/711700/intercept-communications-on-physical-serial-port-using-socat
# https://gist.github.com/krzyklo/e60793b27400be7a330042aa6bdf388a
