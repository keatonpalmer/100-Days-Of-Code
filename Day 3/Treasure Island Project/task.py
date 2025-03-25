# ASCII art courtesy of https://ascii.co.uk/art

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You land on the island and immediately come to a crossroads leads left or right. Which way do you choose? ")

if choice1 == "left":
    choice2 = input('''
          &&& &&  & &&
      && &\/&\|& ()|/ @, &&
      &\/(/&/&||/& /_/)_&/_&
   &() &\/&|()|/&\/ '%" & ()
  &_\_&&_\ |& |&&/&__%_/_& &&
&&   && & &| &| /& & % ()& /&&
 ()&_---()&\&\|&&-&&--%---()~
     &&     \|||
             |||
             |||
             |||
       , -=-~  .-^- _
              
You make your way further into the island and come across a giant pit. You notice some vines nearby that you may be able to use to swing across. Would you like to try and swing on the vines? Please enter yes or no. ''')
    if choice2 == "no":
        choice3 = input('''You decide against swinging across the vines and decide to look around a little more. You end up finding a bridge which leads to a castle. \n                                o
                            .-'"|
                            |-'"|
                                |   _.-'`.
                               _|-"'_.-'|.`.
                              |:^.-'_.-'`.;.`.
                              | `.'.   ,-'_.-'|
                              |   + '-'.-'   J
           __.            .d88|    `.-'      |
      _.--'_..`.    .d88888888|     |       J'b.
   +:" ,--'_.|`.`.d88888888888|-.   |    _-.|888b.
   | \ \-'_.--'_.-+888888888+'  _>F F +:'   `88888bo.
    L \ +'_.--'   |88888+"'  _.' J J J  `.    +8888888b.
    |  `+'        |8+"'  _.-'    | | |    +    `+8888888._-'.
  .d8L  L         J  _.-'        | | |     `.    `+888+^'.-|.`.
 d888|  |         J-'            F F F       `.  _.-"_.-'_.+.`.`.
d88888L  L     _.  L            J J J          `|. +'_.-'    `_+ `;
888888J  |  +-'  \ L         _.-+.|.+.          F `.`.     .-'_.-"J
8888888|  L L\    \|     _.-'     '   `.       J    `.`.,-'.-"    |
8888888PL | | \    `._.-'               `.     |      `..-"      J.b
8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b
8888888  L | |   \   _..--'_.-|.`.          >-'    `., J        |8888b
8888888  |  L L   +:" _.--'_.-'.`.`.    _.-'     .-' | |       JY88888b
8888888   L | |   J \ \_.-'     `.`.`.-'     _.-'   J J        F Y88888b
Y888888    \ L L   L \ `.      _.-'_.-+  _.-'       | |       |   Y88888b
`888888b    \| |   |  `. \ _.-'_.-'   |-'          J J       J     Y88888b
 Y888888     +'\   J    \ '_.-'       F    ,-T"\   | |    .-'      )888888
  Y88888b.      \   L    +'          J    /  | J  J J  .-'        .d888888
   Y888888b      \  |    |           |    F  '.|.-'+|-'         .d88888888
    Y888888b      \ J    |           F   J    -.              .od88888888P
     Y888888b      \ L   |          J    | .' ` \d8888888888888888888888P
      Y888888b      \|   |          |  .-'`.  `\ `.88888888888888888888P
       Y888888b.     J   |          F-'     \ \ ` \ \88888888888888888P'
        Y8888888b     L  |         J       d8`.`\  \`.8888888888888P'
         Y8888888b    |  |        .+      d8888\  ` .'  `Y888888P'
         `88888888b   J  |     .-'     .od888888\.-'
          Y88888888b   \ |  .-'     d888888888P'
          `888888888b   \|-'       d888888888P
           `Y88888888b            d8888888P'
             Y88888888bo.      .od88888888   
             `8888888888888888888888888888
              Y88888888888888888888888888P
               `Y8888888888888888888888P'
                 `Y8888888888888P'
                      `Y88888P'

\nIn said castle, you come across three rooms. \nOne with a red door, one with a yellow door, and one with a blue door. Which door would you like to enter? ''')
        if choice3 == "red":
            print('''
                                        _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
            
            You have found the treasure! You win!''')
        elif choice3 == "yellow":
            print('''     ,.
                    ,_> `.   ,';
                ,-`'      `'   '`'._
             ,,-) ---._   |   .---''`-),.
           ,'      `.  \  ;  /   _,'     `,
        ,--' ____       \   '  ,'    ___  `-,
       _>   /--. `-.              .-'.--\   \__
      '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\\
      _>    \     \ ,'  ') )   `. /     /    <,.
   ,-'   _,  \    ,'    ( /      `.    /        `-,
   `-.,-'     `.,'       `         `.,'  `\    ,-'
    ,'       _  /   ,,,      ,,,     \     `-. `-._
   /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\\
    /-,        ;    (o)      (o)      ;          `'`,
  ,~-'  ,-'    \     '        `      /     \      <_
  /-. ,'        \                   /       \     ,-'
    '`,     ,'   `-/             \-' `.      `-. <
     /_    /      /   (_     _)   \    \          `,
       `-._;  ,' |  .::.`-.-' :..  |       `-.    _\\
         _/       \  `:: ,^. :.:' / `.        \,-'
       '`.   ,-'  /`-..-'-.-`-..-'\            `-.
         >_ /     ;  (\/( ' )\/)  ;     `-.    _<
         ,-'      `.  \`-^^^-'/  ,'        \ _<
          `-,  ,'   `. `"""""' ,'   `-.   <`'
            ')        `._.,,_.'        \ ,-'
             '._        '`'`'   \       <
                >   ,'       ,   `-.   <`'
                 `,/          \      ,-`
                  `,   ,' |   /     /
                   '; /   ;        (
                    _)|   `       (
                    `')         .-'
                      <_   \   /    
                        \   /\(
                         `;/  `
                         \nYou come face to face with a lion who swiftly devours you. Game over.''')
        else:
            print('''                      ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\\
         /' %%@=%o%%%o|   /(_)o%%% `\\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \\
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--/
                \nYou found some pizza. You sort of won, but not really. Game over.''')

    else: print('''As you swing across the pit, the vines snap and you fall to your doom. Game over.
     _.--""--._
    /  _    _  |
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_''')
else:
    print('''
    (_) - - -
               '
       @_  _    '
        )\/(@    '
      __(/ \--._
     (,-.---'--'@
      @ )0_0(     _
        ('-')    (_)
   '    _\Y/_      
   ' .-'-\-/-'-._  '
   _ /    '*     \ '
  (_)  /)  *    .-.))>'
    ._/  \__*_ /\__'.
'<((_'    |__H/  \__\\
          /   ,_/ |_|
          )-- /   |x|
          \ _/    (_ x
          /_/       \_\@
         /_/
        /_/
       /x/
      (_ x
        \_\@
    You come across a clown who pelts you repeatedly with juggling balls until you fall unconscious. Game over. \n
     _.--""--._
    /  _    _  |
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}''')