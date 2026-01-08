# Conectar un agente Azure AI Foundry con Azure Functions

Este repositorio muestra cómo crear y conectar un agente de Azure AI Foundry con Azure Functions para obtener datos en tiempo real de manera segura y escalable.

## Resumen del flujo
Función HTTP en Azure Functions

Crea un endpoint HTTP que devuelve información, por ejemplo, compras de clientes.
Permite a Foundry obtener datos dinámicos en tiempo real.
No almacena credenciales sensibles en el código; se usan claves de Function o identidades administradas.

Agente Azure AI Foundry

Se configura como asistente conversacional.
Usa acciones para conectarse a funciones de Azure y obtener datos.
La función se agrega como acción de tipo “Azure Function”, no como conocimiento estático.

## Pasos realizados para implementar la conexión
1️⃣ Preparar el entorno local
Instalar Python 3.12+
Instalar Visual Studio Code y extensiones:
Python
Azure Functions
REST Client (opcional para pruebas)
Instalar Azure CLI:
brew install azure-cli
az login
Instalar Azure Functions Core Tools v4:
brew tap azure/functions
brew install azure-functions-core-tools@4
Crear entorno virtual y activar:
python3 -m venv .venv
source .venv/bin/activate
Instalar dependencias:
pip install -r requirements.txt

2️⃣ Crear la Function App
En Visual Studio Code:
F1 → Azure Functions: Create New Project
Lenguaje: Python
Tipo de trigger: HTTP trigger
Nombre del endpoint: get_compras

Archivo requirements.txt:
azure-functions==1.24.0
werkzeug==3.1.4
Archivo .gitignore:
.venv/
__pycache__/
local.settings.json
*.pyc

3️⃣ Probar la función localmente
Iniciar la Function local:
func start
Probar endpoint:
curl "https://apichatbot-csawevcnhthfduer.canadacentral-01.azurewebsites.net/api/cliente/compras?id=123&code=YOUR_FUNCTION_KEY"
Respuesta esperada:
{"clienteId": "123", "compras": [{"fecha": "2024-10-01", "total": 950, "estado": "Entregado"}, {"fecha": "2024-10-10", "total": 120, "estado": "Enviado"}]}


4️⃣ Publicar la Function en Azure

Crear Function App en Azure Portal (Python 3.12, Plan de Consumo).
Publicar desde VS Code o CLI:
func azure functionapp publish ApiChatBot
Obtener la URL pública y la Function Key desde Azure Portal.

5️⃣ Conectar el agente en Azure AI Foundry
Ir a Actions / Tools → Add Action → Azure Function
Configurar:
URL de tu Function publicada
Clave de Function
Probar acción enviando un parámetro id y recibir la respuesta de tu API.
⚠️ Nota: No se agrega como conocimiento estático, porque tu API devuelve datos dinámicos en tiempo real. Se agrega como acción que el agente puede ejecutar bajo demanda.

6️⃣ Comprobación
Desde Foundry, el agente puede ejecutar la acción:
{
  "id": "123"
}
Respuesta:
{"clienteId": "123", "compras":[{"fecha": "2024-10-01","total":950,"estado":"Entregado"},{"fecha":"2024-10-10","total":120,"estado":"Enviado"}]}
Resumen de por qué cada paso es necesario
Paso	Por qué
Crear Function App	Permite exponer datos dinámicos a Foundry vía HTTP
Configurar trigger HTTP	Permite recibir parámetros (id) y devolver resultados
Publicar en Azure	Permite que Foundry acceda desde la nube
Agregar acción en Foundry	Accede a datos en tiempo real, no conocimiento estático
Probar localmente	Garantiza que la lógica funciona antes de publicar

7️⃣ Estructura del repositorio

ChatBotLaMarina/
│
├─ function_app.py
├─ requirements.txt
├─ README.md
├─ test.http
└─ .gitignore
