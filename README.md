# Python script to transform the data collected from monster to a form kafka can handle.

To transform the data just run
```bash
python3 transformData.py
```
and the program will take a filename of the input file and a filename of the output file.
The output file will be created if not already existend.

The data set folder contains the original data received from fasten (`monster-dataset*`) and some already transformed sets (`*.mvn.coords.txt`).
Each transformed data set contains a random number (10 or 1000 or full) of packages of the original dataset picked with:
```bash
shuf -n 1000 monster-dataset-full-orinal.txt > monster-dataset-1000.txt
```
The file `monster-dataset-full.txt` is a version of the `monster-dataset-full-original.txt` file without leading spaces, as those cause the python script to crash, as the regex doesn't work anymore. \
For example: \
Most of the time, the string containing the package version is: \
`"version":"version number"` \
But in some cases its: \
`"version": "version number"` \
Same goes for other key value pairs.
