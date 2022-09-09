def findRemainder(n, k):
    
  for i in range(1, n + 1):
    # rem will store the remainder 
    # when i is divided by k.
    rem = i % k  
      
    print(i, "mod", k, "=", 
          rem, sep = " ")
  
# Driver code
if __name__ == "__main__" :
    
  # inputs
  n = 5
  k = 3
    
  # function calling
  findRemainder(n, k)