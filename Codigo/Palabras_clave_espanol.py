import nltk
from math import sqrt
import spacy
from string import punctuation
import networkx as nx
from collections import Counter
from itertools import combinations
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


#español/ingles/aleman

nlp = spacy.load('es_core_news_sm')




def textrank(text):
    window_size=5   
    promedio_importantes = int(sqrt(len(text)))
    # Preprocesamiento
    stop_words = set(stopwords.words('spanish'))
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    filtered_words = [word for word in words if word not in stop_words]

    # Construcción del grafo
    graph = nx.Graph()
    graph.add_nodes_from(filtered_words)

    # Añadir aristas basadas en co-ocurrencias
    for i in range(len(filtered_words) - window_size):
        window = filtered_words[i:i + window_size]
        for pair in combinations(window, 2):
            if graph.has_edge(*pair):
                graph[pair[0]][pair[1]]['weight'] += 1
            else:
                graph.add_edge(pair[0], pair[1], weight=1)

    # Aplicar el algoritmo PageRank
    scores = nx.pagerank(graph, weight='weight')

    # Ordenar las palabras por puntuación
    ranked_words = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    

    # Devolver las palabras clave más importantes
    return [word for word, _ in ranked_words[:promedio_importantes]]

# Ejemplo de uso


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

def textenizar(lista):
    retorno = ""
    for palabra in lista:
        retorno+=palabra + " "
    return retorno

texto = """Las nadadoras estallan, Estados Unidos da un giro drástico a sus normas y España organiza un Foro Internacional para vetar a las atletas trans en el deporte femenino, El terremoto Lía Thomas no amaina. Las consecuencias que la participación de atletas trans tiene para el deporte femenino sigue siendo objeto de debate en Estados Unidos y en el resto del mundo. Lia Thomas, la nadadora transgénero de 22 años que ha batido todos los récords de mujeres en la Universidad de Pensilvania (Penn) mantiene en pie de guerra al mundo del deporte. Antes de realizar su transición compitió durante tres años como hombre, con el nombre de Will Thomas. Si como hombre era mediocre, ahora bate todos los récord en estilo libre 200 metros y estilo libre 500 metros. Hace unos días, 16 miembros del equipo femenino de natación de la Universidad de Pensilvania enviaron una carta a la escuela y a las autoridades de la Ivy League en contra de la participación de su compañera de equipo transgénero Lia Thomas y ahora siguen denunciando lo que supone para ellas compartir competición con la polémica nadadora. La carta fue redactada por Nancy Hogshead-Makar, ex nadadora olímpica y dice que lo hace en nombre de 16 nadadoras de Pennsylvania, que no han querido, por miedo dar su nombre.Temen represalias. Hogshead-Makar asegura que quería ayudar a las nadadoras a contar lo que según ellas, no pueden decir públicamente por lo que pueda pasar. “Lo que más les preocupa es que la dirección se centre en Lia y no en los otros 40 miembros del equipo”, dijo. “Les han dicho que si hablan nunca tendrán trabajo, la gente verá su nombre en Internet y dirá: transfóbica, no la queremos”, denuncia Nancy Hogshead.El horror del vestuario Pero además, ahora han filtrado la incomodidad que sienten en el vestuario:“No siempre se cubre sus genitales masculinos cuando se cambia, estas preocupaciones son ignoradas por los entrenadores”. “Cuando los funcionarios permiten que Lia Thomas exponga sus genitales masculinos a mujeres en el vestuario se viola el Código 3127 de Pensilvania y el Título IX de Acoso Sexual” afirman las compañeras de Lía. La polémica es tal que hasta el mejor nadador de todos los tiempos, Michael Phelps, se atrevió a calificar esta situación como algo similar al dopaje: “Todos deberíamos sentirnos cómodos con quienes somos en nuestra propia piel, pero creo que todos los deportes deberían jugarse en igualdad de condiciones para que haya justicia. Este es mi deporte, este ha sido mi deporte durante toda mi carrera y, sinceramente, lo único que me encantaría es que todos pudieran competir en igualdad de condiciones”, sentenció. Ante el tsunami de denuncias, la federación estadounidense de natación, USA Swimming, se ha visto obligada a tomar medidas para atajar la polémica suscitada por la nadadora trans Lia Thomas y ha anunciado un cambio en sus reglas. En las pruebas de nivel élite, deben acreditar que «su desarrollo físico previo, como hombre, y aunque mitigado por alguna intervención médica, no le otorga ventaja competitiva sobre sus rivales». Además, también piden controles más periódicos y duraderos, teniendo que demostrar que la concentración de testosterona «ha estado por debajo de 5 nanomoles por litro de forma continua durante un periodo de al menos 36 meses antes de la fecha de la solicitud». La federación de natación detectó en su análisis que “la mujer mejor clasificada en 2021, en promedio, estaría clasificada en el puesto 536 en todos los eventos masculinos de piscina corta en el país”, por lo que decidió tomar medidas al respecto y endurecer los criterios para cambiar de disciplina. Esto podría hacer que Lia Thomas se quedara fuera de próximas competiciones. Foro internacional impulsado por España Pero el debate traspasa fronteras y en España no se han quedado al margen creando un foro que han bautizado como Conferencia Internacional en Defensa de las Categorías Deportivas Femeninas para evitar que deportistas ‘trans’ compitan en esta categoría. Entre las entidades promotoras de la iniciativa, figuran la Asociación de Futbolistas Españoles, la Real Federación Española de Atletismo, la Asociación de Mujeres para el Deporte Profesional (AMDP), la Federación Española de Tiro con Arco y otras plataformas como la Alianza Contra el Borrado de la Mujer (CBM), que aglutina a un centenar de organizaciones feministas. También participarán organizaciones de Reino Unido, Canadá y EEUU como Fair Play For Women y Save Women´s Sports. “El incremento a nivel internacional de la participación de varones autoidentificados como “mujeres trans” en competiciones femeninas es una tendencia que se ha pretendido consolidar y normalizar en las OLIMPIADAS DE TOKIO 2021. Estamos observando cómo podios femeninos en competiciones de todo el mundo están siendo copados por personas con cromosomas XY, dejando a las mujeres en una posición de imposibilidad de competir en igualdad de condiciones”, afirman desde la plataforma “contra el Borrado de las Mujeres”, promotora del Foro que se celebra el próximo 19 de Febrero. ¿Y qué pasa con la nueva Ley del Deporte? Asimismo, denuncian que el texto conocido de la nueva Ley del Deporte, perjudica a las mujeres deportistas cuando permite la participación de personas transfemeninas y transgénero en las categorías femeninas. “A esto se suma una nueva norma, ya aprobada en el Consejo de Ministros, que admite que cualquier persona pueda cambiar su sexo registral sin tener que obtener un diagnóstico médico de disforia. Todo esto abre la puerta a la participación de nacidos varones en competiciones deportivas femeninas, dando pie a que el deporte femenino sea copado por personas con ventaja competitiva sobre las deportistas. Si se elimina el sexo para establecer las categorías deportivas, las mujeres desaparecerán de gran parte del deporte. Es dopaje de género”, sentencian."""

palabras_clave = get_importantes(texto)

palabras = textenizar(palabras_clave)

final = textrank(palabras)
print(final)