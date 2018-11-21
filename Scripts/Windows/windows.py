import subprocess
import threading
import os
import platform
import re
print('''
             $"                        "$
                       $"                            '#$
                      P                                  "*$
                    $"                                      '#
                   $"                                        '+'R
                  $"                  :                      < ^o"
                 $"                ~ x"                       "u N#
                $"               z" dF x$   $                  ^k'U
               $"              n4 ."# d$   d$   >               $ $
              $"        u"   ?  .u/ <%'"  d$$  u x              9 $
             $"         .o %'$@ $$  L3" u$$$~ d"x$         r4   $
             F         ''  @H@" "'.z$e@$$$$"x* -"\r     W  E4  :$
            F           #- JMM$u. @$$$$$$$$$z$ 4 .      R :"$ .$
           F              "?MMMR$$$$$$$$$$$ #h.$#     .$" Pd$z
          F                 RMMM$$$$$$$XMf$. '$$"     9F.$
         P                   MMM$$$$L ""N@$$$$$       4d$
        $                  .x *MM$$$$*$$$$$$$*        '$
       $                   $RH.`M$$$$$$$$$$*           $
      $                   :MM$$b "$$$$*""              $
     $                    $MM$$$$8W-                   4
    $                    '$MMM$$$$$      ..             $
   $                       ^*M$$$$$?.     `~~~ ee.      $
  $"                        !.*$$$$$$k         $$$b     '$
 $"    .eu.                  `!'#**7CU         9$**$o    R
 F    @$B*".e.                 `-"$$$$B      ...uC?*MI    $
P    dP"ud$$$WXL                   R$$$   ""#*R$beUJ9$$.  `$
     Ldt$$$l$$$#c                   "$$        *uJC$$$$$N. #$
    @$L$$l$$$Pbc$                     R      ud*"?"*MM$$$$e #$
    $$$G$$$$l$$" z!x                           #$$$$u*MR$$$$b2$
   @$T@$$$T@$* u!$@M$L                        ^*^$$$$$(MMR$$$$N
  :#d$$$#d$P".$$LF$X$Rb.               J$L      ''$$$$$*J#MM$$$E
  )$$$*z$$".@$$$B:$$$$$$$c...ur        $$$.      d:$$#z$$$4RM$$$'
 x$$$)$$" d$$$$$$$$$$BR$$$$$$"        $$$$$:    :$$ $$$$#\4RM$$$>
 eI#@$* d$$$$$$$*t$$$$$$$$$$$L       d$$$$$$L   $$$N$$#o$Lt8M$$$b
 $T$$"zW@IBbW$$$$3$$$$$$$$$$$$$N    d$$$$$$$$o d9$$FuH$$$EMMM$$$$
  "* $$$$$$$$$**#M$$$$$$$$R$$$$$$u d$$$$$$$$$$$$H2h4MM$$$F$RM$$$$
    $$We(?Lx.  ~M$W*$$$$8$$$$$$$$$$$$$$M)W$$#d$RX$ XRM$$$>MRM$$$$L
    $$$$$MM$X   ~$$N"$R$$$$$$$$$` '$$$T@$$$X$*"@$" XMMM$$ MMMM$$$$
    $$$$$BM@R    "$$$7$X$$$$$$$$   $T@$$RM@$$  <"  !$MMM$'R@MM$$$$
    $$$$$$MRR      $$$$$x$$$$$$$$eMo$$$$X$$$Tuu^   'BMMM$tMMMM$$$$L
    $$$$$$MMR      %$$$$$k$$$$$$RX$$$$$$$$8W$$F     #$MMf8MMMM$$$$$
    $$$$$$MM$      $$$$$$$k$$$$l$$$$$$$$$$$$$$       $MM>RMMMM$$$$$.
    $$$$$$$M$     J$$*$$$$$iR$$$$$$$$$$$$$$$$M        $M>MMMM$$$$$$$
    $$$$$$$$5k   .$$$9WeeWWWoeWe@$$$N$$$$$$$$k         $XMMMH$$$$$$$
    $$$$$$$$$$c .$$BRBbebUUWUUCC$$$$$$$$$$$$$$         '$LMMM$$$$$$P
     $$$$$$$$$B.$$$$$$$$$$$$$$$*#$$$$$$$$$$$":"          $8MM$$$$$$
     'MR$$$$$$$8`$$$$M$$$$$$$$F  4$$$$$$$$$$.`~k          "NMM$$$$
      #MMR$$$$$$k$$$$B$$$$$$$$$oz$$$$$$$$$$$$N$$c           ^N$$#
       $MMM$$$$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c
       '$MMR$$$$$N?$$5$$$$$$$$$$$$$$$$$$$$$$$$$$$$c
        `@MMR$$$$$k$B$R$$$$$$$$$$$$$$$$$$$$$$$$$$$$b
         #@MMR$$$$$'#R$$$$$$$$$$$$$$$$$$R*"""   `W@=
          #8MMR$$$$$   '"#**R$$$***""
           #MMMM$$$$b
            #MMMM$$$$i
             #MMMM$$$$L             <
              #MMRM$$$$             '        '.
               "8MM?$$$$             k        `:
                 $MMR$$$N            ?         `:       .
                  #8M$$$$N            M         4:       ~:
      :            ^5M$$$$$$$.        !>         !:       `!:
      M             '$M#$$$$$$u       'X          !h        !?:
      !              "MMM$$$$$$b       !L          !h        ~!!:4
     <!               $MMM$$$$$ $      `!          `Xh        `!!!:?L
     !!               ?MMMM$$$$K$       !h          `!h         ~!!!h"
   b !!                $MMMM$$$$`       ~!           4!h         `!!!!
   c'~`                $"M?Mk#$$k        !!           !!h         '!!!
   R!!!                ^"~#N?N'$$        !!:           !!h          %!
   F!!!                    '  `          '!!           '!!h          `
    !!!                    'L             !!L           `!!h
   '!!f                     X             '!!            ~!!h
   !!!                      ?              !!h            !!!h    ..e@
  E!!!                      !>             `!!            'X!!\*$




''')

