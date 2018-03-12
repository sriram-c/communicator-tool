
                           README

    1. USR(Universal Semantic Representation) file structure:

        each usr file should come with a schema which will contain information regarding the rows in the usr file. 

        for e.g.

        schema file: (currently using the default schema given in "../docs/updated_user_csv_guideline.pdf")

        for e.g. current schema file 

            1	grp	Grouping
            2	concpt_dic	Concept from Concept dictionary
            3	idx_concpt_dic	Index for Concepts
            4	catg	Lexical Category (only for proper nouns, pronouns) AND Ontological Information about nouns
            5	gnp	GNP (Gender, Number, Person) Information
            6	intra_chk	Intrachunk Dependency Relations
            7	inter_chk	Interchunk Dependency Relations
            8	disc_rel	Discourse Relations

    2. Individual sentences in the parallel sentence database will have uniq id.
        e.g. 
            id | Eng_sent   id | Hnd_sent   id | Tamil_sent   id | Telugu_sent

    Logic:

    1. Read the Source (Hindi) USR file and the schema and store each rows information in a hash.

    1. Read Source (Hindi) and Target (Tamil) parallel sentence and map the words in the sentences.

    2. Run the Target(Tamil) morph on each word of the Target(Tamil) sentence.

            2.1. mark the root, vibhakti, tam for each word

    3. generate following files for the target language.
    
        1.  CSV file
        2.  Concept-dictionary
        3.  karaka-vibhakti mapping


   Assumption: 

   Source and Target sentences are parallel and word aligned (i.e same number of words in Hindi and Telugu)



	Set the path of COMMUNICATOR_TOOL inside csv-generator.py

	for e.g. 
	COMMUNICATOR_TOOL_PATH = "/home/sriram/phd/communicator/communicator-tool/"


   To Run:
   python  csv-generator.py   usr-hnd usr-tamil  usr-schema  tamil hnd-tamil-concept.dic karaka-vib 

   Files Required:

   usr-hnd : contains the  Hindi sentences with USR id
   usr-tamil : contains the  Tamil sentences with USR id
   usr-schema: Contains the usr-schema information

   Assumption is that for each USR id the corresponding id.usr file is present in the current directory,  for the source language

    for e.g. 1.usr , 2.usr , 3.usr

    File output:

   id-tamil.usr:  File contains the Tamil usr file for the corresponding Hindi usr file
	e.g. 1-tamil.usr, 2-tamil.usr 
   hnd-tamil-concept.dic: File contains the concept dictionary for Hindi and Tamil sentence pairs.
   karaka-vib: karaka and vibhakti mapping for  Hindi and Tamil 
    
   
           
            



# Tamil Generation:
#generate tamil sentence, given the tamil usr file and hnd-tamil concept dictionary

sh run-tamil-gen.sh

Gives the o/p onto stdout


# To convert csv to html:

Install csv2html from below link

https://github.com/dbohdan/csv2html

give below command

sh run_csv_to_html.sh <csv-file-name>

It will create "csv-file-name.html" 
