#!/bin/env/python
# -*- coding: utf-8 -*-
import sys
import os
import importlib
import glob

def main():
    Home = os.environ['HOME']
    conf_dir = Home + '/.biu.d/'
    sys.path.append(conf_dir)
    if len(sys.argv) == 1:
        print("All commmands:")
        for filename in glob.glob(conf_dir + '*.py'):
            filename = os.path.basename(filename).split('.')[0]
            print(filename)
    else:
        biu = importlib.import_module(sys.argv[1])
        if len(sys.argv) == 2:
            getattr(biu,"help")()
        elif len(sys.argv) == 3:
            getattr(biu,sys.argv[2])()
        else:
            getattr(biu,sys.argv[2])(sys.argv[3:])
    sys.exit()

if __name__ == '__main__':
    main()
