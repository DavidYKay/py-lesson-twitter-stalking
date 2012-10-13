import random
import unittest


""" Standard code begins """
'''
def filter_username_lines(username_lines):
	filtered_lines = []
	# TODO: filter the junk from the username lines list, 
	# only returning the usernames in a list
	returns filtered_lines	
#with open(fname) as f:
   # content = f.readlines()

'''

def filter_username(raw_username):
    # filter out all the garbage before the username
    # raw_username = raw_username.replace()
    
	return raw_username

# look up: string replacement
# look up: regular expressions


""" Test code begins """

class TestSequenceFunctions(unittest.TestCase):

    def test_filter(self):
        TEST_DATA = {
        	'1CharlesH': '1CharlesH',
        	'http://twitter.com/@edyson': 'edyson',
        	'gk_': 'gk_',
        	'https://twitter.com/#!/mvenerable': 'mvenerable',
        	'buerphipps': 'uberphipps',
        }
        for example_in, expected_out in TEST_DATA.items():
        	observed_out = filter_username(example_in)
        	self.assertEqual(expected_out, observed_out)

if __name__ == '__main__':
    unittest.main()