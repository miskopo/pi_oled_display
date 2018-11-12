from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--image",
                    nargs=1,
                    help="Path to image to show")
parser.add_argument("--group",
                    nargs=1,
                    help="Group of screens to show")

