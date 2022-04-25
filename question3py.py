def masx(array):
	max = max(array[0] , array[1])
	second_max = min(array[0], array[1])

	len = len(array)
	
	for i in range( 2 , len):
		if array[i] > max:
			second_max = max
			max = array[i]
		elif array[i] > second_max and max != array[i]:
			second_max = array[i]

    return max, second_max
