# gamedeflib-websem
Título do Projeto: Game Definition Library

Autor: Vinícius Vilas Boas

Fonte de Dados: A API Chicken Coop que usa dados da Metacritic

Erreideficação:
  O processo de erreideificação foi, na maior parte do tempo, um processo de leitura de documentação de padrões, sites com as informações necessário que, no caso, são o Metacritic e DBPedia, e aprendizado do uso da API em questão.
  A Chicken Coop API pede por quatro coisas:
  1 e 2: No cabeçalho do request o link do servidor da api e a minha chave de usuário
  3 e 4: Console e título do jogo desejado
  O request devolvia pra mim, um JSon, que foi lido com facilidade usando apenas simples laços de repetição para ver o conteúdo e depois "puxando" o que eu precisava.
  Depois disso, foi necessário entender o formato turtle (namespaces, namespaces anônimos, propriedades, etc). Após ter corrigido meus erros na confecção manual do arquivo RDF, com a ajuda do meu Professor Ivan R. eu criei um sistema automatizado para criá-lo, usando as seguintes bibliotecas:
  - Built-in: 
      - pathlib (função "Path()"): faz pathing de arquivos, verifica se eles existem, se é de algum tipo específico, etc;
      - os: funções para mexer com "atributos" do sistema operacional (tamanho de arquivo, diretório, etc);
      - json (função ".loads()"): carrega as informações do texto json em forma de listas encadeadas de strings.
  - Built-out:
      - requests (função ".request(Protocolo PHP, url, headers, param)" e ".text" para transformar a informação em texto): possui diversas funções para puxar informações de URLs que o usuário passa, como o HTML do site ou algum arquivo em um link;
      - termcolor (função "cprint("texto", cor, marcador, parâmetros de texto)"): termcolor é uma biblioteca para colorir o texto dentro da função "print()". É possível mudar a cor da fonte, a cor do fundo da fonte e características da fonte (deixar em negrito, mudar a fonte, etc).
      - rdflib (funções "Graph", "Literal" e "query"):
  Utilizando essas bibliotecas específicas e as funções built-in do tipo "file" foi possível salvar toda a informação em um arquivo de texto. Não foi necessário fazer um arquivo do tipo ".txt" e depois converter para o tipo ".ttl". A própria IDE pergunta se ela pode abrir a extensão ".ttl" como se fosse um ".txt", então não ocorreram problemas. O código, bascicamente, escreve um padrão onde, dentro dele, existem lacunas que são completas pelos resultados que podem ser obtidos com a API. Antes disso ele faz uma verificação checando se o arquivo existe e não está vazio. Se está, faz o cabeçalho com os prefixo e começa a salvar, caso contrário, só começa a salvar. Ele também verifica quantos jogos existem salvos para não errar no identificador numérico.
  No vocabulário usado, existem as seguintes coisas:
    - DBPedia:
      - "@prefix dc: 	<http://purl.org/dc/elements/1.1/>" -> Namespace que faz referência ao sistema de padronização de metadados Dublin Core. Foi usado apenas para especificar a propriedade "source" que faz referência ao site do metacritic que possui as informações do jogo ;
      - "@prefix rdf:	<http://www.w3.org/1999/02/22-rdf-syntax-ns#>" -> Namespace que descreve instanciação de classes. Não foi utilizado, mas foi deixado por precaução;
      - "@prefix rdfs:	<http://www.w3.org/2000/01/rdf-schema#>" -> Namespace que descreve ou define uma classe. Com esse prefixo foram utilizadas as seguintes propriedades: label (para dar uma "etiqueta", nome, título, etc)
      - "@prefix foaf:	<http://xmlns.com/foaf/0.1/>" -> Namespace que agrupa objetos de um mesmo tipo. Por exemplo, todas as pessoas que pertencem a Europa participam de um mesmo grupo com essa característica em comum. Cada pessoa possui características únicas mas podem todas serem encontradas pela característica em comum descrita pelo foaf. Com esse prefixo foram utilizadas as seguintes propriedades: name (para descrever o nome de 3 consoles) ;
      - "@prefix dbo: <http://dbpedia.org/ontology/>" -> Namespace que faz referência a página de ontologia ("ontology") da DBPedia. Ontologia, nesse caso, representa um conjunto de dados e como eles se relacionam. Com esse prefixo foram utilizadas as seguintes propriedades: type (para descrever o tipo dos consoles), genre (genêro dos jogos), publisher (distribuidoras), developer (desenvolvedora), computingPlatform (plataforma de computação);
      - "@prefix dbpedia: <http://dbpedia.org/page/>" -> Namespace que faz referência as páginas de objetos (sujeitos) específicos. Com esse prefixo foram utilizadas as seguintes propriedades: Nintendo_Switch, Playstation, Playstation_2, Playstation_3, Playstation_4, Xbox_One, Xbox_360, Computer, Home_video_game_console e Video_game_hardware;
      - "@prefix dbp: <http://dbpedia.org/property/>" -> Namespace que faz referência as página de propriedades específicas da dbpedia. Com esse prefixo foram utilizadas as seguintes propriedades: title (para Computer) e score (para a nota dos jogos);
      - O termo local criado foi "jogo#" onde "#" representa a posição do jogo na lista. Fora isso, foi usado namespace anônimos (blanko nodes) para os jogos.
      
