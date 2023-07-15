# Teste de Web Crawling - README

Este é o meu projeto de teste para avaliar minhas habilidades em web crawling e scraping. O objetivo deste programa é capturar uma lista de proxies a partir do site [freeproxylists.net](http://www.freeproxylists.net), realizar o parser dos dados e salvá-los em um arquivo JSON. Além disso, o programa imprime a quantidade de proxies capturados e o tempo de execução.

## Instruções de Instalação

Para executar este projeto em seu ambiente local, siga as instruções abaixo:

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Clone este repositório em sua máquina.
3. Navegue até o diretório do projeto.

## Dependências

Este projeto requer a instalação das seguintes bibliotecas Python:

- requests
- beautifulsoup4

Você pode instalar as dependências manualmente ou utilizando o arquivo `requirements.txt`. Para instalar as dependências manualmente, execute os seguintes comandos no terminal:

pip install requests
pip install beautifulsoup4

Para instalar as dependências utilizando o arquivo `requirements.txt`, execute o seguinte comando no terminal:

pip install -r requirements.txt

## Execução

Para executar o programa, siga as etapas abaixo:

1. Navegue até o diretório do projeto no terminal.
2. Execute o seguinte comando:

web_crawling_test.py

O programa irá acessar o site [freeproxylists.net](http://www.freeproxylists.net) e capturar a lista de proxies até a página 7. Os dados serão parseados e salvos em um arquivo JSON. Em seguida, a quantidade de proxies capturados e o tempo de execução serão exibidos no console.

## Considerações sobre Segurança em Web Crawling

Ao lidar com web crawling, é importante considerar questões de segurança e ética. Para evitar bloqueios por tecnologias de segurança, como captchas e regras de firewalls, é possível adotar as seguintes medidas:

- Respeite os Termos de Serviço: Sempre leia e respeite os termos de serviço do site que você está rastreando. Entenda quais são as regras e políticas estabelecidas e siga-as.
- Siga as Diretrizes do robots.txt: Verifique se o site alvo possui um arquivo robots.txt que especifica as áreas que não devem ser rastreadas por um crawler. Respeite essas diretrizes para evitar bloqueios e problemas legais.
- Controle a Taxa de Requisições: Evite fazer muitas requisições em um curto período de tempo. Limite a taxa de requisições para não sobrecarregar o servidor e evitar ser identificado como um comportamento suspeito.
- Utilize Proxies e IPs Rotativos: O uso de proxies e a rotação de IPs podem ajudar a evitar o bloqueio por IP. Ao usar proxies, é possível mascarar o endereço IP do crawler e evitar bloqueios em larga escala.
- Trate Captchas e Soluções Anti-Bot: Em casos em que captchas ou soluções anti-bot são implementados, é necessário utilizar técnicas para resolver automaticamente os captchas ou contornar essas solu
- Seja Ético e Transparente: Forneça informações de contato adequadas, como um endereço de e-mail válido, para que os proprietários do site possam entrar em contato caso necessário. Esteja disposto a responder a solicitações de remoção de dados ou fornecer informações sobre o propósito do seu crawler.

Lembre-se sempre de seguir as diretrizes legais e éticas ao realizar web crawling. Respeite os direitos dos proprietários dos dados e esteja ciente das políticas dos sites que você está acessando.