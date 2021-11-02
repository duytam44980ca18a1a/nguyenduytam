def Cau1():
    def snt(n):
        """ check so nguyen to """
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f

    def in_snt(a=30, b=100):
        print("Danh sach so nguuyen to")
        """ Kiem tra so nguyen to trong khoang a va b"""
        for i in range(a, b + 1):
            if snt(i):
                print(i, end="  ")
                print()
    # thuc thi tim so ngyuen to
    in_snt(30, 100)

    if __name__ == "__name__":
     Cau1()
