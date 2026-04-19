def lcs(s1, s2):
    # ให้ s1 เป็นสตริงที่ยาวกว่าหรือเท่ากันเสมอ (เพื่อลดเวลา/พื้นที่ ในการทำรอบหลัง)
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    n, m = len(s1), len(s2)
    # กำหนดค่าสำหรับการทำ Rolling Hash (ใช้ 2 modulo พร้อมกัน เพื่อลดโอกาสเกิด Hash collision)
    base = 131
    mod1 = 10**9 + 7
    mod2 = 10**9 + 9

    def check(L):
        # ฟังก์ชันเช็คว่ามีตัวอักษรเรียงกันเหมือนกันความยาว L หรือไม่
        if L == 0:
            return 0

        h1 = h2 = 0
        p1 = p2 = 1
        seen = {}

        
        # คำนวณ Hash ของข้อความสั้นสุดความยาว L ตัวแรกในสตริงรอง (s2)
        for i in range(L):
            h1 = (h1 * base + ord(s2[i])) % mod1
            h2 = (h2 * base + ord(s2[i])) % mod2
            p1 = (p1 * base) % mod1
            p2 = (p2 * base) % mod2

        seen[(h1, h2)] = 0

        # ใช้ Sliding Window ทยอยเลื่อนและคำนวณ Hash สำหรับส่วนที่เหลือใน s2
        for i in range(L, m):
            h1 = (h1 * base - ord(s2[i-L]) * p1 + ord(s2[i])) % mod1
            h2 = (h2 * base - ord(s2[i-L]) * p2 + ord(s2[i])) % mod2

            key = (h1, h2)
            if key not in seen:
                seen[key] = i - L + 1

        
        h1 = h2 = 0

        # คำนวณ Hash ของข้อความสั้นสุดความยาว L ตัวแรกในสตริงหลัก (s1)
        for i in range(L):
            h1 = (h1 * base + ord(s1[i])) % mod1
            h2 = (h2 * base + ord(s1[i])) % mod2

        # ทดสอบว่าชนกันไหม (หาเจอ)
        if (h1, h2) in seen:
            return 0

        # ใช้ Sliding Window ทยอยเลื่อนและคำนวณ Hash สำหรับส่วนที่เหลือใน s1
        for i in range(L, n):
            h1 = (h1 * base - ord(s1[i-L]) * p1 + ord(s1[i])) % mod1
            h2 = (h2 * base - ord(s1[i-L]) * p2 + ord(s1[i])) % mod2

            if (h1, h2) in seen:
                return i - L + 1 # ชนกัน หมายความว่าเจอ common substring ส่งคืน Index กลับไป

        return None # หาความยาวเท่านี้ร่วมกันไม่เจอ

    # Binary Search แบ่งครึ่งความยาวเพื่อช่วยหาค่าความยาวร่วมกันที่มากที่สุด (Best length) 
    left, right = 0, min(n, m)
    best_len = 0
    best_pos = None

    while left <= right:
        mid = (left + right) // 2
        pos = check(mid)
        if pos is not None:
            # เจอความยาว mid -> ลองหาต่อว่าขยายความยาวกว่านี่ได้ไหม (ย้ายขอบล่างไปทางขวา)
            best_len = mid
            best_pos = pos
            left = mid + 1
        else:
            # ไม่เจอความยาว mid -> ต้องลดเป้าหมายความยาวลงมาหาทางซ้าย (ย้ายขอบบนมาทางซ้าย)
            right = mid - 1

    if best_len == 0:
        print("No common substring.")
    else:
        print(s1[best_pos:best_pos + best_len])
        print(best_len)


def main():
    s1 = input().strip() # รับสตริงชุดแรก
    s2 = input().strip() # รับสตริงชุดที่สอง
    lcs(s1, s2) # เรียกฟังก์ชันค้นหาสตริงย่อยร่วมที่ยาวที่สุด

main()
