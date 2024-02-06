file=open("SortedList.txt",'w')
a=[3,2,4,6,2,1,-2,6,5.5]
file.write("Before Sorting the list: ")
for i in a:
    file.write(str(i))
    file.write(" ")
a.sort()
file.write('\n')
file.write("Ascending Order.......")
file.write('\n')
file.write("After Sorting the list: ")
for i in a:
    file.write(str(i))
    file.write(" ")
a.sort(reverse=True)
file.write('\n')
file.write("descending Order.......")
file.write('\n')
file.write("After Sorting the list: ")
for i in a:
    file.write(str(i))
    file.write(" ")
file.close()
