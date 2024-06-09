from typing import List


class Solution:

    def zigZag(self, n: int, arr: List[int]) -> None:
        flag = True

        for i in range(1, n):
            if flag:  # "<" relation expected
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[
                        i - 1]  # Swap arr[i - 1] and arr[i]
            else:  # ">" relation expected
                if arr[i - 1] < arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[
                        i - 1]  # Swap arr[i - 1] and arr[i]
            flag = not flag  # flip flag
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":

    def isZigzag(n: int, arr: List[int]) -> bool:
        f = 1

        for i in range(1, n):
            if f:
                if arr[i - 1] > arr[i]:
                    return False
            else:
                if arr[i - 1] < arr[i]:
                    return False
            f = f ^ 1

        return True

    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        obj.zigZag(n, arr)
        check = True
        check = isZigzag(n, arr)
        if check:
            print("1")
        else:
            print("0")

# } Driver Code Ends