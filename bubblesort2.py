def sap_xep_ds_tang(a):
   for i in range(len(a)):
       b = i
       for j in range(i + 1, len(a)):
           if a[j] < a[b]:
               b = j
       a[i], a[b] = a[b], a[i]
  
danhSach = input().split()
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   try:
       a = list(map(float, danhSach))
       sap_xep_ds_tang(a)
       print(*a)

   except:
       print("Nhap cac phan tu la so thuc!")
