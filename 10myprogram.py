# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

#-----To change the default behaviour

import argparse
# parser = argparse.ArgumentParser(prog="myprogram")
# parser.add_argument('--foo', help='foo of the %(prog)s program')
# parser.print_help()


parser = argparse.ArgumentParser(prog='PROG',description='A foo that bars')
parser.add_argument('--foo', nargs='?', help='foo help')
parser.add_argument('--bar', nargs='+', help='bar help')
parser.print_help()