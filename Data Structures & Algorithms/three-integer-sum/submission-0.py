class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=sorted(nums)
        n=len(nums)
        result=[]
        for i in range(0,n):
            left=i+1
            right=n-1
            if i>0 and arr[i]==arr[i-1]:
                continue
            while left<right:
                sum=arr[i]+arr[right]+arr[left]
                if sum==0:
                    result.append([arr[i],arr[left],arr[right]])
                    left+=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                elif sum<0:
                    left+=1
                elif sum>0:
                    right-=1
        return result