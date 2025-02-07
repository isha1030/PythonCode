unsortedList = [47, 3, 1000, 679, 14, 56]
for i in range(len(unsortedList)):
	for j in range(i + 1,len(unsortedList)):
    	if unsortedList[i] > unsortedList[j]:
        	unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]
print(unsortedList)
