def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length_array = len(nums)
    rs = [None] * length_array
    
    left = 0
    right = length_array - 1
    index = length_array - 1
    
    while True:
        if left == right:
            rs[index] = nums[right]**2
            break
            
        left_value = nums[left]
        right_value = nums[right]
        
        if abs(left_value) >= abs(right_value):
            rs[index] = nums[left]**2
            left += 1
        elif abs(left_value) < abs(right_value):
            rs[index] = nums[right]**2
            right -= 1
            
        index -= 1
            
    return rs

def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if len(arr) < 3:
        return False

    vertex = -1
    for i, v in enumerate(arr):
        if i == 0:
            continue
            
        if vertex == -1:
            if v == arr[i - 1]:
                return False
            if v < arr[i - 1]:
                vertex = i - 1
        elif vertex != -1:
            if v >= arr[i - 1]:
                return False             
        
    return True if vertex != -1 and vertex != 0 else False

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_one = 0
    temp_ones = []
    
    for i in nums:
        if i == 1:
            temp_ones.append(i)
            
        if len(temp_ones) > 0 and i == 0:
            temp_ones = []
            
        if len(temp_ones) > max_one:
            max_one = len(temp_ones)
            
    return max_one

def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    div_out = []
    mul_out = []
    div_index = []
    is_even = []
    
    for i, v in enumerate(arr):
        if v in div_out or v in mul_out:
            return True

        div_index.append(i)
        if v % 2 == 0:
            is_even.append(v)
            div_out.append(v / 2)
            mul_out.append(v * 2)
        else:
            is_even.append(None)
            div_out.append(None)
            mul_out.append(v * 2)

    return False