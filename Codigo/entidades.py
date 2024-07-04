import spacy
from collections import Counter
from string import punctuation
import PyPDF2
import os
import spacy.displacy as dis

ruta_datos = os.path.join(os.path.dirname(__file__),'Datos')

pdf = os.path.join(ruta_datos,'CAF 001732_2016_1_CS001.pdf')

def sacarTexto(ruta):
    with open(ruta, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        texto = ""

        for page_num in range(len(pdf_reader.pages)):
            page =  pdf_reader._get_page(page_num)
            texto += page.extract_text()
    return texto
texto = sacarTexto(pdf)

nlp = spacy.load('es_core_news_sm')


#doc = nlp(texto)

#dis.serve(doc)

#entidades =[doc.ents]

#subj = [token.text for token in doc if token.dep_ == 'nsubj']

#sustantivos = [token.text for token in doc if token.pos_ == 'NOUN']
#print(sustantivos)


def get_importantes(text):
    resultado = []
    pos_tag = ['ENT','NSUBJ','PROPN','ADJ','NOUN']
    doc = nlp(text.lower())
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            resultado.append(token.text)
    return resultado

importantes = get_importantes(texto)

print(importantes)