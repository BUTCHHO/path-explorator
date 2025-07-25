from unittest import TextTestRunner, TestLoader

test_dir = '/home/butcho/python projects/path-explorator-main/tests'

test_loader = TestLoader()
tests = test_loader.discover(test_dir, 'test_*.py')
test_runner = TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_runner.run(tests)