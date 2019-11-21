import requests
import json
from termcolor import cprint
from pathlib import Path
import os


def console_check(csl, f):
    if csl == 'playstation-4':
        f.write('\tdbo:computingPlatform dbpedia:PlayStation_4.')
    if csl == 'playstation-3':
        f.write('\tdbo:computingPlatform dbpedia:PlayStation_3.')
    if csl == 'playstation-2':
        f.write('\tdbo:computingPlatform dbpedia:PlayStation_2.')
    if csl == 'playstation':
        f.write('\tdbo:computingPlatform dbpedia:PlayStation.')
    if csl == 'xbox-one':
        f.write('\tdbo:computingPlatform dbpedia:Xbox_One.')
    if csl == 'xbox-360':
        f.write('\tdbo:computingPlatform dbpedia:Xbox_360.')
    if csl == 'switch':
        f.write('\tdbo:computingPlatform dbpedia:Nintendo_Switch.')
    if csl == 'pc':
        f.write('\tdbo:computingPlatform dbpedia:Computer.')
        f.write('\n\n')


def initial_warnings():
    cprint("Esse programa funciona usando uma API chamada Chicken Coop API.", "red", attrs=['bold'])
    cprint("Essa API pega informações sobre jogos de determinados consoles.", "red", attrs=['bold'])
    cprint("Para que ela rode corretamente, siga as seguintes instruções:", "cyan", attrs=['bold'])
    cprint("Consoles:", 'yellow', attrs=['bold'])
    cprint("   Playstation 4 -> playstation-4", "green", attrs=['bold'])
    cprint("   Xbox One -> xbox-one", "green", attrs=['bold'])
    cprint("   Computador -> pc", "green", attrs=['bold'])
    cprint("   Nintendo Switch -> switch", "green", attrs=['bold'])
    cprint("Exemplos de jogos: ", 'yellow', attrs=['bold'])
    cprint("   Uncharted: The Lost Legacy", "green", attrs=['bold'])
    cprint("   God of War", "green", attrs=['bold'])
    cprint("   Ori and The Blind Forest", "green", attrs=['bold'])
    cprint("Aviso: Os jogos devem ser escritos com o nome exato e os consoles da maneira demonstrada,"
           " caso contrário, não funcionará!", 'magenta', attrs=['bold'])
    print("\n")


def get_and_write(mc, csl):
    print(f"Title: {mc['result']['title']}")
    print(f"Release Date: {mc['result']['releaseDate']}")
    # print(f"Description: {mc['result']['description']}")
    print(f"Score: {mc['result']['score']}")
    # print(f"Rating: {mc['result']['rating']}")
    print(f"Developer: {mc['result']['developer']}\n")
    mc_title = mc['result']['title']
    # mc_description = mc['result']['description']
    mc_score = mc['result']['score']
    mc_developer = mc['result']['developer']
    rsp = write_file(mc_title, mc_score, mc_developer, mc, csl)
    if rsp:
        write_file(mc_title, mc_score, mc_developer, mc, csl)


