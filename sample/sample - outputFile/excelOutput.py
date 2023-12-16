# Excel出力のサンプルプログラム

# Excel操作をする場合はopenpyxlというライブラリが必要なのでimportします。
# openpyxlについてはpipを使ってインストールしてください。
import openpyxl

# Excelオブジェクトを生成する
excel = openpyxl.Workbook()

# アクティブシートの設定
sheet = excel.active

# セルに値を書き込む(この書き方はA1方式(セル直接指定)です。)
sheet['C1'] = 'Excelの出力プログラム'

# セルに値を書き込む(この書き方はR1C1方式(行番号、列番号を指定)です。)
sheet.cell(row=3, column=2).value = 'Excelの出力プログラム2'

# 出力するファイルのパス指定(パスは環境に合わせて適宜変更してください。)
path = '/Users/gozuchi/Desktop/file/'
fileName = 'test.xlsx'

# Excelを保存する
excel.save(path + fileName)