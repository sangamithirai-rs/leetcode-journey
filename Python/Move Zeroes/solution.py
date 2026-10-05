class Solution:
    def moveZeroes(self, nums):
        # 'write' tells us where the next non-zero number should go
        write = 0

        # 'i' scans through every element
        for i in range(len(nums)):

            # If the current number is NOT zero
            if nums[i] != 0:

                # Put the non-zero number at the 'write' position
                nums[write], nums[i] = nums[i], nums[write]

                # Move 'write' to the next position
                write += 1
