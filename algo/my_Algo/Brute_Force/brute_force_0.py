# 부분집합 합 문제
def subset_sum(nums, target_sum):
    for i in range(2 ** len(nums)):
        subset = [nums[j] for j in range(len(nums)) if (i & (1 << j)) > 0]
        if sum(subset) == target_sum:
            return True
    return False


# 실행 예시
numbers = [1, 2, 3, 4, 5]
target = 9
result = subset_sum(numbers, target)
print(f"Subset with sum {target} exists: {result}")
