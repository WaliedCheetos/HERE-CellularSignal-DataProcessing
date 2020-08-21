import arcpy, math
from math import atan2, pi

tmpwrkspace = "C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\WEAM191F0WWE000AACP8\\"
fc_line = tmpwrkspace + "Streets_Cut.shp"

# Set some variables
tempFeatureClass = tmpwrkspace + "Streets_Offset.shp"



def CopyParallelL(plyP,sLength):
    part=plyP.getPart(0)
    lArray=arcpy.Array()
    for ptX in part:
        dL=plyP.measureOnLine(ptX)
        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
        lArray.add(leftP)
    array = arcpy.Array([lArray])
    section=arcpy.Polyline(array)
    return section


def CopyParallelR(plyP,sLength):
    part=plyP.getPart(0)
    rArray=arcpy.Array()
    for ptX in part:
        dL=plyP.measureOnLine(ptX)
        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
        rArray.add(rightP)
    array = arcpy.Array([rArray])
    section=arcpy.Polyline(array)
    return section


def CopyParallel(plyP,sLength):
    if plyP[0].isMultipart:
        part=plyP.getPart(0)
    else:
        part=plyP[0]
    
    lArray=arcpy.Array();rArray=arcpy.Array()
    for ptX in part:
        dL=plyP[0].measureOnLine(ptX)
        ptX0=plyP[0].positionAlongLine (dL-0.03).firstPoint
        ptX1=plyP[0].positionAlongLine (dL+0.03).firstPoint
        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
        lArray.add(leftP)
        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
        rArray.add(rightP)
    array = arcpy.Array([lArray, rArray])
    section=arcpy.Polyline(array)
    return section


# epsilon
e = 1e-10

def tangentLine(line, dist):
    '''creates a tangent line of length dist at line midpoint
    line - arcpy.Polyline() object
    dist - distance in meters
    '''

    midpoint = line.positionAlongLine(0.5, True)

    # get points immediately before and after midpoint
    before = line.positionAlongLine(0.5-e, True)
    after = line.positionAlongLine(0.5+e, True)

    dX = after.firstPoint.X - before.firstPoint.X
    dY = after.firstPoint.Y - before.firstPoint.Y

    # angle of the midpoint segment
    angle = atan2(dX, dY) * 180 / pi
    newpoint = midpoint.pointFromAngleAndDistance(angle + 90, dist)
    spatial_reference = arcpy.SpatialReference(4326)

    return arcpy.Polyline(arcpy.Array((midpoint.firstPoint, newpoint.firstPoint)), spatial_reference)



def RotateExtend(plyP,sLength):
 l=plyP.length
 ptX=plyP.positionAlongLine (l/2).firstPoint
 ptX0=plyP.firstPoint
 ptX1=plyP.lastPoint
 dX=float(ptX1.X)-float(ptX0.X)
 dY=float(ptX1.Y)-float(ptX0.Y)
 lenV=math.sqrt(dX*dX+dY*dY)
 sX=-dY*sLength/lenV;sY=dX*sLength/lenV
 leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
 rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
 array = arcpy.Array([leftP,rightP])
 section=arcpy.Polyline(array)
 return section


if arcpy.Exists(tempFeatureClass):
    arcpy.Delete_management(tempFeatureClass)

#arcpy.CopyFeatures_management(fc_line, tempFeatureClass)

#cursor = arcpy.da.InsertCursor(tempFeatureClass, ['SHAPE@XY'])

arcpy.CopyFeatures_management([tangentLine(line, 300)
    for line in arcpy.CopyFeatures_management(fc_line, arcpy.Geometry())],
    tempFeatureClass)

#### Perform the move
###with arcpy.da.UpdateCursor(tempFeatureClass, ("Shape@")) as cursor:
###    for shp in cursor:
###        newLine = tangentLine(shp[0], 30)
###        cursor.updateRow([newLine])
###        ##cursor.updateRow([[row[0][0] + xOffset_N, row[0][1] + yOffset_N]])

#if arcpy.Exists(tempFeatureClass):
#    arcpy.Delete_management(tempFeatureClass)

#arcpy.CopyFeatures_management(fc_line, tempFeatureClass)


##with arcpy.da.UpdateCursor(tempFeatureClass,("Shape@","Width")) as cursor:
#with arcpy.da.UpdateCursor(tempFeatureClass,("Shape@")) as cursor:
#    #for shp,w in cursor:    
#    for shp in cursor:
#        twoLines=CopyParallel(shp,3000)
#        cursor.updateRow((twoLines))


##set the offset to +n or -n for direction
#xOffset_P = 0.003
#yOffset_P = 0.003
#xOffset_N = -0.3
#yOffset_N = -0.3



## Perform the move
#with arcpy.da.UpdateCursor(tempFeatureClass, ["SHAPE@XY"]) as cursor:
#    for row in cursor:
#        cursor.updateRow([[row[0][0] + xOffset_P, row[0][1] + yOffset_P]])
#        ##cursor.updateRow([[row[0][0] + xOffset_N, row[0][1] + yOffset_N]])
