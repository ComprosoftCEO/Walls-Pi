#Defines pictures to use in effects

R = (255,0,0)
Y = (255,255,0)
G = (0,255,0)
MG = (0,190,0)
DG = (0,92,0)
B = (0,0,255)
LB = (0,0,64)
T = (0,64,64)
X = (0,0,0)
O = (128,64,0)
W = (128,64,64)
WH = (128,128,128)


RED_KEY = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,R,R,X,X,X,X,X,
    R,X,R,R,R,R,R,R,
    X,R,R,X,X,R,R,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


YELLOW_KEY = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,Y,Y,X,X,X,X,X,
    Y,X,Y,Y,Y,Y,Y,Y,
    X,Y,Y,X,X,Y,Y,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


GREEN_KEY = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,G,G,X,X,X,X,X,
    G,X,G,G,G,G,G,G,
    X,G,G,X,X,G,G,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


BLUE_KEY = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,B,B,X,X,X,X,X,
    B,X,B,B,B,B,B,B,
    X,B,B,X,X,B,B,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


BOOTS = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,T,X,X,X,
    X,T,X,X,T,X,X,X,
    X,T,X,X,T,X,X,X,
    X,T,X,X,T,T,X,X,
    X,T,T,X,T,T,T,X,
    X,T,T,T,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


TORCH = [
    X,X,X,X,X,X,X,X,
    X,X,X,R,R,X,X,X,
    X,X,R,O,O,R,X,X,
    X,X,O,Y,Y,O,X,X,
    X,X,W,W,W,W,X,X,
    X,X,X,W,W,X,X,X,
    X,X,X,W,W,X,X,X,
    X,X,X,X,X,X,X,X
    ]

ENERGY = [
    X,X,R,R,R,R,X,X,
    X,R,O,Y,Y,O,R,X,
    R,O,Y,G,G,Y,O,R,
    R,Y,G,B,B,G,Y,R,
    R,Y,G,B,B,G,Y,R,
    R,O,Y,G,G,Y,O,R,
    X,R,O,Y,Y,O,R,X,
    X,X,R,R,R,R,X,X
    ]

WIN = [
    Y, Y ,LB,LB,LB,LB,LB,LB,
    Y ,LB,LB,LB,LB,WH,WH,LB,
    LB,LB,WH,WH,LB,LB,LB,LB,
    LB,LB,LB,LB,LB,LB,LB,LB,
    LB,LB,DG,LB,LB,DG,LB,LB,
    LB,DG,DG,DG,DG,DG,DG,LB,
    MG,MG,MG,MG,MG,MG,MG,MG,
    G ,G ,G ,G ,G ,G ,G ,G
    ]
