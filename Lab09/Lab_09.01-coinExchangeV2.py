import json

def convert_key(data):
    # แปลง key ของ dictionary จาก string เป็น integer
    return {int(k): v for k, v in data.items()}

def coinExchangeV2(amount, coins):
    # สร้างตาราง dp เพื่อเก็บจำนวนเหรียญที่น้อยที่สุดที่ใช้สำหรับแต่ละจำนวนเงิน
    # เริ่มต้นด้วยค่าอนันต์ (infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 # จำนวนเงิน 0 ใช้เหรียญ 0 เหรียญ

    # สร้างลิสต์ของ dictionary เพื่อเก็บว่าใช้เหรียญอะไรไปบ้างในแต่ละจำนวนเงิน
    used = [{} for _ in range(amount + 1)]

    for coin in coins:
        for _ in range(coins[coin]): # วนลูปตามจำนวนเหรียญที่มีอยู่
            # วนลูปย้อนกลับจาก amount ลดลงจนถึง coin เพื่อป้องกันการใช้เหรียญเดิมซ้ำ (0/1 Knapsack style)
            for i in range(amount, coin - 1, -1):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    used[i] = used[i - coin].copy() # คัดลอกการใช้เหรียญก่อนหน้า
                    used[i][coin] = used[i].get(coin, 0) + 1 # บันทึกการใช้เหรียญปัจจุบันเพิ่มเข้าไป

    if dp[amount] == float('inf'):
        return None, None # คืนค่า None หากไม่สามารถแลกเงินตามระบุได้พอดี

    return dp[amount], used[amount]


def main():
    money = int(input()) # รับจำนวนเงินที่ต้องการแลก
    data = convert_key(json.loads(input())) # รับข้อมูลชนิดและจำนวนของเหรียญที่มี

    # เรียกฟังก์ชันคำนวณการแลกเหรียญที่ใช้น้อยที่สุด
    total_coins, result = coinExchangeV2(money, data)

    print(f"Amount: {money}")
    if result is None:
        print("Can not exchange.")
        return
    print("Coin exchange result:")


    # พิมพ์ผลลัพธ์การแลกเหรียญ โดยเรียงลำดับจากเหรียญที่มีมูลค่ามากไปน้อย (reverse=True)
    for coin in sorted(data.keys(), reverse=True):
        print(f"  {coin} baht = {result.get(coin, 0)} coins")

    print(f"Number of coins: {total_coins}")


main()
