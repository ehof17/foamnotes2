Markdown conversion is inconsistent


```
def convert_pdf_page_to_markdown_via_rag_pipeline(pdf_path: str, page_num: int) -> str:
    """
    Extract one page from a PDF and convert to markdown via the RAG pipeline
    endpoint at crainservices.

    The endpoint accepts a single-page PDF upload and returns:
    ``{"data": [{"pages": {"page_0": {"markdown_text": "..."}}}]}``
    """
    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    writer.add_page(reader.pages[page_num])

    buf = BytesIO()
    writer.write(buf)
    buf.seek(0)

    upload_name = f'{os.path.splitext(os.path.basename(pdf_path))[0]}_page{page_num}.pdf'
    response = requests.post(
        _RAG_PIPELINE_URL,
        files={'File': (upload_name, buf, 'application/pdf')},
    )
    response.raise_for_status()

    result = response.json()
    print(result)
    return result['data'][0]['pages']['page_0']['markdown_text']

```

For the same pdf... [[]]
{'message': 'processed 1 file(s) to markdown', 'data': [{'file_name': '2026-01-30 Sales Support Task Order - Activate OS_page1.pdf', 'pages': {'page_0': {'markdown_text': "# Dolezal Equipment - Activate Question\n\n![Software interface showing search results for Ryan Dolezal](image_0)\n\n### Search Results\n**Contacts Returned: 4**\n\n| Full Name | Account | City | State | Country | Main Phone | CRMID |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| Ryan Dolezal | Dolezal | Secret | NE | USA | (482) 413-6868 | 120271463 |\n| Ryan Dolezal | Ryan Dolezal | Lincoln | NE | USA | (482) 281-5485 | 177276367 |\n| Ryan Dolezal | Sunhills Gilded | Lincoln | NE | USA | (482) 479-1078 | 13411583 |\n| Ryan Dolezal | Sunhills Publishing | Lincoln | NE | USA | (890) 307-5199 | 6832050 |\n\n***\n\n![Software interface showing detailed contact profile for Ryan Dolezal](image_1)\n\n**Contact Details:**\n* **CRMID:** 13411583\n* **Customer's Email:** ryan-dolezal@tractorhouse.com\n* **Address:** 120 West Harvest Drive, Lincoln, NE, 68521 USA\n* **Main Phone Number:** 890 307 5199\n\n***\n\n**Ryan Dolezal – TractorHouse Manager**\n800.307.5199 | 402.458.2982 (Direct)\n120 West Harvest Drive | Lincoln, NE 68521 | [www.tractorhouse.com](http://www.tractorhouse.com)\n\n![TractorHouse, AuctionTime, MarketBook, TruckPaper logos](image_2)", 'errors': {}, 'success': True}}, 'success': True}], 'errors': {}, 'success': True}

{'message': 'processed 1 file(s) to markdown', 'data': [{'file_name': '2026-01-30 Sales Support Task Order - Activate OS_page1.pdf', 'pages': {'page_0': {'markdown_text': '# Dolezal Equipment - Activate Question\n\n![Dolezal Equipment Search Results](image_0)\n\n![Dolezal Equipment Contact Profile](image_1)\n\n**Ryan Dolezal – TractorHouse Manager**\n800.307.5199 | 402.458.2982 (Direct)\n120 West Harvest Drive | Lincoln, NE 68521 | [www.tractorhouse.com](http://www.tractorhouse.com)\n\n![TractorHouse Logos](image_2)', 'errors': {}, 'success': True}}, 'success': True}], 'errors': {}, 'success': True}

again
```json
{'message': 'processed 1 file(s) to markdown', 'data': [{'file_name': '2026-01-30 Sales Support Task Order - Activate OS_page1.pdf', 'pages': {'page_0': {'markdown_text': '![CRM Search Results Screen](image_0)\n\n![CRM Contact Detail Screen](image_1)\n\n**Ryan Dolezal – TractorHouse Manager**\n800.307.5199 | 402.458.2982 (Direct)\n120 West Harvest Drive | Lincoln, NE 68521 | [www.tractorhouse.com](http://www.tractorhouse.com)\n\n![TractorHouse, AuctionTime, MarketBook, Truck Paper logos](image_2)', 'errors': {}, 'success': True}}, 'success': True}], 'errors': {}, 'success': True}
```

Even when passing in Stream=True and timeout
```json
{'message': 'processed 1 file(s) to markdown', 'data': [{'file_name': '2026-01-30 Sales Support Task Order - Activate OS_page1.pdf', 'pages': {'page_0': {'markdown_text': '![CRM Search Results Interface - Contact Search for Dolezal Equipment](image_0)\n\n![CRM Contact Record Detail - Contact Management Options](image_1)\n\n**Ryan Dolezal – TractorHouse Manager**\n800.307.5199 | 402.458.2982 (Direct)\n120 West Harvest Drive | Lincoln, NE 68521 | [www.tractorhouse.com](http://www.tractorhouse.com)\n\n![TractorHouse, AuctionTime, MarketBook, TruckPaper logos](image_2)', 'errors': {}, 'success': True}}, 'success': True}], 'errors': {}, 'success': True}
```


If I pass the file directly to the api...


```json
{
    "message": "processed 1 file(s) to markdown",
    "data": [
        {
            "file_name": "2026-01-30 Sales Support Task Order - Activate OS.pdf",
            "pages": {
                "page_0": {
                    "markdown_text": "**From:** Ryan Dolezal\n**Sent:** Friday, January 30, 2026 11:00 AM\n**To:** Trade Pub Sales\n**Cc:** Shayne Campbell\n**Subject:** Sales Support - Activate\n\nActivate has been added to the Sales Support TO.\n\nThis task will be used for a sales rep with Sales questions you have relating to Activate OS.\n\nNOTE - This is not a replacement for Activate Customer Support / Demos / Onboarding – those tasks remain separate.\n\nLet me know if you have any questions\n\n![Start a Task Interface - Software screenshot showing the process of initiating a support task.](image_0)",
                    "errors": {},
                    "success": true
                },
                "page_1": {
                    "markdown_text": "![Software interface for contact search](image_0)\n\n# Dolezal Equipment - Activate Question\n\n**Assigned To:** Ryan Dolezal\n\n## Search Results\n**Contacts Returned:**\nMatching \"Ryan Dolezal\" continuous\n\n| Full Name | Account | City | State | Country | Main Phone | CRMID |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| Ryan Dolezal | Dolezal | Seward | NE | USA | (402) 413-6668 | 12037163 |\n| Ryan Dolezal | Ryan Dolezal | Lincoln | NE | USA | (402) 281-5485 | 17737637 |\n| Ryan Dolezal | Sunbelt Rentals | Lincoln | NE | USA | (402) 479-1078 | 13415563 |\n| Ryan Dolezal | Sunbelt Publishing | Lincoln | NE | USA | (800) 307-5199 | 6832050 |\n\n***\n\n**Ryan Dolezal – TractorHouse Manager**\n800.307.5199 | 402.458.2982 (Direct)\n120 West Harvest Drive | Lincoln, NE 68521 | [www.tractorhouse.com](http://www.tractorhouse.com)\n\n![TractorHouse Logos](https://example.com/logos) *(Note: Logos for TractorHouse, AuctionTime, MarketBook, Machinery Trader, and Truck Paper appear here)*",
                    "errors": {},
                    "success": true
                }
            },
            "success": true
        }
    ],
    "errors": {},
    "success": true
}
```

