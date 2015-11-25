# -*- coding: utf-8 -*-
import unittest
import sys, os


if __name__ == '__main__':
    dir_list = os.listdir('.')
    test_modules = []

    # Discover tests
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                package = root[2:].replace('/', '.')
                module_id = file[:-3]
                module_fqn = module_id\
                    if package == ''\
                    else '%s.%s' % (package, module_id)

                test_modules.append(module_fqn)

    # Import modules
    map(__import__, test_modules)

    suite = unittest.TestSuite()
    modules = [sys.modules[m] for m in test_modules]
    for m in modules:
        test = unittest.TestLoader().loadTestsFromModule(m)
        suite.addTest(test)
    unittest.TextTestRunner(verbosity=2).run(suite)