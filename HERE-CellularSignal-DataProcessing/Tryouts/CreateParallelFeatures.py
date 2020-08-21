import arcpy, math, traceback, sys, os, time, random, md5, datetime

infc=r'..\SCRARCH\clone.shp'

tmpwrkspace = "C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\WEAM191F0WWE000AACP8\\"
fc_line = tmpwrkspace + "Streets_Cut.shp"

# Set some variables
tempFeatureClassname = "Streets_Offset_test.shp"
tempFeatureClass = tmpwrkspace + tempFeatureClassname
templateFeatureClass = tmpwrkspace + "StreetsOffsetTemplate.shp"

avgLaneWidth = 0.000038

#def CopyParallel(plyP, part, sLength):
#    #part=plyP.getPart(0)

#    lArray=arcpy.Array()
#    rArray=arcpy.Array()
#    for ptX in part:
#        dL=plyP.measureOnLine(ptX)
#        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
#        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
#        dX=float(ptX1.X)-float(ptX0.X)
#        dY=float(ptX1.Y)-float(ptX0.Y)
#        lenV=math.hypot(dX,dY)
#        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
#        leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
#        lArray.add(leftP)
#        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
#        rArray.add(rightP)
#    array = arcpy.Array([lArray, rArray])
#    section=arcpy.Polyline(array)
#    return section

def CopyParallel(plyP, part, sLength):
    #part=plyP.getPart(0)

    lArray=arcpy.Array()
    rArray=arcpy.Array()
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
        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
        rArray.add(rightP)
    #array = arcpy.Array([lArray, rArray])
    array = arcpy.Array(rArray)
    section=arcpy.Polyline(array)
    return section
    #return array



def CopyParallel(plyP, part, sLength, direction):
    #part=plyP.getPart(0)

    lArray=arcpy.Array()
    rArray=arcpy.Array()
    array = None

    for ptX in part:
        dL=plyP.measureOnLine(ptX)
        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
        dX=float(ptX1.X)-float(ptX0.X)
        dY=float(ptX1.Y)-float(ptX0.Y)
        lenV=math.hypot(dX,dY)
        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
        
        if direction.lower() == 'Left'.lower():        
            leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
            lArray.add(leftP)        
        elif direction.lower() == 'Right'.lower():        
            rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
            rArray.add(rightP)        
        elif direction.lower() == 'Right&Left'.lower():        
            leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
            lArray.add(leftP)
            rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
            rArray.add(rightP)
    array = arcpy.Array([lArray, rArray])
    section=arcpy.Polyline(array)
    return section

    


def CopyParallelL(plyP,sLength):
    section = None
    try:
        ##part=plyP.getPart(0)
        part=plyP[0]
        lArray=arcpy.Array()
        x=0
        for ptX in part:
            #dL=plyP.measureOnLine(ptX)
            #ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
            #ptX1=plyP.positionAlongLine (dL+0.01).firstPoint            
            
            ##dL=plyP[0].measureOnLine(ptX[x])
            ##ptX0=plyP[0].positionAlongLine (dL-0.01).firstPoint
            ##ptX1=plyP[0].positionAlongLine (dL+0.01).firstPoint
            ##dX=float(ptX1.X)-float(ptX0.X)
            ##dY=float(ptX1.Y)-float(ptX0.Y)
            ##lenV=math.hypot(dX,dY)
            ##sX=-dY*sLength/lenV;sY=dX*sLength/lenV
            ##leftP=arcpy.Point(ptX[x].X+sX,ptX[x].Y+sY)
            ##lArray.add(leftP)
            ##x=x+1            
            #
            for ptI in ptX:
                dL=plyP[0].measureOnLine(ptI)
                ptX0=plyP[0].positionAlongLine (dL-0.05).firstPoint
                ptX1=plyP[0].positionAlongLine (dL+0.01).firstPoint
                dX=float(ptX1.X)-float(ptX0.X)
                dY=float(ptX1.Y)-float(ptX0.Y)
                lenV=math.hypot(dX,dY)
                sX=-dY*sLength/lenV;sY=dX*sLength/lenV
                leftP=arcpy.Point(ptI.X+sX,ptI.Y+sY)
                lArray.add(leftP)
        array = arcpy.Array([lArray])
        section=arcpy.Polyline(array)
    except Exception as e:
        #log exception
        #
        print("A Python error occured", "ERROR")
        msgs = traceback.format_exception(*sys.exc_info())
        for msg in msgs:
            print(msg.strip(), "ERROR")
    finally:
        return section


