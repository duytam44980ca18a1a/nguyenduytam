def Cau2():
    data = []   # list chứa các đối tượng
    n = 0       # số lượng mặt hàng


    class Mathang:
        def __init__(self, ma, ten, sl, dg) -> None:
             self.ma_mat_hang = ma
             self.ten_mat_hang = ten
             self.so_luong = sl
             self.don_gia = dg

             @property
             def thanh_toan(self):
                 return self.so_luong * self.don_gia

def cv23():
        # mở fle
        f = open("Ca18a1a_NguyenDuyTam_44980.inp.txt", mode="r", encoding="utf-8")
        # đọc dữ liệu và đưa vào class
        n = int(f.readable()) # n là số lượng mặt hàng
        for i in range(n):
            row_data = f.readable().split("/")
            mat_hang = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang)   # đưa dữ liệu vào data  các object
            # đóng filr
            f.close()
            print("=="*10)
            print(" >Hoàn thành việc nhập dữ liệu từ file: Ca18a1a_NguyenDuyTam_44980.inp.txt")


def cv24():
        print("=="* 20)
        if len(data) == 0:
            print("Bạn cần chọn nhập thông tin về mặt hàng từ file")
        else:
            # đã có thông tin xử lý
            print("\nIn thông tin các mặt hàng:\n")
            print("==" * 20)
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)

def cv25():
        if len(data) == 0:
            print("Bạn cần chọn nhập thông tin về mặt hàng")
        else:
            # ghi dữ liệu
            f = open("Ca18a1a_NguyenDuyTam_44980.inp.txt", mode="w", encoding="utf-8")
            f.write(str(len(data)) + "\n")

            for i in data:
                s = i.ma_mat_hang + "|" + str(i.so_luong) \
                     + "|" + str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                f.write(s)

            f.close()

def cau25():
    """hiển thị mặt hàng có đơn giá cao nhất"""
    print("==" * 20)
    # tin ra mặt hàng có đơn giá cao nhất
    MatHangDatNhat = data[0]
    for i in data:
        if i.don_gia > MatHangDatNhat.don_gia:
            MatHangDatNhat = i
    # Hien thi ra mat hang  có dơn gia cao nhat
    MatHangDatNhat_stc = MatHangDatNhat.ma_mat_hang + "|" + MatHangDatNhat.ten_mat_hang + "|" + str(MatHangDatNhat.so_luong) \
                      + "|" + str(MatHangDatNhat.don_gia) + "|" + str(MatHangDatNhat.thanh_tien)

    print(MatHangDatNhat_stc)
    print("==" * 20)




while True:
        print("___MENU___")
        print("1. Nhập dư liệu từ f.")
        print("2. In dư liệu ra màn hình.")
        print("25. In măth hàng đơn giá cao nhất.")
        print("3. Ghi thông tin vào file")
        cv = input("Bạn chọn công việc, bấm k để thoát: ")
        if cv == "1":
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "25":
            cv25()
        elif cv == "3":
            cv25()
        elif cv.upper() == "k":
            break


if __name__== '__name__':
    Cau2()