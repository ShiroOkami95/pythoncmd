 #importing the OS
import os
#TrigoTable function
def TrigoTable():
   #Importing resources
   import time
   import math
   from math import pi

   print("\n\n  xxxxxxxxxx TriFunc 0.1.0 xxxxxxxxxx\n")
   #exponent function
   def expo():
     a=int(input("\nInput a number ==>"))
     b=int(input("Input it's exponential power==>"))
     print(str(int(a))+" to the power "+str(int(b))+" is "+str(int(a)**int(b)))
     print("\n    xxxxxxxxxx +++++++++++++++++++++++++++++++++++ xxxxxxxxxxx\n")
     time.sleep(2)
     start()
   #square root function
   def sq_root():
     c=int(input("\nInput the number ==>"))
     print("\nSquare root of "+str(int(c))+" is "+str((math.sqrt(c))))
     print("\n    xxxxxxxxxx +++++++++++++++++++++++++++++++++++ xxxxxxxxxxx\n")
     time.sleep(2)
     start()
   #Ttigonometric table
   def trigo():
     print("\nxxxxx HERE'S A SIMPLE TRIGONOMETRIC TABLE xxxxxx")
     print("\n\n")
     print("|------------------------------------------------|")     
     print("|*angle|        |        |        |      |       |")
     print("|   °  |   0    |   π/3  |   π/4  | 3π/2 |  π/2  |")
     print("|func x|        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("| Sin  |   0    |   1/2  |  1/√2  | √3/2 |   1   |")
     print("|      |        |        |        |      |       |") 
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("| Cos  |   1    |  √3/2  |  1/√2  | 1/2  |   0   |")
     print("|      |        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("| Tan  |   0    |  1/√3  |    1   | √3   |  NIL  |")
     print("|      |        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("| Cot  |  NIL   |   √3   |    1   | 1/√3 |   0   |")
     print("|      |        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("| Sec  |   1    |  2/√3  |   √2   | 2    |  NIL  |")
     print("|      |        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("|      |        |        |        |      |       |")
     print("|Cosec |  NIL   |   2    |   √2   | 2/√3 |   1   |")
     print("|      |        |        |        |      |       |")
     print("|------------------------------------------------|")
     print("\nxxxxxxxxxx +++++++++++++++++++++++ xxxxxxxxxxx\n")
     time.sleep(2)
     start()
   #Main body
   def start():
     print("\nWhat would you like to do??")
     print("1. Find square root.")
     print("2. Find exponent.")
     print("3. View a trigonometric table.")
     print("4. Exit.")
     x=int(input("==>"))
     if x==1:
       sq_root()
     elif x==2:
       expo()
     elif x==3:
       trigo()
     else:
       print("                Thank you😉\n        Leave a star if you liked it!!!\n\n")
       print("\n\n xxxxxxxxxx xxxxxxxxxx xxxxxxxxxx\n\n")
       cmdprompt()
   start()
  
#Calculator tools
def TimeTable():
  import time
  print("\n\n xxxxxxxxxx Time Tables 0.1.0 xxxxxxxxxx  \n")
  time.sleep(1)
  print("You can find out the time table\nfor any number using this...")
  time.sleep(2)
  #main body
  def body():
    a=int(input("\nPlease input number==>"))
    print("\nTable for "+ str(a)+"\n")
    time.sleep(1)
    print(str(a)+" x 1= "+ str(int(a)*1))
    print(str(a)+" x 2= "+ str(int(a)*2))
    print(str(a)+" x 3= "+ str(int(a)*3))
    print(str(a)+" x 4= "+ str(int(a)*4))
    print(str(a)+" x 5= "+ str(int(a)*5))
    print(str(a)+" x 6= "+ str(int(a)*6))
    print(str(a)+" x 7= "+ str(int(a)*7))
    print(str(a)+" x 8= "+ str(int(a)*8))
    print(str(a)+" x 9= "+ str(int(a)*9))
    print(str(a)+" x 10= "+ str(int(a)*10))
    print(str(a)+" x 11= "+ str(int(a)*11))
    print(str(a)+" x 12= "+ str(int(a)*12))
    print(str(a)+" x 13= "+ str(int(a)*13))
    print(str(a)+" x 14= "+ str(int(a)*14))
    print(str(a)+" x 15= "+ str(int(a)*15))
    print(str(a)+" x 16= "+ str(int(a)*16))
    print(str(a)+" x 17= "+ str(int(a)*17))
    print(str(a)+" x 18= "+ str(int(a)*18))
    print(str(a)+" x 19= "+ str(int(a)*19))
    print(str(a)+" x 20= "+ str(int(a)*20))
    time.sleep(2)
    y=("y")
    x=input("\nWould you like to go again??\n(y or n)==>")
    time.sleep(1)
    if (x== y):
      body()
    else:
      print("\n\nAlright then!!!! Buhbye!!!💓\n Leave a star😉⭐")
      print("\n\n xxxxxxxxxx xxxxxxxxxx xxxxxxxxxx\n\n")
      cmdprompt()
  body()
  
#Age Testing tools
def age():
  print("\n\n  xxxxxxxxxx How many days are you??  xxxxxxxxxx")
  print("                         0.1.0                      ")
  import time
  print("Hi!!!!!")
  time.sleep(2)
  print("What's your name???")
  name= input()
  time.sleep(1)
  print ("Hello "+(name))
  time.sleep(2)
  print("How old are you "+(name)+"?")
  age=input()
  time.sleep(1)
  print("I will now calculate how old you are in terms of days.")
  time.sleep(2)
  print(" ")
  print(" ")
  print(" ")
  print("Calculating the approximate number of days you've lived...")
  print(".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print((name)+ ", you are about " +str (int(age)*12*31)+" days,")
  time.sleep(2)
  print(str(int(age)*12*31*24)+ " hours,")
  time.sleep(2)
  print(str(int(age)*12*31*24*60)+" minutes,")
  time.sleep(2)
  print("and "+str(int(age)*12*31*24*60*60)+" seconds old.")
  time.sleep(2)
  print(" ")
  print("Have a nice day!!!!")
  print("\n  xxxxxxxxxx xxxxxxxxxx xxxxxxxxxx \n\n ")
  cmdprompt()
    
#geometry
def geometry():  
  #installing important files
  import time
  from math import pi
  import math
  
  #Login screen
  print (""" 
  
  
      xxxxxxxxxx Geometry 0.2.0 xxxxxxxxxx
        
        
    """)
  def geo():
    print("""
    Evaluate:
      1. Circle
      2. Sphere
      3. Hemisphere
      4. Cube
      5. Cuboid
      6. Cylinder
      7. Cone
      8. Exit
    """)
    x=input("==> ")
    if x =="1":
      circle()
    elif x =="2":
      sphere()
    elif x=="3":
      hsphere()
    elif x=="4":
      cube()
    elif x=="5":
      cuboid()
    elif x=="6":
      cylinder()
    elif x=="7":
      cone()
    else:
      time.sleep(1)
      print("\n xxx Exiting xxx\n")
      cmdprompt()
      
  #margin line between operations
  def m():
    time.sleep(0.5)
    print("\n |---------------------|\n")
    time.sleep(0.5)
    
  #main menu function
  def back():
    time.sleep(1)
    print("\n xxx Exiting xxx\n")
    time.sleep(1)
    geo()
  
  #error function
  def error():
    time.sleep(1)
    print("\n ERROR!!!!!!!!!!\n")
    time.sleep(1)
  
  #circle
  def circle():
    m()
    def circ():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nCircumference = "+str(2*pi*int(r)))
      time.sleep(1)
      circle()
    def area():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nArea = "+str(pi*int(r)**2))
      time.sleep(1)
      circle()
    print("""
    Find:
      1. Circumference
      2. Area
      3. Back
        """)
    x=input("==> ")
    if x=="1":
      circ()
    elif x=="2":
      area()
    elif x=="3":
      back()
    else:
      error()
      circle()
      
  #sphere
  def sphere():
    m()
    def SA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(4*pi*int(r)**3))
      time.sleep(1)
      sphere()
    def vol():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nVolume = "+str(4/3*pi*r**3))
      time.sleep(1)
      sphere()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SA()
    elif x=="2":
      vol()
    elif x=="3":
      back()
    else:
      error()
      sphere()
  
  #hemisphere
  def hsphere():
    m()
    def CSA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nCurved surface area = "+str(2*pi*r**2))
      time.sleep(1)
      hsphere()
    def TSA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nTotal surface area = "+str(3*pi*r**2))
      time.sleep(1)
      hsphere()
    def hvol():
      r=int(input("\Input radius ==> "))
      time.sleep(1)
      print("\Volume = "+str(2/3*pi*r**3))
      time.sleep(1)
      hsphere()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      CSA()
    elif x=="2":
      TSA()
    elif x=="3":
      hvol()
    elif x=="4":
      back()
    else:
      error()
      hsphere()
  
  #cube
  def cube():
    m()
    def SAC():
      a=int(input("\nInput length of side ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(6*a**2))
      time.sleep(1)
      cube()
    def volC():
      a=int(input("\nInput length of side ==> "))
      time.sleep(1)
      print("\nVolume = "+str(a**3))
      time.sleep(1)
      cube()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SAC()
    elif x=="2":
      volC()
    elif x=="3":
      back()
    else:
      error()
      cube()
  
  #cuboid
  def cuboid():
    m()
    def SACu():
      l=int(input("\nInput length ==> "))
      h=int(input("Input height ==> "))
      b=int(input("Input breadth ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(2*(l*b+b*h+h*l)))
      time.sleep(1)
      cuboid()
    def volcu():
      l=int(input("\nInput length ==> "))
      h=int(input("Input height ==> "))
      b=int(input("Input breadth ==> "))
      time.sleep(1)
      print("\nVolume = "+str(l*b*h))
      cuboid()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SACu()
    elif x=="2":
      volcu()
    elif x=="3":
      back()
    else:
      error()
      cuboid
  
  #cylinder
  def cylinder():
    def csacy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nCurved surface area = "+str(2*pi*r*h))
      time.sleep(1)
      cylinder()
    def tsacy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nTotal surface area = "+str(2*pi*r*(h+r)))
      time.sleep(1)
      cylinder()
    def volcy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nVolume = "+str(pi*h*r**2))
      time.sleep(1)
      cylinder()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      csacy()
    elif x=="2":
      tsacy()
    elif x=="3":
      volcy()
    elif x=="4":
      back()
    else:
      error()
      cylinder()
  
  #cone
  def cone():
    m()
    def csaco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nCurved surface area = "+str(pi*r*l))
      time.sleep(1)
      cone()
    def tsaco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nTotal surface area = "+str(pi*r*(l+r)))
      time.sleep(1)
      cone()
    def volco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==>"))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nVolume = "+str(1/3*pi*h*r**2))
      time.sleep(1)
      cone()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      csaco()
    elif x=="2":
      tsaco()
    elif x=="3":
      volco()
    elif x=="4":
      back()
    else:
      error()
      cone()
  
  geo()

#divisibilitytesting
def div():
  #importing important modules
  import math
  import time
  print("\n\n xxxxxxxxxx DivisiTest 0.1.0 xxxxxxxxxx")
  #intros
  print("\n\nThis program checks if the first number you\ninput is divisible by the second number")
  time.sleep(1)
  print("\nTo end, type 'end'")
  time.sleep(1)
  #main body
  def one():
    x=input("\nInput number X ==>")
    end=("end")
    if x==end:
      time.sleep(1)
      print("\nThank you!! Leave a star if you liked it😉")
      print("\n\n xxxxxxxxxx xxxxxxxxxx xxxxxxxxxx\n")
      cmdprompt()
    else:
      print(" ")
      y=input("Input number Y ==>")
      z=(((int(x)))/((int(y))))
      a, whole=math.modf(z)
      if a>0:
        time.sleep(1)
        print(" ")
        print(str(int(x))+" is not divisible by "+str(int(y))+"\n The quotient is "+str(float(z)))
      else:
        time.sleep(1)
        print(" ")
        print(str(int(x))+" is divisible by "+str(int(y))+"\n The quotient is "+str(float(z)))
      one()
  one()

#TicTacToe game
def game():
  #THANKS FOR THE 500 STARS WITH ❤
  #check my profile for my other codes
  #this is a INTERMEDIATE LEVEL tic-tac-toe game
  #I bet you will win if you have good strategy thinking
  from random import choice #To select who will play first between player and computer
  from time   import sleep  #
  
  print("\n\n    ********    TIC TAC TOE    ********")
  print("\n(note- this game wasn't created by me)")
  print("(Original files forked from 'sameer39')")
  #welcome display
  def Welcome():
      print('\n\n   ****Welcome to tic-tac-toe game****')
      #dont take sleep more than 2 seconds then user will get bored
      sleep(1)
      print()
      print('Computer will decide who will play first')
      print()
      #for Hint Feature In Computer AI i have passed Player letter instead of computer letter
      print('If you need Hint in the middle of game \npress any of this [Hint,hint,H,h]')
      sleep(1)
      print()
      print('''      ******* Format of Game ******
            |    |         1 | 2 | 3
         - - - - - -      - - - - - - 
            |    |         4 | 5 | 6
         - - - - - -      - - - - - - 
            |    |         7 | 8 | 9
                                           ''')


  #Fuction to draw Board
  #you can modify this sleep method if you dont need it
  def DrawBoard(board,NeedSleep=True):
      #I thought for hint u dont need sleep method so i given default value for Needsleep 
      if NeedSleep:
          sleep(1)
      print()
      print('             '+board[1]+'  |  '+board[2]+'  |  '+board[3])
      print('             - - - - - - - ')
      print('             '+board[4]+'  |  '+board[5]+'  |  '+board[6])
      print('             - - - - - - - ')
      print('             '+board[7]+'  |  '+board[8]+'  |  '+board[9])
      print()
  
  #asking the player to choose thier Letter  (X or O)
  def InputPlayerLetter():
      letter=''
      #Ask untill user enters x or o
      while not(letter == 'X' or letter == 'O'):
          print('Do you want to be X or O')
          letter = input().upper()
       
      #returning list bcz of later use
      if letter == 'X':
        return ['X','O']
      if letter == 'O':
        return ['O','X']

  #Deciding who should play first randomly
  #in usual tic-tac-toe games player first,but it selects randomly between computer and player
  def WhoFirst():
      opponents = ['computer','player']
      if choice(opponents) == 'computer':
          return 'computer'
      else :
          return 'player'
          
  #this function asks player to play again
  def PlayAgain():
      print()
      print('Do you want to Play Again (y or n)')
      playagain = input().lower().startswith('y')
      return playagain
  
  #function for making move
  def MakeMove(board,letter,move):
      board[move] = letter

  #check if any one win,returns True if wins
  #In tic-tac-toe there are 8 possibilities of winning
  #horizontal => 3 | vertical => 3 | diagonal => 2
  def IsWinner(board,letter):
      return ( (board[7] == letter and board[8] == letter and board[9] == letter ) or
               (board[4] == letter and board[5] == letter and board[6] == letter ) or
               (board[1] == letter and board[2] == letter and board[3] == letter ) or
               (board[1] == letter and board[4] == letter and board[7] == letter ) or
               (board[2] == letter and board[5] == letter and board[8] == letter ) or
               (board[3] == letter and board[6] == letter and board[9] == letter ) or
               (board[1] == letter and board[5] == letter and board[9] == letter ) or
               (board[3] == letter and board[5] == letter and board[7] == letter )  )
  
  #duplicate board is useful when we wanted to make temporary changes to the temporary copy of the board without changing the original board
  def GetBoardCopy(board):
      DupeBoard = []
      for i in board:
          DupeBoard.append(i)
      return DupeBoard
      
  #fuction to check is space is free
  def IsSpaceFree(board,move):
      return board[move] == ' '
  
  #Getting the player move
  def GetPlayerMove(board):
    move = ''
 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board,int(move)):
          print()
          print('Enter your move (1 - 9)')
          move = input()
          #if player wants Hint
          if move in HintInput:
              return move
              break  
    return int(move)
  
  #choose random move from given list
  #it is used when AI  wants to choose out of many possibilities
  def ChooseRandomFromList(board,MoveList):
      PossibleMoves = []
      for i in MoveList:
          if IsSpaceFree(board,i):
              PossibleMoves.append(i)
      if len(PossibleMoves) != 0:
          return choice(PossibleMoves)
      else:
          return None
  
  #creating computers AI
  #this ai works on this algorithm
  #1.it checks if computer can win in next move,else
  #2.it checks if player can win in next move,then it blocks it,else
  #3.it chooses any available spaces from the corner[1,3,7,9],else
  #4.it fills middle square if space free,else
  #5.it chooses any available spaces from sides,ie,[2,4,6,8]
  #if you interchange the 3 and 4 steps the AI becomes little Hard,ie,it fills middle then corner
  #--------------------------------------
  #Get computer move
  def GetComputerMove(board,ComputerLetter):
      if ComputerLetter == 'X':
          PlayerLetter = 'O'    
      else:
         PlayerLetter = 'X'
  
      #1.check computer can win in next move
      for i in range(1,10):
          copy = GetBoardCopy(board)
          if IsSpaceFree(copy,i):
              MakeMove(copy,ComputerLetter,i)
              if IsWinner(copy,ComputerLetter):
                  return i
  
  
      #2.check player can win in next move
      for i in range(1,10):
          copy = GetBoardCopy(board)
          if IsSpaceFree(copy,i):
              MakeMove(copy,PlayerLetter,i)
              if IsWinner(copy,PlayerLetter):
                  return i
  
      #3.checking for corner
      move = ChooseRandomFromList(board,[1,3,7,9])
      if move != None:
          return move
          
      #4.checking for the center
      if IsSpaceFree(board,5):
          return 5
          
      #5.checking for sides
      return ChooseRandomFromList(board,[2,4,6,8])
    
  #---------------------------------------   
  
  #checking board is full or not
  def IsBoardFull(board):
      for i in range(1,10):
          if IsSpaceFree(board,i):
              return False
      return True
              
  #fuction to print  the final win or tie board
  #made this to separate usual board and winning or tie board
  def FinalBoard(board,NeedSleep=True):
      print('            |-------------|')
      DrawBoard(board,NeedSleep)
      print('            |-------------|')
  
                      
  #LETS START THE GAME
  Welcome()
  while True:
      #intialising board
      TheBoard = [' '] * 10
      PlayerLetter,ComputerLetter = InputPlayerLetter()
      turn = WhoFirst()
      print(f'The {turn} will go first')
      
      #gameloop
      Playing = True
      while Playing:
          
          if turn == 'player':
              print(f"    Turn => {turn}") 
              HintInput = ['Hint','hint','H','h'] 
              #taking players input
              move = GetPlayerMove(TheBoard)
              #if player needs Hint
              while move in HintInput:                
                    #following code gives hint to the user
                  #it runs player letter to computer AI
                  HintBox = []
                  for i in TheBoard:
                      HintBox.append(i)
                  hint = GetComputerMove(HintBox,PlayerLetter)
                  MakeMove(HintBox,PlayerLetter,hint)
                  print(f'HINT : placing at {hint} is better')
                  FinalBoard(HintBox,False)
                  move = GetPlayerMove(TheBoard)
                
              MakeMove(TheBoard,PlayerLetter,move)
              
              
              if IsWinner(TheBoard,PlayerLetter):
                  FinalBoard(TheBoard)                
                  print('❤You have WON the game❤')
                  Playing = not Playing
              elif IsBoardFull(TheBoard):
                  FinalBoard(TheBoard)
                  print('The game is TIE\nIts good to PLAY untill you WIN❤')
                  Playing = not Playing
              else :
                  DrawBoard(TheBoard)
                  turn = 'computer'
   
          else :
              #computer move
              print(f"    Turn => {turn}")
              move = GetComputerMove(TheBoard,ComputerLetter)
              MakeMove(TheBoard,ComputerLetter,move)
            
            
              if IsWinner(TheBoard,ComputerLetter):
                  FinalBoard(TheBoard)
                  print('❤Try again bro you will win❤')
                  Playing = not Playing
              elif IsBoardFull(TheBoard):
                  FinalBoard(TheBoard)
                  print('The game is TIE\nIts good to PLAY untill you WIN❤')
                  Playing = not Playing
              else :
                  DrawBoard(TheBoard)
                  turn = 'player'
  
      if not PlayAgain():
          print("********❤GIVE STAR ONLY IF YOU LIKE❤********\n\n")
          cmdprompt()
          
   
  
  #The algorithm of above code is written by 'Albert Sweigart ' in his book "Invent  Your  Own Computer  Games  with Python" 
  #i have just modified the source code
  #it is free to download in http://inventwithpython.com
  #if u only need this game then u can read online this chapter at http://inventwithpython.com/invent4thed/chapter10.html
  #if any doubts see that book,he clearly explained everything

#calculator
def calc():
  import time
  import math
  print(" \n\n    xxxxxxxxxx PYCalculator xxxxxxxxxx\n")
  print(" (type'end' to end)\n\n")
  x=input("Input operation\n(eg. 27-6)\n\n==>")
  if x=="end":
    print(" \n\n    xxxxxxxxxx EXIT xxxxxxxxxx\n\n")
    cmdprompt()
  else:
    print("\n")
    print(str(x)+"= "+str(eval(x)))
    time.sleep(3)
    calc()
    
#cmd function
def cmdprompt():
  #Intro to my command prompt
  print("\n\n\n xxxxxxxxxx  Python CMD 0.1  .0  xxxxxxxxxx  ")
  print("\n\nFor Beginners-")
  print("help- shows available commands")
  print("show- gives a list of the currently available tools")
  print("info- to know more about creator/ creator's social media")
  print(" \n\n")
  print("     ________________ NOTE ___________________ ")
  print("    |                                         |")
  print("    |    I will keep updating this command    |")
  print("    |  prompt with new tools. So, stay tuned  |")
  print("    |   for new updates. Any suggestions are  |")
  print("    |               welcome                   |")
  print("    |                                         |")
  print("    |_________________________________________|")
  print("\n\n")
  #commands loop
  def cmd():
    code=input("==>")
    if code=="logout":
      print("\n\n  xxxxxxxxxx  Log out  xxxxxxxxxx  \n\n")
      exit()
    elif code=="show":
      print("\nCalculator-> A python-based calculator.")
      print("             To run, type 'run calc'")
      print("\nTrigoTable-> This file consists of three")
      print("             things. A sq.root finder, an")
      print("             exponent finder and a trig-")
      print("             onometric table")
      print("             To run, type 'run TrigoTable'")
      print("\nCircle-> This file contains a program that")
      print("         can find out the circumference, vol.")
      print("         and surface area  of circles and spheres")
      print("         To run, type 'run circle'")
      print("\nTimeTable-> This file  contains a program that")
      print("            displays the time table of any number")
      print("            the user inputs.")
      print("            To run, type 'run TimeTable'")
      print("\nDivisiTest-> This program tests the divisibility")
      print("            of the numbers inputted")
      print("            To run, type 'run DivisiTest'")
      print("\nAgeTest-> This program asks the user for age and ")
      print("          calculates the number of days user have")
      print("          lived")
      print("          To run, type 'run  AgeTest'")
      print("\ntictactoe-> A python-based   TicTacToe game with")
      print("           an AI")
      print("           **Original files were forked from")
      print("           sameer39")
      print("           To run, type 'run TTT'")
      cmd()
    elif code=="info":
      print("\n\n|----------------- About creator ----------------|")  
      print("|     I am a newbie at programming, currently    |")
      print("|    learning python, html, css and JavaScript   |")
      print("|         For more info, contact me at~          |")
      print("|          Instagram- @wallace.thiago            |")
      print("|           Facebook- Wallace Thiago             |")
      print("|________________________________________________|\n\n")
      cmd()     
    elif code=="run TrigoTable":
      TrigoTable()
    elif code=="run circle":
      circ()
    elif code=="run TTT":
      game()
    elif code=="run TimeTable":
      TimeTable()
    elif code=="run AgeTest":
      age()
    elif code=="run DivisiTest":
      div()
    elif code=="run calc":
      calc()
    elif code=="ls":
      print(""" 
      Available Tools~
          
                TrigoTable
                circle
                TicTacToe (TTT)
                AgeTest
                DivisiTest
                Calculator (calc)
                
                
      """)
      cmd()
    elif code=="help":
      print("""   Available commands->
                   
                   ls
                   run (file-name)
                   show
                   info
                   help
                   logout
      """)
      cmd()
    else:
      os.system(code)
      cmd()
  cmd()


cmdprompt()










