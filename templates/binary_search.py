"""
Given a `sorted array`, narrow down the search
range by half each interval.

Generic question:
- Find target in array, if not found return 0
arr = [1,3,4,5,6,7,9]
target = 3
- Start with mid, change left and right boundaries
to lower search area

Can further extend this pattern by making
the conditions generic with a `is_feasible`
function.
"""

class BinarySearch:
    
    def __init__(self, arr: list, target: int):
        self.arr = arr
        self.target = target

    def find_target(self) -> int:
        left, right = 0, len(self.arr)-1
        
        while left<=right:
            mid = (left+right)//2
            if self.arr[mid] == self.target:
                return mid
            if self.arr[mid] < self.target:
                # We know we won't find the target in
                # left half of array, might as well ignore it
                left = mid+1
            else:
                # Opposite of above branch, ignore right half.
                right = mid-1

    def generic_binary_search(self) -> int:
        left, right = 0, len(self.arr)-1
        res = -1

        while left <= right:
            mid = (left+right)//2
            if self.is_feasible(mid):
                res = mid
                right = mid-1   # or left=mid+1 depending on condition
            else:
                left = mid+1    # Same thing here
        
        return res

    def is_feasible(self, mid) -> bool:
        """
        A function that determines if condition is met to reduce
        the range of the binary search array.

        For example:
        trying to find first occurrence of a target.

        This is for seperation of concerns (and to keep your code clean)
        
        """
        if self.arr[mid] >= self.target:
            return True
        
        return False
            

        
