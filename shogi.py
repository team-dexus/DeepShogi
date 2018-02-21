import numpy as np
PIECE_DIC = {"0": "ー ",
             "01":"玉 ",
             "02":"飛 ","02+":"竜 ",
             "03":"角 ","03+":"馬 ",
             "04":"金 ",
             "05":"銀 ","05+":"全 ",
             "06":"桂 ","06+":"圭 ",
             "07":"香 ","07+":"杏 ",
             "08":"歩 ","08+":"と ",
             "11":"玉v",
             "12":"飛v","12+":"竜v",
             "13":"角v","13+":"馬v",
             "14":"金v",
             "15":"銀v","15+":"全v",
             "16":"桂v","16+":"圭v",
             "17":"香v","17+":"杏v",
             "18":"歩v","18+":"とv"}

class board:
    def __init__(self):
        self.board = [
         ["17","16","15","14","11","14","15","16","17"],
         ["0" ,"12","0" ,"0" ,"0" ,"0" ,"0" ,"13","0"],
         ["18","18","18","18","18","18","18","18","18"],
         ["0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ],
         ["0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ],
         ["0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ,"0" ],
         ["08","08","08","08","08","08","08","08","08"],
         ["0" ,"03","0" ,"0" ,"0" ,"0" ,"0" ,"02","0" ],
         ["07","06","05","04","01","04","05","06","07"]]
    
        self.P1_in_hand = []
        self.P2_in_hand = []
        
        
        """
        先手0
        後手1
        成駒は最後に+
        例　先手の飛車は02、後手の角は13。
        玉 1
        飛 2
        角 3
        金 4
        銀 5
        桂 6
        香 7
        歩 8
        
        """
    def print_board(self):
        #後手持ち駒
        line = "後手持ち駒:"
        for i in range(len(self.P2_in_hand)):
            line = line + PIECE_DIC[self.P2_in_hand[i]]
        print(line)
        print("")
        
        #盤面
        for i in range(9):
            line = ""
            for j in range(9):
                line = line + PIECE_DIC[self.board[i][j]]
            print(line)
            
        #先手持ち駒
        print("")
        line = "先手持ち駒:"
        for i in range(len(self.P1_in_hand)):
            line = line + PIECE_DIC[self.P1_in_hand[i]]
        print(line)
        
