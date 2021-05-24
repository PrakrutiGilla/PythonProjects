print("T1|T2|T3")
print("--+--+--")
print("M1|M2|M3")
print("--+--+--")
print("D1|D2|D3")

board={'T1':' ','T2':' ','T3':' ','M1':' ','M2':' ','M3':' ','D1':' ','D2':' ','D3':' '}
total_moves=0



while True:
    
    
    player1_input=input("Player 1: ")
    total_moves=total_moves+1
    
    
    if player1_input in board and board[player1_input]==' ':
         board[player1_input]='X'
          
    else:
         print("Invalid Input")
         continue    
    
    player2_input=input("Player 2: ")
    total_moves=total_moves+1
    if player2_input in board and board[player2_input]==' ':
         board[player2_input]='O'
             
    else:
         print("Invalid Input")
         continue
            
    print(board['T1'],"|",board['T2'],"|",board['T3'])
    print("--+---+--")
    print(board['M1'],"|",board['M2'],"|",board['M3'])
    print("--+---+--")
    print(board['D1'],"|",board['D2'],"|",board['D3'])   
    
    conditions1=[board['T1']==board['T2']==board['T3']=='X',
               board['D1']==board['D2']==board['D3']=='X',
               board['T1']==board['M2']==board['D3']=='X',
               board['M1']==board['M2']==board['M3']=='X',
               board['T3']==board['M2']==board['D3']=='X',
               board['T1']==board['M1']==board['D1']=='X',
               board['T2']==board['M2']==board['D2']=='X' ,
               board['T3']==board['M3']==board['D3']=='X']  

    conditions2=[board['T1']==board['T2']==board['T3']=='O',
               board['D1']==board['D2']==board['D3']=='O',
               board['T1']==board['M2']==board['D3']=='O',
               board['M1']==board['M2']==board['M3']=='O',
               board['T3']==board['M2']==board['D3']=='O',
               board['T1']==board['M1']==board['D1']=='O',
               board['T2']==board['M2']==board['D2']=='O' ,
               board['T3']==board['M3']==board['D3']=='O']
    
   
    if any(conditions1):
        print("Player 1 won")
        break   
                
    if any(conditions2):
        print("Player 2 won")
        break
            
    if total_moves==9:
        print("It is a tie")
        break
        
