open_list = ["[","{","("]
close_list = ["]","}",")"]


def check(strr):
	test = []
	for i in strr:
		if i in open_list:
			test.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(test) > 0) and
				(open_list[pos] == test[len(test)-1])):
				test.pop()
			else:
				return "Unbalanced"
	if len(test) == 0:
		return "Balanced"
	else:
		return "Unbalanced"



strr = "({{}[]})"
print(check(strr))

strr = "{[(){}]}"
print(check(strr))

strr = "{{{()}}"
print(check(strr))
