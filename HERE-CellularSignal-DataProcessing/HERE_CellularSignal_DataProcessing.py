
# Import the required modules
#
import arcpy
import sys
import traceback
import pyodbc


## before running this script make sure you have create spearte featureclasses from each carrier 
##i.e. 
##a- featureclass for Cellular Signal Information for Vodafone in country X
##b- featureclass for Cellular Signal Information for Orange in country X
## then run the script on each carrier featureclass to maintain separate layer for presentation rather than cartographic repsentation in ArcMap


##arcpy.env.workspace = "C:/WaliedCheetos/Cheetos.gdb"

in_CarrierCellularSignal_FC_Name = 'C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Cellular Signals\\From Zimka\\ORD_FGDB\\ORD_CELL_SIGNAL.gdb\\CELLULAR_GEOMETRY' ##arcpy.GetParameterAsText(0)
in_CarrierCellularSignal_Field_LinkID = 'TOPOLOGY_SEGMENT_ID' ##arcpy.GetParameterAsText(1)
## example:
# TOPOLOGY_SEGMENT_ID

in_DB_ConnectionString = 'Driver={SQL Server};Server=4AELAHMADMOH;Database=HERE_DB;Trusted_Connection=yes;' ##arcpy.GetParameterAsText(2)
## example: 
# DRIVER={ODBC Driver 17 for SQL Server};SERVER=4AELAHMADMOH\MSSQLSERVER;DATABASE=HERE_DB;Trusted_Connection=yes;
# DRIVER={ODBC Driver 17 for SQL Server};SERVER=4AELAHMADMOH\MSSQLSERVER;DATABASE=HERE_DB;UID=WaliedCheetos;PWD=P@ssw0rd;

in_CarrierCellularSignal_Field_Percentage = 'PERCENT_TOPOLOGY_SEGMENT_END' ##arcpy.GetParameterAsText(3)
## example:
# PERCENT_TOPOLOGY_SEGMENT_END

in_CarrierCellularSignal_FC_PointsAlongLinesName = 'C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Cellular Signals\\From Zimka\\ORD_FGDB\\ORD_CELL_SIGNAL.gdb\\WCheetos_Ouput01' ##arcpy.GetParameterAsText(4)

#in_CarrierCellularSignal_FC_SplitLinesName = arcpy.GetParameterAsText(3)




try:
    ##arcpy.CreateSpatialReference_management()
    #--------------------------
    # Your code goes here
    #
    ## 1- loop cellular segment geometry featureclass features, and add point feature at the mentioned percentatge and do not foregt to append all the attributes from the parent feature (Cellular Signal Linear Feature)
    #
    # 
    ##fields_cur = [i.name for i in arcpy.ListFields(in_CarrierCellularSignal_FC_Name, 'Layer*')]
    with arcpy.da.SearchCursor(in_CarrierCellularSignal_FC_Name, '*') as cursor:
        for row in cursor:
            ##print(row)
            CurrentRow_LinkID_Value = row[2]
            print("Current Link ID: " + str(CurrentRow_LinkID_Value))
            
            ## 2- loop cellular segment (by link id) career information in order to know all the carrier informatio (i.e. signal strength, percentage of the segment, ...)
            DB_Connection = pyodbc.connect(in_DB_ConnectionString)
            # Create cursor associated with connection
            DB_Connection_Cursor = DB_Connection.cursor()

             # Call SP and trap execute error, if raised
            try:
                DB_Connection_Cursor.execute('{call _spt_GetCellularSegmentInfoByLinkId (?)}', str(CurrentRow_LinkID_Value))                
                
                # Fetch row generated by execute
                Cursor_Rows=DB_Connection_Cursor.fetchall()
                if len(Cursor_Rows) != 0:
                    for Row in Cursor_Rows:
                        CurrentRow_Percentage_Value = Row[7]
                        print("Current PERCENT_TOPOLOGY_SEGMENT_END: " + str(CurrentRow_Percentage_Value))
                        ## 2a- create points along each line by the percentage information
                        arcpy.GeneratePointsAlongLines_management(
                            in_CarrierCellularSignal_FC_Name, 
                            in_CarrierCellularSignal_FC_PointsAlongLinesName, 
                            'PERCENTAGE',
                            CurrentRow_Percentage_Value)

            except pyodbc.Error, err:
                print 'Error !!!!! %s' % err
            
            except arcpy.ExecuteError: 
                # Get the tool error messages 
                msgs = arcpy.GetMessages(2) 

                # Return tool error messages for use with a script tool 
                arcpy.AddError(msgs) 

                # Print tool error messages for use in Python/PythonWin 
                print(msgs)

            except:
                # Get the traceback object
                tb = sys.exc_info()[2]
                tbinfo = traceback.format_tb(tb)[0]

                # Concatenate information together concerning the error into a message string
                pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
                msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

                # Return python error messages for use in script tool or Python window
                arcpy.AddError(pymsg)
                arcpy.AddError(msgs)

                # Print Python error messages for use in Python / Python window
                print(pymsg)
                print(msgs)

            finally:
                # Close and delete cursor
                DB_Connection_Cursor.close()
                del DB_Connection_Cursor
                
                # Close Connection
                DB_Connection.close()


            ### 2a- create points along each line by the percentage information
            #arcpy.GeneratePointsAlongLines_management(in_CarrierCellularSignal_FC_Name, in_CarrierCellularSignal_FC_PointsAlongLinesName, 'PERCENTAGE', Percentage=row[in_CarrierCellularSignal_FC_Percentage_FieldName])
            ### 2b- split each line at each point and make sure the attributes remain the same with the corresponding signal strenght value.
            #arcpy.SplitLineAtPoint_management();

except arcpy.ExecuteError: 
    # Get the tool error messages 
    msgs = arcpy.GetMessages(2) 

    # Return tool error messages for use with a script tool 
    arcpy.AddError(msgs) 

    # Print tool error messages for use in Python/PythonWin 
    print(msgs)

except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return python error messages for use in script tool or Python window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python window
    print(pymsg)
    print(msgs)


