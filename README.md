# Trabalho de Redes
Este projeto demonstra a implementação de um sistema de chat simples usando sockets TCP/IP, com um servidor centralizado que gerencia a comunicação entre múltiplos clientes. A estrutura modular e o uso de threading garantem que o servidor possa escalar para suportar várias conexões simultâneas, enquanto os clientes podem enviar e receber mensagens em tempo real.

Projeto estruturado e implementado em: 

![Linguagem Utilizada](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

## Arquivo "client.py"
O arquivo client.py contém a implementação do cliente de chat. Ele possui as seguintes funcionalidades:

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/35765b8e-1075-4ec1-8b8f-9213825f1f42" width="450" height="400" >

A função send_message é executada em uma thread separada que permite ao usuário enviar mensagens para o servidor. As mensagens são codificadas em UTF-8.
O método init configura o logger, estabelece a conexão com o servidor e inicia uma thread para o envio de mensagens. O método utiliza das funções abaixo para cumprir sua tarefa : 

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/af720052-34df-441b-be1d-f2297a658e10" width="400" >


O setup_socket cria um socket, conecta-o ao servidor usando o endereço e a porta fornecidos, e retorna o socket configurado. O setup_logger cria e configura um logger que exibe mensagens no console com nível de debug.

## Arquivo "server.py"

O arquivo server.py implementa um servidor de chat que permite a comunicação entre múltiplos clientes conectados.

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/e0f35835-2179-4564-8eca-0bd271c80168" width="400" >

O método init inicializa o servidor, configurando o logger, o socket, e a lista de conexões ativas. Faz isso com ajuda de duas funções.

- setup_socket : cria um socket, configura-o para reutilizar o endereço, vincula-o ao endereço e porta fornecidos, e começa a escutar por conexões.

- setup_logger : cria e configura um logger que exibe mensagens no console com nível de debug.
  
<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/04fbd0ec-3626-4f9a-b877-4e8f9882503e" width="400" >

O método run é o loop principal do servidor. Ele continuamente aceita novas conexões de clientes, adiciona cada nova conexão à lista de conexões ativas e utiliza um ThreadPoolExecutor para gerenciar as threads de cada conexão.

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/75648a3c-5da5-468c-8bef-d194bc80bbfa" width="400" >

O método relay_messages recebe mensagens de um cliente e as repassa para todos os outros clientes conectados. Ele adiciona o endereço do remetente e um timestamp à mensagem antes de enviá-la. Se não houver dados recebidos (not data), o loop é interrompido.

## Agradecimentos

Agradecemos por explorar este projeto de chat simples em Python. Esperamos que este código sirva como uma base sólida para entender a comunicação em rede usando sockets e inspire melhorias e novas funcionalidades.

## Integrantes 
Rafael Neiva

Guilherme Coelho

Redes de Computadores - Universidade Federal Fluminense

