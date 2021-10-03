str = """
(\__/)  
(='.'=) 
(")_(") """
N = int(input())
third = len(str)//3
print(str[1:third]*N, '\n', str[third+1:third*2]*N, '\n', str[third*2+1:]*N, sep='')