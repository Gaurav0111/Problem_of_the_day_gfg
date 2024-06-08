class Solution:

    def findExtra(self, n, a, b):

        # initializing pointers
        low = 0
        high = n - 2
        index = n - 1

        # binary search
        while (low <= high):

            mid = (low + high) // 2
            if (a[mid] == b[mid]):
                low = mid + 1
            else:
                index = mid
                high = mid - 1

        return index

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends