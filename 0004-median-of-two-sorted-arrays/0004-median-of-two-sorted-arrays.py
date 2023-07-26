class Solution:
    def get_mid(self, arr):
        is_odd = bool(len(arr) % 2 != 0)
        if is_odd:
            return arr[len(arr)//2]
        else:
            return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        if not nums1:
            return self.get_mid(nums2)
        elif not nums2:
            return self.get_mid(nums1)
        tol_len = len(nums1) + len(nums2)
        mid_idx = tol_len // 2 if tol_len % 2 == 0 else tol_len // 2 + 1
        merged_nums = []
        while len(merged_nums) < mid_idx + 1:
            if nums1 and nums2:
                if nums1[-1] >= nums2[-1]:
                    merged_nums.append(nums1.pop())
                else:
                    merged_nums.append(nums2.pop())
            elif nums1:
                merged_nums.append(nums1.pop())
            elif nums2:
                merged_nums.append(nums2.pop())
        if tol_len % 2 != 0:
            return merged_nums[-2]
        else:
            return (merged_nums[-1] + merged_nums[-2])/2