file_ob=open("gowri.txt","a")
print("file created")
file_ob.write("hello this is gowri\n.......villa\n s180311")
file_ob.close()
print("end of the file")
#read
file_ob=open("gowri.txt","r")
print("file reading")
text=file_ob.read()
print(text)
a=file_ob.tell()
print(a)
file_ob.seek(10)
b=file_ob.tell()
print(b)
file_ob.close()
