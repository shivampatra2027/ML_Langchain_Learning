from langchain_community.document_loaders import CSVLoader

loader=CSVLoader('random_sample_data.csv')
docs=loader.load();
print(docs[0].metadata);