def write_file(title, score, developer, mc, csl):
    source = "<https://www.metacritic.com/game/"
    aux_title = ''
    source = source + csl + '/'
    path = Path('gamedeflib_rdf.ttl')
    if path.is_file() and os.stat('gamedeflib_rdf.ttl').st_size > 0:
        file = open('gamedeflib_rdf.ttl', 'r')
        count = 1
        for element in file:
            jogo = f'_:game{count}\n'
            if element == jogo:
                count = count + 1
        file.close()
        file = open('gamedeflib_rdf.ttl', 'a+')
        file.write(f'\n_:game{count}\n')
        file.write(f'\trdfs:label "{title}";\n')
        file.write(f'\tdbp:score {score};\n')
        genre_number(mc, file)
        publisher_number(mc, file)
        file.write(f'\tdbo:developer "{developer}";\n')
        aux_title = title.lower()
        aux_title = aux_title.replace(":", "")
        aux_title = aux_title.replace(" ", "-")
        source = source + aux_title + ">"
        file.write(f'\tdc:source {source};\n')
        console_check(csl, file)
        file.close()
    else:
        file = open('gamedeflib_rdf.ttl', 'w+')
        file.write("@prefix dc: 	<http://purl.org/dc/elements/1.1/> .\n")
        file.write("@prefix rdf:	<http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n")
        file.write("@prefix rdfs:	<http://www.w3.org/2000/01/rdf-schema#> .\n")
        file.write("@prefix foaf:	<http://xmlns.com/foaf/0.1/> .\n")
        file.write("@prefix dbo: <http://dbpedia.org/ontology/> .\n")
        file.write("@prefix dbpedia: <http://dbpedia.org/page/> .\n")
        file.write("@prefix dbp: <http://dbpedia.org/property/> .\n")
        file.write('dbpedia:PlayStation_4\n'
                   '\tfoaf:name "PlayStation 4";\n'
                   '\tdbo:type dbpedia:Home_video_game_console;\n'
                   '\trdfs:label "PlayStation 4".\n\n')
        file.write('dbpedia:PlayStation_3\n'
                   '\tdbo:type dbpedia:Home_video_game_console;\n'
                   '\trdfs:label "PlayStation 3".\n\n')
        file.write('dbpedia:PlayStation_2\n'
                   '\tdbo:type dbpedia:Home_video_game_console;\n'
                   '\trdfs:label "PlayStation 2".\n\n')
        file.write('dbpedia:PlayStation\n'
                   '\tdbp:type dbpedia:Video_game_console;\n'
                   '\trdfs:label "PlayStation".\n\n')
        file.write('dbpedia:XBox_One\n'
                   '\tfoaf:name "XBox One";\n'
                   '\tdbo:type dbpedia:Home_video_game_console;\n'
                   '\trdfs:label "XBox One" .\n\n')
        file.write('dbpedia:XBox_360\n'
                   '\tdbo:type dbpedia:Home_video_game_console;\n'
                   '\trdfs:label "XBox 360" .\n\n')
        file.write('dbpedia:Nintendo_Switch\n'
                   '\tfoaf:name "New Nintendank New Wii U 2.0+";\n'
                   '\tdbo:type dbpedia:Video_game_hardware;\n'
                   '\trdfs:label "Nintendo Switch" .\n\n')
        file.write('dbpedia:Computer\n'
                   '\tdbp:title "Computer";\n'
                   '\trdf:type dbo:Device;\n'
                   '\trdfs:label "Computer" .\n\n')
        return 1


def genre_number(mc, f):
    tam = len(mc['result']['genre'])
    for x in range(0, tam):
        print(f"Genre number {x+1}: {mc['result']['genre'][x]}")
        aux = mc['result']['genre'][x]
        f.write(f'\tdbo:genre "{aux}";\n')


def publisher_number(mc, f):
    tam = len(mc['result']['publisher'])
    for x in range(0, tam):
        print(f"Publisher number {x + 1}: {mc['result']['publisher'][x]}")
        aux = mc['result']['publisher'][x]
        f.write(f'\tdbo:publisher "{aux}";\n')


def main():
    print('Digite o console do jogo desejado: ', end='')
    console = str(input())
    print('Digite o título do jogo desejado: ', end='')
    title = str(input())
    try:
        url = "https://chicken-coop.p.rapidapi.com/games/"+title

        querystring = {"platform": console}

        headers = {
            'x-rapidapi-host': "chicken-coop.p.rapidapi.com",
            'x-rapidapi-key': "c3df04dcc0msh2d6e3cc8ccd93dep1c9851jsn230c81227b26"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        metacritic = json.loads(response.text)

        if metacritic['result'] == 'No result':
            print("\nAlguma informação digitada está incorreta. Tente novamente.")
        else:
            get_and_write(metacritic, console)

    except Exception as err:
        print("Algum erro desconhecido ocorreu durante a execucação.\nTente novamente.")
        cprint(err, 'red')


initial_warnings()
main()
while True:
    print('Gostaria de adicionar outro jogo na base RDF: (1 - Sim/0 - Não): ', end='')
    try:
        ans = int(input())
        if ans == 1:
            main()
        elif ans == 0:
            print('Encerrando o script')
            break
        else:
            print('Valor digitado deve ser 0 ou 1.')
    except ValueError as e:
        print('Valor foi inserido incorretamente. Tente denovo.')
        cprint(e, 'red')
