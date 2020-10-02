def today_lunch():
    lunch = ['しょうが焼き定食', 'ロースカツ定食', 'ラーメンと半炒飯', 'レバニラ炒め定食', 'ナポリタンとハンバーグ定食']
    select = input('数字を入力してください：')
    index = int(select) % len(lunch)
    print('今日のランチは')
    print(lunch[index])
today_lunch()