print("""
 /$$$$$$            /$$                                 /$$$$$$$             /$$               /$$             /$$
 /$$__  $$          | $$                                | $$__  $$           | $$              |__/            | $$
| $$  \__/ /$$   /$$| $$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$    /$$$$$$  /$$  /$$$$$$  /$$$$$$
| $$      | $$  | $$| $$__  $$ /$$__  $$ /$$__  $$      | $$$$$$$/|____  $$|_  $$_/   /$$__  $$| $$ /$$__  $$|_  $$_/
| $$      | $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$____/  /$$$$$$$  | $$    | $$  \__/| $$| $$  \ $$  | $$
| $$    $$| $$  | $$| $$  | $$| $$_____/| $$            | $$      /$$__  $$  | $$ /$$| $$      | $$| $$  | $$  | $$ /$$
|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$            | $$     |  $$$$$$$  |  $$$$/| $$      | $$|  $$$$$$/  |  $$$$/
 \______/  \____  $$|_______/  \_______/|__/            |__/      \_______/   \___/  |__/      |__/ \______/    \___/
           /$$  | $$
          |  $$$$$$/
           \______/
""")
#You ain't removing my sexy ascii anime girl

print('this is only to be used as admin!')
print('this does not handle forensics questions')
runnin = True
#while runnin == True:
def startup():
    runnin90s = input('''
    Enter the number coresponding to the desired function
    0 - Run the full script (will skip unachievable functions and print them to a log file)
    1 - Run full while skiping windows Update
    2 - Win update only
    3 - Finds Users ONLY
    4 - Find currupt users and removes them
    5 - adds or changes usr password
    6 - adds usr
    7 - Update an application
    8 - Remove an application
    9 - Checks to see if password file is unencrypted and removes it
    10 -
    ''')



def openTheWindows():
#Auto-Updates Windows
    ver = platform.release()
    if ver == 10: #if win version is 10 it will run powershell because the other command will not work on win 10
        #will implement try/catch if there is no powershell later
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()" , ";"], shell = True)
        #Don't know if the powershell command will work will test later
    else:
        subprocess.call(r' wuauclt.exe /detectnow', shell = True)



def findUsr():
#finds currupt users and deletes them
    subprocess.call(r'net user', shell = True)
    c = input('''/
    0 - go back to menu
    1 - add usr
    2 - rm usr
    3 - change usr password
    ''')
def rmUsr(): #removes users
    n = input('enter the name of the user you wish to remove. Type quit to return to menu')
    dict = subprocess.call(r'net user', shell = True) #get list of user
    if n == 'quit' || 'Quit':
        startup()
    f = re.findall(n , dict) #finds input name
    if f:
        subprocess.call('net user ' + n + ' /delete' , shell = True) #if found removes usr
        r = input('would you like to run again "y" for yes')
        if r == 'y' || 'Y':
            rmUsr()
        else:
            startup()
    else:
        print("please input a valid user")#if not prompts usr again
        rmUser()
def addUsr(): #adds users obiously
    n = input('enter the name of user you wish to add. Type "quit" to quit')
    if n == 'quit' || 'Quit':
        startup()
    p = input("enter the password for the user")
    subprocess.call(r'net user ' + n + " " + p + ' /add', shell = True)
    r = input('would you like to run again "y" for yes')
    if r == 'y' || 'Y':
        addUsr()
    else:
        startup()

def checkPass():
    passwdf = open(r'\Windows\System32\config', 'w')
