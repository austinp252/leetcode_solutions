import numpy as np


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # unintuitive method
        # create merged array
        # index for each array, add lesser value
        # get median

        # loop that runs while at least some values remaining
        # end condition at index = len(list) - check at start of loop
        # not end cond, check values of each list at current index
        # get lesser value of two, increment index and add value to merged list
        # get median after loop terminates
        # if odd num of items, return item at len(list)/2
        # if even num of items, return average at len(list)/2-1 and len(list)/2

        mergedList = []
        index1 = 0
        index2 = 0
        # loop that runs while at least some values remaining
        while(True):
            # end condition at index = len(list) - check at start of loop
            if(len(nums1) == index1 and len(nums2) == index2):
                break
            # not end cond, check values of each list at current index
            else:
                # get value of nums1
                if(len(nums1) > index1):
                    val1 = nums1[index1]
                else:
                    val1 = np.inf
                # get value of nums2
                if(len(nums2) > index2):
                    val2 = nums2[index2]
                else:
                    val2 = np.inf

                # get lesser value of two, increment index and add value to merged list
                if(val1 > val2):
                    mergedList.append(val2)
                    index2 += 1
                else:
                    mergedList.append(val1)
                    index1 += 1

        # print(mergedList)
        # conditionals for getting median
        # even number of items
        if(len(mergedList) % 2 == 0):
            median = float(
                (mergedList[(len(mergedList)/2)-1]+mergedList[len(mergedList)/2]))/2
        else:
            median = float(mergedList[len(mergedList)/2])
        return median
