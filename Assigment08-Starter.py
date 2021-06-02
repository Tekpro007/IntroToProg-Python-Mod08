# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

#GitHub URL: https://github.com/Tekpro007/IntroToProg-Python-Mod08.git
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kyle Gilpin, 5.31.2021, Created IO functions
# Kyle Gilpin, 5.31.2021, Created file processor functions
# Kyle Gilpin, 5.31.2021, Created Class production functions
# Kyle Gilpin, 6.1.2021, Finished creating presenation portion of script
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strUserMenuInput = ''
strProduct = ''
fltPrice = ''

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        """
        Defines how the class prints the string
        """
        return 'Product = ' + str(self.__product_name) + ', $' + str(self.__product_price)

    @property
    def product_price(self):
        """
        Returns the product price
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        """
        Sets the product price
        :param name: (string) name of the product price
        """
        try:
            float(value)
            self.__product_price = value
        except ValueError:
            raise Exception("Price Must be a number")

    @property
    def product_name(self):
        """
        Returns the product name
        """
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        """
        Sets the product name
        :param name: (string) name of the product
        """
        if not str(name).isnumeric():
            self.__product_name = name
        else:
            raise Exception("Names can not be numbers")


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def read_file_data(file_name, list_of_rows):
        """ Reads data from a file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        """
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    product, price = line.split(",")
                    row = Product(product.strip(), price.strip())
                    list_of_rows.append(row)
                return file.read()
        except FileNotFoundError as e:
            print('File not found!')


    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves data to the file
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        """
        file = open(file_name, "a")
        for row in list_of_rows:
            file.write(row.product_name + "," + str(row.product_price) + '\n')
        file.close()
        print("Saved Data.")
        return list_of_rows, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('Menu of Options')
        print('1) Show current data in list of products: ')
        print('2) Add data to list of products: ')
        print('3) Save current data to a file and exit): ')
        print()

    @staticmethod
    def input_menu():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_product_and_price():
        """ Inputs data from users
        :param product: (string) with name of product:
        :param price: (string) price of the product:
        :return: product & price
        """
        product = str(input('Enter a product: '))
        price = str(float(input('Enter a Price: ')))

        return product, price

    @staticmethod
    def show_current_data(list_of_rows):
        """ Shows the current data in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("The Current Data is:")
        for row in list_of_rows:
            print(row)
        print('\n')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
FileProcessor.read_file_data(strFileName, lstOfProductObjects)

# Get user's menu option choice
while (True):
    IO.print_menu()
    strUserMenuInput = IO.input_menu()

    # Show user current data in the list of product objects
    if strUserMenuInput.strip() == '1':
        IO.show_current_data(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif strUserMenuInput.strip() == '2':
        product, price = IO.input_product_and_price()
        objProduct = Product(product, price)
        lstOfProductObjects.append(objProduct)

    # let user save current data to file and exit program
    elif strUserMenuInput.strip() == '3':
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        print('Programing closing')
        break




# Main Body of Script  ---------------------------------------------------- #

