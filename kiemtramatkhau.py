i = 0 #khời tạo biến đếm
while True: #tạo vòng lặp vô hạn
    mk_nhap = input("Nhập mật khẩu: ") #gán input cho mk_nhap
    if mk_nhap == "1234": #kiểm tra mk_nhap
        print(f"đăng nhập thành công, mật khẩu là {mk_nhap}")
        break #thoát vòng lặp
    else:
        i += 1 #tăng biến đếm
        sai = f"còn {3-i} lần nhập,"
        if i < 3: #kiểm tra đã sai 3 lần hay chưa
            print(sai,"vui lòng nhập lại")
        else:
            print(sai,"đột ngột vi phạm, thoát chương trình")
            exit() #thoát chương trình
            
print("tiếp tục code")
