from tkinter.filedialog import Directory

from langchain_community.document_loaders import DirectoryLoader, PyPDFDirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path='../books',
    glob='**/*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()
print(docs[0].metadata);