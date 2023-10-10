import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='int', type=int, choices=range(30))
parser.parse_args(['20'])