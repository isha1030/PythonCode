linearList = [2, 4, 16, 78, 34, 55]

linearUserElement = int(input("Enter a value:"))

def linearSearch(element):
	count = 0
	for i in linearList:
    	if element == i:
        	count += 1
        	print(element, "found at index:", linearList.index(element))
	if count == 0:
    	print("number is not in list")
linearSearch(linearUserElement)
