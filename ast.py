# --------------------------------------[ IMPORT SECTION HERE ]------------------------------------------------------- #
from time import sleep
import os
import webbrowser as auto
from sys import stdout
try:
    from pyautogui import write
except ImportError:
    os.system("pip install pyautogui")
    from pyautogui import write 
# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
banner='''
\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31mLAPTOP VERSON > 2.3
\033[0;32m
 \033[1;39m ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗞𝗜𝗡𝗚\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙉𝘼𝙈𝙀\033[1;34m       : [★]  CYBER COP BANGLADESH\033[1;39m ┃
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[1;34m   : [★]  CYBER COP\033[1;39m            ┃
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙂𝙄𝙏𝙃𝙐𝘽\033[1;34m     : [★]  CYBERCOP-404\033[1;39m         ┃
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\033[1;34m : [★]  𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\033[1;39m          ┃
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\033[1;34m   : [★]  +8809638223345\033[1;39m       ┃
\033[1;39m ┃ \x1b[1;95m[🥱][☠️]\x1b[1;96m 𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\033[1;31m : [★]  AUTO-MASSAGE        \033[1;39m ┃
 \033[1;39m┗━━━━━━━━━━━━━━━━━━━\033[1;32m 𝙁𝙄𝙍𝙀\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━┛
'''
# --------------------------------------[ MAIN ANNIMATION ]------------------------------------------------------------ #
animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
def anima(animation):
    for i in range(len(animation)):
        sleep(0.5)
        stdout.write("\r[😊] PREPARING... " + animation[i % len(animation)])
        stdout.flush()
# --------------------------------------[ CLEAR PROGRAM ]------------------------------------------------------------- #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# --------------------------------------[ URL HERE ]---------------------------------------------------------- #
url ="https://www.github.com/cybercop-404"
# --------------------------------------[ MAIN BODY ]------------------------------------------------------- #
anima(animation)
clear()
print(banner)
count=int(input('\033[1;31m[☠️] HOW MANY MASSAGE DO YOU WANT TO SENT :~ '))
clear()
msg=input('\033[1;32m[☠️] ENTER YOUR MASSAGE :~ ')
for i in range(5, 0, -1):
    print(f'\033[1;31mSTART THE PROGRAM AFTER {i} SECONDS')
    sleep(1)
    clear()
i=1
for i in range(1,count+1):
    write(f'[{i}] {msg} \n ')
    sleep(2)
auto.open_new_tab(url)
# Developer :~ MD.NAHIDUL ISLAM
