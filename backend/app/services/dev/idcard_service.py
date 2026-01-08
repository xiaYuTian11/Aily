import random
from datetime import datetime, timedelta

AREA_CODES = {
    "110000": "北京市", "310000": "上海市", "440100": "广州市", "440300": "深圳市",
    "330100": "杭州市", "320100": "南京市", "510100": "成都市", "420100": "武汉市"
}

def generate_idcard() -> dict:
    area = random.choice(list(AREA_CODES.keys()))
    start = datetime(1970, 1, 1)
    end = datetime(2005, 12, 31)
    birth = start + timedelta(days=random.randint(0, (end - start).days))
    birth_str = birth.strftime("%Y%m%d")
    seq = f"{random.randint(0, 999):03d}"
    base = area + birth_str + seq
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_chars = "10X98765432"
    total = sum(int(base[i]) * weights[i] for i in range(17))
    check = check_chars[total % 11]
    idcard = base + check
    gender = "男" if int(seq) % 2 == 1 else "女"
    return {"idcard": idcard, "area": AREA_CODES[area], "birth": birth.strftime("%Y-%m-%d"), "gender": gender}