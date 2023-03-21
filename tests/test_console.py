#!/usr/bin/python3
import unittest
import console
from console import HBNBCommand


class Test_console(unittest.TestCase):
    """Test class"""

    def test_console(self):
        """checking for documentation"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.help_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.help_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.help_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.help_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.help_update.__doc__)

