# Trabalho de Redes
Este projeto demonstra a implementação de um sistema de chat simples usando sockets TCP/IP, com um servidor centralizado que gerencia a comunicação entre múltiplos clientes. A estrutura modular e o uso de threading garantem que o servidor possa escalar para suportar várias conexões simultâneas, enquanto os clientes podem enviar e receber mensagens em tempo real.

Projeto estruturado e implementado em: 

![Linguagem Utilizada](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

## Arquivo "server.py"

O arquivo **server.py** implementa um servidor de chat que permite a comunicação entre múltiplos clientes conectados.

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/e0f35835-2179-4564-8eca-0bd271c80168" width="400" >

* O método init inicializa o servidor, configurando o logger, o socket, e a lista de conexões ativas. Faz isso com ajuda de duas funções.
* **setup_socket** : cria um socket, configura-o para reutilizar o endereço, vincula-o ao endereço e porta fornecidos, e começa a escutar por conexões.
* **setup_logger** : cria e configura um logger que exibe mensagens no console com nível de debug.
  
<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/04fbd0ec-3626-4f9a-b877-4e8f9882503e" width="400" >

* O método run é o loop principal do servidor. Ele continuamente aceita novas conexões de clientes, adiciona cada nova conexão à lista de conexões ativas e utiliza um **_ThreadPoolExecutor_** para gerenciar as threads de cada conexão.

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/75648a3c-5da5-468c-8bef-d194bc80bbfa" width="400" >

* O método **relay_messages** recebe mensagens de um cliente e as repassa para todos os outros clientes conectados. Ele adiciona o endereço do remetente e um timestamp à mensagem antes de enviá-la. Se não houver dados recebidos (not data), o loop é interrompido.


## Arquivo "client.py"
O arquivo client.py contém a implementação do cliente de chat. Ele possui as seguintes funcionalidades:

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/35765b8e-1075-4ec1-8b8f-9213825f1f42" width="450" height="400" >

* A função send_message é executada em uma thread separada que permite ao usuário enviar mensagens para o servidor. As mensagens são codificadas em UTF-8.
* O método init configura o logger, estabelece a conexão com o servidor e inicia uma thread para o envio de mensagens. O método utiliza das funções abaixo para cumprir sua tarefa : 

<img src="https://github.com/guiosc/trabalho_redes/assets/102327512/af720052-34df-441b-be1d-f2297a658e10" width="400" >


* O setup_socket cria um socket, conecta-o ao servidor usando o endereço e a porta fornecidos, e retorna o socket configurado. 
* O setup_logger cria e configura um logger que exibe mensagens no console com nível de debug.

## Arquivo Dockerfile
Em nosso arquivo _Dockerfile_ ele cria uma imagem Docker pronta para executar um servidor Python.

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/dockerfile.png" width="400" >

* Primeiramente definimos a AMI (_python:3.11.5-alpine_) que será utilizada em nossa imagem.
* Atualizamos e instalamos dependências necessárias.
* Definimos o diretório de trabalho dentro do Container.
* Copiamos todos os arquivos da aplicação para o diretório de trabalho dentro do Container.
* A gente expõe a porta que o servidor usará.
* E demos o comando para rodar a aplicação.

Em resumo, esse Dockerfile cria uma imagem Docker pronta para executar um servidor Python com base na versão 3.11.5, usando o Alpine Linux como sistema operacional base. O servidor será executado no diretório /app e estará disponível na porta 4333.

## Arquivo Docker-compose
Em nosso arquivo _docker-compose_ fazemos a configuração para orquestrar múltiplos contêineres usando o Docker Compose.

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/docker_compose.png" width="400" >

* **version: '3'**: Define a versão do formato do arquivo do Docker Compose.
* **chat-server:**: É o nome do primeiro serviço. Ele será construído a partir do contexto atual (diretório local) usando as instruções definidas no Dockerfile. A porta 4333 do host será mapeada para a porta 4333 do contêiner.
* **netshoot:**: É o nome do segundo serviço. Ele usará uma imagem existente chamada nicolaka/netshoot. O modo de rede será definido como “service:chat-server”, o que significa que ele compartilhará a rede com o serviço chat-server. O comando ["tcpdump"] será executado dentro desse contêiner.

O método _tcpdump_ serve para rastrearmos o trafêgo de rede entre o servidor e o cliente.

## Logs do Trafêgo de Rede

### Servidor & Tcpdump rodando

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/log_server_running.png" width="1000" >

* *netshoot-1* está executando tcpdump, uma ferramenta de captura de pacotes de rede.

### Neighbor Solicitation:

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/log_ICMPv6_ARP.png" width="1000" >

* Capturas de pacotes ICMPv6, que são usados para comunicação de rede IPv6.
* Mensagens ARP (Address Resolution Protocol) que são usadas para mapear endereços IP para endereços MAC.
* Está perguntando "quem tem" (who has) o endereço IPv6 **fe80::42:74ff:fe16:63c0**.
* Comprimento do pacote é 32 bytes.

O servidor está enviando uma solicitação de vizinhança (neighbor solicitation) para descobrir o endereço MAC correspondente a um endereço IPv6 específico. Isso é comum quando um dispositivo está tentando verificar se outro dispositivo está presente na rede local ou tentando estabelecer uma comunicação.

### ARP Request & Reply
**ARP Request:** É uma **solicitação** ARP usada para descobrir o endereço MAC correspondente a um endereço IP.

* Está perguntando "quem tem" (who has) o endereço IP **172.20.0.1**.
* A solicitação foi feita pelo host com o endereço MAC **7d58a9879a12**.

**ARP Reply:** É uma **resposta** ARP indicando a correspondência entre o endereço IP e o endereço MAC.

* Informa que o endereço IP **172.20.0.1** está associado ao endereço MAC **02:42:74:16:63:c0**
* (oui Unknown) significa que o endereço MAC não pôde ser associado a um Organizationally Unique Identifier (OUI) conhecido.

### Conexão dos clientes

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/log_client.png" width="1000" >

Informa as novas conexões no servidor.

### Envio das mensagens

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/log_troca_mensagem.png" width="1000" >

* **Troca de dados**:
    * Os pacotes com a flag [P.] indicam que há dados sendo transferidos (35 bytes em cada caso).
    * As respostas com a flag [.] são ACKs, confirmando a recepção dos dados.
*  **Sincronização de Sequências e ACKs:**
    * As sequências e números de confirmação mostram que os dados estão sendo enviados e reconhecidos corretamente.
    * O primeiro pacote envia 35 bytes de dados (`seq 1:36`), e o segundo pacote confirma a recepção desses 35 bytes (`ack 36`).
* **Janela de Recepção:**
    * Os tamanhos da janela (win) são 510 e 512, indicando a capacidade de recepção de dados dos hosts.
* **Opções TCP:**
    * As opções `TS val` e `TS ecr` são usadas para marcação de tempo, ajudando a medir o tempo de ida e volta (RTT) e outras métricas de desempenho.

Os logs mostram uma troca de pacotes TCP normal entre dois endereços IP, com dados sendo enviados e recebidos corretamente. As confirmações (ACKs) estão alinhadas com os pacotes de dados enviados, e os valores de janela indicam uma comunicação estável entre os dois hosts.

### Exit

<img src="https://github.com/guiosc/trabalho_redes/blob/main/assets/log_exited.png" width="1000" >

* **Resumo da Captura de Pacotes:**
    * **93 pacotes capturados:** Estes são os pacotes que foram registrados durante a captura.
    * **95 pacotes recebidos pelo filtro:** Indica que o filtro configurado para a captura considerou 95 pacotes, mas apenas 93 foram realmente capturados e registrados.
    * **0 pacotes descartados pelo kernel:** Significa que nenhum pacote foi perdido devido a limitações do kernel durante a captura.
* **Finalização dos Contêineres:**
    * Ambos os contêineres (`netshoot-1` e `chat-server-1`) terminaram suas execuções sem erros, indicando que o teste ou processo de captura foi concluído com sucesso.

## Agradecimentos

Agradecemos por explorar este projeto de chat simples em Python. Esperamos que este código sirva como uma base sólida para entender a comunicação em rede usando sockets e inspire melhorias e novas funcionalidades.

## Integrantes 
Rafael Neiva

Guilherme Coelho

Redes de Computadores - Universidade Federal Fluminense

