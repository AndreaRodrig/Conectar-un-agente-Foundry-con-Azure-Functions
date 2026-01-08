# Conectar-un-agente-Foundry-con-Azure-Functions

Este proyecto muestra cómo conectar un agente de Azure AI Foundry con Azure Functions para obtener datos de compras de clientes en tiempo real.

## Requisitos

- Python 3.12+
- Azure Functions Core Tools v4
- Visual Studio Code con extensión Azure Functions
- Azure Subscription

## Instalación local

1. Clonar repositorio:

git clone https://github.com/tuusuario/ChatBotLaMarina.git
cd ChatBotLaMarina

2. Crear y activar entorno virtual:
python3 -m venv .venv
source .venv/bin/activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar Function localmente:
func start

5. Probar endpoint:
curl "https://apichatbot-csawevcnhthfduer.canadacentral-01.azurewebsites.net/api/cliente/compras?id=YOUR_CLIENT_ID&code=YOUR_FUNCTION_KEY"

## Publicación en Azure

1. Crear Function App en Azure Portal (Python 3.12)
2. Publicar desde VS Code:
func azure functionapp publish ApiChatBot

3. Obtener URL y Function Key en Azure Portal.

## Conexión con Foundry

1. Agregar acción Azure Function en Foundry.
2. Configurar URL de la Function y la clave.
3. Enviar parámetro id para obtener compras de cliente.

