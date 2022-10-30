def num_ways(n):
    return count_num_ways_from(1, n) + count_num_ways_from(2, n)

def count_num_ways_from(step, remaining):
    if step == remaining:
        return 1
    elif step > remaining:
        return 0
    else:
        return count_num_ways_from(1, remaining - step) + count_num_ways_from(2, remaining - step)