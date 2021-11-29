from datetime import datetime 

# the color class that could change the display of the letters in the terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_first_page():
    """
    Prints warning message when user is trying to 
    go to the previous page when on the first page
    """ 
    print(bcolors.WARNING + "\nYou are on the first page" + bcolors.ENDC)

def print_last_page():
    """
    Prints warning message when user is trying to 
    go to the next page when on the last page
    """ 
    print(bcolors.WARNING + "\nYou are on the last page" + bcolors.ENDC)

def print_invalid_ticket_id():
    """
    Prints error message when user entered an invalid ticket number(id)
    """ 
    print(bcolors.FAIL + "\nYou did not enter a valid ticket number" + bcolors.ENDC)

def print_invalid_option():
    """
    Prints warning message when user entered an invalid input for in the main menu
    """ 
    print(bcolors.FAIL + "\nYou did not enter a valid option" + bcolors.ENDC)

def print_main_menu():
    """
    Prints the main menu 
    """ 
    print(bcolors.OKBLUE +"\n\t Select an option")
    print("\t* 1: view all tickets")
    print("\t* 2: view a ticket")
    print("\t* q: exit the program\n" + bcolors.ENDC)

def print_tickets_menu(current_page):
    """
    Prints the menu when user is viewing all the tickets
    """ 
    print(bcolors.OKBLUE + "\n\t Select an option")
    print("\t* n: next page")
    print("\t* p: previous page")
    print("\t* m: starting menu")
    print("\t* q: exit program\n" + bcolors.ENDC)

def print_individual_ticket_menu():
    """
    Prints the menu when user is viewing all the tickets
    """ 
    print(bcolors.OKBLUE + "\n\t Select an option")
    print("\t* {#}: enter valid ticket ID")
    print("\t* m: starting menu")
    print("\t* q: exit program\n" + bcolors.ENDC)

def print_ticket(data):
    """
    Prints the details for a ticket

    :param data: the data of the ticket details in a json format
    """ 
    # convert the string format into a datetime object to extract the information to display
    # if fails, just keep the original
    try:
        date = datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%S%z")
        # convert the datetime object back into a string that looks more user friendly
        date_time_str = date.strftime("%d %b %Y %I:%M%p")
    except:
        date_time_str = data['updated_at']
    print(bcolors.OKGREEN +"\nSUBJECT: \n"+ bcolors.ENDC + data['subject'])
    print(bcolors.OKGREEN + "REQUESTER: \n" + bcolors.ENDC + str(data['requester_id']))
    print(bcolors.OKGREEN + "UPDATED AT: \n" + bcolors.ENDC + date_time_str)
    print(bcolors.OKGREEN + "DESCRIPTION:\n" + bcolors.ENDC + data['description'])


def print_page(page):   
    """
    Prints all the tickets in a pagination format
    
    :param pages: a dictionary where the key is the page number and the vlaues are the data
    :param input_page: the page number the user is viewing
    """ 
    if not page:
        return
    print(bcolors.OKGREEN+"\n  |{:^6}|{:^55}|{:^20}|{:^30}|".format("ID", "SUBJECT", "OPENED BY", "UPDATED"))
    print('-'*125)
    for t in page:
        # convert the string format into a datetime object to extract the information to display if fails, just keep it
        try:
            date = datetime.strptime(t['updated_at'], "%Y-%m-%dT%H:%M:%S%z")
            # convert the datetime object back into a string that looks more user friendly
            date_time_str = date.strftime("%d %b %Y %I:%M%p")
        except:
            date_time_str = t['updated_at']
        print("  |{:^6}|{:^55}|{:^20}|{:^30}|".format(str(t['id']), t['subject'], t['requester_id'], date_time_str))

def print_api_error(error):
    if not error:
        # the returned json result does not contain an error object
        print(bcolors.FAIL + "\nWe were unable to connect the to the API please make check the connection" + bcolors.ENDC)
    else:
        # display the customized error message along with the returned error reason
        print(bcolors.FAIL + "\nWe were unable to connect the to the API. " + error + bcolors.ENDC)

def print_large_page_size():
    print(bcolors.FAIL + "\n The provided page size is too big" + bcolors.ENDC)
    
