# Task:-    
# 1.Practice all Methods 
# 2. Take a set of no,take elements from the user, remove that element  from the existing set  and store in the new set.



num = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
val = int(input("enter how many elements you want to remove : "))
new_set = set()
for i in range(1,val+1,1):
    inp = int(input("please select a number to remove from set : "))
    new_set.add(inp)
    num.remove(inp)
print(num)
print(new_set)
    
