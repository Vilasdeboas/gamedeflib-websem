from rdflib import Graph, Literal

g = Graph()

filename = 'websem.ttl'

g.parse(filename, format='turtle')

g.bind('dbp', 'http://dbpedia.org/property/#')
g.bind('dbo', 'http://dbpedia.org/ontology/#')
g.bind('dbpedia', 'http://dbpedia.org/page/')
g.bind('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')

print('Escolha entre as duas opções (1 ou 2):')
print('1 - Digite o valor de uma nota entre 0 a 100.'
      ' O SPARQL mostrará apenas as os jogos e seus publicadores de acordo com as notas maiores ou iguais '
      'ao valor escolhido (ordem ascendente).')
print('2 - Ordena da maior para a menor nota dentre os jogos existentes (ordem descendente).')
print('3 - Ordena da menor para a maior nota dentre os jogos existentes (ordem ascendente).')
print('4 - Mostra os gêneros na ordem alfabética e seus respectivos títulos')
print('Opção: ', end='')
rsp = int(input())
if rsp == 1:
    try:
        print('Valor: ', end='')
        x = int(input())
        if 0 > x or x > 100:
            print('Valor não está entre 0 e 100.')
        else:
            disc = Literal(x)

            query = """SELECT ?x ?z WHERE{
                        ?r dbp:score ?y .
                        ?r dbo:publisher ?z .
                        ?r rdfs:label ?x
                        FILTER(?y >= ?w)}
                        ORDER BY ASC(?x)"""

            ans = g.query(query, initBindings={'w': disc})

            for stmt in ans:
                print(f"Título: %s - Distribuidora: %s" % stmt)
    except ValueError as e:
        print('Valor incorreto.')
        print(e)
if rsp == 2:
    try:
        query = """SELECT ?x ?y WHERE{
                    ?r dbp:score ?y .
                    ?r rdfs:label ?x}
                    ORDER BY DESC(?y)"""

        ans = g.query(query)

        for stmt in ans:
            print(f"Título: %s - Nota: %s" % stmt)

    except Exception as e:
        print('Algo deu errado.')
        print(e)
if rsp == 3:
    try:
        query = """SELECT ?x ?y WHERE{
                    ?r dbp:score ?y .
                    ?r rdfs:label ?x}
                    ORDER BY ASC(?y)"""

        ans = g.query(query)

        for stmt in ans:
            print(f"Gênero: %s - Título: %s" % stmt)

    except Exception as e:
        print('Algo deu errado.')
        print(e)
if rsp == 4:
    try:
        query = """SELECT ?x ?y WHERE{
                    ?r dbo:genre ?x .
                    ?r rdfs:label ?y}
                    ORDER BY ASC(?x)"""

        ans = g.query(query)

        for stmt in ans:
            print(f"Título: %s - Nota: %s" % stmt)

    except Exception as e:
        print('Algo deu errado.')
        print(e)
