# １．変数とデータ型
x = 100
y = 50
print('問題１：', x + y)

# ２．条件分岐
num_input = input('問題２： 数値を入力してください: ')
number = int(num_input)
if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')

# ３．ループ処理
sum_1_to_100 = 0
for i in range(101):
    sum += i
print('問題３：', sum)

# ４．リストの操作
numbers = [10, 200, 30, 400, 50, 600]
print('問題４：', [num for num in numbers if num >= 100])

# ５．関数の作成
def add_numbers(a, b):
    return a + b
a = 5
b = 3
print('問題５：', add_numbers(a, b))

# ６．辞書の操作
person = {"name": "Taro", "age": 30, "job": "engineer"}
person["age"] += 1
person["city"] = "Tokyo"
person.pop("name")
print('問題６：', person)

# ７． タプルの活用
numbers = (10, 25, 8, 42, 17)
print('問題７： 合計値＝', sum(numbers), '、最大値＝', max(numbers))

# ８． 辞書のキー・値の取得
fruits = {"apple": 3, "banana": 5, "orange": 2}
keys = list(fruits.keys())
values = list(fruits.values())
print('問題８： キーのリスト', keys, '、値のリスト', values)

# ９．辞書の内包表記
keys = ["name", "age", "city"]
my_dict = {i: None for i in keys}
print('問題９：', my_dict)

# １０．タプルのアンパック
data = (100, 200, 300)
x, y, z = data
print('問題１０： x =', x ,' y =', y ,' z =', z)