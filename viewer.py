import requests
from requests.auth import HTTPBasicAuth
from http.client import HTTPSConnection
from format import *
# from base64 import b64encode

class viewer():
    """This is a viewer class to create a ticket viewer.

    Attributes:
        url (str): The url the user provides to get the tickets
        auth (HTTPBasicAuth): The authentication to connect to the api
    """
    base_url: str
    auth: HTTPBasicAuth

    def __init__(self, accountname, email, password, page_size):
        # create the base url to get the tickets using the account name and the size of each page

        # the pagination size limit according to the documents provided
        page_size_limit = 100
        if page_size > page_size_limit:
            # exit the program if the page_size is out of the limit
            print_large_page_size()
            exit()
        self.base_url = "https://" + accountname + ".zendesk.com/api/v2/tickets.json?page[size]=" + str(page_size)
        self.auth = HTTPBasicAuth(username=email, password=password)

    def fetch_data(self, url):
        """
        Fetches data from the url

        Parameters:
            url (str): A url to fetch the data from

        Returns:
            error_msg (str): The error message thrown if the request failed
            data (json): json object which is the result of the request

        """ 
        # try to get the request using the base url
        try:
            r = requests.get(url, auth = self.auth)
        except:
            # throw an error message to return
            error_msg = "Failed to get the request: Check the URL and authentication."
            return None, error_msg
        
        # try converting the returned result in to a json format
        try:
            data = r.json()
        except:
            # throw an error message to return
            error_msg = "Did not recieve the proper json format."
            return None, error_msg
        
        # the result got back but still failed
        if "error" in data:
            return None, data['error']

        return data, None

    def get_ticket_url(self, id):
        """
        Properly formats the ticket url the user wants to look up

        Parameters:
            id (int): The ID of the ticket user is trying to look up

        Returns:
            ticket_url (str): The formatted url to get the data of the ticket
        """ 
        # split the base url by /
        arr = self.base_url.split('/')

        # cerate the url of the ticket by reconstructing without the last part 
        ticket_url = '/'.join(arr[:-1])

        # properly format the id of the ticket to the url
        ticket_url += "/tickets/" + str(id) + ".json"
        return ticket_url
            
    
    def run_ticket_page_viewer(self, page):
        """
        Creates the viewer that has pagination to view tickets

        Parameters:
            page (json): The json object that contains data of the first page
        
        """ 
        # user starts on the first page
        print_page(page['tickets'])
        prev_curso_of_first_page = page['meta']['before_cursor']
        while True:
            links = page['links']
            print_tickets_menu(1)
            
            page_input = input("Enter your option: ")

            if page_input == 'q':
                # user would like to quit
                exit()
            elif page_input == 'm':
                # user would like to go to the main menu
                return
            elif page_input == 'n':
                # user would like to go to the next page
                if 'next' not in links or not links['next'] or not page['meta']['has_more']:
                    # already on the last page
                    print_last_page()
                    continue
                page, error_msg = self.fetch_data(links['next'])
                 # get the next page and error message while fetching the API
                if error_msg:
                    # there was an error while getting the data from the API
                    print_api_error(error_msg)
                    continue
                # print the next page
                print_page(page['tickets'])
            elif page_input == 'p':
                prev_cursor = page['meta']['before_cursor']
                # user would like to go to the previous page
                if 'prev' not in links or not links['prev'] or prev_curso_of_first_page == prev_cursor:
                    # already on the first page
                    print_first_page()
                    continue
                # get the previous page and error message while fetching the API
                page, error_msg = self.fetch_data(links['prev'])
                if error_msg:
                    # there was an error while getting the data from the API
                    print_api_error(error_msg)
                    continue
                # print the previous page
                print_page(page['tickets'])
            else:
                # invalid input
                print_invalid_option()

    def run_individual_ticket_viewer(self):
        """
        Creates the viewer that contains the detailed information of a valid ticket
        """ 
        while True:
            # print the menu that gives the users the options
            print_individual_ticket_menu()
            ticket_input = input("Enter your option: ")
            if ticket_input == 'q':
                # user wants to quit the program
                exit()
            elif ticket_input == 'm':
                # user wants to navigate to the main menu
                return
            else:
                # try converting the input into a integer
                try:
                    ticket_id = int(ticket_input)
                except:
                    print_invalid_ticket_id()
                    continue
                
                # create a url using the ticketid
                ticket_url = self.get_ticket_url(ticket_id)

                # fetch the data that was requested using the ticket url
                ticket_data, error_msg = self.fetch_data(ticket_url)

                if error_msg:
                    # error message was thrown so print out the error message
                    print_api_error(error_msg)
                else:
                    # no errors: print out the ticket detail
                    print_ticket(ticket_data['ticket'])

    def run_main_viewer(self):
        """
        Creates the viewer of that combines the pages and individual tickets
        """ 

        # try fetching the base url user has provided
        tickets, error_msg = self.fetch_data(self.base_url)

        
        while not tickets:
            # the fetch failed: ask if user would like to refresh
            print_api_error(error_msg)
            answer = input("Press q to exit and any other key to refresh")
            if answer == 'q':
                exit()

        while True:
            print_main_menu()
            word = input("Enter your option: ")
            if word == 'q':
                # user wants to exit the program
                break
            elif word == '1':
                # run the ticket pages
                self.run_ticket_page_viewer(tickets)
            elif word == '2':
                # run the ticket search
                self.run_individual_ticket_viewer()
            else:
                # invalid input
                print_invalid_option()
