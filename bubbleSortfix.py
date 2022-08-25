n = int(input("Nhap so luong phan tu(bang so)"))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def DSso():
    for i in range(len(a)):
        b = i
        for j in range(i + 1, len(a)):
            if a[j] < a[b]:
                b = j
        a[i], a[b] = a[b], a[i]
    print(a)


DSso()
