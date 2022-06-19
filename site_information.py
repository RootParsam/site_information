import builtwith
from colorama import Fore,init,Back
init()
site = input("Enter a Site : ")

res = builtwith.builtwith("https://"+site)

for i in res:
    print(Fore.RED+i,res[i])