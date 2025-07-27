import time
import os

# ANSI escape para vermelho
red = "\033[91m"
reset = "\033[0m"

ascii_logo = f"""{red}



                    mm        mm                  
                mmmmmmmmmmmmmmmmmmmm              
              mmmmmmmmmmmmmmmmmmmmmmmm            
            mmmmmmmmmmmmmmmmmmmmmmmmmmmm          
            mmmmmmmmmmmmmmmmmmmmmmmmmmmm          
            mmmmmm    mmmmmmmm    mmmmmm          
            mmmmmm      mmmm      mmmmmm          
          mmmmmmmm      mmmm      mmmmmmmm        
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm        
          mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm        
            mmmmmmmm            mmmmmmmm          


{reset}"""

os.system("clear")
print(ascii_logo)
time.sleep(1.5)

print("BAD KIT\n")
time.sleep(1)

print("1 - Apagar servidor")
print("2 - Banir todos")
print("3 - Spam")
print("4 - (em desenvolvimento)")
