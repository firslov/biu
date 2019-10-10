#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import importlib
import glob

# setup look-up directory properly
CONF_DIR = os.path.join(os.environ['HOME'] + '/.biu.d/')
sys.path.append(CONF_DIR)

def list_of_commands():
    """Return available biu commands"""
    files = [f for f in glob.glob(CONF_DIR+'*.py')]
    return [os.path.basename(f).split('.')[0] for f in files]

def list_of_recipes(mod):
    """Return available recipes in a module"""
    d = mod.__dict__
    return [f for f in d if "<f" in str(d[f])]

def list_of_all_recipes():
    "Return all available recipes across all modules"
    mod_names = list_of_commands()
    recipes = []
    for mod_name in mod_names:
        mod = importlib.import_module(mod_name)
        rs = list_of_recipes(mod)
        recipes.extend([f"{mod_name} {r}" for r in rs])
    return recipes

def main():
    try:
        ret = None
        # show all available commands
        if len(sys.argv) == 1:
            print("Available biu commands:")
            for filename in list_of_commands():
                print(f"- {filename}")
        else:
            mod_name = sys.argv[1]
            if len(sys.argv) == 2:
                # check for special keywords
                if mod_name == "list":
                    for r in list_of_all_recipes():
                        print(r)
                else:
                    # print all functions
                    mod = importlib.import_module(mod_name)
                    print(f"Available {mod_name} recipes:")
                    for r in list_of_recipes(mod):
                        print(f"- {r}")
            elif len(sys.argv) == 3:
                mod = importlib.import_module(mod_name)
                ret = getattr(mod, sys.argv[2])()
            else:
                mod = importlib.import_module(mod_name)
                ret = getattr(mod, sys.argv[2])(*sys.argv[3:])

            if isinstance(ret, list):
                print("======================")
                print("Run: \n")
                for cmd in ret:
                    print(cmd)
                    os.system(cmd)
                print("======================")
    except:
        print("Illegal command, please input again.")
    sys.exit()

if __name__ == '__main__':
    main()
