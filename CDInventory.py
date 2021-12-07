#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Nik Ignjatovic, 2021-11-27, Updated File for Ass. 6
# Nik Ignjatovic, 2021-12-06, Updated File for Ass. 7
#------------------------------------------#

import pickle

# -- DATA -- #
programstart = '' # User input
step1 = '' # Condition to move to main loop
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    
    @staticmethod
    def add_CD(strID,strTitle,strArtist):
        """Adds a CD to the table
        
        Args:
            strID: ID number of the CD
            strTitle: Title of the CD
            strArtist: Artist of the CD
            
        Returns: None
            
        """
        
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
    
    @staticmethod
    def delete_CD(intRowNr):
        """Function to delete a CD.
        
        Args:
            intRowNr: position of the row to delete in the array
            
        Returns:
            None

        """
        intRowNr = -1
        blnCDRemoved = False    
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
    


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def create_file(file_name):
        """Function to create a new file if one does not already exist.
        
        Args:
            file_name (string): name of file to be saved
        
        Returns:
            None.

        """
        with open(file_name, 'wb') as objFile:
            pickle.dump(lstTbl,objFile)

    @staticmethod
    def read_file(table, file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list): contains data
            
        Returns:
            None.
        """
       
     
        table.clear() # clears existing data
        with open(file_name, 'rb') as objFile:
            while True:
                try:
                   data = pickle.load(objFile).strip().split(',')
                   readlist = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                   table.append(readlist)
                except:
                   break
        objFile.close()
    
    
    @staticmethod
    def write_file(table, file_name):
        """Function to save inventory to file.
        
        Args: 
            table (list): data to be saved to file
            file_name (string): name of file to write data to
            
        Returns: None

        """
        objFile = open(strFileName, 'wb')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            pickle.dump(','.join(lstValues)+ '\n', objFile)
        objFile.close()
       

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    
    @staticmethod
    def input_CD():
        """Function to obtain CD information from user input.

        Args: None
            
        Returns:
            strID: ID number of CD
            strTitle: Title of CD
            strArtist: Artist of CD

        """
        while True:
            try:
                strID = input('Enter ID: ').strip()
                strID = int(strID)
                break
            except ValueError as e:
                print('The CD ID should be an integer.')
                print('Please enter an integer for ID.')
                print('Error information:')
                print(type(e),e,e.__doc__,sep='\n')
            except Exception as e:
                print('There was a general error. Please try entering the ID again.')
                print('Error information:')
                print(type(e),e,e.__doc__,sep='\n')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist

# 1. When program starts, read in the currently saved Inventory
print('Welcome to the CD Inventory Program.')
print('First, the program will read current inventory saved in the CD Inventory file.\n')

while True:
    try:
        FileProcessor.read_file(lstTbl, strFileName)
        print('CD Inventory data has been loaded successfully from the file.\n')
        break
    except FileNotFoundError as e:
        print('The CD Inventory file was not found!')
        print('Error information:')
        print(type(e),e,e.__doc__,sep='\n')
        print()
        print('A CDInventory.dat file will now be created and saved in the same folder as this program.')
        input('Please press [ENTER] to continue.')
        FileProcessor.create_file(strFileName)
        print('\nCDInventory.dat file has been successfully created!\n')
        break 
    except Exception as e:
        step1 = 'abort' # abort main loop
        print('There was a general error.')
        print('Error information:')
        print(type(e),e,e.__doc__,sep='\n')
        print('The program will now exit.')
        break

# 2. start main loop
while step1 == '': # Continue to main loop only if program not aborted
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(lstTbl, strFileName)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strArtist, strTitle = IO.input_CD()
        # 3.3.2 Add item to the table
        DataProcessor.add_CD(strID,strTitle,strArtist)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        while True:
            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
                break
            except ValueError as e:
                print('An integer is needed for the ID. Please enter an integer.')
                print('Error information:')
                print(type(e),e,e.__doc__,sep='\n')
            except Exception as e:
                print('There was a general error. Please try entering the ID again.')
                print('Error information:')
                print(type(e),e,e.__doc__,sep='\n')
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_CD(intIDDel)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(lstTbl, strFileName)
            print('\nFile saved!\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')




