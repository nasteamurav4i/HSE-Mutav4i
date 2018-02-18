import random                   
import codecs

file = codecs.open('Words.csv', encoding = 'utf-8')     
string = file.read();          
string = string[ 1: ]            
file.close();                  
words = []               
combinations = []       
readingState = False;    
word = ""                
combination = ""          

for char in string :    
    if char == ',' :                       
        words.append(word)         
        word = ""                       
        readingState = True        
        continue
    
    if char == '\n' :                                  
        combinations.append(combination)         
        combination = ""                               
        readingState = False                   
        continue
      
    if readingState != True :                    
        word += char                             
        
    else : 
        combination += char                     

combinations.append(combination)               

while True :  
    number = random.randint( 0, len( combinations ) - 1 );             
    print( "Отгадайте слово : " + combinations[ number ] )        
    answer = str( input() )                                           
    
    if answer == words[ number ] :                                   
        print( "Вы выиграли!" )       
    else :       
        print( "Вы проиграли!" )
     
    print( "Продолжить? ( да / нет )" )                          
    answer = input()                                            
    
    if answer == "нет" : break                                    
        
