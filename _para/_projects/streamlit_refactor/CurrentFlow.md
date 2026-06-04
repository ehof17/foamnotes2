Chat bot daily job is ran every day
http://mltraining:8080/job/machine_learning_bis_chat_bot_daily/

It runs get_pdfs.py
https://devops.sandhills.int/tfs/SandhillsSoftware/Analytics_ArtificialIntelligence/_git/chat_bot_pipeline?path=/get_pdfs.py

Saves pdfs to  /mnt/Machine_Learning/bis/chat_bot/data/unboxed/mm-dd-Y of day it runs


Ethan:
Goes to CVAT http://wimldev101:7766/tasks/65/jobs/62 to draw boxes around relavent info.
After that, its exported into an XML file

Then that XML file is uploaded in the Annotization tab

The annotization tab
reads from /data/chat_bot/data/metadata/annotation.json
Then dumps an updated dictionary there

Then, he goes to 'PDF to qdrant tab' to find the pdf groupings. Its usually the day before, but it looks at the folders in mnt/Machine_Learning/bis/chat_bot/data/unboxed, which are generated from the daily job

The streamlit then Converts the selected pdfs to text via pdf_to_text.
Pdf to text opens the annotation to set the ann_dict, and calls an llm.
So I think this can instead just call the rag_pipeline_api

text_directory = '/data/chat_bot/data/finished/texts
done_directory = '/data/chat_bot/data/finished/pdfs


uh oh
since the streamlit sends to qdrant
maybe it does processing that I don't do in the new job


New flow:
rag_pipleline_doc_retreival embeds and sends the text to qdrant

So streamlit... how would it edit?
Will have to edit the file in markdown mirror,
then send that to qdrant. Will have to remove the file from qdrant and re embed it I guess.

Edit tab with different configurations
- markdown mirror path
- unsupported files logging path
- failed files path
- qdrant collection name


config_showpad = {
    "markdown_mirror_path": '/mnt/Machine_Learning/bis/chat_bot/data/showpad_markdown_mirror"
    UNSUPPORTED_FILES_LOGGING_PATH =/mnt/Machine_Learning/bis/chat_bot/data/ShowpadLogging'
    FAILED_FILES_LOGGING_PATH = /mnt/Machine_Learning/bis/chat_bot/data/failed_files_showpad
    QDRANT_COLLECTION_NAME = 'showpad_pdfs_hybrid'
}
config_hr = {
    BASE_DATA_PATH = /mnt/Machine_Learning/bis/chat_bot/data/'
    MARKDOWN_MIRROR = /mnt/Machine_Learning/bis/chat_bot/data/hr_markdown_mirror
    UNSUPPORTED_FILES_LOGGING_PATH =/mnt/Machine_Learning/bis/chat_bot/data/HumanResourceLogging
    FAILED_FILES_LOGGING_PATH = /mnt/Machine_Learning/bis/chat_bot/data/failed_files
    QDRANT_COLLECTION_NAME = "hr_files"
}

EDIT PAGE:
Read in the filenames of everything in the configs markdown mirror
Allow for editing, which will update the file in the markdown mirror
Then reembed and send it to qdrant

FAILED FILES PAGE:
Read in the failed files json for the selected environments
Load in the partial markdown file
For the failed pages, use docling to read in the pages as a baseline for the markdown conversion
Allow the user to make any edits to the markdown, then allow them to upload
The file will be added to the markdown mirror, and removed from the corresponding failed files json file

With each config, allow to select environments staging or live
- It will then 

## changes
- support hr files and showpad
- Instead of streamlit running a pdf to text converter, it should look in the markdown mirror.
- If not there allow user to try again


