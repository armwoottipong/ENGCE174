n = int(input("กรอกเลข : "))
def loop(row, max_row):
    if row < max_row:
        print('* ' * (row + 1))  # พิมพ์ดอกจันทร์ '*' ตามจำนวนของ row + 1
        loop(row + 1, max_row)

# เรียกใช้งานฟังก์ชันเพื่อพิมพ์ดอกจันทร์ตามรูปแบบที่ต้องการ ( บรรทัด)
loop(0, n)
print("------------------------------------")
def loop(row, max_row):
    if row < max_row:
        print('* ' * (max_row - row))  # พิมพ์ดอกจันทร์ '*' ตามจำนวนของ max_row - row
        loop(row + 1, max_row)

# เรียกใช้งานฟังก์ชันเพื่อพิมพ์ดอกจันทร์ตามรูปแบบที่ต้องการ ( n บรรทัด)
loop(0, n)
print("------------------------------------")
def loop(row, max_row):
    if row < max_row:
        print(' ' * (max_row - row - 1) + '* ' * (row + 1))  # พิมพ์ดอกจันทร์ '*' ตามจำนวนของ row + 1
        loop(row + 1, max_row)

# เรียกใช้งานฟังก์ชันเพื่อพิมพ์ดอกจันทร์ตามรูปแบบที่ต้องการ ( n บรรทัด)
loop(0, n)
print("------------------------------------")
def loop(row, max_row):
    if row < max_row:
        print(' ' * row + '* ' * (max_row - row))  # พิมพ์ดอกจันทร์ '*' ตามจำนวนของ max_row - row
        loop(row + 1, max_row)

# เรียกใช้งานฟังก์ชันเพื่อพิมพ์ดอกจันทร์ตามรูปแบบที่ต้องการ ( n บรรทัด)
loop(0, n)
print("------------------------------------")
def loop(row, max_row):
    if row <= max_row:
        print('  ' * (max_row - row) + '* ' * row)
        loop(row + 1, max_row)

# เรียกใช้งานฟังก์ชันเพื่อพิมพ์ดอกจันทร์ตามรูปแบบที่ต้องการ ( n บรรทัด)
loop(0, n)
