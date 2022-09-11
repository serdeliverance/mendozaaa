def partition_equal_subset_sum(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    return canPartition(nums, 0, 0, total)


def canPartition(nums, index, sum, total):
    if (sum * 2 == total):
        return True
    if (sum * 2 > total or index >= len(nums)):
        return False
    return canPartition(nums, index + 1, sum, total) or canPartition(nums, index + 1, sum + nums[index], total)
