import os
import argparse
import platform

# os.system("cp -v -R \"/Users/aamod/Aamod/UMass/\" \"/Volumes/HDD/Aamod/UMass/\"")
def backup(origin, dest, verbose = False):
    v = ""
    if origin is None:
        origin = "/Users/aamod/Aamod/UMass/"
    if dest is None:
        dest = "/Volumes/HDD/Aamod/UMass/"
    if verbose:
        v = "-v "
    if platform.system() == 'Windows':
        cmd = "robocopy " + origin + " " + dest + " /I /V"
    else:
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
