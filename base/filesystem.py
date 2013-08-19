# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
import os, math, hashlib
from PIL import Image
from django.core.files.storage import FileSystemStorage

def get_partition_id(pk, chunk_size=1000):
    """
    Given a primary key and optionally the number of models that will get
    shared access to a directory, return an integer representing a directory
    name.
    """
    return int(math.ceil(pk / float(chunk_size)))


def safe_filename(filename):
    """Generate a safe filename for storage."""
    name, ext = os.path.splitext(filename)
    return "%s%s" % (hashlib.md5(name.encode('utf8')).hexdigest(), ext)

class ImageStorage(FileSystemStorage):
    """
    A Filesystem Storage that only support images
    """

    format_extensions = {
        'PNG': 'png',
        'GIF': 'gif',
        'JPEG': 'jpg',
        'JPG': 'jpg',
    }

    def _save(self, name, content):
        name, ext = os.path.splitext(name)
        image = Image.open(content)
        if image.format in self.format_extensions:
            name = "%s.%s" % (name, self.format_extensions[image.format])
        else:
            raise Exception("Unknown image format: %s" % (image.format,))
        name = super(ImageStorage, self)._save(name, content)
        image.save(self.path(name), image.format)
        return name