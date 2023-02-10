



tours = 0
timer = 0

noir = ("black",0,0,0)
blanc = ("white",255,255,255)
couleur = None
etat = False
piece = None
coord = [i][j]


case1 = {coord:[1][1],couleur:noir,etat:True,piece:Tour}
case2 = {coord:[1][2],couleur:blanc,etat:True,piece:Cavalier}
case3 = {coord:[1][3],couleur:noir,etat:True,piece:Fou}
case4 = {coord:[1][4],couleur:blanc,etat:True,piece:Reine}
case5 = {coord:[1][5],couleur:noir,etat:True,piece:Roi}
case6 = {coord:[1][6],couleur:blanc,etat:True,piece:Fou}
case7 = {coord:[1][7],couleur:noir,etat:True,piece:Cavalier}
case8 = {coord:[1][8],couleur:blanc,etat:True,piece:Tour}
case9 = {coord:[2][1],couleur:blanc,etat:True,piece:Pion}
case10 = {coord:[2][2],couleur:noir,etat:True,piece:Pion}
case11 = {coord:[2][3],couleur:blanc,etat:True,piece:Pion}
case12 = {coord:[2][4],couleur:noir,etat:True,piece:Pion}
case13 = {coord:[2][5],couleur:blanc,etat:True,piece:Pion}
case14 = {coord:[2][6],couleur:noir,etat:True,piece:Pion}
case15 = {coord:[2][7],couleur:blanc,etat:True,piece:Pion}
case16 = {coord:[2][8],couleur:noir,etat:True,piece:Pion}
case17 = {coord:[3][1],couleur:noir,etat:False,piece:None}
case18 = {coord:[3][2],couleur:blanc,etat:False,piece:None}
case19 = {coord:[3][3],couleur:noir,etat:False,piece:None}
case20 = {coord:[3][4],couleur:blanc,etat:False,piece:None}
case21 = {coord:[3][5],couleur:noir,etat:False,piece:None}
case22 = {coord:[3][6],couleur:blanc,etat:False,piece:None}
case23 = {coord:[3][7],couleur:noir,etat:False,piece:None}
case24 = {coord:[3][8],couleur:blanc,etat:False,piece:None}
case25 = {coord:[4][1],couleur:blanc,etat:False,piece:None}
case26 = {coord:[4][2],couleur:noir,etat:False,piece:None}
case27 = {coord:[4][3],couleur:blanc,etat:False,piece:None}
case28 = {coord:[4][4],couleur:noir,etat:False,piece:None}
case29 = {coord:[4][5],couleur:blanc,etat:False,piece:None}
case30 = {coord:[4][6],couleur:noir,etat:False,piece:None}
case31 = {coord:[4][7],couleur:blanc,etat:False,piece:None}
case32 = {coord:[4][8],couleur:noir,etat:False,piece:None}
case33 = {coord:[5][1],couleur:noir,etat:False,piece:None}
case34 = {coord:[5][2],couleur:blanc,etat:False,piece:None}
case35 = {coord:[5][3],couleur:noir,etat:False,piece:None}
case36 = {coord:[5][4],couleur:blanc,etat:False,piece:None}
case37 = {coord:[5][5],couleur:noir,etat:False,piece:None}
case38 = {coord:[5][6],couleur:blanc,etat:False,piece:None}
case39 = {coord:[5][7],couleur:noir,etat:False,piece:None}
case40 = {coord:[5][8],couleur:blanc,etat:False,piece:None}
case41 = {coord:[6][1],couleur:blanc,etat:False,piece:None}
case42 = {coord:[6][2],couleur:noir,etat:False,piece:None}
case43 = {coord:[6][3],couleur:blanc,etat:False,piece:None}
case44 = {coord:[6][4],couleur:noir,etat:False,piece:None}
case45 = {coord:[6][5],couleur:blanc,etat:False,piece:None}
case46 = {coord:[6][6],couleur:noir,etat:False,piece:None}
case47 = {coord:[6][7],couleur:blanc,etat:False,piece:None}
case48 = {coord:[6][8],couleur:noir,etat:False,piece:None}
case49 = {coord:[7][1],couleur:noir,etat:True,piece:Pion}
case50 = {coord:[7][2],couleur:blanc,etat:True,piece:Pion}
case51 = {coord:[7][3],couleur:noir,etat:True,piece:Pion}
case52 = {coord:[7][4],couleur:blanc,etat:True,piece:Pion}
case53 = {coord:[7][5],couleur:noir,etat:True,piece:Pion}
case54 = {coord:[7][6],couleur:blanc,etat:True,piece:Pion}
case55 = {coord:[7][7],couleur:noir,etat:True,piece:Pion}
case56 = {coord:[7][8],couleur:blanc,etat:True,piece:Pion}
case57 = {coord:[8][1],couleur:blanc,etat:True,piece:Tour}
case58 = {coord:[8][2],couleur:noir,etat:True,piece:Cavalier}
case59 = {coord:[8][3],couleur:blanc,etat:True,piece:Fou}
case60 = {coord:[8][4],couleur:noir,etat:True,piece:Reine}
case61 = {coord:[8][5],couleur:blanc,etat:True,piece:Roi}
case62 = {coord:[8][6],couleur:noir,etat:True,piece:Fou}
case63 = {coord:[8][7],couleur:blanc,etat:True,piece:Cavalier}
case64 = {coord:[8][8],couleur:noir,etat:True,piece:Tour}

E =[[case1,case2,case3,case4,case5,case6,case7,case8],\
    [case9,case10,case11,case12,case13,case14,case15,case16],\
    [case17,case18,case19,case20,case21,case22,case23,case24],\
    [case25,case26,case27,case28,case29,case30,case31,case32],\
    [case33,case34,case35,case36,case37,case38,case39,case40],\
    [case41,case42,case43,case44,case45,case46,case47,case48],\
    [case49,case50,case51,case52,case53,case54,case55,case56],\
    [case57,case58,case59,case60,case61,case62,case63,case64]]




