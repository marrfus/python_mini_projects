position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [" "," "," "," "," "," "," "," "," "]
play= True
currentPlayer= "X"
eingabe = {"X":[],"O":[]}
counter = 0

 
def printBoard(a:list):

    print(rf"""        
          {a[0]} | {a[1]} | {a[2]} 
        -------------
          {a[3]} | {a[4]} | {a[5]} 
        -------------
          {a[6]} | {a[7]} | {a[8]} 
        """)  
      

def playGame():    
    global currentPlayer
    global eingabe

    wahl = int(input(f"{currentPlayer} dran:  "))
    while board[wahl-1] != " ":
        wahl = int(input(f"Leider ist Feld {wahl} schon besetzt.\nWahl bitte freie Feld:   "))
    board[wahl-1] = currentPlayer
    eingabe[currentPlayer].append(wahl) 
    switchPlayer()

 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer="X"
 

def checkWin():
    global play
    global currentPlayer
    global counter 

    counter += 1
    win_liste = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for i in win_liste:
        if all(zahl in eingabe["X"] for zahl in i):
            play = False
            print(f"Huu-hhuuu!!! Spieler X hat gewonnen!")
            break
        if all(zahl in eingabe["O"] for zahl in i):
            play = False
            print(f"Huu-hhuuu!!! Spieler O hat gewonnen!")
            break
    if counter == 9 and play == True:
        play = False
        print("Es ist Unentschieden. Ende!")
        
    

print("Lass uns XO spielen!\nHier sind die mögliche Positionnen:")
printBoard(position)
while play:
    playGame()
    printBoard(board)
    # print(f"eingabe:  {eingabe}")
    checkWin()