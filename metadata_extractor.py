def metadata_extractor(directory):
    import os
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    files = os.listdir(directory)
    for file in files:
        if '.' in file:
            if file.split(".")[1] == "pdf":
                fp = open(directory+"/"+file, 'rb')
                parser = PDFParser(fp)
                doc = PDFDocument(parser)
                print(file, "Metadata")
                print("")
                print(doc.info)
                print("__________________________________________________________________________________________________________________")
                print("")

import os
metadata_extractor(os.getcwd())                