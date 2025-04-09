try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import aniobjects
   
except ModuleNotFoundError as e:
    print(
        f"{e}! Please ensure the module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")


class BuildWeb:
    def __init__(self):
        pass