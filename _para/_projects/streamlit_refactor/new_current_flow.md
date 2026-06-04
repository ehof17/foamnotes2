
streamlit/pages/3_pdf_to_qdrant.py
/mnt/Machine_Learning/bis/chat_bot/data/unboxed
- reads files from unboxed
- Converts to pdf
- Sends to qdrant
- Moves files /mnt/Machine_Learning/bis/chat_bot/data/unboxed
- to /data/chat_bot/data/finished/pdfs

> Issue: rag_pipeline expects files to exist in /mnt/Machine_Learning/bis/chat_bot/data/unboxed


TagRedis.run('mnt/Machine_Learning/bis/chat_bot/data/metadata/pdf_info.json)
    self.load_pdf_info(file_path)
    self.loc_pub_dict()
    self.compare(redis_key)

