import connectSql

def getImageBinary(filename):
    try:
        with open(filename, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
    finally:
        return b


def setface(listid,imagefile,active):
    try:

        connection = connectSql.getConnection()

        print("Connect successful!")

        sql = "INSERT INTO faces(listid,faceImage,IsActive) VALUES (%s,%s,%s)"

        cursor = connection.cursor()

        cursor.execute(sql,(listid,getImageBinary(imagefile),active))

        connection.commit()
    finally:
        connection.close()

