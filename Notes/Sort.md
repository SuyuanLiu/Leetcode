Sort
merge sort：
- 从中间分开，左边递归归并，右边递归归并，使得左边有序，右边有序，然后利用额外空间合并这两个有序数  组，然后再把合并好的数组倒腾到原来的数组里去（耗费很多时间）
- 分治思想，局部有序，最后整体有序；

quick sort
- 做partition，从数组中随机挑选一个数，比它小的放前面，大的放后面；（一般挑选中间的值，挑第一个或者最后一个也可以，只是容易构造它的最后情况）
- 分治思想，先整体有序，然后局部有序

merge sort：O(nlogn)  O(n)  稳定
quick sort：O(nlogn)  O(1)  不稳定

排序中nlogn的堆排序不是分治法，但也利用了这个思想；
实际中快排用的多一点，因为不耗费额外空间，归并排序还要把合并好的新数组放到之前的数组里去，也很耗时间；

稳定性：对于key-value情况，或者排坐标(1,1),(1,2),(1,3)按照x排...

时间复杂度分析：
归并：每次合并两个有序数组耗费的时间是O(n)，然后一半一半的分最后是logn；
     树状结构，每一层合并数组的时间加起来都是O(n),（合并n/2的数组为O(n)...）
快排：是平均复杂度为nlogn
     最好的情况nlogn，平均情况nlogn，最坏的情况n^2；
     最坏：每次partition之后的x都是最小或者最大的数（每次partition时间O(n)），最后要做n次；
     平均是按照概率来算的；
     （在网上看的一个方法，快排之前先把数组打乱一下） 
