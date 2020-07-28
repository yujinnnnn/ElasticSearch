from konlpy.tag import Kkma

file = open("text.txt", mode ='r', encoding='utf-8')
doc = file.read()
file.close()
print(doc)

kkma = Kkma()

ex_sent = kkma.sentences(doc)

nouns = []
for sent in ex_sent:
    for noun in kkma.sentences(sent):
        #단어 전처리 : 2음절 이상, 수사 제외
        if len(str(noun)) >= 2 and not(match('^[0-9]', noun)):
            nouns.append(noun)
#-----------------------------------------------------------------------------------------------------

para = "형태소 분석을 시작합니다. 저는 김유진 입니다."

ex_sent = kkma.sentences(para)
print(len(ex_sent))
print(ex_sent)

ex_nouns = kkma.nouns(para)
print(len(ex_nouns))
print(ex_nouns)

ex_pos = kkma.pos(para)
print(len(ex_pos))
print(ex_pos)

text_data = []

for (text, tclass) in ex_pos:
    if tclass == 'NNG' or tclass == 'NNP' or tclass == 'NP' :
        text_data.append(text)

print(text_data)

from konlpy.tag import Hannanum

hannanum = Hannanum()

para = "형태소 분석을 시작합니다. 저는 김유진 입니다."

hanana = hannanum.analyze(para)
print(hanana)
