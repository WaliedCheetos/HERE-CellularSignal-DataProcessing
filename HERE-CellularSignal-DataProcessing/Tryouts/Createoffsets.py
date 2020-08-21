##-------------------------------------------------------------------------------
## Name:        CreateOffsets.py
## Purpose:     creates roads sides representations from road centerline (using # of lanes, and average lane width), and future plan is to create lanes representation depending on lanes information
##
## Author:      WalieDCheetoS©, HERE Europe B.V.
##
## Created:     22/08/2019
## Copyright:   (c) WalieDCheetoS 2019,  HERE Europe B.V.
## Licence:     <your licence>
##-------------------------------------------------------------------------------



#import arcpy, math, traceback, sys, os, time, random, md5, datetime


#tmpwrkspace = "C:\\Users\\ahmadmoh\\Downloads\\WHAM191F0WWH000AACQU\\WHAM191F0WWH000AACQU\\"
#fc_line = tmpwrkspace + "Streets.shp"

## Set some variables
#tempFeatureClass = tmpwrkspace + "Streets_Offset.shp"

#def CreateOffset(Polyline_Original, Width):
#    try:
#        lArray=arcpy.Array();
#        rArray=arcpy.Array()
#        for ptX in Polyline_Original:
#            dL=Polyline_Original.measureOnLine(ptX)
#            ptX0=Polyline_Original.positionAlongLine (dL-0.01).firstPoint
#            ptX1=Polyline_Original.positionAlongLine (dL+0.01).firstPoint
#            dX=float(ptX1.X)-float(ptX0.X)
#            dY=float(ptX1.Y)-float(ptX0.Y)
#            lenV=math.hypot(dX,dY)
#            sX=-dY*sLength/lenV;sY=dX*sLength/lenV
#            leftP=arcpy.Point(ptX.X+sX,ptX.Y+sY)
#            lArray.add(leftP)
#            rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
#            rArray.add(rightP)

#        array = arcpy.Array([lArray, rArray])

#        spatial_reference = arcpy.SpatialReference(4326)

#        section=arcpy.Polyline(array, spatial_reference)

#        return section

#    except Exception as e:
#        #log exception
#        #
#        print("Source: _main_, " +  "A Python error occured", "ERROR")
#        msgs = traceback.format_exception(*sys.exc_info())
#        for msg in msgs:
#            print(msg.strip(), "ERROR")


#def CopyParallelR(plyP,sLength):
#    part=plyP.getPart(0)
#    rArray=arcpy.Array()
#    for ptX in part:
#        dL=plyP.measureOnLine(ptX)
#        ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
#        ptX1=plyP.positionAlongLine (dL+0.01).firstPoint
#        dX=float(ptX1.X)-float(ptX0.X)
#        dY=float(ptX1.Y)-float(ptX0.Y)
#        lenV=math.hypot(dX,dY)
#        sX=-dY*sLength/lenV;sY=dX*sLength/lenV
#        rightP=arcpy.Point(ptX.X-sX, ptX.Y-sY)
#        rArray.add(rightP)
#    array = arcpy.Array([rArray])
#    section=arcpy.Polyline(array)
#    return section

#def CopyParallelL(plyP,sLength):
#    section = None
#    try:
#        ##part=plyP.getPart(0)
#        part=plyP[0]
#        lArray=arcpy.Array()
#        x=0
#        for ptX in part:
#            #dL=plyP.measureOnLine(ptX)
#            #ptX0=plyP.positionAlongLine (dL-0.01).firstPoint
#            #ptX1=plyP.positionAlongLine (dL+0.01).firstPoint            
            
