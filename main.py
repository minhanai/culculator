# FastAPIをインポート
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


# FastAPIのインスタンス作成
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

# 変数
KIGOU_TASU = 1
KIGOU_HIKU = 2
KIGOU_KAKERU = 3
KIGOU_WARU = 4

# GETメソッドでルートURLにアクセスされたときの処理
@app.get("/{no1}/{no2}/{kigou}") 
async def root(request: Request):
    req = request.path_params
    no1 = int(req.get("no1"))
    no2 = int(req.get("no2"))
    kigou = int(req.get("kigou"))

    if kigou == KIGOU_TASU:
        print(no1 + no2)
        return (no1 + no2)
    elif kigou == KIGOU_HIKU:
        print(no1 - no2)
        return (no1 - no2)
    elif kigou == KIGOU_KAKERU:
        print(no1 * no2)
        return (no1 * no2)
    elif kigou == KIGOU_WARU:
        print(no1 / no2)
        return (no1 / no2)
    else:
        return ("記号は1から4までの数字でお願いします")
    