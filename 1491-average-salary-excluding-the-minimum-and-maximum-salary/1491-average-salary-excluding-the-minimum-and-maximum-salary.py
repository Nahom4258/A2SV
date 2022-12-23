class Solution:
    def average(self, salary: List[int]) -> float:
        # define necessary variables
        my_sum = 0
        average = 0
        
        # sort the salary to make easier to exclude min and max salaries
        salary.sort()
        
        # add the salaries except max & min salaries
        for i in range(1, len(salary) - 1):
            my_sum += salary[i]
           
        # calculate the average
        average = my_sum / (len(salary) - 2)
        
        return average
        