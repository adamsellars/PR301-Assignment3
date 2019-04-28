import os
import logging
from tkinter import *
from tkinter import filedialog


class FileHandler:
    # Created by Leroi
    @staticmethod
    def read_file():
        root = Tk()
        try:
            name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.txt*"), ("All files", "*.txt*")))
            with open(name_of_file) as file:
                file_data = file.read()
        except FileNotFoundError:
            return FileNotFoundError
        except PermissionError:
            return PermissionError
        finally:
            root.destroy()
        return file_data

    # Created by Adam
    # Different way to read data from file requires user to enter complete file path
    @staticmethod
    def read_file_from_path(path) -> str:
        try:
            with open(path) as file:
                data = file.read()
                assert type(data) is str, "data must be a String data type"
        except FileNotFoundError:
            print("Error, file does not exist!")
        except PermissionError:
            print("Error, you do not have permission to access this file!")
        else:
            print("\nfile loaded...\n")
            assert type(data) is str, "data must be a String data type"
            return data

    # Created by Leroi
    @staticmethod
    def choose_directory():
        root = Tk()
        try:
            dir_name = filedialog.askdirectory()
        except TypeError:
            return TypeError
        except Exception as e:
            logging.exception(e)
        else:
            return dir_name
        finally:
            root.destroy()

    # Created by Leroi
    @staticmethod
    def write_file(directory_name: str, content: str, a_plant_class: str):
        root = Tk()
        file_name = a_plant_class.class_name.lower()
        try:
            with open(directory_name + "/{}.py".format(file_name.lower()), "w+") as f:
                f.write(content)
        except FileNotFoundError:
            return FileNotFoundError
        except PermissionError:
            return PermissionError
        except TypeError:
            return TypeError
        finally:
            root.destroy()

    # Created by Adam different way to handle creating directories
    @staticmethod
    def write_file_to_path(path: str, content: str, a_plant_class: str):
        try:
            # give a default directory if user doesn't choose one
            if "/" not in path:
                path = "generated_code/" + path
            name = a_plant_class.class_name.lower()
            filename = path + name + ".py"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w+") as file:
                file.write(content)
        except FileNotFoundError:
            return FileNotFoundError
            # print("Error, no file inserted")
        except PermissionError:
            return PermissionError
            # print("Error, you do not have permission to access this file!")
        except TypeError:
            return TypeError
        except Exception as e:
            logging.exception(e)
            return e
        else:
            print("File successfully written\n")

