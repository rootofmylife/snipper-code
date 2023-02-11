# snipper-code

# To install the package:

```bash
pip3 install git+https://github.com/rootofmylife/snipper-code
```

# Usage:

```py
from snipper_code.main import checkIfExist

print(checkIfExist([10,2,5,3]))
# true
```

# API

`checkIfExist(arr: List[int]) -> bool`

Given an array arr of integers, check if there exist two indices i and j such that :

```
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
```

`findMaxConsecutiveOnes(nums: List[int]) -> int`

Given a binary array nums, return the maximum number of consecutive 1's in the array.

`sortedSquares(nums: List[int]) -> List[int]`

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

`validMountainArray(arr: List[int]) -> bool`

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

```
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
```