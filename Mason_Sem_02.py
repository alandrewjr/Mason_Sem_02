#def Testr():
# return "Hello World!"
#print(Testr())

def sum_of_digits(n):
    l = list(str(n))
    tot = 0
    for x in l:
        tot = tot + int(x)
    return tot
#print(sum_of_digits(33003))


def SumOfList(li):
    tot = 0
    for x in li:
        tot = tot + int(x)
    return tot

def multiply_until_total_reached(original, total, n):
    NumOfLoops = 0
    List1 = []
    List1.append(original)
    Product = original

    while SumOfList(List1) < total:
        NLI = Product * n
        List1.append(NLI)
        Product = NLI
        NumOfLoops = NumOfLoops + 1
    return NumOfLoops

#print(multiply_until_total_reached(2, -9, 5))

def count_2d(xss, v):
    count = 0
    for item in xss:
        for item2 in item:
            if item2 == v:
                count += 1
    return count

#print(count_2d([[2,3,3],[4,3,5]], 3))

def locate_second_divisor(xs, n):
    count = 0
    ReturnText = ""
    for x in range(len(xs)):
        TheItem = xs[x]
        mod = n % TheItem
        if mod == 0:
            count += 1
            if count == 2:
                return x
                break
    if count == 0:
        return None

#print(locate_second_divisor([20,3,5,9,3], 12))

def all_primes(xs):
    prime = True
    for num in xs:
        if prime:
    
            if num > 1:
                # check for factors
                for i in range(2,num):
                    if (num % i) == 0:
                        prime = False
                        #print(num,"is not a prime number")
                        break
                else:
                    prime = True
                    #print(num,"is a prime number")
                    #if input number is less than or equal to 1, it is not prime
            else:
                prime = False
                #print(num,"is not a prime number")
        else:
            break
    
    
    

    return prime
    
                

print(all_primes([5,2,11,37]))