#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scgis_project.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scgis_django.settings")
>>>>>>> b59ecb4991c4566acd45340a5202e4e3b09fd592

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
