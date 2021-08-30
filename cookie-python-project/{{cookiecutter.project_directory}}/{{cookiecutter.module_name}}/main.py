"""This is a main file"""
from {{cookiecutter.module_name}} import arguments
from {{cookiecutter.module_name}} import configs

def main():
    """This is the main Function"""
    #args = arguments.parse_args()
    config = configs.parse_config()
    return 1
