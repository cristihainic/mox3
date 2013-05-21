# Unit tests for stubout.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This is a fork of the pymox library intended to work with Python 3.
# The file was modified by quermit@gmail.com and dawid.fatyga@gmail.com

import unittest

from mox3 import mox
from mox3 import stubout
from . import stubout_helper


class StubOutForTestingTest(unittest.TestCase):
    def setUp(self):
        self.mox = mox.Mox()
        self.sample_function_backup = stubout_helper.SampleFunction

    def tearDown(self):
        stubout_helper.SampleFunction = self.sample_function_backup

    def testSmartSetOnModule(self):
        mock_function = self.mox.CreateMockAnything()
        mock_function()

        stubber = stubout.StubOutForTesting()
        stubber.SmartSet(stubout_helper, 'SampleFunction', mock_function)

        self.mox.ReplayAll()

        stubout_helper.SampleFunction()

        self.mox.VerifyAll()


if __name__ == '__main__':
    unittest.main()
