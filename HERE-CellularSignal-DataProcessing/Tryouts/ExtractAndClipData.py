import arcpy

##The source code of the tool.
##
try:
    print("WaliedCheetos: Hollla ...!!!")

    arcpy.defense

except Exception as e:
    #log exception
    #
    print("A Python error occured", "ERROR")
    msgs = traceback.format_exception(*sys.exc_info())
    for msg in msgs:
        print(msg.strip(), "ERROR")
    
finally:
    print("WaliedCheetos: Done ...!!!")