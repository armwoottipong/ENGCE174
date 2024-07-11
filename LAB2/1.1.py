#รับ input
n = int(input("กรอกเลข : "))

for i in range (1, n+1):
    print("* " * i)
print("--------------------------------------------")
for i in range (n, 0 , -1): 
    print("* " * i) 
print("--------------------------------------------")
for i in range(1, n+1): #เริ่ม 1 ถึง n และ + 1
    spaces = ' ' * (n - i)
    star = "* " * i
    print(spaces + star)
print("--------------------------------------------")
for i in range (n, 0 , -1): # เริ่มตั้งแต่ n ถึง 0 โดยเพิ่มทีละ -1 
    spaces = ' ' * (n - i)
    star = "* " * i
    print(spaces + star)
print("--------------------------------------------")   
for i in range(1, n+1): #เริ่ม 1 ถึง n และ + 1
    spaces = ' ' * (n - i)
    star = "*" * i
    print(spaces + star)
print("--------------------------------------------")