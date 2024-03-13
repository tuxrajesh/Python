def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle the case where k is larger than the length of the array
    # Use slicing to efficiently rotate the array
    nums[:] = nums[-k:] + nums[:-k]
    pass

def check_duplicates(nums):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def find_single_instance(nums):
    """
    Find the number that occurs only once in a the sequence
    
    Example: nums = [4,1,2,1,2] should return 4
    """    
    seen = {}
    for num in nums:
        if num in seen.keys():
            seen[num] += 1
        else:
            seen[num] = 1
            
    single_instance = [key for key, value in seen.items() if value == 1]
    return single_instance

def singleNumber(nums):
    result = 0
    for num in nums:
        print(f"Before XOR: {result}")        
        result ^= num
        print(f"After XOR: {result}")
    return result

def intersection_of_arrays(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an 
    array of their intersection. Each element in the result 
    must appear as many times as it shows in both arrays and 
    you may return the result in any order.
    
    Example 1:
    >>> Input: nums1 = [1,2,2,1], nums2 = [2,2]
    >>> Output: [2,2]
    
    Example 2:
    >>> Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    >>> Output: [4,9]
    Explanation: [9,4] is also accepted.
    """
    result = []
    for num in nums1:
        if num in result:
            continue        
        print(f"Num: {num}")
        if num in nums2:
            count_of_num1 = nums1.count(num)
            count_of_num2 = nums2.count(num)
            print(f"Nums1: {count_of_num1}, Nums2: {count_of_num2}")
            if count_of_num1 >= count_of_num2:
                for i in range(count_of_num2):
                    result.append(num)
            else:
                for i in range(count_of_num1):
                    result.append(num)
    return result    

def plus_one(digits):
    """
    You are given a large integer represented as an integer array digits, where each 
    digits[i] is the ith digit of the integer. The digits are ordered from most 
    significant to least significant in left-to-right order. The large integer does not 
    contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.

    Example 1: Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].    
    """
    i = 1
    
    digits[-i] += 1
    
    while digits[-i] == 10 and i <= len(digits) - 1:
        digits[-i] = 0
        i += 1
        digits[-i] += 1
        
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    
    return digits

def move_zero(nums):
    """
    Given an integer array nums, move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.
    
    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
            
    while j < len(nums):
        nums[j] = 0
        j += 1
    return nums

def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the 
    two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you 
    may not use the same element twice. You can return the answer in any order.
    
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    for first in range(len(nums)):
        for next in range(first + 1, len(nums)):
            if nums[first] + nums[next] == target:
                return [first, next]
            
    num_dict = {}    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
    return None

def valid_sudoku(board):
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
    
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    """
    if len(board) != 9:
        return False
    
    import collections
    
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    
    for row in range(len(board)):        
        if len(board[row]) != 9:
            return False        
        
        for col in range(len(board)):
            if board[row][col] == ".":
                continue
            
            if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3,col//3)]:
                return False
                  
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[(row//3,col//3)].add(board[row][col])
    return True

def rotate(matrix):
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.  
    
    >>> Example:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14, 15, 16]]
    Output: [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    """
    n = len(matrix)
    for row in range(n):
         for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
    for row in range(n):
        matrix[row].reverse()
        
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print(rotate(matrix))

# print(intersection_of_arrays(nums1, nums2))