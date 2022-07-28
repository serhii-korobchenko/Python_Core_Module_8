import collections

# Count number of elements in collection
student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
#print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

# Check friequency of elements in collection
student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
""" print(mark_counts.most_common(1))  # [(4, 4)]
print(mark_counts.most_common(2))  # [(4, 4), (6, 3)] """

# subtract of elements

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)    # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})