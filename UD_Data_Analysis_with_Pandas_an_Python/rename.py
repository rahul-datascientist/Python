#!/usr/bin/env python

from datetime import datetime
import os
import os.path
import sys


def main(target):
    dir_path = os.path.abspath(target)
    for i in os.listdir(target):
        old_name = os.path.join(dir_path, i)
        d = datetime.strptime(i, '%d %b %Y').strftime('%Y-%m-%d')
        new_name = os.path.join(dir_path, d)
        os.rename(old_name, new_name)

if __name__ == '__main__':
    main('L:\jijaji-chat-par-hai')