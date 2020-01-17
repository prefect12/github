def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
sortColors([0,1,2,0])