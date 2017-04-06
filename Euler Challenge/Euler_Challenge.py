#Challenge 1: Sum of multiple of 3 or 5 under 1000
# numbers = [num for num in range(1000)]
# print len(numbers)

# sum = 0
# for num in numbers:
#     if num%3 == 0 or num%5 == 0:
#         sum += num

# print sum

#Challenge 2:Even Finnacci numbers  
# fib_list = [1,2]
# value = 0
# while (value <= 4000000):
#     lens = len(fib_list) - 1
#     value = fib_list[lens-1] + fib_list[lens]
#     fib_list.append(value)

# sum = 0
# for num in fib_list:
#     if num % 2 == 0:
#         sum += num

# print sum

#Challenge 3: Largest prime factor 
# value = 1
# num = 600851475143
# nums = num/71
# nums = nums/839
# nums = nums/1471
# newvalue = 0

# for i in range(1,1000000):
#     if nums%i == 0 and i != 1:
#         newvalue = i
#         break

# print newvalue

#Challenge 4:Largest Pallidrome product
# largest = 0
# list = [i for i in range(1,999)]

# def is_pall(num):
#   str_num = str(num)
#   rev = ""
#   for i in str_num:
#       rev += str_num[len(str_num) - str_num.index(i) - 1]
#   if (rev == str_num):
#       return True
#   else:
#         return False

# for num in list:
#     for num1 in list:
#         num2 = num1 * num
#         if (is_pall(num2)):
#             if(num2 >= largest):
#                 largest = num2

# print largest

#Challenge 5: Smallest Multiple 
# Smallest Number That is divisable by 1 to 20 (With Online Assistance)
# def find():
#     i = 0
#     while True:
#         i += 10
#         if divide(i):
#             return i
# def divide(num):
#     for i in range(1, 21):
#         if not num%i == 0:
#             return False
#     return True
# print find()

#Challenge 6: Sum Square Difference 
#The difference between the sum of first 100 numbers each squared 
#and the sum of first 100 number total squared

# list = [i for i in range(1,101)]

# sq_sum = 0
# sum_sq = 0
# sum_dif = 0
# for i in list:
#     sum_sq += i
#     sq_sum += i ** 2

# sum_dif = sum_sq ** 2 - sq_sum
# print sum_dif

#Challenge 7: 10001st Prime Number
#2,3,5,7,11,13 first 5 prime numbers 

# def prime(n,c):
#     prime = []
#     sieve = [True] * (n+1)
#     for p in range(2,n+1):
#         if (sieve[p]):
#             prime.append(p)
#             for i in range(p,n+1,p):
#                 sieve[i] = False

#     print prime[c-1]

# print (prime(1000000,10001))
# 104743
# Learned a new way to find primes using the sieve method!

#Challenge 8: Largest Product in the Series
#Product of the largest 13 adjacent values in 1000 digit number 

# num = """
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# """

# products = []
# product = 1
# pure_num = ""

# for i in range(0,len(num)):
#     try:
#         x = int(num[i])
#         pure_num += num[i]
#     except ValueError:
#         continue

# for i in range(0,len(pure_num)):
#     if (i + 13 < len(pure_num)):
#         for j in range(i,i+13):
#             product *= int(pure_num[j])
#         products.append(product)
#         product = 1
    
# print max(products)
#5000940
# Pitfalls: indicies manipulation, resetting product to 1 and purifying given number literal 

#Challenge 9: Special Pythagorean Triple 
# a + b + c = 1000 find the product of abc

# a = b = c = 0
# n = 1
# m = 2
# for nth in range (n,500):
#     for mth in range(n,500):
#         a = nth ** 2 - mth ** 2
#         b = 2 * nth * mth
#         c = nth ** 2 + mth ** 2
#         if ((a + b + c == 1000) and a > 0 and b > 0 and c > 0):
#             print a*b*c


















