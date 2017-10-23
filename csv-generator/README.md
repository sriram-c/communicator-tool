# TO RUN:

Set the path of COMMUNICATOR_TOOL inside csv-generator.py

for e.g. 
COMMUNICATOR_TOOL_PATH = "/home/sriram/phd/communicator/communicator-tool/"


python csv-generator.py parallel-sent/hnd-tamil-sent.csv tamil.csv hnd-tamil-concept.dic

tamil.csv : file containing the tamil csv o/p
hnd-tamil-concept.dic: Hindi and Tamil concept dictionary

# Tamil Generation:

sh run-tamil-gen.sh

Gives the o/p onto stdout


# To convert csv to html:

Install csv2html from below link

https://github.com/dbohdan/csv2html

give below command

sh run_csv_to_html.sh <csv-file-name>

It will create "csv-file-name.html" 
