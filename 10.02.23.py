open_list = ["[","{","("]
close_list = ["]","}",")"]


def check(strr: str) -> str:
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



if __name__ == "__main__":
	braces = "({{}[]})"
	print(check(braces))

	braces2 = "{[(){}]}"
	print(check(braces2))

	braces3 = "{{{()}}"
	print(check(braces3))
