i = 0
while True:
    mk_nhap = input("Nhập mật khẩu: ")
    if mk_nhap == "1234":
        print(f"đăng nhập thành công, mật khẩu là {mk_nhap}")
        break
    else:
        i += 1
        sai = f"còn {3-i} lần nhập,"
        if i == 3:
            print(sai,"đột ngột vi phạm, thoát chương trình")
            exit()
        else:
            print(sai,"vui lòng nhập lại")

print("tiếp tục code")