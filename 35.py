word0 = input("１つ目の文字列を入力してください：")
word1 = input("２つ目の文字列を入力してください：")
word2 = input("３つ目の文字列を入力してください：")

print("{0}は{1}{2}です。{2}です".format(word0,word1,word2))

num0 = int(input("個数を入力："))
num1 = int(input("金額を入力："))

num2 = num0 * num1

print("{0:<}個{1:>15,}円".format(num0,num2))

