# CSV出力のサンプルプログラム

# CSV操作をする際はcsvモジュールをインポートします。
import csv

# ヘッダーとデータ行の設定(データ業は２次元配列で定義することで複数行出力されます。)
header = ['ID', 'name']
rows = [[1, '牛頭孝典'], [2, '安井孝弘']]

# 出力するファイルのパス指定(パスは環境に合わせて適宜変更してください。)
path = '/Users/gozuchi/Desktop/file/'
fileName = 'test.csv'

# with文を使うと短いコードで書くことができます。
with open(path + fileName, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(rows)