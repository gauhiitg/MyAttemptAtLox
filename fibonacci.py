'''
Fibonacci Sequence
-------------------------------------------------------------
'''

fib_cache = {}


def fib_memo(input_val):
   if input_val in fib_cache:
       return fib_cache[input_val]

   if input_val == 0:
       val = 0
   elif input_val < 2:
       val = 1
   else:
       val = fib_memo(input_val - 1) + fib_memo(input_val - 2)

   fib_cache[input_val] = val
   return val

n = int(input('enter the number'))
print('======== Fibonacci Series ========')
for i in range(1, n):
    print(f'Fibonacci ({i}) : {fib_memo(i)}')