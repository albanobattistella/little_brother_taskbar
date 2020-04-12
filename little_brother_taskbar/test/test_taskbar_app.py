# -*- coding: utf-8 -*-

#    Copyright (C) 2019  Marcus Rickert
#
#    See https://github.com/marcus67/python_base_app
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest
import os.path

from python_base_app.test import base_test
from little_brother_taskbar import taskbar_app

SECTION_NAME = "MySection"
INT_VALUE = 123
NEW_INT_VALUE = 456
STRING_VALUE = "Hello"
BOOLEAN_VALUE = True

class TestTaskbarApp(base_test.BaseTestCase):

    def test_config_model(self):

        a_config = taskbar_app.TaskBarAppConfigModel()


if __name__ == '__main__':
    unittest.main()
