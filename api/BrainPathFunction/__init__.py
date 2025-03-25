import azure.functions as func
import logging
import json
from Backend.routes import predict, mrpredict, multipredict

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # URL yolunu al
        route = req.route_params.get('route')
        
        if route == 'predict':
            result = await predict.predict(req.files.get('file'))
        elif route == 'mrpredict':
            result = await mrpredict.predict(req.files.get('file'))
        elif route == 'multipredict':
            result = await multipredict.predict(
                handwriting_file=req.files.get('handwriting_file'),
                mr_file=req.files.get('mr_file')
            )
        else:
            return func.HttpResponse(
                "Route not found",
                status_code=404
            )

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        ) 