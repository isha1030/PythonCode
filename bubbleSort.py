unsortedList = [47, 3, 1000, 679, 14, 56]
for j in range(len(unsortedList)-1):
	for i in range(len(unsortedList)-j-1):
    	if unsortedList[i] > unsortedList[i+1]:
        	unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i]
        	print(unsortedList)
