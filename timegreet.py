print("Calculator using functions")
def summ(*nums):
    for i in nums:
        sum=0
        sum=sum+i
    return sum   
userInput=input("Enter number seprated by comma ,")
elem=userInput.strip().split(',')
myTuple=tuple(map(int,elem))
# print(type(myTuple[0]))
# print(myTuple[0])
x=summ(*myTuple)
print(x)