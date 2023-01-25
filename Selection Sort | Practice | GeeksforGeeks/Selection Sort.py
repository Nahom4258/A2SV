// { Driver Code Starts
import java.util.*;

class GFG
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t>0)
		{
			int n = sc.nextInt();
			int arr[] = new int[n]; 
			for(int i=0;i<n;i++)
			{
				arr[i] = sc.nextInt();
			}
		
			Solution obj = new Solution();
			obj.selectionSort(arr, n);
			
			for(int i=0;i<n;i++)
		    	System.out.print(arr[i]+" ");
		    System.out.println();
			t--;
		}
		
	}
}
// } Driver Code Ends


class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int selected = arr[i];
        for (int j = i + 1; j < arr.length; j++) {
            if (selected > arr[j]) {
                selected = arr[j];
            }
        }
        return selected;
	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    for(int i = 0; i<n; i++){
	        if(arr[i] != select(arr, i)){
	            int index = 0;
	            for(int j = i + 1; j<n; j++){
	                if(arr[j] == select(arr, i))
	                    index = j;
	            }
	            
	            int temp = arr[i];
	            arr[i] = arr[index];
	            arr[index] = temp;
	        }
	    }
	}
}
