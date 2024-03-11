# FastAPIをインポート
from fastapi import FastAPI, Request

# FastAPIのインスタンス作成
app = FastAPI()

# GETメソッドでルートURLにアクセスされたときの処理
@app.get("/{no1}/{no2}/{kigou}") 
async def root(request: Request):
    req = request.path_params
    no1 = int(req.get("no1"))
    no2 = int(req.get("no2"))
    kigou = int(req.get("kigou"))

    if kigou == 1:
        print(no1 + no2)
        return (no1 + no2)
    elif kigou == 2:
        print(no1 - no2)
        return (no1 - no2)
    elif kigou == 3:
        print(no1 * no2)
        return (no1 * no2)
    elif kigou == 4:
        print(no1 / no2)
        return (no1 / no2)
    else:
        return ("記号は1から4までの数字でお願いします")
    