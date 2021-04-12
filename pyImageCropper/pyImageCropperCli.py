#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse

from pyImageCropper import ImageCropper

# ================================================================
#
# Main
#
# ================================================================


def main():
    '''
    pyImageCropperCli.py "F:/test stuff/inputImages" "F:/test stuff/outputImages"
    '''
    parser = argparse.ArgumentParser(description='Loads all the images in the inputDir for cropping and saves them in outputDir')

    # args
    parser.add_argument("inputDir", help="url to crawl")
    parser.add_argument("outputDir", help="unique url identifier")

    # parse
    args = parser.parse_args()

    # run
    ImageCropper(args.inputDir,
                 args.outputDir).run()


if __name__ == '__main__':
    main()
