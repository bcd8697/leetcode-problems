# на вход функции подается строка, в которой присутствуют символы "*"
# нужно написать функцию, которая будет заменять несколько "*" идущих подряд на одну "*"
# при этом нет ограничений по памяти, а сложность алгоритма - линейная, O(n)

# "****Hello*guys***!**" -> "*Hello*guys*!*"
  
  def spaces(s):
    
    character = "*"
    res = ""
    counter = 0
    
		for i in s:
      if i == "*" and counter >= 1:
        counter += 1
        
      elif i == "*" and counter == 0:
        res += i
        counter += 1
      
      else:
        res += i
        counter = 0
        
    return res
