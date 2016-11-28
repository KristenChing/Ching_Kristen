#Kristen Ching
nums = [2, 6, 8, 9, 10, 12, 13, 15, 17, 24, 55, 66, 78, 77, 79]
def gFactor(num):
    for x in range(2, num):
        if num%x == 0:
            return 1
        else:
            return 0
def removeComposites():
    for num in nums:
        if gFactor(num) == 0:
            nums.remove(num)
removeComposites()
print(nums)