##The source code of the tool.
##
try:
    print("WaliedCheetos: Hollla ...!!!")

    if arcpy.Exists(tempFeatureClass):
        arcpy.Delete_management(tempFeatureClass)

    ##arcpy.CopyFeatures_management(fc_line, tempFeatureClass)

    # Use Describe to get a SpatialReference object
    spatial_reference = arcpy.Describe(templateFeatureClass).spatialReference
    # Execute CreateFeatureclass
    arcpy.CreateFeatureclass_management(tmpwrkspace, tempFeatureClassname, 'POLYLINE', templateFeatureClass, 'DISABLED', 'DISABLED', spatial_reference)


    ## Enter for loop for each feature
    ##
    #for row in arcpy.da.SearchCursor(tempFeatureClass, ["OID@", "SHAPE@"]):
    #    # Print the current multipoint's ID
    #    #
    #    print("Feature {}:".format(row[0]))
    #    partnum = 0

    #    # Step through each part of the feature
    #    #
    #    for part in row[1]:
    #        # Print the part number
    #        #
    #        print("Part {}:".format(partnum))

    #        # Step through each vertex in the feature
    #        #
    #        for pnt in part:
    #            if pnt:
    #                # Print x,y coordinates of current point
    #                #
    #                print("{}, {}".format(pnt.X, pnt.Y))
    #            else:
    #                # If pnt is None, this represents an interior ring
    #                #
    #                print("Interior Ring:")
    #        partnum += 1

    # Use SearchCursor 
    #
    with arcpy.da.SearchCursor(fc_line, ['LINK_ID', 'SHAPE@', 'FROM_LANES', 'TO_LANES', 'DIR_TRAVEL', 'NUM_STNMES']) as cursor:
        # Open an InsertCursor and insert the new geometry
        insertCursor = arcpy.da.InsertCursor(tempFeatureClass, ['LINK_ID', "SHAPE@", "FROM_LANES", "TO_LANES"])

        for row in cursor:
            print("==================================================   " + ("link {}:".format(row[0])) + "   =====================================================================")
            
            partnum = 0

            ###------------------------------------------NEW------------------------------------------##
            #RoadEdgeOffset_R = ((row[5]/2) * avgLaneWidth)
            #RoadEdgeOffset_L = ((row[5]/2) * avgLaneWidth)

            ## Step through each part of the feature
            ##
            #for part in row[1]:

            #    dblLine=CopyParallel(row[1], part, RoadEdgeOffset_R, 'Right')
            #    if dblLine != None:
            #        insertCursor.insertRow((row[0], dblLine, row[2], row[3]))
            #        print("link {}:".format(row[0]), " right edge - has been processed")

            #    dblLine=CopyParallel(row[1], part, RoadEdgeOffset_L, 'Left')
            #    if dblLine != None:
            #        insertCursor.insertRow((row[0], dblLine, row[2], row[3]))
            #        print("link {}:".format(row[0]), " left edge - has been processed")

            #    partnum = partnum+1
            #    print("part {}:".format(partnum))

            ###------------------------------------------NEW------------------------------------------##

            RoadEdgeOffset_R = 0
            RoadEdgeOffset_L = 0

            if (row[0] == 1202606650):

                ##link represents only north direction (from)
                #if ( (row[2] > 0) & (row[3] == 0) ):
                if ( (row[4].upper() == 'F'.upper()) ):
                    print("North lanes ONLY")
                    RoadEdgeOffset_R = ((row[2]/2) * avgLaneWidth)
                    RoadEdgeOffset_L = ((row[2]/2) * avgLaneWidth)

	            ##link represents only south direction (to)
                #elif ( (row[2] == 0) & (row[3] > 0) ):
                elif ( (row[4].upper() == 'T'.upper()) ):
                    print("South lanes ONLY")
                    RoadEdgeOffset_R = ((row[3]/2) * avgLaneWidth)
                    RoadEdgeOffset_L = ((row[3]/2) * avgLaneWidth)

                ##link represents north/south direction with/without lanes information
                elif ( (row[4].upper() == 'B'.upper()) ):
                    if (row[2] == 0):
                        RoadEdgeOffset_R = (1 * avgLaneWidth)
                    else:
                        RoadEdgeOffset_R = (row[2] * avgLaneWidth)                
                    
                    if (row[3] == 0):
                        RoadEdgeOffset_L = (1 * avgLaneWidth)
                    else:
                        RoadEdgeOffset_L = (row[3] * avgLaneWidth)

                # Step through each part of the feature
                #
                for part in row[1]:

                    dblLine=CopyParallel(row[1], part, RoadEdgeOffset_R, 'Right')
                    if dblLine != None:
                        insertCursor.insertRow((row[0], dblLine, row[2], row[3]))
                        print("link {}:".format(row[0]), " right edge - has been processed")

                    dblLine=CopyParallel(row[1], part, RoadEdgeOffset_L, 'Left')
                    if dblLine != None:
                        insertCursor.insertRow((row[0], dblLine, row[2], row[3]))
                        print("link {}:".format(row[0]), " left edge - has been processed")

                    partnum = partnum+1
                    print("part {}:".format(partnum))


        del insertCursor





except Exception as e:
    #log exception
    #
    print("A Python error occured", "ERROR")
    msgs = traceback.format_exception(*sys.exc_info())
    for msg in msgs:
        print(msg.strip(), "ERROR")
    
finally:
    print("WaliedCheetos: Done ...!!!")
