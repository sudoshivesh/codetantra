#WAP to find min, max and average of elements of a list having numeric data
a=int(input("How many numbers: "))
li=[]
for i in range(a):
  item=int(input("Enter number "))
  li.append(item)
length=len(li)
print("Maximum element in the list is :",max(li),'')
print("Minimum element in the list is :",min(li))
print("Average = ",(sum(li)/length))
