'''
解题思路：

Solution 1:
- 二分查找
- 要找到中位数，就要对数组进行划分，中位数左右侧数组长度固定；
- 在nums1上进行二分查找，假设nums1的划分点是partition1，那么nums2的划分点是(m+n+1)//2-partition1
  nums1： a1, a2, | a3, a4, a5, a6                     ( | 表示分割点)
  nums2： b1, b2, b3, b4, b5, b6, | b7, b8, b9
  数组有序，已经满足 a2 < a3, b6 < b7;
  如果再满足： a2 < b7, b6 < a3, 那么分割点左侧所有的数值都小于分割点右侧的值，那么中位数就在 [a2, b6, a3, b7] 之间产生；
  如果 a2 > b7, 说明左边的数值太大，需要把nums1的分割点向左移；
  如果 a2 < b7, 说明左边的数值太小，需要把nums1的分割点向右移；
- 当m+n为偶数时，中位数为 (max(L1,L2)+min(R1,R2))/2， 否则max(L1,L2)。  （其中L1,R1,L2,R2分别为两分割线左右侧的值）

时间复杂度 O(n), 空间复杂度 O(1)


Solution 2:
Solution 2
- 二分法（by NineChap)
- 转换为：在两个有序数组中，找合并后的第K个数（第k小的数...）；那么中位数就是第 (n+m)/2 个数，或者找中间两个数；

A: _  _  _  _  _  _  _  _  _         B:  _  _  _  _  _  _  _  _  _  _  _  _
           k/2                                   k/2

- 对于两个有序数组，要找第K个数，可以分别在两个数组中找到第 k/2 个数(那么下标就是 k/2-1 )，比较这两个数的大小;
  如果 A[k/2-1] < B[k/2-1]， 说明A的前k/2个数都在前K个数里面，
  也就是说在合并两个有序数组过程中，A的前k/2个数都被拿出来后，B还没到第k/2个数；
  因此可以扔掉A的前k/2个数，然后从A的后面以及B中再去找第 k-k/2 个数；再在A，B中找到第 （k-k/2）/2 个数进行比较...
- 对于特殊情况，如果A的数组长度不够 k/2， 那么我们只扔掉B的前 k/2 个数，（因为B的前k/2个数一定会包含在前K个数里面）
  这样就假设A的第 k/2 位置的值为无穷大∞，然后去比较 A，B 的第 k/2 个数的大小；
- 如果有一个数组为空，直接返回另一个数组的第k个数即可；

时间复杂度 O(logn), 空间复杂度 O(1)

- 关于扔掉数组的一部分，其实是使用两个下标分别标记两个数组的位置；
- 在代码中，判断如果k==1，就直接比较两个数组的第一位值；
  如果不比较，可以看到下面的if else里面传进去的k一直是0，不会发生变化，递归就会发生死循环；
- 注意这边找的数组中第 k/2 个，对应的下标要减1.
'''
# Solution 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        p1 = n // 2
        while True:
            p2 = (n + m + 1) // 2 - p1
            
            L1 = nums1[p1-1] if p1 >0 else -float('inf')
            R1 = nums1[p1] if p1 < n else float('inf')
            L2 = nums2[p2-1] if p2 > 0 else -float('inf')
            R2 = nums2[p2] if p2 < m else float('inf')
            
            if L1 <= R2 and L2 <= R1:
                return (max(L1, L2) + min(R1, R2)) / 2 if (n+m) % 2 == 0 else max(L1, L2)
            elif L1 > R2:
                p1 -= 1
            else:
                p1 += 1


# Solution 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            return self.findKthNum(nums1, 0, nums2, 0, (m+n)//2+1)
        else:
            return (self.findKthNum(nums1, 0, nums2, 0, (m+n)//2+1) + \
                   self.findKthNum(nums1, 0, nums2, 0, (m+n)//2)) / 2   

    def findKthNum(self, nums1, n1, nums2, n2, k):
        if n1 >= len(nums1):
            return nums2[n2 + k - 1]
        if n2 >= len(nums2):
            return nums1[n1 + k - 1]
        if k == 1:
            return min(nums1[n1], nums2[n2])
        
        tp1 = n1 + k//2 - 1
        tp2 = n2 + k//2 - 1
        v1 = nums1[tp1] if tp1 < len(nums1) else float('inf')
        v2 = nums2[tp2] if tp2 < len(nums2) else float('inf')
        if v1 < v2:
            return self.findKthNum(nums1, tp1+1, nums2, n2, k - k//2)
        else:
            return self.findKthNum(nums1, n1, nums2, tp2+1, k - k//2)
