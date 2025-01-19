import spacy
from spacy.matcher import Matcher
import boto3

# Carregando o modelo do Spacy para português
nlp = spacy.load("pt_core_news_sm")  # ou "pt_core_news_lg" se disponível

def read_s3_file(bucket_name, file_key, aws_access_key_id, aws_secret_access_key):
    """
    Lê um arquivo do bucket S3 e retorna seu conteúdo como uma string.
    """
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = obj['Body'].read()
    return body.decode('utf-8')

# Função para extrair proposições relacionadas às palavras-chave
def extract_kpi_sentences(text, keywords):
    doc = nlp(text)
    sentences = []
    for sentence in doc.sents:
        for keyword in keywords:
            if keyword in sentence.text:
                sentences.append(sentence.text)
                break
    return sentences

    def find_keywords_in_text(self, text, keywords):
        """
        Busca por palavras-chave no texto e conta as ocorrências.
        """
        doc = self.nlp(text.lower())
        lemma_keywords = [self.nlp(keyword)[0].lemma_ for keyword in keywords]
        matcher = Matcher(self.nlp.vocab)
        
        for lemma_keyword in lemma_keywords:
            matcher.add("KeywordMatcher", [[{"LEMMA": lemma_keyword}]])
        
        matches = matcher(doc)
        keywords_found = {keyword: 0 for keyword in keywords}
        
        for match_id, start, end in matches:
            match_text = doc[start:end].text
            for keyword in keywords:
                if match_text in keyword:
                    keywords_found[keyword] += 1
        
        return keywords_found

    def process_file_from_s3(self, bucket_name, file_key, aws_access_key_id, aws_secret_access_key, keywords):
        """
        Processa um arquivo de texto do S3, buscando por palavras-chave.
        """
        text = self.read_s3_file(bucket_name, file_key, aws_access_key_id, aws_secret_access_key)
        keywords_found = self.find_keywords_in_text(text, keywords)
        for keyword, count in keywords_found.items():
            print(f"'{keyword}': {count} ocorrências")
        
if __name__ == "__main__":
    aws_access_key_id = 'aws_access_key_id'
    aws_secret_access_key = 'aws_secret_access_key'
    bucket_name = 'bucket_name'
    file_key = 'file_key'
    
    # Palavras-chave desejadas
    keywords = ['lucro', 'dividendo', 'investimento']
    
    # Leitura do arquivo S3
    text = read_s3_file(bucket_name, file_key, aws_access_key_id, aws_secret_access_key)
    
    # Extração e impressão de sentenças relevantes
    relevant_sentences = extract_kpi_sentences(text, keywords)
    for sentence in relevant_sentences:
        print(sentence)


# In[ ]:


