#Checks if a number is even or odd
def checkOE():
    num = int(input("Enter a number:"))
    if num%2 == 1:
        print('The number you entered is odd')
    elif num%4 == 0:
        print('The number you entered is divisible by 4')
    else:
        print('The number is even') 
    
#prints out a string that says if a number is divisible by another
def check_div(num,check):
    if num%check == 0:
        print('The number is divisible by {}' .format(check))
    else:
        print('The number is not divisible by {}'.format(check))

#prints out a list of all integers < a user specified input
def under_ten(a):
    b = int(input("Enter a number:"))
    c = [i for i in a if i < b]
    print(c)

#prints out a list of all the factors 
def factors(a):
    b = []
    for i in range(1,a+1):
        if (a%i) == 0:
            b.append(i)
    print(b)

#compares and prints the common objects in a list to a new list without repetation
def common_list(a,b):
    c = []
    for i in a:
        if i in b:
            if i not in c:
                c.append(i)
    print(c)

def common_list1(a,b):
    return (a&b)

#read a string and verify if its a palindrome
def palindrome(a):
    b = list(a)  #it is not necessary to convert the string into a list, but if we need to change in-place, it will help.
    b.reverse()
    c = list(a)
    if c == b:
        print('its a palindrome')
    else:
        print('not a palindrome')

def palindrome_trivial(a):
    #b = list(a)
    count = 0
    for i in range(int(len(a)/2)+1):
        if a[i] == a[ len(a) -i - 1]:
            count +=1
        else:
            count+=0
    if count >= int(len(a)/2):
        print('its a palindrome')
    else:
        print('not a palindrome')

#make a new list of all even numbers from a given list in one line
def even_list(a):
    b=[i for i in a if i%2 == 0]
    return b

#guess a random number
def guess_num():
    import random
    
    str_input = ''
    count = 0
    while str_input is not 'exit':
        b = random.randint(1,9)
        count += 1
        i_input = input("enter a number:")
        if i_input == 'exit':
            str_input = 'exit'
        elif int(i_input) == b:
            print('correct')
        elif int(i_input) > b:
            print(b)
            print('too high')
        else:
            print(b)
            print('too low')
    print("number of attempts:{}".format(count - 1))

#prime or not
def primality(a):
    c = []
    for i in range(1, a+1):
        if a%i == 0:
            c.append(i)
    if c == [1,a]:
        print('the number is prime')
    else:
        print('the number is not prime. These are its factors: {}'.format(c))

#fibonacci series
def fibonacci_seq(n):
    a = [0,1]
    for i in range(1,n+1):
        a.append( a[i] + a[i-1])
    print(a)

#list remove duplicates
def rem_dup_list(a):
    a = list(a)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

def rem_dup_set(a):
    a = list(a)
    b = list(set(a))
    return b

#reverse word order
def rev_word():
    a = input("enter a string:")
    b = a.split(" ")
    c = []
    for i in range(len(b)):
        c.append(b[len(b) - i - 1])
    b.reverse()
    print(" ".join(b))
    return c

#find the median of sorted arrays
def findMedianSortedArrays(nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) == 0:
            return 0
        elif len(nums3) == 1:
            return nums3[0]
        elif len(nums3) % 2 == 1:
            return nums3[int(len(nums3)/2)]
        else:
            a = float((nums3[int(len(nums3)/2) -1] + nums3[int(len(nums3)/2)]))
            return a/2

#sum of two numbers in an array equals target
def twoSum(nums, target):
    a = []
    if len(nums) <= 1:
        return False
    else:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    a.append(i)
                    a.append(j)
    return a

def twoSum1(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1

#finding hamming distance
def hammingDistance(x, y):
        count = 0
        z = x^y
        z = list(bin(z)[2:])
        for i in z:
            if i == '1':
                count += 1
        return count

#find the sum of all digits
def addDigits(num):
        #d = [int(i) for i in list(str(num))]
        #num = sum(d)
        while num>9:
            d = [int(i) for i in list(str(num))]
            num = sum(d)
            addDigits(num)
        else:
            return num

def findContentChildren(g, s):
        count = 0
        a = []
        s = list(set(s))
        print(s)
        for i in s:
            if i in g:
                count += 1
                g.remove(i)
                a.append(i)
            
        print(count)
        g.sort()
        for i in a:
            s.remove(i)
        
        for i in s:
            for j in g:
                if i > j:
                    count += 1
                    g.remove(j)
                    break

#Ransom Note
def canConstruct(ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

def canConstruct(ransomNote, magazine):
        count = 0
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        
        if ransomNote == [] and magazine == []:
            return True
        else:
            for i in ransomNote:
                if i in magazine:
                    magazine.remove(i)
                    count += 1
                    
                    
        if count == len(ransomNote):
            return True
        else:
            return False
                
#intersection of two arrays
   # def intersection(nums1, nums2):
    #    return list(set(nums1)&set(nums2))

#sum if squares of n integers
def sum_of_squares(n):
    count = 0
    for i in range(n+1):
        count += i**2
    return count

#check if integer repeats
def int_rep(a):
    import collections
    b = list(dict(collections.Counter(a)).values())
    if 2 in b:
        print('repetitions yes')
    else:
        print('no repetitions')

#p-norm
def norm(v,p=2):
    a = [i**p for i in v]
    b = sum(a)**(1/p)
    print(b)

#int to binary
def converti_b(a):
    c = 0
    while a>0:
        b = a%2
        a = int(a/2)
        c += 1
    return c

def firstUniqChar(s):
        count = [0]*len(s)
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    count[i] += 1
        print(count)

        if s == '':
            return -1
        else:
            if 1 in count:
                for i in range(len(count)):
                    if count[i] == 1:
                        return i 
                        break
            else:
                return -1


#def firstUniqChar_1(s):

#find integer value of excel column
def titleToNumber(s):
        count = 0
        a = len(s)
        for i in range(a):
            count+= (26**(a-i-1))*(ord(s[i])-64)
            
        return count








            
