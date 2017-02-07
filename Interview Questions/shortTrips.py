def shortestTrip(A):
    trip = {}
    for i in A:
        if i not in trip:
            trip[i] = 0
    mini = len(A) + 1
    found = 0
    needto = len(trip)
    start = 0
    loops = 0

    for end in range(len(A)):
        loops += 1
        if trip[A[end]] == 0:
            found += 1
            needto -= 1
        trip[A[end]] += 1

        while needto == 0:
            loops += 1
            if len(A[start:end + 1]) < mini:
                mini = len(A[start:end + 1])
            trip[A[start]] -= 1
            start += 1
            if trip[A[start - 1]] == 0:
                found -= 1
                needto += 1
                break
    # print loops, len(A) # keeping track of growth
    return mini


print shortestTrip([1, 2, 3, 3, 4, 1, 1, 1, 1, 2, 3, 4, 1])
print shortestTrip([1, 2, 3, 2, 4, 1])
print shortestTrip([1, 4, 2, 3, 2, 1])
print shortestTrip([1, 1, 1, 1, 1, 1])
