#sets don't allow duplicate elements(contains unique data)
#unordered collection

# create a student_id set integer type
stu_id = {112, 113, 114, 115}
print(stu_id)

# create a string type set
letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

# create a mixed set
mixed_set = {"Hello", 1, -7, 8.9}
print(mixed_set)

# create an empty set
#empty_set = set()
#print(empty_set)

#Examples
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#add element
A.add(7)
print(A)

#clear
#A.clear()
#print(A)

#copy
C = A.copy()
print(C)

#difference
print(A.difference(B))
# or
print(A - B)

#difference Update
A.difference_update(B)
print(A)

#discard
A.discard(2)
print(A)

#intersection
print(A.intersection(B))
# or
print(A & B)
#intersection_update
A.intersection_update(B)
print(A)
#isdisjoint
print(A.isdisjoint(B))

#issubset
print(A.issubset(B))
#Proper subset
{3,4} < B
#pop()
#A.pop()
#print(A)
#remove()
#A.remove(2)
#print(A)
#union()
A.update(B)
print(A)
#update()
A.update(B)
print(A)
