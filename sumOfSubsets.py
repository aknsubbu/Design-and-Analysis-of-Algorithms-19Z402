# program to find the all possible subsets of the given list using backtracking 

class sumOfSubsets:
    def __init__(self,array,target):
        self.subsets = []
        self.array = array
        self.total = 0
        self.target  = target

    def checkSafe(self,subset):
        if sum(subset) == self.target:
            return True
        return False
    
    def findSubsets(self):
        subsets=[]

            #find all possible combinations without applying checkSafe or checking target
            # find only the possible combinations
        def findCombinationsUtil(start,subset):
            if start == len(self.array):
                subsets.append(subset)
                return
            findCombinationsUtil(start+1,subset)
            findCombinationsUtil(start+1,subset+[self.array[start]])

        
        findCombinationsUtil(0,[])

            
        return subsets,len(subsets)
    

    def findSubsetsWithSum(self,combinations):
        subsets=[]
        for subset in combinations:
            if self.checkSafe(subset):
                subsets.append(subset)
        
        return subsets,len(subsets)



if __name__ == "__main__":
    test = sumOfSubsets([1,2,3,4,5,6,7,8,9],10)
    print(test.findSubsetsWithSum(test.findSubsets()[0]))