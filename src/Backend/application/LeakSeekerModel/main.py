from fastapi import FastAPI
import uvicorn

from routes.process_csv import router as process_csv_router
from routes.consumption_table import router as consumption_table_router

app = FastAPI(
    description="API que recebe um CSV e retorna um CSV com uma coluna a mais da previsão e outra coluna do consumo médio"
)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API! Use /process para processar CSV e /consumption para obter dados de consumo."}

app.include_router(process_csv_router, prefix="/process")
app.include_router(consumption_table_router, prefix="/consumption")

def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main():
    run_app()

if __name__ == '__main__':
    main()
