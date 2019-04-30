import unittest
import coverage
from tests import pep8_converter_tests
from tests import class_finder_tests
from tests import interpreter_controller_tests


cov = coverage.Coverage()
cov.start()
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(pep8_converter_tests))
suite.addTests(loader.loadTestsFromModule(class_finder_tests))
suite.addTests(loader.loadTestsFromModule(interpreter_controller_tests))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
cov.stop()
cov.save()
cov.html_report()
