#!/usr/bin/python3
"""Log stdin network input"""
import sys

to_print = 0
total_file_size = 0
status_codes = {}
possible_status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        if to_print > 9:
            to_print = 0
            print(f'File size: {total_file_size}')
            for code in possible_status_code:
                value = status_codes.get(code)
                if value:
                    print(f"{code}: {value}")
        try:
            args = line.split(" ")
            if len(args) != 9:
                continue
            status_code = args[-2]
            file_size = args[-1]
            int(status_code)
            file_size = int(file_size)
            if status_codes.get(status_code) == None: 
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1
                total_file_size += file_size
        except Exception as e:
            pass
        finally:
            to_print += 1
except Exception as e:
    pass
finally:
    print(f'File size: {total_file_size}')
    for code in possible_status_code:
        value = status_codes.get(code)
        if value:
            print(f"{code}: {value}")


