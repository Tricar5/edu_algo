

def removeElement(nums: list[int], val: int) -> int:

    size = len(nums)
    idx = 0

    while idx < size:

        if nums[idx] == val:
            nums.pop(idx)
            size-=1
        else:
            idx+=1

    print(nums)

    return size


arr = [1,1,2,1,1,1]
val = 1



removeElement(arr,val)