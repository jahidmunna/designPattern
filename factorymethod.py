from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def create(self):
        pass


class PDFDocument(Document):
    def create(self):
        return "PDF Document created"


class HTMLDocument(Document):
    def create(self):
        return "HTML Document created"


def create_document(doc_type):
    if doc_type == "pdf":
        return PDFDocument()
    elif doc_type == "html":
        return HTMLDocument()
    else:
        raise ValueError("Invalid document type")


if __name__ == "__main__":
    pdf_doc = create_document("pdf")
    print(pdf_doc.create())  # Output: PDF Document created
