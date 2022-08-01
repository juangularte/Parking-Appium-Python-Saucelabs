# 1. Import the files
import unittest
from tests.android.native.test_android_native import TestAndroidNative
# from tests.ios.native.test_ios_native import TestIOSNative


# 2. Create the object of the class using unitTest
android_native = unittest.TestLoader().loadTestsFromModule(TestAndroidNative())
# ios_native = unittest.TestLoader().loadTestsFromTestCase(TestIOSNative)


# 3. Create TestSuite
regressionTests = unittest.TestSuite([android_native])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTests)

# Note : All the methods in test files should define in proper run order
