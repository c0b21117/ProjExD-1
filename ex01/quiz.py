import random
quiz = {'サザエの旦那の名前は？':['ますお','マスオ'],'カツオの妹の名前は？':['わかめ','ワカメ'],
'タラオはカツオから見てどんな関係？':['甥','おい','甥っ子','おいっこ']}

select1, select2 = random.choice(list(quiz.items()))

print('問題:')
print(select1)
answer = input('答えるんだ:')
if answer in select2:
    print('正解!!!')
else:
    print('出直してこい')