#            ##dL=plyP[0].measureOnLine(ptX[x])
#            ##ptX0=plyP[0].positionAlongLine (dL-0.01).firstPoint
#            ##ptX1=plyP[0].positionAlongLine (dL+0.01).firstPoint
#            ##dX=float(ptX1.X)-float(ptX0.X)
#            ##dY=float(ptX1.Y)-float(ptX0.Y)
#            ##lenV=math.hypot(dX,dY)
#            ##sX=-dY*sLength/lenV;sY=dX*sLength/lenV
#            ##leftP=arcpy.Point(ptX[x].X+sX,ptX[x].Y+sY)
#            ##lArray.add(leftP)
#            ##x=x+1            
#            #
#            for ptI in ptX:
#                dL=plyP[0].measureOnLine(ptI)
#                ptX0=plyP[0].positionAlongLine (dL-0.05).firstPoint
#                ptX1=plyP[0].positionAlongLine (dL+0.01).firstPoint
#                dX=float(ptX1.X)-float(ptX0.X)
#                dY=float(ptX1.Y)-float(ptX0.Y)
#                lenV=math.hypot(dX,dY)
#                sX=-dY*sLength/lenV;sY=dX*sLength/lenV
#                leftP=arcpy.Point(ptI.X+sX,ptI.Y+sY)
#                lArray.add(leftP)
#        array = arcpy.Array([lArray])
#        section=arcpy.Polyline(array)
#    except Exception as e:
#        #log exception
#        #
#        print("A Python error occured", "ERROR")
#        msgs = traceback.format_exception(*sys.exc_info())
#        for msg in msgs:
#            print(msg.strip(), "ERROR")
#    finally:
#        return section


#try:
#    if arcpy.Exists(tempFeatureClass):
#        arcpy.Delete_management(tempFeatureClass)

#    arcpy.CopyFeatures_management(fc_line, tempFeatureClass)

#    with arcpy.da.UpdateCursor(tempFeatureClass,("Shape@")) as cursor:
#        x=0
#        for shp in cursor:
#            x=x+1
#            LeftLine=CopyParallelL(shp,0.0003)
#            if LeftLine != None:
#                print(x, "- done")
#                cursor.updateRow(([LeftLine]))
            


#    #with arcpy.da.UpdateCursor(tempFeatureClass,("Shape@")) as cursor:
#    #    for shp in cursor:
#    #        line=CreateOffset(shp[0],300)
#    #        cursor.updateRow(([line]))

#except Exception as e:
#    #log exception
#    #
#    print("A Python error occured", "ERROR")
#    msgs = traceback.format_exception(*sys.exc_info())
#    for msg in msgs:
#        print(msg.strip(), "ERROR")

####################################################################################################################################


####################################################################################################
## Purpose:     creates roads sides representations from road centerline (using # of lanes, and average lane width), and future plan is to create lanes representation depending on lanes information
## Author:      WalieDCheetoS©, HERE Europe B.V.
##
## Created:     22/08/2019
## Modified:    07/09/2019
## Copyright:   (c) WalieDCheetos 2019,  HERE Europe B.V.
## Licence:     <your licence>
####################################################################################################


import math, os, arcpy, traceback, sys, time, random, md5, datetime
from arcpy import env

def calcoffsetpoint(pt1, pt2, offset):
    theta = math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])
    theta += math.pi/2.0
    return (pt1[0] + math.cos(theta) * offset, pt1[1] + math.sin(theta) * offset)

def getoffsetintercept(pt1, pt2, m, offset):
    """From points pt1 and pt2 defining a line in the Cartesian plane, the slope of the line m,
    and an offset distance, calculates the y intercept of the new line offset from the original."""
    x, y = calcoffsetpoint(pt1, pt2, offset)
    return y - m * x

def getpt(pt1, pt2, pt3, offset):
    """Gets intersection point of the two lines defined by pt1, pt2, and pt3; offset is the
    distance to offset the point from the polygon."""
    ### Get first offset intercept
    if pt2[0] - pt1[0] != 0:
        m = (pt2[1] - pt1[1])/(pt2[0] - pt1[0])
        boffset = getoffsetintercept(pt1, pt2, m, offset)
    else: # if vertical line (i.e. undefined slope)
        m = "undefined"
        
    ### Get second offset intercept
    if pt3[0] - pt2[0] != 0:
        mprime = (pt3[1] - pt2[1])/(pt3[0] - pt2[0])
        boffsetprime = getoffsetintercept(pt2, pt3, mprime, offset)
    else: # if vertical line (i.e. undefined slope)
        mprime = "undefined"
                
    ### Get intersection of two offset lines
    if m != "undefined" and mprime != "undefined":
        # if neither offset intercepts are vertical
        newx = (boffsetprime - boffset)/(m - mprime)
        newy = m * newx + boffset
    elif m == "undefined":
        # if first offset intercept is vertical
        newx, y_infinity = calcoffsetpoint(pt1, pt2, offset)
        newy = mprime * newx + boffsetprime
    elif mprime == "undefined":
        # if second offset intercept is vertical
        newx, y_infinity = calcoffsetpoint(pt2, pt3, offset)
        newy = m * newx + boffset
    elif m == "undefined" and mprime == "undefined":
        # if both offset intercepts are vertical (same line)
        newx, y_infinity = calcoffsetpoint(pt1, pt2, offset)
        newy = pt2[1]
    return newx, newy

