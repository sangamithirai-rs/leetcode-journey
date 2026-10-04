class Solution:
    def threeSum(self, nums):
        # 1. Sort the array
        nums.sort()

        # Store all valid triplets
        result = []

        # 2. Fix one number at a time
        for i in range(len(nums)):

            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 3. Two pointers
            left = i + 1
            right = len(nums) - 1

            # Search for two numbers
            while left < right:

                # Calculate the sum of three numbers
                total = nums[i] + nums[left] + nums[right]

                # 4. Found a valid triplet
                if total == 0:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # 5. Sum is too small
                elif total < 0:
                    left += 1

                # 6. Sum is too large
                else:
                    right -= 1

        # Return all valid triplets
        return result
