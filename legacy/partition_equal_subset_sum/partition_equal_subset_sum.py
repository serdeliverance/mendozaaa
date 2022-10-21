def partition_equal_subset_sum(nums):
    """solution using dynamic programming"""
    total = sum(nums)
    if total % 2 != 0:
        return False
    return canPartition(nums, 0, 0, total, {})


def canPartition(nums, index, sum, total, state):
    # using dict/hash map to avoid recalculating already computed values
    current = str(index) + str(sum)
    if (state.get(current) != None):
        return state.get(current)

    if (sum * 2 == total):
        return True

    if (sum * 2 > total or index >= len(nums)):
        return False

    foundPartition = canPartition(
        nums, index + 1, sum, total, state) or canPartition(nums, index + 1, sum + nums[index], total, state)

    state[current] = foundPartition

    return foundPartition
