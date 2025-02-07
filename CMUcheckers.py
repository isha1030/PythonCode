# checkerboard design
Rect(0, 0, 400, 400, fill = rgb(62,79,63),  border = rgb(51, 49, 46), borderWidth = 3)
Rect(25, 25, 350, 350, fill = rgb(212, 208, 201), border = rgb(51, 49, 46), borderWidth = 2)
Rect(38, 38, 324, 324, fill = rgb(51, 49, 46), borderWidth = 2, dashes = (100, 0))
Rect(40, 40, 320, 320, fill = rgb(230,229,227))

Line(0, 0, 40, 40, fill = rgb(51, 49, 46), opacity = 70)
Line(0, 400, 40, 360, fill = rgb(51, 49, 46), opacity = 70)
Line(400, 0, 360, 40, fill = rgb(51, 49, 46), opacity = 70)
Line(400, 400, 360, 360, fill = rgb(51, 49, 46), opacity = 70)

# tiles
playableTiles = [
    Rect(80, 40, 40, 40, fill = rgb(212, 208, 201)),
    Rect(160, 40, 40, 40, fill = rgb(212, 208, 201)),
    Rect(240, 40, 40, 40, fill = rgb(212, 208, 201)),
    Rect(320, 40, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(40, 80, 40, 40, fill = rgb(212, 208, 201)),
    Rect(120, 80, 40, 40, fill = rgb(212, 208, 201)),
    Rect(200, 80, 40, 40, fill = rgb(212, 208, 201)),
    Rect(280, 80, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(80, 120, 40, 40, fill = rgb(212, 208, 201)),
    Rect(160, 120, 40, 40, fill = rgb(212, 208, 201)),
    Rect(240, 120, 40, 40, fill = rgb(212, 208, 201)),
    Rect(320, 120, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(40, 160, 40, 40, fill = rgb(212, 208, 201)),
    Rect(120, 160, 40, 40, fill = rgb(212, 208, 201)),
    Rect(200, 160, 40, 40, fill = rgb(212, 208, 201)),
    Rect(280, 160, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(80, 200, 40, 40, fill = rgb(212, 208, 201)),
    Rect(160, 200, 40, 40, fill = rgb(212, 208, 201)),
    Rect(240, 200, 40, 40, fill = rgb(212, 208, 201)),
    Rect(320, 200, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(40, 240, 40, 40, fill = rgb(212, 208, 201)),
    Rect(120, 240, 40, 40, fill = rgb(212, 208, 201)),
    Rect(200, 240, 40, 40, fill = rgb(212, 208, 201)),
    Rect(280, 240, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(80, 280, 40, 40, fill = rgb(212, 208, 201)),
    Rect(160, 280, 40, 40, fill = rgb(212, 208, 201)),
    Rect(240, 280, 40, 40, fill = rgb(212, 208, 201)),
    Rect(320, 280, 40, 40, fill = rgb(212, 208, 201)),
    
    Rect(40, 320, 40, 40, fill = rgb(212, 208, 201)),
    Rect(120, 320, 40, 40, fill = rgb(212, 208, 201)),
    Rect(200, 320, 40, 40, fill = rgb(212, 208, 201)),
    Rect(280, 320, 40, 40, fill = rgb(212, 208, 201))
    ]

Line(80, 200, 322, 200, fill = 'dimgray', lineWidth = 320, dashes = (1, 39))
Line(200, 80, 200, 322, fill = "dimgray", lineWidth = 320, dashes = (1, 39))


positionList = [
    Label("12", 100, 60),
    Label("14", 180, 60),
    Label("16", 260, 60),
    Label("18", 340, 60),
   
    Label("21", 60, 100),
    Label("23", 140, 100),
    Label("25", 220, 100),
    Label("27", 300, 100),
    
    Label("32", 100, 140),
    Label("34", 180, 140),
    Label("36", 260, 140),
    Label("38", 340, 140),
     
    Label("41", 60, 180),
    Label("43", 140, 180),
    Label("45", 220, 180),
    Label("47", 300, 180),
    
    Label("52", 100, 220),
    Label("54", 180, 220),
    Label("56", 260, 220),
    Label("58", 340, 220),
    
    Label("61", 60, 260),
    Label("63", 140, 260),
    Label("65", 220, 260),
    Label("67", 300, 260),
    
    Label("72", 100, 300),
    Label("74", 180, 300),
    Label("76", 260, 300),
    Label("78", 340, 300),
    
    Label("81", 60, 340),
    Label("83", 140, 340),
    Label("85", 220, 340),
    Label("87", 300, 340)
    ]

for position in positionList:
    position.fill = rgb(212, 208, 201)
    
# pieces
brownPieces = [
    Circle(100, 60, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(180, 60, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(260, 60, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(340, 60, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(60, 100, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(140, 100, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(220, 100, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(300, 100, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(100, 140, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(180, 140, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(260, 140, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88))),
    Circle(340, 140, 18, fill = gradient(rgb(54, 53, 46), rgb(54, 53, 46), rgb(92, 92, 88)))
    ]

grayPieces = [
    Circle(60, 260, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(140, 260, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(220, 260, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(300, 260, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(100, 300, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(180, 300, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(260, 300, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(340, 300, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(60, 340, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(140, 340, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(220, 340, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155))),
    Circle(300, 340, 18, fill = gradient(rgb(110, 115, 112), rgb(110, 115, 112), rgb(153, 158, 155)))
    ]

# label
Rect(5, 365, 390, 30, fill = rgb(230,229,227), border = rgb(51, 49, 46), borderWidth = 2)
message = Label("gray plays first | pieces can only move diagonally", 200, 380, fill = "black", font = "monospace", size = 12)

app.currentPlace = 0
app.finalPlace = 0
app.selectedPiece = 0
app.pieceSelected = False
app.grayTurn = True

# function for finding position of tiles
def getTile(positionValue):
    for position in positionList:
        if positionValue == int(position.value):
            positionIndex = positionList.index(position)
            tile = playableTiles[positionIndex]
            return tile


def isValidMove():
    #  during gray piece's turn
    if app.grayTurn == True:
        # check if piece is moving to either -11 or -9
        if app.currentPlace - 11 == app.finalPlace or app.currentPlace - 9 == app.finalPlace:
            # make sure that there is no brown/gray piece in the final place
            tile = getTile(app.finalPlace)
            for brownPiece in brownPieces:
                if brownPiece.hitsShape(tile) == True:
                    return False
            for grayPiece in grayPieces:
                if grayPiece.hitsShape(tile) == True:
                    return False
            return True
        # check if piece is moving to either -22 or -18
        elif app.currentPlace - 22 == app.finalPlace or app.currentPlace - 18 == app.finalPlace:
            tile = getTile(app.finalPlace)
            for brownPiece in brownPieces:
                if brownPiece.hitsShape(tile) == True:
                    return False
            for grayPiece in grayPieces:
                if grayPiece.hitsShape(tile) == True:
                    return False
            # make sure that there is a brown piece in the middle
            if app.currentPlace - 22 == app.finalPlace:
                tile = getTile(app.currentPlace - 11)
                for brownPiece in brownPieces:
                    if brownPiece.hitsShape(tile) == True:
                        return True
            elif app.currentPlace - 18 == app.finalPlace:
                tile = getTile(app.currentPlace - 9)
                for brownPiece in brownPieces:
                    if brownPiece.hitsShape(tile) == True:
                        return True
            else:
                return False
        else:
            return False
    else:
        if app.currentPlace + 11 == app.finalPlace or app.currentPlace + 9 == app.finalPlace:
            # make sure that there is no brown/gray piece in final place
            tile = getTile(app.finalPlace)
            for brownPiece in brownPieces:
                if brownPiece.hitsShape(tile) == True:
                    return False
            for grayPiece in grayPieces:
                if grayPiece.hitsShape(tile) == True:
                    return False
            return True
        # check if piece is moving to either +22 or +18
        elif app.currentPlace + 22 == app.finalPlace or app.currentPlace + 18 == app.finalPlace:
            tile = getTile(app.finalPlace)
            for brownPiece in brownPieces:
                if brownPiece.hitsShape(tile) == True:
                    return False
            for grayPiece in grayPieces:
                if grayPiece.hitsShape(tile) == True:
                    return False
            # make sure that there is a gray piece in the middle
            if app.currentPlace + 22 == app.finalPlace:
                tile = getTile(app.currentPlace + 11)
                for grayPiece in grayPieces:
                    if grayPiece.hitsShape(tile) == True:
                        return True
            elif app.currentPlace + 18 == app.finalPlace:
                tile = getTile(app.currentPlace + 9)
                for grayPiece in grayPieces:
                    if grayPiece.hitsShape(tile) == True:
                        return True
            else:
                return False
        else:
            return False
    
# get rid of opponent pieces    
def killOpponent():
    # on brown piece's turn
    if app.grayTurn == False:
        # skipping a row
        if app.currentPlace + 18 == app.finalPlace:
            for position in positionList:
                if app.currentPlace + 9 == int(position.value):
                    positionIndex = positionList.index(position)
                    tile9 = playableTiles[positionIndex]
                    for grayPiece in grayPieces:
                        if grayPiece.hitsShape(tile9) == True:
                            # get rid of piece
                            grayPiece.visible = False
                            grayPieces.remove(grayPiece)
        elif app.currentPlace + 22 == app.finalPlace:
            for position in positionList:
                if app.currentPlace + 11 == int(position.value):
                    positionIndex = positionList.index(position)
                    tile9 = playableTiles[positionIndex]
                    for grayPiece in grayPieces:
                        if grayPiece.hitsShape(tile9) == True:
                            grayPiece.visible = False
                            grayPieces.remove(grayPiece)
    else:
        if app.currentPlace - 18 == app.finalPlace:
            for position in positionList:
                if app.currentPlace - 9 == int(position.value):
                    positionIndex = positionList.index(position)
                    tile9 = playableTiles[positionIndex]
                    for brownPiece in brownPieces:
                        if brownPiece.hitsShape(tile9) == True:
                            brownPiece.visible = False
                            brownPieces.remove(brownPiece)
        elif app.currentPlace - 22 == app.finalPlace:
            for position in positionList:
                if app.currentPlace - 11 == int(position.value):
                    positionIndex = positionList.index(position)
                    tile9 = playableTiles[positionIndex]
                    for brownPiece in brownPieces:
                        if brownPiece.hitsShape(tile9) == True:
                            brownPiece.visible = False
                            brownPieces.remove(brownPiece)
                

def onMousePress(mouseX, mouseY):
 
    if app.pieceSelected == False:
        if app.grayTurn == True:
            for grayPiece in grayPieces:
                if grayPiece.hits(mouseX, mouseY) == True:
                    app.selectedPiece = grayPiece
                    app.pieceSelected = True
                    app.grayTurn = True
                    for position in positionList:
                        if grayPiece.hitsShape(position) == True:
                            app.currentPlace = int(position.value)
                      
        if app.grayTurn == False:              
            for brownPiece in brownPieces:
                if brownPiece.hits(mouseX, mouseY) == True:
                    app.selectedPiece = brownPiece
                    app.pieceSelected = True
                    app.grayTurn = False
                    for position in positionList:
                        if brownPiece.hitsShape(position) == True:
                            app.currentPlace = int(position.value)
        
    else:
        for tile in playableTiles:
            if tile.hits(mouseX, mouseY) == True:
                tileIndex = playableTiles.index(tile)
                app.finalPlace = int(positionList[tileIndex].value)
                app.pieceSelected = False
                if isValidMove() :
                    app.selectedPiece.centerX = positionList[tileIndex].centerX
                    app.selectedPiece.centerY = positionList[tileIndex].centerY
                    killOpponent()
                    if app.grayTurn :
                        app.grayTurn = False
                    else:
                        app.grayTurn = True
                
            



