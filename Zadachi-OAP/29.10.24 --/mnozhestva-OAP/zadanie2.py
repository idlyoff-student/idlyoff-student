#Играем в города с программой – помощником Еленой. Есть два множества городов: 
#✓ в множестве all_cities хранятся все города, которые она знает, 
#✓ в множестве used_cities — города, которые уже были названы в игре, их уже нельзя 
#использовать. 
#Научите Елену получать перечень городов, которые ещё не были названы в игре. 
#В коде объявлена функция print_valid_cities(), допишите её. Она должна: 
#✓ принять на вход множества all_cities и used_cities; 
#✓ создать множество городов, которые ещё не использовались в игре; для этого нужно найти 
#разницу множеств all_cities и used_cities; 
#✓ напечатать это множество на экране, разделяя города запятой и пробелом. 
 
#def print_valid_cities(...): 
    # Здесь напишите тело функции, которая 
    # принимает и обрабатывает аргументы all_cities и used_cities, 
    # а затем печатает результат в нужном формате 
 
#all_cities = { 
 #   'Абакан', 
  #  'Астрахань',  
   # 'Бобруйск',  
    #'Калуга', 
    #'Караганда', 
   # 'Кострома', 
  #  'Липецк',  
 #   'Новосибирск' 
#} 
# 
#used_cities = {'Калуга', 'Абакан' , 'Новосибирск'} 
#print_valid_cities(all_cities, used_cities) 

#SRC CODE HERE:

all_cities = { 
    'Абакан', 
    'Астрахань',  
    'Бобруйск',  
    'Калуга', 
    'Караганда', 
    'Кострома', 
    'Липецк',  
    'Новосибирск' 
} 

used_cities = {'Калуга', 'Абакан', 'Новосибирск'} 

valid_cities = all_cities - used_cities

print("Города, которые еще не были названы:", ', '.join(valid_cities))
