import setFace

filename = input("Enter a fileName: ")
listid = input("Enter a list ID: ")
active = input("IS active 1 for true 2 for false: ")

try:
    setFace.setface(listid,filename,active)
    print("Saved")
except:
    print("Image save error")
finally:
    print("Done!")