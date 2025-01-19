import spacy
import boto3
# Função para ler arquivo do S3
def read_s3_file(bucket_name, file_key, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = obj['Body'].read()
    return body.decode('utf-8')
# Função para extrair sentenças e contar palavras-chave
def extract_and_count_keywords(text, keywords):
    nlp = spacy.load("pt_core_news_sm")  # Carrega o modelo do Spacy para português
    doc = nlp(text)
    sentences = []
    keyword_counts = {keyword: 0 for keyword in keywords}  # Inicializa contadores para cada palavra-chave
    for sentence in doc.sents:
        sentence_has_keyword = False
        for keyword in keywords:
            if keyword in sentence.text.lower():  # Checa se a palavra-chave está na sentença
                sentence_has_keyword = True
                keyword_counts[keyword] += sentence.text.lower().count(keyword)  # Incrementa o contador
        if sentence_has_keyword:
            sentences.append(sentence.text)
    return sentences, keyword_counts
if __name__ == "__main__":
    aws_access_key_id = 'aws_access_key_id'
    aws_secret_access_key = 'aws_secret_access_key'
    bucket_name = 'bucket_name'
    file_key = 'file_key'
    keywords = ['lucro', 'dividendo', 'investimento']  # Palavras-chave desejadas
    
    # Leitura do arquivo S3
    text = read_s3_file(bucket_name, file_key, aws_access_key_id, aws_secret_access_key)
    
    # Extrai sentenças e conta as palavras-chave
    relevant_sentences, keyword_counts = extract_and_count_keywords(text, keywords)
    
    # Imprime resultados
    print("Sentenças relevantes:")
    for sentence in relevant_sentences:
        print(sentence)
    
    print("\nContagem das palavras-chave:")
    for keyword, count in keyword_counts.items():
        print(f"'{keyword}': {count} ocorrências")
# In[5]:
if __name__ == "__main__":
    import spacy
    nlp = spacy_stanza.load_pipeline("pt")
    nlp.add_pipe("openie")
    text = [
        "O lucro do terceiro trimestre da empresa Ambev, foi 7% inferior ao trimestre anterior",
        ]
    with open('out.txt', 'w') as output:
        for s in text:
            doc = nlp(s)
            #explacy.print_parse_info(nlp, s)
            output.write(s + '\n')
            for prop in doc._.clauses:
                output.write('\t' + str(prop.to_propositions(inflect=None)) + '\n')
        output.close()
# In[8]:
from transformers import AutoModel, AutoTokenizer
# Using the community model
# BERT Base
tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')
model = AutoModel.from_pretrained('neuralmind/bert-base-portuguese-cased')
# BERT Large
tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-large-portuguese-cased')
model = AutoModel.from_pretrained('neuralmind/bert-large-portuguese-cased')
# or, using BertModel and BertTokenizer directly
from transformers import BertModel, BertTokenizer
tokenizer = BertTokenizer.from_pretrained('path/to/vocab.txt', do_lower_case=False)
model = BertModel.from_pretrained('path/to/bert_dir')  # Or other BERT model class
