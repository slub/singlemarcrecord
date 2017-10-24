# singlemarcrecord

generates single record MARC files

## requirements

pymarc

### install pymarc

1. (optionally) install easy_install3:

    sudo apt-get install python3-setuptools

2. (optionally) install pip for python 3.x:

   sudo easy_install3 pip

3. install pymarc with pip (e.g. pip3.5):

   sudo -H pip3.5 install pymarc 

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
