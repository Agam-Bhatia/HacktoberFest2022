def threeSumClosest(nums, target):
    cSum = nums[0] + nums[1] + nums[2]
    res = cSum

    # if target < 0:
    #     target *= -1
    minDiff = cSum - target

    if minDiff < 0:
        minDiff *= -1

    for i in range(len(nums)):


        l, r = 0, len(nums) - 1
        if i == l:
            continue
        while l < r:
            if i == l:
                continue
            cSum = nums[i] + nums[l] + nums[r]

            diff = cSum - target
            if diff < 0:
                diff *= -1
            if diff <= minDiff:
                minDiff = diff
                res = cSum
            print(diff)
            r -= 1
    print("Result ")
    return res+1


nums = [1,2,4,8,16,32,64,128]

target = 82

print(threeSumClosest(nums, target))