def offsetpolygon(polyx, offset):
    """Offsets a clockwise list of coordinates polyx distance offset to the outside of the polygon.
    Returns list of offset points."""
    polyy = []
    # need three points at a time
    for counter in range(0, len(polyx) - 3):
        # get first offset intercept
        pt = getpt(polyx[counter],
                   polyx[counter + 1],
                   polyx[counter + 2],
                   offset)
        # append new point to polyy
        polyy.append(pt)
    # last three points
    pt = getpt(polyx[-3], polyx[-2], polyx[-1], offset)
    polyy.append(pt)
    pt = getpt(polyx[-2], polyx[-1], polyx[0], offset)
    polyy.append(pt)
    pt = getpt(polyx[-1], polyx[0], polyx[1], offset)
    polyy.append(pt)
    return polyy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Offset]

class Offset(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Offset"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        # First parameter
        param0 = arcpy.Parameter(
            displayName = "Input features",
            name = "inFC",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Input")
        param0.filter.list = ["Polyline", "Polygon"]
        
        # Second parameter
        param1 = arcpy.Parameter(
            displayName = "Output features",
            name = "outFC",
            datatype = "GPFeatureLayer",
            parameterType = "Required",
            direction = "Output")

        # Third parameter
        param2 = arcpy.Parameter(
            displayName = "Offset distance",
            name = "offset_dist",
            datatype = "GPDouble",
            parameterType = "Required",
            direction = "Input")

        params = [param0, param1, param2]
        
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        ### get parameters
        inFC = parameters[0].valueAsText
        outFC = parameters[1].valueAsText
        offset_dist = parameters[2].valueAsText

        ### check geometry type (Polygon or Polyline)
        desc = arcpy.Describe(inFC)
        geomType = desc.shapeType
        if geomType == 'Polygon':
            
            ### convert offset_dist to float
            offset_dist = float(offset_dist)
    
            ### Print progress
            spat = arcpy.Describe(inFC).spatialReference
            units = spat.linearUnitName
            arcpy.AddMessage("Offsetting %s %s..." % (offset_dist, units))
    
            ### Enable overwrite permission
            arcpy.env.overwriteOutput = True
    
            ### Create output shapefile by copying input shapefile
            outFC = arcpy.CopyFeatures_management(inFC, outFC).getOutput(0)
    
            ### Create empty Array objects
            parts = arcpy.Array()
            rings = arcpy.Array()
            ring = arcpy.Array()
    
            ### Create cursor and update vertex coordinates
            cursor = arcpy.UpdateCursor(outFC)
            shapefield = arcpy.Describe(outFC).shapeFieldName
    
            ### Loop through features of inFC
            for row in cursor:
                newPartList = []
                # loop trough parts of feature
                for part in row.getValue(shapefield):
                    coordList = []
                    counter = 0
                    # loop through points in part
                    for pnt in part:
                        if counter == 0: #skip first point
                            counter += 1
                        else:
                            if pnt:
                                coordList.append((pnt.X, pnt.Y))
                                counter += 1
                            else: #null point, denotes beginning of inner ring
                                counter = 0 #reset counter
                                offsetList = offsetpolygon(coordList, offset_dist) #calculate offset points
                                newPartList.append(offsetList) #add coordinates to new list
                                coordList = [] #empty list
    
                    ### Add final (or only) offset coordinates for part
                    offsetList = offsetpolygon(coordList, offset_dist)
                    newPartList.append(offsetList)
                           
                ### loop through newPartList, to create new polygon geometry object for row
                for part in newPartList:
                    for pnt in part:
                        if pnt:
                            ring.add(arcpy.Point(pnt[0], pnt[1]))
                        else: #null point
                            rings.add(ring)
                            ring.removeAll()
                            
                    ### if last ring, add it
                    rings.add(ring)
                    ring.removeAll()
    
                    ### if only one ring, remove nesting
                    if len(rings) == 1:
                        rings = rings.getObject(0)
    
                    parts.add(rings)
                    rings.removeAll()
                    
                ### if single-part, remove nesting
                if len(parts) == 1:
                    parts = parts.getObject(0)
    
                ### create polygon object based on parts array
                polygon = arcpy.Polygon(parts)
                parts.removeAll()
                
                ### replace geometry with new polygon object
                row.setValue(shapefield, polygon)
    
                ### update cursor
                cursor.updateRow(row)
                
        elif geomType == 'Polyline':
            ### print progress
            units = desc.spatialReference.linearUnitName
            arcpy.AddMessage("Offsetting %s %s..." % (offset_dist, units))

            ### enable overwrite permission
            arcpy.env.overwriteOutput = True

            ###TODO: update code to offset polylines
            
        return



        """The source code of the tool."""

        """The source code of the tool."""



tmpwrkspace = "C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\WEAM191F0WWE000AACP8\\"
fc_line = tmpwrkspace + "Streets_Cut.shp"

# Set some variables
tempFeatureClass = tmpwrkspace + "Streets_Offset.shp"

##The source code of the tool.
##
try:
    print("WaliedCheetos: Hollla ...!!!")
    
    ### get parameters

    #inFC = parameters[0].valueAsText
    inFC = fc_line

    #outFC = parameters[1].valueAsText
    outFC = tempFeatureClass
    
    #offset_dist = parameters[2].valueAsText
    offset_dist = 0.000035

    ### check geometry type (Polygon or Polyline)
    desc = arcpy.Describe(inFC)
    geomType = desc.shapeType

    if (geomType.lower() == 'Polyline'.lower()):
            
        ### convert offset_dist to float
        offset_dist = float(offset_dist)
    
        ### Print progress
        spat = arcpy.Describe(inFC).spatialReference
        units = spat.linearUnitName
        arcpy.AddMessage("Offsetting %s %s..." % (offset_dist, units))
    
        ### Enable overwrite permission
        arcpy.env.overwriteOutput = True
    
        ### Check if shapefile exists, then delete it
        if arcpy.Exists(outFC):
            arcpy.Delete_management(outFC)

        ### Create output shapefile by copying input shapefile
        outFC = arcpy.CopyFeatures_management(inFC, outFC).getOutput(0)
    
        ### Create empty Array objects
        parts = arcpy.Array()
        rings = arcpy.Array()
        ring = arcpy.Array()
    
        ### Create cursor and update vertex coordinates
        cursor = arcpy.UpdateCursor(outFC)
        shapefield = arcpy.Describe(outFC).shapeFieldName
    
        ### Loop through features of inFC
        for row in cursor:
            newPartList = []
            # loop trough parts of feature
            for part in row.getValue(shapefield):
                coordList = []
                counter = 0
                # loop through points in part
                for pnt in part:
                    if counter == 0: #skip first point
                        counter += 1
                    else:
                        if pnt:
                            coordList.append((pnt.X, pnt.Y))
                            counter += 1
                        else: #null point, denotes beginning of inner ring
                            counter = 0 #reset counter
                            offsetList = offsetpolygon(coordList, offset_dist) #calculate offset points
                            newPartList.append(offsetList) #add coordinates to new list
                            coordList = [] #empty list
    
                ### Add final (or only) offset coordinates for part
                offsetList = offsetpolygon(coordList, offset_dist)
                newPartList.append(offsetList)
                           
            ### loop through newPartList, to create new polygon geometry object for row
            for part in newPartList:
                for pnt in part:
                    if pnt:
                        ring.add(arcpy.Point(pnt[0], pnt[1]))
                    else: #null point
                        rings.add(ring)
                        ring.removeAll()
                            
                ### if last ring, add it
                rings.add(ring)
                ring.removeAll()
    
                ### if only one ring, remove nesting
                if len(rings) == 1:
                    rings = rings.getObject(0)
    
                parts.add(rings)
                rings.removeAll()
                    
            ### if single-part, remove nesting
            if len(parts) == 1:
                parts = parts.getObject(0)
    
            ### create polygon object based on parts array
            polygon = arcpy.Polygon(parts)
            parts.removeAll()
                
            ### replace geometry with new polygon object
            row.setValue(shapefield, polygon)
    
            ### update cursor
            cursor.updateRow(row)
                
except Exception as e:
    #log exception
    #
    print("A Python error occured", "ERROR")
    msgs = traceback.format_exception(*sys.exc_info())
    for msg in msgs:
        print(msg.strip(), "ERROR")
    
finally:
    print("WaliedCheetos: Done ...!!!")