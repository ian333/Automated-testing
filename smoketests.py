from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests_2 import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'smoke-report',
    "report_name":'Smoke_Test'
}
runner = HTMLTestRunner(**kwargs).run(smoke_test)

