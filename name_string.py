import random
import unittest


""" Standard code begins """


def create_string_from_usernames(names):
    # change a list of names into a single string of names
    # fname = "stalking.csv"
    # myList = [line.strip() for line in open(fname)]
    return ",".join(names)


""" Test code begins """

class TestSequenceFunctions(unittest.TestCase):

    def test_filter(self):
        TEST_DATA = [
		"rsarver",
		"episod",
		"jasoncosta",
		"theseancook",
		"kurrik",
		"froginthevalley",
        ]

        EXPECTED_OUT = 'rsarver,episod,jasoncosta,theseancook,kurrik,froginthevalley'

	observed_out = create_string_from_usernames(TEST_DATA)
	self.assertEqual(EXPECTED_OUT, observed_out)

if __name__ == '__main__':
    unittest.main()
