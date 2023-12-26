# Azure Event Hub
Neste repositório, exploramos o Azure Event Hub, criando um script chamado Event Producer. Este script simula um produtor de eventos, essencial para a configuração do laboratório na plataforma Azure para o nosso estudo. Além disso, foi desenvolvido script do Event Consumer que recebe os eventos e faz a ingestão no datalake, utilizando o Azure Storage Gen2 para armazenar os eventos gerados.

O objetivo principal é estudar e aprimorar a compreensão do Azure Event Hub e outras serviços como o Azure Stream Analytics, proporcionando uma abordagem prática por meio da simulação de produção e consumo de eventos. A escolha do Azure Storage Gen2 como Data Lake oferece uma solução robusta para armazenar os eventos gerados, contribuindo para uma implementação eficiente e escalável do sistema.

Este repositório serve como um guia prático e educativo para explorar as capacidades do Azure Event Hub e demonstra como integrar componentes essenciais, como o EventProducer e o Event Consumer, em um ambiente de local ou nuvem utilizando python.

## Projeto técnico
Requisitos funcional: Controlar a temperatura em tempo real de uma câmara fria

1) Criar um EventHub
2) Conectar o EventHub com o Datalake
3) Criar o Azure Stream Analytics para analisar os dados do EventHub
4) Construir o App (script) para simular os eventos
	1) Construir uma aplicação: Event Producer
	2) Construir uma que trabalhará com o Event Consumer
5) Testar a solução completa e conectar ao Power BI 

--

1) Conectar ao EventHub com as credenciais do Azure Namespace
2) Criar um EventHubProducerClient utilizando python
3) Enviar uma mensagem para o EventHub

1) Criar storage account: DataLakeStorageGen2 (Habilitar Hierarchical namespace = DataLake)
2) Ingestão de dados do eventhub para o DataLake
3) Criar um EventHubConsumerClient utilizando python


## Referências
[Event Hub connection with python](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send?tabs=connection-string%2Croles-azure-portal)
<br>
[azure-eventhub](https://pypi.org/project/azure-eventhub/)
<br>
[azure-identity](https://pypi.org/project/azure-identity/)
<br>
[AIOHTTP](https://pypi.org/project/aiohttp/)
<br>
[Repository Azure Github](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/eventhub)