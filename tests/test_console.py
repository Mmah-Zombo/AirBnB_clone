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

    def test_destroy(self):
        # Test destroy command
        obj = BaseModel()
        with patch('sys.stdin', StringIO(f"destroy BaseModel {obj.id}\n")):
            self.console.cmdloop()
        obj_key = f"{type(obj).__name__}.{obj.id}"
        self.assertNotIn(obj_key, storage.all())

    def test_all(self):
        # Test all command
        with patch('sys.stdin', StringIO("all\n")):
            self.console.cmdloop()
        output = self.console_output.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_count(self):
        # Test count command
        with patch('sys.stdin', StringIO("BaseModel.count()\n")):
            self.console.cmdloop()
        output = self.console_output.getvalue().strip()
        self.assertEqual(output, "1")

    def test_update(self):
        # Test update command
        obj = BaseModel()
        with patch('sys.stdin', StringIO(f"update BaseModel {obj.id} name 'New Name'\n")):
            self.console.cmdloop()
        self.assertEqual(obj.name, "New Name")

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

    def test_empty_line(self):
        # Test empty line command
        with patch('sys.stdin', StringIO("\n")):
            self.console.cmdloop()

    def test_help(self):
        # Test help command
        with patch('sys.stdin', StringIO("help\n")):
            self.console.cmdloop()

    # Add similar tests for other commands (count, update, etc.)
    # Test all classes (User, State, City, Place, Amenity, Review) in the same way as BaseModel

if __name__ == "__main__":
    unittest.main()
