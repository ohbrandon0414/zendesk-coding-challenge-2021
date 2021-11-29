from http.client import error
import unittest

from viewer import viewer
import json

class TestSum(unittest.TestCase):

    def test_fetch_all_ticekts_with_invalid_url_no_https(self):
        url = 'not a url'
        test_viewer = viewer(url, "", "", 25)
        tickets, error_msg = test_viewer.fetch_data(url)
        expected_msg = "Failed to get the request: Check the URL and authentication."
        self.assertEqual(error_msg, expected_msg)
    
    def test_fetch_all_ticekts_with_invalid_url_with_https(self):
        url = 'https://thisurldoesnotexist'
        test_viewer = viewer(url, "", "", 25)
        tickets, error_msg = test_viewer.fetch_data(url)
        expected_msg = "Failed to get the request: Check the URL and authentication."
        self.assertEqual(error_msg, expected_msg)

    def test_fetch_all_ticekts_with_valid_url_invalid_auth(self):
        url = 'https://zendesk.com'
        test_viewer = viewer(url, "", "", 25)
        tickets, error_msg = test_viewer.fetch_data(url)
        expected_msg = "Did not recieve the proper json format."
        self.assertEqual(error_msg, expected_msg)

    
    def test_get_ticket_url(self):
        test_viewer = viewer("temp_account", "", "", 25)
        actual = test_viewer.get_ticket_url(3)
        expected = "https://temp_account.zendesk.com/api/v2/tickets/3.json" 
        self.assertEqual(actual, expected)

    
if __name__ == '__main__':
    unittest.main()