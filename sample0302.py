from random import randint
def today_lunch(menu):
    lunch = ['しょうが焼き定食', 'ロースカツ定食', 'ラーメンと半炒飯', 'レバニラ炒め定食', 'ナポリタンとハンバーグ定食']
    index = menu % len(lunch)
    print('今日のランチは')
    print(lunch[index])
menu = randint(0, 5)
today_lunch(menu)