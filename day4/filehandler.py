import json


class FileHandler:

    FILE_NAME = "data.txt"

    @staticmethod
    def save_data(data):

        with open(FileHandler.FILE_NAME, "w") as file:

            json.dump(data, file, indent=4)

    @staticmethod
    def load_data():

        try:

            with open(FileHandler.FILE_NAME, "r") as file:

                return json.load(file)

        except:

            return []