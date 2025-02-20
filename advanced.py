'''
１．文字列操作
ユーザーから入力された文字列を逆順にして表示するプログラムを書いてください。（例: "python" → "nohtyp"）
'''
str_input = input('文字列を入力してください：')
str_list = list(str_input)
str_list.reverse()
str = ''.join(str_list)
print('問題１：', str)

'''
２．辞書の操作
次の辞書 scores を使い、各生徒の平均点を求めるプログラムを作成してください。
'''
scores = {
    "Alice": [80, 90, 70],
    "Bob": [60, 50, 80],
    "Charlie": [90, 100, 85]
}

class Student:
    def avg(self, name, math, english, japanese):
        print(name, (math + english + japanese) / 3)

print('問題２：')
student = Student()
student.avg("Alice", *scores["Alice"])
student.avg("Bob", *scores["Bob"])
student.avg("Charlie", *scores["Charlie"])

'''
３．ファイル操作
data.txt というファイルを作成し、その中に "Hello, Python!" という文字を書き込むプログラムを作成してください。
'''
import os

f = open('data.txt', 'w')
f.write('Hello, Python!')
f.close()

if os.path.isfile('data.txt'):
    print('問題３：data.txtが作成されました。')
else:
    print('問題３：data.txtが存在しません。')

'''
４．クラスの作成
Person クラスを作成し、name と age を属性として持たせ、introduce() メソッドを呼び出すと 
"私は〇〇です。〇〇歳です。" と表示するようにしてください。
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('問題４：私は', self.name, 'です。', self.age, '歳です。')

myself = Person('菅井', 26)
myself.introduce()

'''
５．例外処理
ユーザーに数値を入力してもらい、それを整数に変換するプログラムを作成してください。
ただし、数値以外が入力された場合は "数値を入力してください" と表示するようにしてください。
'''
while True:
    num_input = input('数値を入力してください：')
    if num_input.isdigit() == True:
        break
print('問題５：', int(num_input))
