import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestHBnBConsole(unittest.TestCase):

    def setUp(self):
        # Redirect standard output to capture command outputs
        self.console_output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.console_output
        # Create an instance of HBNBCommand for each test
        self.console = HBNBCommand()

    def tearDown(self):
        # Restore standard output
        sys.stdout = self.saved_stdout
        # Clear storage between tests
        storage.delete_all()

    def test_create(self):
        # Test create command
        with patch('sys.stdin', StringIO("create BaseModel\n")):
            self.console.cmdloop()
        output = self.console_output.getvalue().strip()
        self.assertTrue(output.startswith("2"))

    def test_show(self):
        # Test show command
        obj = BaseModel()
        with patch('sys.stdin', StringIO(f"show BaseModel {obj.id}\n")):
            self.console.cmdloop()
        output = self.console_output.getvalue().strip()
        self.assertTrue(obj.id in output)

    # Add similar tests for other commands (destroy, all, count, update, etc.)

    def test_quit(self):
        # Test quit command
        with self.assertRaises(SystemExit):
            with patch('sys.stdin', StringIO("quit\n")):
                self.console.cmdloop()

    def test_EOF(self):
        # Test EOF command
        with self.assertRaises(SystemExit):
            with patch('sys.stdin', StringIO("EOF\n")):
                self.console.cmdloop()

if __name__ == "__main__":
    unittest.main()
