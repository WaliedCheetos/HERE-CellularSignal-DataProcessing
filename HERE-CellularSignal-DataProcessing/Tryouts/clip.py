import arcpy
from arcpy import env
import os

# Set the workspace for the ListFeatureClass function
#
env.workspace = "C:/Users/ahmadmoh/O_o/HERE/Clients/Bayanat/United Arab Emirates Shapefile UTF SLFC12"
env.overwriteOutput = True

# Set local variables
in_features = ""
clip_features = "C:/Users/ahmadmoh/Desktop/RasAlKhaima_AOI/RasAlKhaima_AOI/RasAlKhaima_AOI.shp"
out_feature_class = "C:/Users/ahmadmoh/O_o/HERE/Clients/Bayanat/Clipped"
xy_tolerance = ""


##The source code of the tool.
##
try:
    print("WaliedCheetos: Hollla ...!!!")

    # Use the ListFeatureClasses function to return a list of 
    #  all shapefiles.
    #
    fcList = arcpy.ListFeatureClasses()

    for fc in fcList:
        print('To Clip ... ' + fc.rstrip(".shp"))

        # Execute Clip
        arcpy.Clip_analysis(fc, clip_features, (out_feature_class + os.sep + fc.rstrip(".shp")) , xy_tolerance)

        print('Clipped ... ' + fc.rstrip(".shp"))
except Exception as e:
    #log exception
    #
    print("A Python error occured", "ERROR")
    msgs = traceback.format_exception(*sys.exc_info())
    for msg in msgs:
        print(msg.strip(), "ERROR")
    
finally:
    print("WaliedCheetos: Done ...!!!")


