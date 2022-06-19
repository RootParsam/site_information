import builtwith
from colorama import Fore,init,Back


print ("""\n        _)   |              _)            _|                                      |    _)                 
   __|   |   __|    _ \      |   __ \    |      _ \     __|   __ `__ \     _` |   __|   |    _ \    __ \  
 \__ \   |   |      __/      |   |   |   __|   (   |   |      |   |   |   (   |   |     |   (   |   |   | 
 ____/  _|  \__|  \___|     _|  _|  _|  _|    \___/   _|     _|  _|  _|  \__,_|  \__|  _|  \___/   _|  _| """)

print ("""                      Created By RootParsam
                            instagram : parsam._.mhmdi """)
init()

site = input("\nEnter a Site : ")

res = builtwith.builtwith("https://"+site)

for i in res:
    print(Fore.RED+i,res[i])
