# import argparse

# class FooAction(argparse.Action):
#     def __init__(self, option_strings, dest, nargs=None, **kwargs):
#         if nargs is not None:
#             raise ValueError('nargs not allowed')
        
#         super().__init__(option_strings, dest=dest, nargs=0, **kwargs)

#     def __call__(self, parser, namespace, values, option_string=None):
#         print('%r %r %r' % (namespace, values, option_string))
#         setattr(namespace, self.dest, values)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--foo', action=FooAction)
#     parser.add_argument('bar',action=FooAction)

#     args = parser.parse_args()
#     #print(args)


# import argparse

# def hyphenated(string):
#     return '-'.join([word[:4] for word in string.casefold().split()])

# parser = argparse.ArgumentParser()
# parser.add_argument('shor_title',type=hyphenated)

# args = parser.parse_args()
# print(hyphenated(args.shor_title))

#ARGPARSE WITH OPTIONS[ROCK PAPER SCISSORS]

import argparse

parser = argparse.ArgumentParser(description='game.py')
parser.add_argument('--move', choices=['rock', 'paper','scissors'],required=True)

args = parser.parse_args()
print(args.move)