'''
１．フィボナッチ数列（再帰）
再帰を用いて n 番目のフィボナッチ数を求める関数 fibonacci(n) を作成してください。
ただし、 n = 1 のとき 0 、 n = 2 のとき 1 とし、 n >= 3 のときは n-1 番目と n-2 番目の和を返すものとします。
'''
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print('問題１：', fibonacci(5))

'''
２．リスト内の部分リストの最大合計
整数リスト nums が与えられたとき、連続する部分リストの中で最大の合計を
求める関数 max_subarray_sum(nums) を作成してください。（カダネのアルゴリズムを使用）
'''
def max_subarray_sum(nums):
    max_sum = nums[0]
    max_ending = nums[0]

    for i in range(len(nums)):
        max_ending = max(max_ending + nums[i], nums[i])
        max_sum = max(max_ending, max_sum)

    return max_sum

nums = [-2, 1,-3, 4,-1, 2, 1,-5, 4]
print('問題２：', max_subarray_sum(nums))

'''
３．アナグラム判定
2つの文字列が与えられたとき、それらがアナグラム（同じ文字を使って並べ替えた単語）
かどうかを判定する関数 is_anagram(s1, s2) を作成してください。
'''
def is_anagram(s1, s2):
    print(f'{s1, s2} → {sorted(list(s1)) == sorted(list(s2))}')

print('問題３：')
is_anagram('listen', 'silent')
is_anagram('hello', 'world')

'''
４．JSONファイルの読み書き
Pythonの辞書をJSON形式でファイル data.json に保存し、再度読み込むプログラムを作成してください。
'''
import json

python_dec = {'country': 'England', 'city': 'Liverpool', 'place': 'First'}

with open('data.json', 'w') as f:
    json.dump(python_dec, f)

with open('data.json') as f:
    print('問題４：', json.load(f))

'''
５．2つのソート済みリストのマージ
ソートされた2つのリストを統合して1つのソート済みリストを返す関数 merge_sorted_lists(list1, list2) を作成してください。
（マージソートのマージ部分）
'''
def merge_sorted_list(list1, list2):
    list1.extend(list2)
    print('問題５：', sorted(list1))

merge_sorted_list([1, 3, 5], [2, 4, 6])

'''
６．クラスの継承
Animal クラスを作成し、 Dog クラスと Cat クラスをそれぞれ継承して、鳴き声を出す speak() メソッドをオーバーライドしてください。
'''
class Animal:
    def __init__(self, cry):
        self.cry = cry
    
    def speak(self):
        print(self.cry)

class Dog(Animal):
    def __init__(self, cry):
        super().__init__(cry)

class Cat(Animal):
    def __init__(self, cry):
        super().__init__(cry)

dog = Dog('ワン')
cat = Cat('ニャー')
print('問題６：')
dog.speak()
cat.speak()
