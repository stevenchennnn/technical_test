# -*- coding: UTF-8 -*-
import getopt
import sys
import pytest

from logger.logger import initial_logger


def execute_testcase():
    """
    1. Check arg from cli (get specific test case)
    2. Execute pytest command


    """

    options, arguments = getopt.getopt(sys.argv[1:], "hc:", ["help", "case_name="])

    if options:
        # Parse argument from cli
        for option, argument in options:
            # Need help!!!
            if option in ("-h", "--help"):
                print('How to use : python3 execute_test.py --case_name XXXXXXX')
                sys.exit()
            # Run specific case
            elif option in ("-c", "--case_name"):
                # Bind testcase path
                case_name = ('./test/test_%s.py' % argument)
                # Remove old report
                pytest.main(["-s", "-v", case_name])

    else:
        # Run all test case
        pytest.main(["-s", "-v"])


if __name__ == '__main__':
    """
    Technical Test Framework v0.0.1
    
    """
    initial_logger()
    execute_testcase()
    sys.exit()
