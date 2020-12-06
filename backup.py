import os
import argparse

# os.system("cp -v -R \"/Users/aamod/Aamod/UMass/\" \"/Volumes/HDD/Aamod/UMass/\"")
def backup(origin, dest, verbose = False):
    v = ""
    if origin is None:
        origin = "CHANGE ME"
    if dest is None:
        dest = "CHANGE ME"
    if verbose:
        v = "-v "
    cmd = "cp "+v+"-R \"" + origin + "\" \"" + dest +"\""
    os.system(cmd)

def main():
    parser = argparse.ArgumentParser(description='Deep copy folders')

    parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='Output files while copying')

    parser.add_argument('-origin', type = str,
                        help ='Origin pathname with escape characters.',
                        metavar = 'o')
    parser.add_argument('-destination', type = str,
                        help ='Destination pathname with escape characters.',
                        metavar = 'd')

    args = parser.parse_args()
    print(args)
    backup(args.origin, args.destination, args.verbose)

if __name__ == "__main__":
    main()
