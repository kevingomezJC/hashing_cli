import argparse
import hashlib
import os
import sys


def hash_file(file_path, hash_algorithm):
    """
    hashes a file with the given hash algorithm
    """
    with open(file_path, 'rb') as file_handle:
        file_content = file_handle.read()
        hash_object = hashlib.new(hash_algorithm)
        hash_object.update(file_content)
        return hash_object.hexdigest()


def hash_directory(directory_path, hash_algorithm):
    """
    hashes a directory with the given hash algorithm
    """
    hashed_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            hashed_files.append((file_path, hash_file(file_path, hash_algorithm)))
    return hashed_files


def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description='hashs files and directories with multiple algorithms')
    parser.add_argument('-a', '--algorithm', type=str, required=True, help='hash algorithm to use')
    parser.add_argument('-f', '--file', type=str, help='file to hash')
    parser.add_argument('-d', '--directory', type=str, help='directory to hash')
    args = parser.parse_args()

    if args.file:
        print(hash_file(args.file, args.algorithm))
    elif args.directory:
        print(hash_directory(args.directory, args.algorithm))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
