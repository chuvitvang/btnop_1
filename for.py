tieude ="Chương trình ứng dụng của nhóm 7 - DH23HM"

for i in range(3):
    mk_nhap = input("Nhập mật khẩu: ")
    if  i < 2 and mk_nhap != "1234":
        print(f"còn {-(i-2)} lần nhập,vui lòng nhập lại")
    else:
        if mk_nhap == "1234":
            print(f"Đăng nhập thành công, mật khẩu là: {mk_nhap}\n{tieude}\ntiếp tục code")
            break
        else:
            print("đột ngột vi phạm,thoát chương trình",f"\n{tieude}"),exit()
