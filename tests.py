import unittest
import random
import time
from credit_card_validator import credit_card_validator as ccv


class TestCreditCardValidator(unittest.TestCase):

    def test1(self):
        stop_time = time.time() + 20

        while time.time() <= stop_time:  # runs for nearly 20 seconds
            path = random.randint(0, 4)
            randomNum = str(random.randint(0, 10000000000000000))

            if (path == 0):  # Prefix 4
                randomNum = '4' + randomNum[1:]
                ccv(randomNum)

            if (path == 1):  # Prefixes 51 - 55
                temp = str(random.randint(51, 55))
                randomNum = temp + randomNum[2:]
                ccv(randomNum)

            if (path == 2):  # Prefixes 2221 - 2720
                temp = str(random.randint(2221, 2720))
                randomNum = temp + randomNum[4:]
                ccv(randomNum)

            if (path == 3):  # Prefixes 34 - 37
                temp = str(random.randint(34, 37))
                randomNum = temp + randomNum[2:]
                ccv(randomNum)

            if (path == 4):  # Random
                ccv(randomNum)


if __name__ == '__main__':
    unittest.main()
