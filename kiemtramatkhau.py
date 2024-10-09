def tieude(): #hàm tiêu đề 
    print("Chương trình ứng dụng của nhóm 7 - DH23HM")

i = 0 #khời tạo biến đếm
while True: #tạo vòng lặp vô hạn
    mk_nhap = input("Nhập mật khẩu: ") #gán input cho mk_nhap
    if mk_nhap == "1234": #kiểm tra mk_nhap
        print(f"đăng nhập thành công, mật khẩu là {mk_nhap}") #nếu mk đúng thì thoát vòng lặp in ra mk_nhap
        break #thoát vòng lặp
    else:
        i += 1 #tăng biến đếm
        sai = f"còn {3-i} lần nhập," #biến đếm số lần còn lại
        if i < 3: #kiểm tra đã sai 3 lần hay chưa
            print(sai,"vui lòng nhập lại")
        else:
            print(sai,"đột ngột vi phạm, thoát chương trình") #sai 3 lần thoát chương trình
            tieude()
            exit() #thoát chương trình
            
print("tiếp tục code")
tieude()
