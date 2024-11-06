from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import pandas as pd
import io
from pipeline.PipeLineHandler import PipeLineHandler

router = APIRouter()

@router.post("/process_csv")
async def process_csv(request: Request):
    try:
        # Recebe o CSV no corpo da requisição
        body = await request.body()

        # Lê o CSV como DataFrame
        df = pd.read_csv(io.BytesIO(body), delimiter=";")

        # Processa o DataFrame com o PipelineHandler (sem cálculos)
        df = PipeLineHandler.process(df)

        # Faz as predições e agrega os resultados ao DataFrame
        df = PipeLineHandler.predict_and_aggregate(df)

        # Salva o DataFrame processado em um novo arquivo CSV
        output_filename = "processed_data.csv"
        PipeLineHandler.save_to_csv(df, output_filename)

        # Converte o DataFrame para um CSV em memória para resposta
        stream = io.StringIO()
        df.to_csv(stream, index=False)

        # Retorna o CSV processado como resposta
        response = StreamingResponse(
            iter([stream.getvalue()]),
            media_type="text/csv"
        )
        response.headers["Content-Disposition"] = f"attachment; filename={output_filename}"
        return response

    except Exception as e:
        return {"error": str(e)}
