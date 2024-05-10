#!/usr/bin/python3
'''a script that reads from stdin
parses the output and logs expected result
'''
import sys
import re
from datetime import datetime
from signal import signal, SIGINT


if __name__ == "__main__":
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET\s?\/projects'
    pattern += r'\/260 HTTP\/1\.1\" (\d{3}) (\d{1,})'
    total_file_size = 0
    stat_dict = {}

    def handler(signum, frame):
        '''handles system interupt signal'''
        print(f"File size: {total_file_size}")
        for code in sorted(stat_dict):
            print(f'{code}: {stat_dict[code]}')
        raise KeyboardInterrupt

    signal(SIGINT, handler)

    while 1:
        for i, line in zip(range(10), sys.stdin):
            line = line.rstrip()
            match = re.fullmatch(pattern, line)
            if match:
                total_file_size += int(match.groups()[1])
                code = int(match.groups()[0])
                if code in stat_dict:
                    stat_dict[code] = stat_dict[code] + 1
                else:
                    stat_dict[code] = 1
            else:
                continue

        print(f"File size: {total_file_size}")
        for code in sorted(stat_dict):
            print(f'{code}: {stat_dict[code]}')
