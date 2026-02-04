
from torch import embedding
from langchain_astradb import AstraDBVectorStore

from langchain_huggingface import HuggingFaceEndpointEmbeddings #HuggingFaceEmbeddings

from flipKart.data_converter import DataConverter

from flipKart.config import Config as cfg

class DataIngestor:
    def __init__(self):
        
        self.embedding = HuggingFaceEndpointEmbeddings(model=cfg.EMBEDDING_MODEL)

        self.vstore = AstraDBVectorStore(embedding=self.embedding, 
                                         collection_name="flipKart_db",
                                         api_endpoint = cfg.ASTRA_DB_API_ENDPOINT,
                                         token= cfg.ASTRA_DB_APPLICATION_TOKEN,
                                         namespace = cfg.ASTRA_DB_KEYSPACE

                                         )
    def ingest(self, load_existing=True):
        if load_existing == True:
            self.vstore
        docs = DataConverter(cfg.data_path).convert()

        lengths = [len(doc.page_content.split()) for doc in docs]
        avg_len = sum(lengths) / len(lengths)
        print(f"Average words per chunk:{avg_len} for {sum(lengths)} words in {len(lengths)} chunks.")
        
        
        
        BATCH_SIZE = 16 

        for i in range(0, len(docs), BATCH_SIZE):
            batch = docs[i:i + BATCH_SIZE]
            self.vstore.add_documents(batch)

        return self.vstore
    
if __name__ == "__main__":
    ingestor = DataIngestor()
    ingestor.ingest(load_existing=False)