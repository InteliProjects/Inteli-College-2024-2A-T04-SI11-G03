# 1. Deploy no Azure

Como a empresa utiliza o Azure para suas operações, foi criado um tutorial específico para subir o modelo, o backend e o frontend na infraestrutura do Azure. Abaixo estão as instruções detalhadas para realizar o deploy dos três componentes (modelo, backend e frontend) usando serviços do Azure.

## 1.1 Pré-requisitos:
- Conta no Azure e assinatura ativa.
- Angular e Flask instalados no ambiente local.
- Azure CLI instalado no ambiente local.
- Projeto Angular e Flask funcionando localmente.
- Modelo de Deep Learning em um script `.py` salvo.

# 2. Configurações

Certifique-se de que o projeto Flask possui um arquivo `requirements.txt` contendo todas as dependências:

```bash
pip freeze > requirements.txt
```

Crie um arquivo `startup.sh` para definir os comandos de inicialização do Flask:

```bash
#!/bin/bash
python3 -m pip install -r requirements.txt
python3 -m flask run --host=0.0.0.0 --port=8000
```

## 2.1 Criar e Configurar um Web App

**Login no Azure CLI**:

```bash
az login
```

Criar um grupo de recursos

```bash
az group create --name <leak-seeker> --location <location>
```

## 2.2 Configurações Backend

Criar um App Service para o backend

```bash
az webapp create --leak-seeker <leak-seeker> --plan <app-service-plan> --name <backend-leak-seeker> --runtime "PYTHON:3.9"
```

Configurar as variáveis de ambiente

```bash
az webapp config appsettings set --leak-seeker <leak-seeker> --name <backend-leak-seeker> --settings FLASK_ENV=production
```

Após configurar o deploy pelo GitHub, o Azure automaticamente executará o deploy do backend.

O backend estará disponível em `https://<backend-leak-seeker>.azurewebsites.net`.

## 2.3 Configurações Frontend

Certifique-se de que o `environment.ts` do Angular está apontando para o backend:

```typescript
export const environment = {
  production: true,
  apiUrl: 'https://<backend-leak-seeker>.azurewebsites.net'
};
```

Gere a build de produção do Angular:

```bash
ng build --prod
```

### 2.3.1 Criar um Web App

Criar o App Service

```bash
az webapp create --leak-seeker <leak-seeker> --plan <app-service-plan> --name <frontend-leak-seeker> --runtime "NODE|14-lts"
```

O Azure automaticamente executará o deploy da build do Angular.

```bash
az webapp config set --leak-seeker <leak-seeker> --name <frontend-leak-seeker> --web-sockets-enabled true
```

O frontend estará disponível em `https://<frontend-leak-seeker>.azurewebsites.net`.

## 2.4 Configurações do Modelo

Criar um Serviço de Machine Learning

1. No portal do Azure, crie um serviço de **Azure Machine Learning**.
2. Configure um `Workspace` para hospedar o modelo.


Subir o Modelo para o Azure

```bash
az ml workspace show --leak-seeker <leak-seeker> --name <workspace-name>
```

Subir o modelo

No terminal, vá até o diretório onde o modelo `.py` está localizado e execute:

```bash
az ml model register --model-name <model-name> --model-path <path-to-model> --leak-seeker <leak-seeker> --workspace-name <workspace-name>
```

Crie um endpoint de serviço para expor o modelo

```bash
az ml service create realtime --model <model-name> --workspace <workspace-name> --service-name <service-name> --leak-seeker <leak-seeker>
```

# 3. Testar a aplicação

Agora que o backend, frontend, e o modelo estão no Azure, pode-se testar a aplicação completa:

1. Acesse o frontend em `https://<frontend-leak-seeker>.azurewebsites.net`.
   
2. Realize um upload de um arquivo CSV para disparar o processamento no backend.
   
3. Verifique se o backend está comunicando corretamente com o modelo de Machine Learning e retornando as predições esperadas.

## 3.1 Formato esperado para o arquivo CSV

Para que a aplicação processe corretamente os dados, o arquivo CSV deve ter 7 colunas com os seguintes nomes e tipos:

- matricula: string
- referencia: string
- categoria: string
- cod_latitude: number
- cod_longitude: number
- volume_estimado: number
- desc_ocorrencia: string

Certifique-se de que o CSV siga esse formato e contenha as colunas na ordem especificada, pois qualquer desvio pode resultar em erros de processamento ou falhas na previsão do modelo.