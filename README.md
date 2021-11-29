# Zendesk Ticket Viewer 

## Overview
Zendesk Ticket Viewer is a ticket viewer and is CLI based program 

## Installation

Use this github to download the code and run it on your preferred choice of terminal.


## Requirements/Dependencies
* Python: version higher than 3.90
* [Requests](https://docs.python-requests.org/en/latest/): Python HTTP library that was used to make API calls .
* Users information should be added in run.py to make the program run properly (subdomain, username, password, page size)

## Usage/Features

After making sure that user's information is put into run.py, there are two features in the program:

1. **The first feature is to view tickets and navigate them through pages**

If you select 1 in the main menu to view all the tickets, you start with the first page of the tickets. If the given size of the page is bigger than the number of tickets, there would be no extra pages. The first page would look like: 

![image](https://user-images.githubusercontent.com/55033266/143853453-d13f7372-cec4-4391-ad8c-11ca1666f52b.png)

If you press n to move to the next page you could get something like:

<img width="449" alt="image" src="https://user-images.githubusercontent.com/55033266/143853030-2aebb6d4-7f9a-458d-8eb6-335e01c055d0.png">

Similar to navigating to the next page, you could also navigate to the previous page.

2. **The second feature is to search a ticket number(ID) to view its detailed infromation**

In the main menu, if you select the second option you should be able to enter a ticket number. If the entered input is valid you should see something like: 

![image](https://user-images.githubusercontent.com/55033266/143853849-0b68e480-c4b4-423c-87ad-e149dd4b6e28.png)



## License
[MIT](https://choosealicense.com/licenses/mit/)
