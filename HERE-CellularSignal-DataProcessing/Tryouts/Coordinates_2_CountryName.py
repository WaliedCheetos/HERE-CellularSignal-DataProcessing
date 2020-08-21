import geopy;
import xlrd;


def do_ReverseGeocoding(xylocation):
    try:
        geopy.geocoders.options.default_timeout = None;
        geolocator = geopy.geocoders.Nominatim();
        return geolocator.reverse(xylocation, timeout=None);
        #print (location.raw['address']['country_code']);
        #return geopy.geocode(location)
    except geopy.exc.GeocoderTimedOut:
        return do_ReverseGeocoding(xylocation);


##fname = join(dirname(dirname(abspath(__file__))), 'test_data', 'Cad Data Mar 2014.xlsx')

# Open the workbook
xl_workbook = xlrd.open_workbook("C:\\Users\\ahmadmoh\\O_o\\HERE\\Clients\\Careem\\June21-July3.xlsx");


#  (sheets are zero-indexed)
#
xl_sheet = xl_workbook.sheet_by_index(0);


## Print all values, iterating through rows and columns
##
#num_cols = xl_sheet.ncols   # Number of columns
#for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
#    print ('-'*40)
#    print ('Row: %s' % row_idx)   # Print row number
#    for col_idx in range(0, num_cols):  # Iterate through columns
#        cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
#        print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

##geolocator = geopy.geocoders.Nominatim();


for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
    ##print (xl_sheet.cell(row_idx, 1))  # Get cell object by row, col
    ##print (xl_sheet.cell(row_idx, 2))  # Get cell object by row, col
    
    ##location = geolocator.reverse((str(xl_sheet.cell(row_idx, 1).value) + "," + str(xl_sheet.cell(row_idx, 2).value)), timeout=None);
    location = do_ReverseGeocoding((str(xl_sheet.cell(row_idx, 1).value) + "," + str(xl_sheet.cell(row_idx, 2).value)));

    try:
        print (location.raw['address']['country_code']);
    except Exception as e:
        print(e);

    #print ('-'*40)
    #print ('Row: %s' % row_idx)   # Print row number
    #for col_idx in range(0, num_cols):  # Iterate through columns
    #    cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
    #    print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))

print ('done');






