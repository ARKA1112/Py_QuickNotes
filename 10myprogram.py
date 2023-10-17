# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

#-----To change the default behaviour

import argparse
import textwrap
# parser = argparse.ArgumentParser(prog="myprogram")
# parser.add_argument('--foo', help='foo of the %(prog)s program')
# parser.print_help()


# parser = argparse.ArgumentParser(prog='PROG',description='A foo that bars')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('--bar', nargs='+', help='bar help')
# parser.print_help()

# parent_parser = argparse.ArgumentParser(add_help=False)
# parent_parser.add_argument('--parent', type=int)
# foo_parser = argparse.ArgumentParser(parents=[parent_parser])
# foo_parser.add_argument('foo')
# foo_parser.parse_args(['--parent','2','XXX'])

# parser = argparse.ArgumentParser(

#     prog='PROG',
#     description='''this description
#         was indented weird
#             but that is okay''',
#     epilog='''
#             likewise for this epilog whose whitespace will 
#             be cleaned up and whose words will be wrapped
#             across a couple lines''')

# parser.print_help()

# parser = argparse.ArgumentParser(
#     prog='PROG',
#     formatter_class = argparse.RawDescriptionHelpFormatter,
#     description= textwrap.dedent('''\
#         Please do not messs up this text!
            
#             I have indented it
#             exactly  the way
#             I want it
#                                 '''                    )
# )
# parser.print_help()


#USING MetavarTypeHelpFormatter 

# parser = argparse.ArgumentParser(
#     prog = 'PROG',
#     formatter_class=argparse.MetavarTypeHelpFormatter)

# parser.add_argument('-foo',type=int)
# parser.add_argument('--bar',type=float)
# parser.print_help()

#USING PREFIX CHARS

# parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
# parser.add_argument('+f')
# parser.add_argument('++bar')
# parser.parse_args('+f X ++bar Y'.split())
# parser.print_help()

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action='append')
# parser.parse_args('--foo 1 --foo 2'.split())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.parse_args(['-vvv'])

