import pymysql.cursors


# Function return a connection.
def getConnection():
    # You can change the connection arguments.
    connection = pymysql.connect(host='192.168.0.62',
                                 user='coby',
                                 password='PASSOWRD!!',
                                 db='face_info',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
