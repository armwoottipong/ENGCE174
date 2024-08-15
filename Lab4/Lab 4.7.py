set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4}

union_set = set1 | set2                     #รวมสมาชิกทั้งสองเซตเข้าด้วยกัน โดยไม่ซ้ำกัน
intersection_set = set1 & set2              #ค้นหาสมาชิกที่ซ้ำกันในทั้งสองเซต
difference_set = set1 - set2                #ค้นหาสมาชิกที่อยู่ใน set1 แต่ไม่อยู่ใน set2
symmetric_difference_set = set1 ^ set2      #ค้นหาสมาชิกที่อยู่ใน set1 หรือ set2 แต่ไม่ซ้ำกันในทั้งสองเซต

print("Union = ", union_set)                                # Output {1, 2, 3, 4}
print("Intersection = ",intersection_set)                   # Output {1, 2, 3, 4}
print("Difference = ",difference_set)                       # Output set()
print("Symmetric_difference = ",symmetric_difference_set)   # Output set()