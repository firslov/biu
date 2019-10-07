#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import importlib
import glob

# setup look-up directory properly
CONF_DIR = os.path.join(os.environ['HOME'] + '/.biu.d/')
sys.path.append(CONF_DIR)

def main():
    # show all available commands
    if len(sys.argv) == 1:
        print("Available biu commands:")
        for filename in glob.glob(CONF_DIR + '*.py'):
            filename = os.path.basename(filename).split('.')[0]
            print(f"- {filename}")
    else:
        mod_name = sys.argv[1]
        mod = importlib.import_module(mod_name)
        if len(sys.argv) == 2:
            try:
                ret = getattr(mod, "help")()
            except Exception:
                ret = None
                print(f"No help found for {mod_name}!")
        elif len(sys.argv) == 3:
            ret = getattr(mod, sys.argv[2])()
        else:
            ret = getattr(mod, sys.argv[2])(*sys.argv[3:])

        if isinstance(ret, list):
            print("======================")
            print("Run: \n")
            for cmd in ret:
                print(cmd)
                os.system(cmd)
            print("======================")
    sys.exit()

if __name__ == '__main__':
    main()
