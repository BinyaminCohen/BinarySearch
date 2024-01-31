# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

NOT_FOUND = -1


class BinarySearch(object):

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return nums[mid], mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return target, NOT_FOUND


num, idx = BinarySearch().binary_search([-1, 0, 3, 5, 9, 12], 9)

if idx != NOT_FOUND:
    print(f"{num} exists in num list and its index is {idx}.")

else:
    print(f"{num} does not exist in num list so return {idx}.")
