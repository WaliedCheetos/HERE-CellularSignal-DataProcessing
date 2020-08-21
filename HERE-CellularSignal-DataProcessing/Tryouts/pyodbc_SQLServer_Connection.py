import sys
import traceback
import pyodbc

try:
    ## 2- loop cellular segment (by link id) career information in order to know all the carrier informatio (i.e. signal strength, percentage of the segment, ...)
    DB_Connection = pyodbc.connect('Driver={SQL Server};Server=4AELAHMADMOH;Database=HERE_DB;Trusted_Connection=yes;')
    # Create cursor associated with connection
    DB_Connection_Cursor = DB_Connection.cursor()

    # Call SP and trap execute error, if raised

    DB_Connection_Cursor.execute('{call _spt_GetCellularSegmentInfoByLinkId (?)}', str(395925162))                
                
    # Fetch row generated by execute
    Cursor_Rows=DB_Connection_Cursor.fetchall()
    if len(Cursor_Rows) != 0:
        for Row in Cursor_Rows:
            print(Row)
            CurrentRow_Percentage_Value = Row[7]

except pyodbc.Error, err:
    print 'Error !!!!! %s' % err

finally:
    # Close and delete cursor
    DB_Connection_Cursor.close()
    del DB_Connection_Cursor
                
    # Close Connection
    DB_Connection.close()

