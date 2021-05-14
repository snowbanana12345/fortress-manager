import os

import pygame

import definitions


class ImageManager:
    def __init__(self):
        root = definitions.ROOTDIR
        labels = []
        image_paths = []

        labels.append("wood_icon")
        image_paths.append(os.path.join(root, "assets\\icons\\resource_icons", "wood_icon.png"))
        labels.append("gold_icon")
        image_paths.append(os.path.join(root, "assets\\icons\\resource_icons", "gold_icon.png"))

        self.image_directory = {}
        for index in range(len(image_paths)):
            self.image_directory[labels[index]] = image_paths[index]

    def getImage(self, image_label):
        try:
            return self.image_directory[image_label]
        except KeyError:
            print("Invalid image label : Image does not exist!")
            raise Exception
