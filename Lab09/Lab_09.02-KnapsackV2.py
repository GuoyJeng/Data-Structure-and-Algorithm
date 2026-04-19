import json

class Item:
    # คลาสสำหรับเก็บข้อมูลของสิ่งของแต่ละชิ้น (ชื่อ, ราคา, น้ำหนัก)
    def __init__(self, name, price, weight):
        self.name = name
        self.weight = weight
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight


def knapsackV2(amount, itemList):
    n = len(itemList)

    # สร้างตาราง dp สีเหลี่ยมขนาด (n+1) x (amount+1) เก็บมูลค่าสูงสุด
    dp = [[0]*(amount+1) for _ in range(n+1)]


    # เติมค่าในตาราง dp แถวต่อแถว (วนหามูลค่าที่ดีที่สุด)
    for i in range(1, n+1):
        item = itemList[i-1]
        for w in range(amount+1):
            if item.get_weight() <= w:
                # เลือกชิ้นนี้ หรือ ไม่เลือกชิ้นนี้ (เอามูลค่ามากที่สุด)
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w - item.get_weight()] + item.get_price()
                )
            else:
                # น้ำหนักของชิ้นนี้เกินกระเป๋า ณ ตอนนี้ (w) จึงไม่สามารถใส่ได้ นำค่าก่อนหน้ามาใส่ได้เลย
                dp[i][w] = dp[i-1][w]


    w = amount
    picked = []

    # แกะรอยย้อนกลับ (Backtracking) เพื่อหาว่ามีสิ่งของชิ้นใดบ้างถูกเลือกมาเพื่อให้ได้มูลค่าเหล่านั้น
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]: # ถ้าย้ายแถวแล้วค่าเปลี่ยนแปลว่าของรหัสนั้นถูกเลือก
            item = itemList[i-1]
            picked.append(item)
            w -= item.get_weight() # ลบน้ำหนักของชิ้นที่เลือกออกเพื่อค้นหาต่อสำหรับแถวก่อนหน้า

    # เรียงลำดับของที่เลือกตามชื่อจากน้อยไปมาก
    picked.sort(key=lambda x: x.get_name())

    return dp[n][amount], picked


def main():
    raw = json.loads(input().strip()) # รับข้อมูลอาร์เรย์สิ่งของและแปลงจากรูปแบบ json
    amount = int(input().strip()) # รับค่าน้ำหนักสูงสุดของกระเป๋า

    items = [Item(name, price, weight) for name, price, weight in raw]

    total, picked = knapsackV2(amount, items)

    print(f"Total: {total}")
    for item in picked:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
main()
