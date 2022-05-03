"""
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
"""


#엘리먼트를 출력해야 하기 때문에 주어진 배열을 정렬해도 괜찮다. for i 에 대해 0을 계산하는 투포인터방식으로 계산한다.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i in range(len(nums)-2): # 마지막 순서대로 3개인 경우까지니까 nums-2개만 조사하면 된다.
            if i >0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                sum = num[i] + num[left] + num[right]
                if sum <0:
                    left += 1
                elif sum >0:
                    right -= 1
                else:
                    results.append((num[i], num[left], num[right]))
                    #후속처리 필수적이진 않으나 성능 향상
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1

                    # 둘 다 이동시키는 이유는
                    left += 1

        return results
