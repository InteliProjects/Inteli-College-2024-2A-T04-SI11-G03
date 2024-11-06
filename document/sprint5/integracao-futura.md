# 1. Manual de Integração do Sistema

Este manual orienta a integração entre a plataforma Angular e a API desenvolvida em Flask, destinada ao sistema de detecção de fraudes no consumo de água. O objetivo é fornecer um guia completo para que desenvolvedores possam configurar, testar e garantir a comunicação entre o front-end e o back-end.

## 1.1 Pré-requisitos

Para assegurar que o seu ambiente está devidamente configurado conforme as especificações deste projeto, acesse a documentação do <a href="https://github.com/Inteli-College/2024-2A-T04-SI11-G03/blob/main/src/Frontend/AquaGuard/README.md">front-end </a> e do <a href="https://github.com/Inteli-College/2024-2A-T04-SI11-G03/blob/main/src/application/LeakSeekerModel/readme.md">back-end</a>.

## 1.2 Fluxo de Dados

1. O front-end em Angular envia solicitações HTTP para o backend FlaskAPI.
2. A API processa os dados recebidos e utiliza o modelo de Machine Learning para prever a possibilidade de fraude no consumo de água.
3. A resposta é enviada de volta para o Angular, onde os resultados são exibidos ao usuário final.


# 2. Integração

Após seguir os tutoriais de configuração, o back-end estará disponível em `http://localhost:8000/` e o front-end em `http://localhost:4200`.

## 2.1 Primeiros passos

No diretório `src/environments`  do frontend, configure a URL da API:

```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000/'
};
```

## 2.2 Comunicação Angular - Flask

No Angular, crie um serviço para comunicação com a API.

```typescript
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class FraudService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  processCSV(file: File): Observable<Blob> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post(`${this.apiUrl}/process_csv`, formData, {
      responseType: 'blob',
    });
  }
}
```

Essa configuração permite fazer o upload do arquivo CSV e processá-lo pela rota `process_csv` do backend. Use como base nos componentes, ajustando a lógica conforme as informações que deseja exibir na interface.

# 7. Testes e Validação

- Envie dados simulados para a API e valide se os resultados estão corretos.
- Verifique a estabilidade do fluxo de dados em diferentes cenários (sucesso, erro de conexão, etc.).
- Certifique-se de que novas funcionalidades não quebrem as integrações existentes.
  

## 7.1 Formato esperado para o arquivo CSV

Para que a aplicação processe corretamente os dados, o arquivo CSV deve ter 7 colunas com os seguintes nomes e tipos:

- matricula: string
- referencia: string
- categoria: string
- cod_latitude: number
- cod_longitude: number
- volume_estimado: number
- desc_ocorrencia: string

Certifique-se de que o CSV siga esse formato e contenha as colunas na ordem especificada, pois qualquer desvio pode resultar em erros de processamento ou falhas na previsão do modelo.

# 8. Conclusão

Após seguir todos os passos descritos, a integração estará concluída. Certifique-se de validar todas as interações e realizar testes de desempenho no sistema.