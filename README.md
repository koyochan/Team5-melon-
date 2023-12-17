# 初回環境構築
.env.sampleをコピーして.envファイルを作る
または新規.envファイル作成して中身をdiscordで共有した情報で入れる

```shell
python3 -m venv venv
. venv/bin/activate

pip install Flask
pip install python-dotenv
pip install requests

python3 app.py
```

# 2回め以降
```shell
. venv/bin/activate
python3 app.py
```

# Body_make.py
```shell
pip install pytz
pip install python-dateutil
```