import azure.functions as func
import json

app = func.FunctionApp()

# MOCK de datos
MOCK_CLIENTES = {
    "123": {
        "clienteId": 123,
        "compras": [
            {"fecha": "2024-10-01", "total": 950, "estado": "Entregado"},
            {"fecha": "2024-10-10", "total": 120, "estado": "Enviado"}
        ]
    }
}

@app.route(route="cliente/compras", methods=["GET"], auth_level=func.AuthLevel.FUNCTION)
def get_compras(req: func.HttpRequest) -> func.HttpResponse:
    cliente_id = req.params.get("id")

    if not cliente_id:
        return func.HttpResponse(
            json.dumps({"error": "Falta parámetro id"}),
            status_code=400,
            mimetype="application/json"
        )

    data = MOCK_CLIENTES.get(cliente_id)

    if not data:
        return func.HttpResponse(
            json.dumps({"error": "Cliente no encontrado"}),
            status_code=404,
            mimetype="application/json"
        )

    return func.HttpResponse(
        json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )
