# Question - 1

# import math 

# numbers = input("provide D : ")
# numbers = numbers.split(',')

# result_list = [ ]
# for D in numbers:
#     Q = round(math.sqrt(2 * 50 * int(D) / 30))
#     result_list.append(Q)
# print(result_list)


# Question - 2

# class Shape(object):

#     def __init__(self):
#       pass  
#     def area(self):
#         return(0)

# class Square(Shape):

#     def __init__(self,length=0):
#         Shape.__init__(self)
#         self.length = length 

#     def area(self):
#         print(self.length * self.length)
       
# s = Square(10)
# s.area()  


# Question - 3
# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# Question - 4
# class Time(object):
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours
#         self.minutes = minutes

#     @staticmethod
#     def addTime(time1, time2 ):
#         hours = time1.hours + time2.hours
#         minutes = time1.minutes + time2.minutes
#         hours += minutes//60
#         minutes %= 60
#         return Time(hours=hours, minutes=minutes)

#     def displayTime(self):
#         print("{hour} hour and {minutes} minutes".format(
#             hour=self.hours, minutes=self.minutes))

#     def displayMinute(self):
#         print("{minutes} minutes".format(
#             minutes= (self.hours * 60 + self.minutes)))

# t1 = Time(hours=2, minutes=50)
# t2 = Time(hours=1, minutes=20)

# t = Time.addTime(t1, t2)
# t.displayTime()
# t.displayMinute()  
         

# Question - 5
# class Person(object):
#     def __init__(self, age=0):
#         self.age = 0
#         if age < 0:
#             print("Age is not valid, setting age to 0")
#         else:
#             self.age = age
#     def yearPasses(self, years=0):
#         self.age += years
#         return self.age
#     def amIOld(self, age):
#         if age < 0:
#             print("Age is not valid, setting age to 0")
#         elif 0 <= age < 13:
#             print("You are young")
#         elif 12 < age < 20:
#             print("You are a teenager")
#         else:
#             print("You are old")

# p = Person()
# p.amIOld(-1)
# p.amIOld(4)
# p.amIOld(10)
# p.amIOld(16)
# p.amIOld(18)
# p.amIOld(64)
# p.amIOld(38)

# p2 = Person(38)
# print(p2.yearPasses(4))