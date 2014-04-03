#/usr/bin/env python
# -*- coding: utf-8 -*-

'''Main application all tools and debugers are connected here.The moudles also could be used alone. This python file connect different tools toghether and make the code smaller.
'''

import argparse
import drama.drama

def set_verbose_level(level,quiet=False):
    verbose = "ERROR"
    if(level == 0 or quiet):
        verbose = "ERROR"
    elif(level == 1):
        verbose = "WARNING"
    elif (level == 2):
        verbose = "INFO"
    elif (level > 2):
        verbose = "DEBUG"
    return verbose

def main():
    parser = argparse.ArgumentParser(description="TEIReader, see the help for all the option and arguments.")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", help="verbose logging",action="count",default=0)
    group.add_argument("-q","--quiet",help="without any log",action="store_true")
    args = parser.parse_args()
    verbose = set_verbose_level(args.verbose,args.quiet)

if __name__ == "__main__":
    main()
