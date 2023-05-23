#User function Template for python3

class Solution:
    def heappop(self,heap):
        if not heap:
            return None
        min_value = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        current = 0
        self.heapify_down(heap, len(heap), current)
        return min_value

    def heapify_down(self,arr, n, current):
        small=current
        left=(2*current)+1
        right = (2*current)+2
        if right < n and arr[right]<arr[small]:
            small=right
        if left < n and arr[left] < arr[small]:
            small = left
        
        if small!=current:
            arr[small],arr[current]=arr[current],arr[small]
            self.heapify_down(arr,n,small)
            
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        parent=(i-1)//2
        if i>0 and arr[i]<arr[parent]:
            arr[i],arr[parent]=arr[parent],arr[i]
            self.heapify(arr,n,parent)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(len(arr)):
            self.heapify(arr,n,i)

    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        result=[]
        
        while arr:
            result.append(self.heappop(arr))
        
        arr.extend(result)
            
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends