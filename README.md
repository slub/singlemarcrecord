# singlemarcrecord

generates single record MARC files

takes a given binary MARC records file (containing multiple MARC records) and splits it into single binary MARC records files, whereby the file names will be constructed with following pattern:

    [ID].mrc

whereby ID will be constructed of:

    [PREFIX]-[SOURCE ID]-[MARC RECORD ID FROM 001]

## requirements

* [argparse](https://docs.python.org/3/library/argparse.html#module-argparse)
* [pymarc](https://github.com/edsu/pymarc)

### install requirements

1. (optionally) install [pip](https://pip.pypa.io/) for Python 3.x:

    sudo apt-get install python3-pip

2. install requirements with pip:

    sudo -H pip3 install -r requirements.txt 

## usage

    singlemarcrecord.py [-h] [-prefix PREFIX] [-source_id SOURCE_ID]
                           [-input_file INPUT_FILE]
                           [-output_folder OUTPUT_FOLDER]

optional arguments:

    -h, --help            show this help message and exit
    -prefix PREFIX        set prefix for id generation
    -source_id SOURCE_ID  set source id for id generation
    -input_file INPUT_FILE the input MARC file
    -output_folder OUTPUT_FOLDER the output folder for the single record MARC files

### usage example

    ./singlemarcrecord.py -prefix [PREFIX] -source_id [SOURCE ID] -input_file [INPUT BINARY MARC FILE] -output_folder [OUTPUT FOLDER FOR SINGLE MARC RECORD FILES]
