from collections import Counter
#Counter는 sort기능을 가지고 있다 -> 정렬은 검색에 있어서 중요한 기능

lst = ['aa','cc','bb','aa','dd','ee']

dic = {'가':3, '나':2, '다':4}
# print(Counter(dic))

counter = Counter()
counter.update("aabbccddeeff")
cc = counter.elements()

print(counter)
print(list(cc))
