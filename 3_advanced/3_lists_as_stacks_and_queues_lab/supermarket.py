text = input()
paren_index_stack = []
for index in range(len(text)):
	if text[index] == '(':
		paren_index_stack.append(index)
	elif text[index] == ')':
		start_index = paren_index_stack.pop()
		end_index = index + 1
		print(text[start_index:end_index])
