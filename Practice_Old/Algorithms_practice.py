#find the max of a list in O(n):
def max_element(a):
    b = 0
    for i in a:
        if i > b:
            b = i
    return b

#finding prefix average in O(n):
def prefix_avg(a):
    b = [0]*len(a)
    b[0] = a[0]
    total = 0
    for i in range(len(a)):
            total = total + a[i]
            b[i] = total/(i+1)
    return b

#checking for duplicates in O(n):
def dup_element(a):
    count = 0
    for i in range(len(a)-1):
        if a[i] in a[i+1:]:
            count += 1
    if count > 0:
        return True
    else:
        return False


def isPowerOfThree(n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            n = float(format((n/3),'.8f'))
        else:
            a = n
        if a == 1:
            return True
        else:
            return False

def max_product(a):
    if a == []:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        b = max(a)
        a.pop(a.index(b))
        c = max(a)
        return b*c

#largest string without repetations:
def lengthOfLongestSubstring(s):
        a = []
        b = []
        if s == '':
            return 0
        else:
            for i in s:
                if i not in a:
                    a.append(i)
                    print(a)
                else:
                    b.append(a)
                    print(b)
                    a = [i]
        b.append(a)
        print(b)

#reversing an array
def reverse_array(a):
    temp = 0
    for i in range(int(len(a)/2)):
        temp = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp
    return a
        
