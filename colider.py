
def colider(boatg_x,boatg_y,al1,al2,anch1,anch2,boatb_x,boatb_y):
    if (boatg_x < boatb_x + anch2 and boatg_x + anch1 > boatb_x and boatg_y < boatb_y + al2 and boatg_y + al1 > boatb_y):
        return True 
    else:
        return False     