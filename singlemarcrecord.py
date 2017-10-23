#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import os
import base64
from pymarc import MARCReader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generates single record MARC files')
    parser.add_argument('-prefix', type=str, default="dswarm-", help='set prefix for id generation')
    parser.add_argument('-source_id', type=str, default="0", help='set source id for id generation')
    parser.add_argument('-input_file', type=str, default="[NO DEFAULT]",
                        help='the input MARC file')
    parser.add_argument('-output_folder', type=str, default=".",
                        help='the output folder for the single record MARC files')
    args = parser.parse_args()
    prefix = args.prefix
    sourceId = args.source_id
    inputFile = args.input_file
    outputFolder = args.output_folder

    with open(inputFile, 'rb') as fh:
        reader = MARCReader(fh)
        for record in reader:
            recordId = prefix + "-" + sourceId + "-" + str(
                base64.urlsafe_b64encode(bytes(record['001'].value(), 'utf-8')).decode('utf-8')).rstrip('=')
            fileName = recordId + '.mrc'
            out = open(os.path.join(outputFolder, fileName), 'wb')
            out.write(record.as_marc())
            out.close()
