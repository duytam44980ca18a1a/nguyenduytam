"""
Author: Nguyen Duy Tam
Date: 26/11/2000

Problem:
   How does a Python programmer round a float value to the nearest int value?
Solution:
hàm int chuyển đổi float thành int bằng cách cắt ngắn, không phải bằng cách làm tròn thành
số nguyên gần nhất. Việc cắt bớt chỉ đơn giản là cắt bỏ phần phân số của con số. Vòng
hàm làm tròn một float đến int gần nhất như trong ví dụ tiếp theo:
>>> int(6.75)
6
>>> round(6.75)
7

    ....
"""