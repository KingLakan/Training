import argparse

parser = argparse.ArgumentParser(description='SysDef to be processed')
parser.add_argument('--file',
                    metavar='FILE_PATH',
                    type=str,
                    action='store',
                    help='Path+name of file to append to')

args = parser.parse_args()
print(args, "\n")
print("inputted file: {}".format(args.file))

with open(args.file, 'a') as file_object:
    file_object.write("hello\n")
