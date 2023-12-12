arr = [9,8,7,6,5,4,3,2,1]
for i in range(len(arr) - 1):
		for j in range(len(arr) - 1 - i):
			num1 = arr[j] 
			num2 = arr[j+1]
			print(num1, " ", num2)
			if num1 > num2:
					arr[j], arr[j+1] = arr[j+1], arr[j]
					print(arr)
print(arr)