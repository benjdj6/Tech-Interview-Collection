import random


# Returns the size of the shortest sublist of list A
# that contains all of the unique values of A
# e.g. [1, 1, 2, 2, 3, 1] => len([2, 3, 1]) = 3
def shortestTrip(A):
    # trip will be used to track the unique values of
    # the array A
    trip = {}
    for i in A:
        if i not in trip:
            trip[i] = 0

    mini = len(A) + 1   # used to keep track of the shortest sublist found
    found = 0   # keeps track of unique values contained within current sublist
    needto = len(trip)  # tracks unique values missing from sublist
    start = 0   # starting index
    loops = 0   # counts loops for tracking time growth
    length = 0  # tracks the length of the current sublist

    for end in range(len(A)):
        # increment loops and length as endpoint moved forward
        # expanding the sublist
        loops += 1
        length += 1

        # checks if A[end] is already contained if not
        # increment found and decrement needto
        if trip[A[end]] == 0:
            found += 1
            needto -= 1
        trip[A[end]] += 1

        # if the current sublist contains all unique elements
        # move the start point forward until this is no longer the case
        while needto == 0:
            loops += 1

            # if the current sublist is shortest so far update mini
            if length < mini:
                mini = length

            trip[A[start]] -= 1
            start += 1
            length -= 1

            # if there is now a missing value break the loop
            # and update found and needto appropriately
            if trip[A[start - 1]] == 0:
                found -= 1
                needto += 1
                break
    print loops, len(A)  # keeping track of growth
    return mini


######################
# Tests
print shortestTrip([1, 2, 3, 3, 4, 1, 1, 1, 1, 2, 3, 4, 1])
print shortestTrip([1, 2, 3, 2, 4, 1])
print shortestTrip([1, 4, 2, 3, 2, 1])
print shortestTrip([1, 1, 1, 1, 1, 1])
print shortestTrip([1] * 10000)
print shortestTrip([1] * 1000)
print shortestTrip([1] * 100)


a = []
for i in range(100):
    a.append(random.randint(1, 100))

print shortestTrip(a)

for i in range(900):
    a.append(random.randint(1, 100))

print shortestTrip(a)

for i in range(9000):
    a.append(random.randint(1, 100))

print shortestTrip(a)
