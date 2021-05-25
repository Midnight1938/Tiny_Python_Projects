# importing sys
import sys
  
# adding Folder_2 to the system path
sys.path.insert(0, "/home/skshm/MEGA/Python/PythonFiles/Modules")
from String_Mods import replaceMultiple

text = "ABC@hmail.com"

#! into abc*HMAIL*COM
def Sawp_n_star(str):
    str = str.swapcase()
    replaceMultiple(str, ["@","."], "*")
    print(str)

print("\n")    
Sawp_n_star(text)


