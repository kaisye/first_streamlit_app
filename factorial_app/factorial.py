def fact(n: int) -> int:
    """Tính giai thừa của số nguyên không âm n.

    Giai thừa được định nghĩa như sau:
    - 0! = 1
    - 1! = 1
    - n! = n x (n - 1) x ... x 2 x 1

    Hàm này dùng vòng lặp thay vì đệ quy để tránh lỗi vượt giới hạn đệ quy
    khi người dùng nhập số lớn.
    """
    # Không cho phép số âm vì giai thừa trong phạm vi cơ bản chỉ áp dụng
    # cho số nguyên không âm.
    if n < 0:
        raise ValueError("n phải là số nguyên không âm")

    # 0! và 1! đều bằng 1, đây là quy ước toán học.
    result = 1

    # Nhân lần lượt các số từ 2 đến n để tạo ra n!.
    for value in range(2, n + 1):
        result *= value

    return result
