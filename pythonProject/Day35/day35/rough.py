class Add:
    def __int__(self):
        pass
    def add(self, digits):
        sum1 = str(digits[0])
        for i in range(1,len(digits)):
            sum1 = sum1 +"+"+ str(digits[i])
            print(f"{sum1}={sum(digits[:i+1])}")

nums = []
for i in range(6):
    nums.append(int(input()))

object = Add()
object.add(nums)