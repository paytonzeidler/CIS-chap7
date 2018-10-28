title = input("Enter a title for the data:\n")

print("You entered:",title)
print()

col1_head = input("Enter the column 1 header:\n")
print("You entered:",col1_head)
print()
col2_head = input("Enter the column 2 header:\n")
print("You entered:",col2_head)
print()

dataArray = {}

data_points = input("Enter a data point (-1 to stop input):\n")
while data_points != '-1':
	if ',' not in data_points:
		print("Error: No comma in string.\n")
	elif data_points.count(',') >1:
		print("Error: Too many commas in input.\n")
	else:
		d_array = data_points.split(',')
		d_string = d_array[0]
		d_int = d_array[1]
		try:
			if not isinstance(int(d_int),int):
				print("Error: Comma not followed by an integer.\n")
			else:
				d_int = int(d_int)
				print("Data string:",d_string)
				print("Data integer:",d_int)
				print()
				dataArray[d_string] = d_int
		except ValueError:
			print("Error: Comma not followed by an integer.\n")
	data_points = input("Enter a data point (-1 to stop input):\n")
	
#print table
title_w = 33
col1_w = 20
col2_w = 23
print()
print("{0:>{1}}".format(title[:title_w],title_w))
print("{0:<{1}}|{2:>{3}}".format(col1_head[:col1_w],col1_w,col2_head[:col2_w],col2_w))
print("-"*44)
for key in dataArray:
	print("{0:<{1}}|{2:>{3}}".format(key[:col1_w],col1_w,str(dataArray[key])[:col2_w],col2_w))
print()

hist_w = 20

for key in dataArray:
	print("{0:>{1}}".format(key[:hist_w],hist_w),end=' ')
	print('*'*dataArray[key])
