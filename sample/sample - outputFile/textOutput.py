# Text出力のサンプルプログラム

# 出力するファイルのパス指定(パスは環境に合わせて適宜変更してください。)
path = '/Users/gozuchi/Desktop/file/'
fileName = 'test.txt'

# ファイルをオープン('a'はオプションで追記モードでの書き込み)
file = open(path + fileName, 'a')

# ファイルに書き込む
file.write('テスト')

# ファイルを閉じる
file.close()