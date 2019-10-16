gia={"HP":600,"DELL":650,"MACBOOK":12000,"ASUS":400,"ACER":350,"TOSHIBA":600,"FUJITSU":900,"ALIENWARE":1000}
hangmay=input("Nhap hang may:")
soluong=int(input("Nhap so luong:"))
a=gia.get(hangmay)
tong=a*soluong
print(tong)
