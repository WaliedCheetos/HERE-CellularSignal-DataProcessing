##import xml.dom.minidom
import xml.etree.ElementTree as XML_ElementTree
import logging

class config:
    message_Welcome = 'WaliedCheetos says Holllla'
    message_Processing = 'WaliedCheetos tells U I am still processing, U better wait ey!' 
    message_Error = 'WaliedCheetos tells U I am a little buggy :(' 
    message_Exception = 'WaliedCheetos tells U, exceptions are for real men :(' 
    message_Finished = 'WaliedCheetos tells U, U re the king of all times ;)'
    
    flag_EnableFileLog = False

    filePath_LogFile = 'WaliedCheetos.log'
    filePath_HEREPlacesXML = 'C:\\Users\\ahmadmoh\\O_o\\HERE\\Data\\Places XML MEA S201_E1 S201\\MEA_201E1\\ARE\\ARE_004.xml\\ARE_004.xml'



def createCustomLogger():
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    ##c_handler.setLevel(logging.WARNING)
    c_handler.setLevel(logging.INFO)    
    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    # Add handlers to the logger
    logger.addHandler(c_handler)

    if config.flag_EnableFileLog:
        f_handler = logging.FileHandler(config.filePath_LogFile)    
        ##f_handler.setLevel(logging.ERROR)
        f_handler.setLevel(logging.INFO)
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)

def main():
    try:
        createCustomLogger()

        logging.info(config.message_Welcome)

        for event, elem in XML_ElementTree.iterparse(config.filePath_HEREPlacesXML):
            pass
            ##... do something ...


        ## use the parse() function to load and parse an XML file
        #doc = xml.dom.minidom.parse(config.filePath_HEREPlacesXML)

        ## get a list of XML tags from the document and print each one
        #placeNodes = doc.getElementsByTagName("Place")
        #for placeNode in placesNodes:
        #    pass
        
        
        
        ###load the HERE Places XML file where the data exists
        #tree = XML_ElementTree.parse(config.filePath_HEREPlacesXML)
        #root = tree.getroot()

        ## all items data
        #logging.info('Expertise Data:')

        #for elem in root:
        #   for subelem in elem:
        #      print(subelem.text)

        


    except Exception as e:
        ##logging.error("Exception occurred", exc_info=True)
        logging.exception(config.message_Exception)


if __name__ == "__main__":
    main();

