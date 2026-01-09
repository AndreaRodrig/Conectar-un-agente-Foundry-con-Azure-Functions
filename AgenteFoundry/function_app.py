import azure.functions as func
import json

app = func.FunctionApp()

mock = {
    "123": {
        "clienteId": 123,
        "compras": [
            {"fecha": "2024-10-01", "total": 950, "estado": "Entregado"},
            {"fecha": "2024-10-10", "total": 120, "estado": "Enviado"}
        ]
    },
    "456": {
        "clienteId": 456,
        "compras": [
            {"fecha": "2024-11-01", "total": 50, "estado": "Entregado"},
            {"fecha": "2024-11-10", "total": 30, "estado": "Enviado"}
        ]
    }
}

def generar_prediccion(compras):
    total = sum(c["total"] for c in compras)
    promedio = total / len(compras)

    if promedio > 500:
        riesgo = "bajo"
    elif promedio > 200:
        riesgo = "medio"
    else:
        riesgo = "alto"

    return {
        "gasto_promedio": round(promedio, 2),
        "proxima_compra_estimado": round(promedio * 1.1, 2),
        "riesgo_abandono": riesgo
    }

@app.route(route="cliente/compras", methods=["GET"], auth_level=func.AuthLevel.FUNCTION)
def get_compras(req: func.HttpRequest) -> func.HttpResponse:
    cliente_id = str(req.params.get("id"))

    if not cliente_id:
        return func.HttpResponse(
            json.dumps({"error": "Falta parámetro id"}),
            status_code=400,
            mimetype="application/json"
        )

    data = mock.get(cliente_id)

    if not data:
        return func.HttpResponse(
            json.dumps({"error": "Cliente no encontrado"}),
            status_code=404,
            mimetype="application/json"
        )

    # Generar la predicción según el cliente que viene en la petición
    data["prediccion"] = generar_prediccion(data["compras"])

    return func.HttpResponse(
        json.dumps(data),
        status_code=200,
        mimetype="application/json"
    )

