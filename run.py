from viewer import viewer


# provide the basic info:
# account name is the subdomain that starts with zcc
accountname = ''
# the email and password that authenticates the zendesk API
email = ''
password = ''
# the page size the user would like to view in
page_size = 50

myViewer = viewer(accountname, email, password, page_size)
myViewer.run_main_viewer()
