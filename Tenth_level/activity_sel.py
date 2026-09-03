# Given two arrays start[] and finish[], where start[i] 
# and finish[i] represent the start time and finish time of the i-th activity, 
# find the maximum number of activities that a single person can perform.

# A person can perform only one activity at a time, 
# and no two selected activities can overlap. If an activity finishes at time x,
# the next selected activity must start at a time greater than x.
def activity_selection(start, finish):
    n = len(start)
    activities = sorted(zip(start, finish), key=lambda a: a[1])

    count = 1
    last_finish = activities[0][1]

    for s, f in activities[1:]:
        if s >= last_finish:
            count += 1
            last_finish = f

    return count

# Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]