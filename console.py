#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    valid_classes = {'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'}

    # ... (existing code)

    def do_create(self, arg):
        """Creates a new instance of a class, saves it to the JSON file, \
            and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based \
            on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objs = BaseModel.all()
        all_objs.update(User.all())
        all_objs.update(State.all())
        all_objs.update(City.all())
        all_objs.update(Amenity.all())
        all_objs.update(Place.all())
        all_objs.update(Review.all())
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and \
            id (save the change into the JSON file)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objs = BaseModel.all()
        all_objs.update(User.all())
        all_objs.update(State.all())
        all_objs.update(City.all())
        all_objs.update(Amenity.all())
        all_objs.update(Place.all())
        all_objs.update(Review.all())
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
            return

        all_objs.pop(key)
        BaseModel.save_to_file()

    def do_all(self, arg):
        """Prints all string representation of all instances based \
            or not on the class name."""
        args = arg.split()
        all_objs = BaseModel.all()
        all_objs.update(User.all())
        all_objs.update(State.all())
        all_objs.update(City.all())
        all_objs.update(Amenity.all())
        all_objs.update(Place.all())
        all_objs.update(Review.all())

        if not args:
            obj_list = list(all_objs.values())
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for key, obj in all_objs.items() if key.startswith(class_name)]

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objs = BaseModel.all()
        all_objs.update(User.all())
        all_objs.update(State.all())
        all_objs.update(City.all())
        all_objs.update(Amenity.all())
        all_objs.update(Place.all())
        all_objs.update(Review.all())
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        obj = all_objs[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
