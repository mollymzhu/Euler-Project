# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:42:43 2016

@author: mollyz
"""
from numpy import prod
import math
import os
#os.chdir('''''')

# shared function #
def is_prime(number):
    assert type(number) is long or type(number) is int, "n must be int or long"
    if number <= 1:
        return False

    if number == 2:
        return True
        
    if number%2 == 0:
        return False
    i = 3
    while i <= 1 + int(sqrt(number))+1:
        if (number <> i) & (number % i == 0):
            return False
        i += 2
    return True
    
    
def fibo(n):
    output = [1]
    assert type(n) is int, "n must be int"
    assert n > 0, "n must be positive"
    if n == 1:
        return output

    output.append(2)
    if n == 2:
        return output
    for i in range(2,n):
        output.append(output[i-2]+output[i-1])
    return output
    
    
def find_factors(n):
    output = [1,n]
    assert type(n) is long or type(n) is int, "n must be int"
    assert n > 0, "n must be positive"
    if n==1:
        return output
    i = 2

    while i <= long(math.sqrt(n)):
        if n % i == 0:
            output.append(i)
            if i != n/i:
                output.append(n/i)
        i += 1
    return sorted(output)
            
def next_prime(min):
    i = min + 1
    while is_prime(i)==False:
        i+=1
    return i
        
###############################################    
###############################################
# problem 1 #   

natural_num = range(1,1000)
natural_num_3_5 = [num for num in natural_num if num%3 == 0 or num%5 ==0]
sum(natural_num_3_5)
    
    
###############################################
# problem 2 #     
def sum_even_fibo(max):
    running_fibo = [1,2,3]
    running_sum = 2
    while running_fibo[2] < max:
        running_fibo[0:2] = running_fibo[1:3]
        running_fibo[2] = running_fibo[0] + running_fibo[1]
        if (running_fibo[2]%2 == 0) & (running_fibo[2] <= max):
            running_sum += running_fibo[2]          
    return running_sum

###############################################
# problem 3 #
def find_prime_factors(n):
    output = find_factors(n)
    return [num for num in output if is_prime(num) == True]

print find_prime_factors(600851475143)

   
###############################################
# problem 4 #     
def is_palindrome(n):
    assert type(n) is int, "n must be int"
    assert n > 0, "n must be positive"
    return (str(n)==str(n)[::-1])
    
def is_prod_of_3_digit(n):
    if n < 100*100:
        return False
    if n > 999*999:
        return False
    for i in range(100,1000):
        if (n%i == 0) & (n/i >=100) & (n/i <=999):
            return True
    return False
    
def print_largest_palindrome_prod_of_3_digit():
    n = 999*999
    while n>=100*100:
        if is_palindrome(n) == True & is_prod_of_3_digit(n) == True:
            print n
            break
        n -= 1
    return None
    
###############################################
# problem 5 #     
prime_num = 2

product = 1
n=20
while prime_num <= n:
    power = 0
    while pow(prime_num,power+1)<=n:
        power+=1
    product*=pow(prime_num,power)
    print (prime_num,pow(prime_num,power),product)
    prime_num = next_prime(prime_num)
    
print product
    
###############################################
    
    
def sum_square_diff(n):
    assert type(n) is int, "n must be int"
    assert n > 0, "n must be positive"
    sum_of_square = sum([x*x for x in range(1,n+1)])
    square_of_sum = sum(range(1,n+1)) * sum(range(1,n+1)) 
    return abs(sum_of_square - square_of_sum)
    
def find_greatest_prod_adjcent_n_digit(input_number, n):
    if type(input_number) is str:
        string = input_number
    else:
        string = str(input_number)
    greatest_prod = long()
    greatest_string = []
    product = long()
    for i in range(len(string)-n+1):
        digits = [int(x) for x in string[i:i+n]]
        product = prod(digits,dtype = long)
        
        if product > greatest_prod:
            greatest_prod = product
            greatest_string = digits
            #print product, digits
    return greatest_prod,greatest_string
        
    
    
def print_test_eight():
    a='73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'
    a = a.replace('\n','')
    print find_greatest_prod_adjcent_n_digit(a,13)

###############################################
# problem 7 #
prime = 2
for i in range(1,10001):
    prime = next_prime(prime)
    
print prime

###############################################
# problem 9 # 
def prob_9():
    for i in range(1,1000):
        for j in range(i+1,1000):
            if 2*i*j == 2000*(i+j)-1000000:
                print i,j,1000-i-j

###############################################
# problem 10 #
output = [i for i in range(3,2000000)[::2] if is_prime(i)==True]
output.append(2)
print(sum(output))

###############################################
# problem 13 # 
def prob_13():
    a='37107287533902102798797998220837590246510135740250\
46376937677490009712648124896970078050417018260538\
74324986199524741059474233309513058123726617309629\
91942213363574161572522430563301811072406154908250\
23067588207539346171171980310421047513778063246676\
89261670696623633820136378418383684178734361726757\
28112879812849979408065481931592621691275889832738\
44274228917432520321923589422876796487670272189318\
47451445736001306439091167216856844588711603153276\
70386486105843025439939619828917593665686757934951\
62176457141856560629502157223196586755079324193331\
64906352462741904929101432445813822663347944758178\
92575867718337217661963751590579239728245598838407\
58203565325359399008402633568948830189458628227828\
80181199384826282014278194139940567587151170094390\
35398664372827112653829987240784473053190104293586\
86515506006295864861532075273371959191420517255829\
71693888707715466499115593487603532921714970056938\
54370070576826684624621495650076471787294438377604\
53282654108756828443191190634694037855217779295145\
36123272525000296071075082563815656710885258350721\
45876576172410976447339110607218265236877223636045\
17423706905851860660448207621209813287860733969412\
81142660418086830619328460811191061556940512689692\
51934325451728388641918047049293215058642563049483\
62467221648435076201727918039944693004732956340691\
15732444386908125794514089057706229429197107928209\
55037687525678773091862540744969844508330393682126\
18336384825330154686196124348767681297534375946515\
80386287592878490201521685554828717201219257766954\
78182833757993103614740356856449095527097864797581\
16726320100436897842553539920931837441497806860984\
48403098129077791799088218795327364475675590848030\
87086987551392711854517078544161852424320693150332\
59959406895756536782107074926966537676326235447210\
69793950679652694742597709739166693763042633987085\
41052684708299085211399427365734116182760315001271\
65378607361501080857009149939512557028198746004375\
35829035317434717326932123578154982629742552737307\
94953759765105305946966067683156574377167401875275\
88902802571733229619176668713819931811048770190271\
25267680276078003013678680992525463401061632866526\
36270218540497705585629946580636237993140746255962\
24074486908231174977792365466257246923322810917141\
91430288197103288597806669760892938638285025333403\
34413065578016127815921815005561868836468420090470\
23053081172816430487623791969842487255036638784583\
11487696932154902810424020138335124462181441773470\
63783299490636259666498587618221225225512486764533\
67720186971698544312419572409913959008952310058822\
95548255300263520781532296796249481641953868218774\
76085327132285723110424803456124867697064507995236\
37774242535411291684276865538926205024910326572967\
23701913275725675285653248258265463092207058596522\
29798860272258331913126375147341994889534765745501\
18495701454879288984856827726077713721403798879715\
38298203783031473527721580348144513491373226651381\
34829543829199918180278916522431027392251122869539\
40957953066405232632538044100059654939159879593635\
29746152185502371307642255121183693803580388584903\
41698116222072977186158236678424689157993532961922\
62467957194401269043877107275048102390895523597457\
23189706772547915061505504953922979530901129967519\
86188088225875314529584099251203829009407770775672\
11306739708304724483816533873502340845647058077308\
82959174767140363198008187129011875491310547126581\
97623331044818386269515456334926366572897563400500\
42846280183517070527831839425882145521227251250327\
55121603546981200581762165212827652751691296897789\
32238195734329339946437501907836945765883352399886\
75506164965184775180738168837861091527357929701337\
62177842752192623401942399639168044983993173312731\
32924185707147349566916674687634660915035914677504\
99518671430235219628894890102423325116913619626622\
73267460800591547471830798392868535206946944540724\
76841822524674417161514036427982273348055556214818\
97142617910342598647204516893989422179826088076852\
87783646182799346313767754307809363333018982642090\
10848802521674670883215120185883543223812876952786\
71329612474782464538636993009049310363619763878039\
62184073572399794223406235393808339651327408011116\
66627891981488087797941876876144230030984490851411\
60661826293682836764744779239180335110989069790714\
85786944089552990653640447425576083659976645795096\
66024396409905389607120198219976047599490197230297\
64913982680032973156037120041377903785566085089252\
16730939319872750275468906903707539413042652315011\
94809377245048795150954100921645863754710598436791\
78639167021187492431995700641917969777599028300699\
15368713711936614952811305876380278410754449733078\
40789923115535562561142322423255033685442488917353\
44889911501440648020369068063960672322193204149535\
41503128880339536053299340368006977710650566631954\
81234880673210146739058568557934581403627822703280\
82616570773948327592232845941706525094512325230608\
22918802058777319719839450180888072429661980811197\
77158542502016545090413245809786882778948721859617\
72107838435069186155435662884062257473692284509516\
20849603980134001723930671666823555245252804609722\
53503534226472524250874054075591789781264330331690'

    parts = [a[i:i+50] for i in range(0, len(a), 50)]
    sum_parts = sum(int(x) for x in parts)
    print sum_parts

###############################################
# problem 14 #   
def collatz_next(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

def length_collatz(max):
    seq_length ={1:1,2:2}

    start = 3
    
    while start <= max:
        running_len = 1
        next_num = collatz_next(start)
        while next_num not in seq_length:
            running_len+=1
            next_num = collatz_next(next_num)
        running_len += seq_length[next_num]
        seq_length[start] = running_len
        start +=1
    return seq_length

col = length_collatz(1000000)
maximum = max(col, key=col.get)  
print(maximum, col[maximum])

###############################################
# problem 15 #   
print math.factorial(40)/math.factorial(20)/math.factorial(20)

###############################################
# problem 25 #     
def find_fibo_index(min):
    running_fibo = [1,2,3]
    running_index = 4
    while running_fibo[2] < min:
        running_fibo[0:2] = running_fibo[1:3]
        running_fibo[2] = running_fibo[0] + running_fibo[1]
        running_index += 1
    return running_index
    
find_fibo_index(pow(10,999))

###############################################
# problem 27 #

n_max=0

for b in range(1,1001):
    for a in range(-b-1,1001):
        n=0
        while is_prime(n*n+a*n+b):
            n += 1
        if n > n_max:
            n_max = n
            a_max = a
            b_max = b
            
print a_max*b_max

##################################################
# problem 48 #  

     
def self_power(n):
    power_sum = long()
    for i in range(1,n+1):
        power_sum += pow(i,i)
    return power_sum
       

###############################################
# problem 49 #        

def split_number_to_digits(n,sort=0):
    string = str(n)
    digits = [int(digit) for digit in string]
    if sort == 1:
        digits.sort()
    return digits

def list_to_string(list):
    string = ''
    for x in list:
        string += str(x)
    return string



def find_arithmetic_sequence(list_of_num):
    output = []
    sorted_seq=[]
    l = len(list_of_num)
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                sorted_seq = [list_of_num[i],list_of_num[j],list_of_num[k]]
                sorted_seq.sort()
                #print sorted_seq
                if sorted_seq[1] == 0.5*(sorted_seq[0]+sorted_seq[2]):
                    output.append(sorted_seq)
    return output
    
def problem_49():
    d = dict()
    key = ''
    for i in range(1000,10000):
        key = list_to_string(split_number_to_digits(i,1))
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    #print d
    prime_permu = []
    for key in d:
        prime_permu = [permu for permu in d[key] if is_prime(permu)==True]
        if (len(prime_permu)>=3) & (find_arithmetic_sequence(prime_permu) != []):  
            print find_arithmetic_sequence(prime_permu)
            #print key, prime_permu
            
            
            
###############################################
# problem 52 #
               
def problem_52():
    i = long()
    flag = False
    while i < pow(2,32):
        #print i,split_number_to_digits(i)[0]
        if split_number_to_digits(i)[0] == 1:
            flag = True
            key = split_number_to_digits(i,1)
            for j in range(2,7):
                if split_number_to_digits(j*i, 1) != key:
                    flag = False
                if flag == False:                    
                    break
        if flag == True:
            print i
            break
        i += 1
        
###############################################
# problem 63 #
def problem_63():
    n = 1
    count = 0
    while (len(split_number_to_digits(pow(9,n))) >= n) & (n<=100000):
        for j in range(1,10):        
            if len(split_number_to_digits(pow(j,n))) == n:
                #print j,n,pow(j,n)
                count += 1
        n += 1
        #print n
    print count
        

       
###############################################
# problem 81 #
class elements_81(object):

    def __init__(self,row,column,value):
        self.row = row
        self.column = column
        self.value = value
        self.direction = ''
        self.sum_to_end = None
        
    def set_direction_and_sum(self,value_if_r, value_if_d):
        if value_if_r <= value_if_d:
            self.direction = 'r'
            self.sum_to_end = self.value + value_if_r
        else:
            self.direction = 'd'
            self.sum_to_end = self.value + value_if_d


def find_shortest_path(input_matrix):
    n = len(input_matrix)
    calc_matrix = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            calc_matrix[i][j] = elements_81(i,j,input_matrix[i][j])
    
    # last element        
    calc_matrix[n-1][n-1].sum_to_end = calc_matrix[n-1][n-1].value
    
    # last row can only move right
    for i in list(range(n-1))[::-1]:
        calc_matrix[n-1][i].direction = 'r'  
        calc_matrix[n-1][i].sum_to_end = calc_matrix[n-1][i].value + calc_matrix[n-1][i+1].sum_to_end 
    # last col can only move down    
    for i in list(range(n-1))[::-1]:    
        calc_matrix[i][n-1].direction = 'd'
        calc_matrix[i][n-1].sum_to_end = calc_matrix[i][n-1].value + calc_matrix[i+1][n-1].sum_to_end 
        
    for k in range(1,n):
        for i in list(range(n-k))[::-1]:
            #print n-k-1,i,input_matrix[n-k-1][i],calc_matrix[n-k-1][i+1].value,calc_matrix[n-k][i].value
            calc_matrix[n-k-1][i].set_direction_and_sum(calc_matrix[n-k-1][i+1].sum_to_end, calc_matrix[n-k][i].sum_to_end)
            calc_matrix[i][n-k-1].set_direction_and_sum(calc_matrix[i][n-k].sum_to_end, calc_matrix[i+1][n-k-1].sum_to_end)
            
    return calc_matrix[0][0].sum_to_end

def problem_81():
    input_matrix = [
    [131,  673,	234,	103,	18],
    [201,	96,	342,	965,	150],
    [630,	803,	746,	422,	111],
    [537,	699,	497,	121,	956],
    [805,	732,	524,	37,	331]]
    assert find_shortest_path(input_matrix)==2427, 'result incorrect'
    
    with open ( 'p081_matrix.txt' , 'r') as f:
        l = [ map(int,line.split(',')) for line in f ]
    #print len(l)
    print find_shortest_path(l)
###############################################
# problem 92 #
def digits_square(n):
    return sum([i*i for i in split_number_to_digits(n)])

def return_stop(n):
    while n != 89 and n != 1:
        n=digits_square(n)
    return n
    
output= {1:1}
n=10000000
for i in range(2,n):
    stop = False
    j = i
    while stop == False:
        j = digits_square(j)
        #print (i,j)
        if j in output:
            output[i]=output[j]
            stop = True
        if j == 1 or j == 89:
            output[i] = j
            stop = True
    i+=1
            
#output
sum( stop_value == 1 for stop_value in output.values() )   
10000000-1-1418853

###############################################
# problem 99 #

def problem_99():
    with open ( 'p099_base_exp.txt' , 'r') as f:
        l = [ map(int,line.split(',')) for line in f ]   
    max_exp = 0.0
    line_num = 0
    for i, number in enumerate(l):
        if number[1]*math.log(number[0]) > max_exp:
            max_exp = number[1]*math.log(number[0])
            line_num = i
    print line_num
    
###############################################
# problem 100 #   
n=1000000000000-1
p=0
stop = False
while stop == False:
    n += 1
    p = 0.5* (1+ math.sqrt(1+2*n*n-2*n))    
    if p%1==0:
        if int(p)*(int(p)-1)*2 == (n*(n-1)):
            stop = True
    
#int(p)*(int(p)-1)*2 == (n*(n-1)) 
print (n,p)
#the above doesn't work for the initial value

#using quadratic diophantine equation
#https://www.alpertron.com.ar/QUAD.HTM
n = 21
p = 15
target = 1000000000000
while n < target:
    n_temp = 4*p + 3*n - 3
    p_temp = 3*p + 2*n - 2
    n = n_temp
    p = p_temp
    
print (n,p)
    
###############################################
# problem 243 #   

    
def share_factor(a,b):
    if a==1 or b==1:
        return False
    if a == b:
        return True
    if a%2==0 and b%2==0:
        return True
    i = 3
    while i <= min(a,b):
        if a%i==0 and b%i ==0:
            return True
        i+=1
    return False
    
def find_resilient_fraction(n):
    natural_num = range(1,n)
    resilient = [num for num in natural_num if not share_factor(num,n)]
    return float(len(resilient))/float(n-1)
#while find_resilient_fraction(d)>=float(15499)/float(94744):
#    d+=1
#print d
def find_shared_fraction(n):
    natural_num = range(1,n)
    shared = [num for num in natural_num if share_factor(num,n)]
    return len(shared)

def totient_function_for_prime_factorial(max_prime):
    assert is_prime(max_prime)
    i = 2
    factorial = 1
    fraction = 1
    while i<=max_prime:
        factorial *= i
        fraction*=(1-1.0/float(i))
        i = next_prime(i)
    return int(factorial* fraction)
    
    
d = 1  #starting value
d_min = 6
running_core = 6
running_max_prime = 3

running_shared = find_shared_fraction(running_core)
running_fraction = find_resilient_fraction(running_core)
#ceiling = 0.25
ceiling=float(15499)/float(94744)
while running_fraction>=ceiling:
    
    for i in range (2,next_prime(running_max_prime)): 
        d = running_core*i
        
        running_fraction = float(totient_function_for_prime_factorial(running_max_prime)*i)/float(d-1)
        #print (d, running_fraction)
        if running_fraction<ceiling:
                d_min = d
                break
    if running_fraction<ceiling:
        break
    running_max_prime = next_prime(running_max_prime)

    running_core *= running_max_prime    
  
    d = running_core
    running_fraction = float(totient_function_for_prime_factorial(running_max_prime))/float(d-1)
    d_min = d
    #print (d, running_fraction)
    #print d
 
print (ceiling,d_min)      
      
###############################################
# problem 429 #  
      
n=100000000
fac = math.factorial(n)

natural_num = range(1,fac+1)
unitary_divisor = [num for num in find_factors(math.factorial(n)) if not share_factor(num,math.factorial(n)/num)]
print unitary_divisor

# max power of prime p as a factor of factorial n!
def Legendre(n,p):
    assert is_prime(p)
    i = 1    
    sum = 0
    while i<= math.log(n,p):
        sum += int(math.floor(n/pow(p,i)))
        i += 1
    return sum

def find_prime_factors(n):
    return [x for x in find_factors(n) if is_prime(x)]    
    
def per(n):
    output = []
    i = 0
    while i < (1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        output.append(map(int,list(s)))
        i += 1
    return output

n_max = 20
output = [1,3,8,24]

for n in range(5,n_max+1):
    if is_prime(n):
        output += [x*n for x in output]

    else:
        prime_fac = find_prime_factors(n)
        for p in prime_fac:
            power = Legendre(n,p)-Legendre(n-1,p)
            output = [x*pow(p,power) if x%p==0 else x for x in output]
    #prime_fac = [pow(p,Legendre(n,p)) for p in xrange(1,n+1) if is_prime(p)]
    n += 1    
    #print output
    print sum(i*i for i in output)%1000000009
    
    
    iter_all = per(len(prime_fac))
    
    for it in iter_all:
        temp = [a*b for a,b in zip(prime_fac,it)]
        output.append(int(prod([i for i in temp if i!=0])))

    print output
    print sum(i*i for i in output)
