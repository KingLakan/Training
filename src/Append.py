import argparse
from os.path import exists

parser = argparse.ArgumentParser(description='SysDef to be processed')
parser.add_argument('--file',
                    metavar='FILE_PATH',
                    type=str,
                    action='store',
                    help='Path+name of file to append to')
args = parser.parse_args()

print("inputted file: {}".format(args.file), "\n")

if exists(args.file):
    with open(args.file, 'a') as file_object:
        file_object.write("hello\n")
        print("Line appended to {}".format(args.file), "\n")
else:
    with open(args.file, 'w') as file_object:
        file_object.write("hello\n")
        print("New file {} created".format(args.file), "\n")
