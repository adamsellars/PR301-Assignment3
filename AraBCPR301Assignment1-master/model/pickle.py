import pickle
import logging
from tkinter import *
from tkinter import filedialog


class Pickler:

    # Leroi wrote this
    @staticmethod
    def pickle_file(file_data):
        root = Tk()
        try:
            with open("data.pickle", "wb") as file:
                pickle.dump(file_data, file)
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            return FileNotFoundError
        except Exception as e:
            logging.exception(e)
            return e
        # else:
        #     pickled_successfully = True
        #     return pickled_successfully
        finally:
            root.destroy()

    # Adam wrote this
    @staticmethod
    def unpickle_file():
        root = Tk()
        try:
            name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.pickle*"), ("All files", "*.pickle*")))
            with open(name_of_file, "rb") as file:
                file_data = pickle.load(file)
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            return FileNotFoundError
        except Exception as e:
            logging.exception(e)
            return e
        else:
            return file_data
        finally:
            root.destroy()


