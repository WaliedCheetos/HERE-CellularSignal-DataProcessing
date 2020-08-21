import arcpy

line_lyr = 'C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Cellular Signals\\From Zimka\\ORD_FGDB\\ORD_CELL_SIGNAL.gdb\\CELLULAR_GEOMETRY'
pt_lyr =  "C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Cellular Signals\\From Zimka\\ORD_FGDB\\ORD_CELL_SIGNAL.gdb\\splt_pnts"
##interval = 200

insertCursor = arcpy.da.InsertCursor(pt_lyr, ["SHAPE@XY"]) # this is the pre-existing pt feature class

with arcpy.da.SearchCursor(line_lyr, ['OID@','SHAPE@'], where_clause='TOPOLOGY_SEGMENT_ID = 413318764') as searchCursor: # this is the line feature on which the points will be based
    for row in searchCursor:
        point = row[1].positionAlongLine(0.90,True).firstPoint
        insertCursor.insertRow([point])

# Close and delete cursor
del insertCursor

        #lengthLine = round(row[1].length) # grab the length of the line feature, i'm using round() here to avoid weird rounding errors that prevent the numberOfPositions from being determined
        #if int(lengthLine % interval) == 0:
        #    numberOfPositions = int(lengthLine // interval) - 1
        #else:
        #    numberOfPositions = int(lengthLine // interval)

        #print "lengthLine", lengthLine
        #print "numberOfPositions", numberOfPositions
        #if numberOfPositions > 0: # > 0 b/c we don't want to add a point to a line feature that is less than our interval
        #    for i in range(numberOfPositions): # using range, allows us to not have to worry about
        #        distance = (i + 1) * interval
        #        xPoint = row[1].positionAlongLine(distance).firstPoint.X
        #        yPoint = row[1].positionAlongLine(distance).firstPoint.Y
        #        xy = (xPoint, yPoint)
        #        insertCursor.insertRow([xy])