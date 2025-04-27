# CarPool API - Azure Function

This is a FastAPI-based CarPool API implemented as an Azure Function.

## Project Structure

```
carpool-api-azure/
├── CarPoolAPI/
│   ├── __init__.py        # Main application code
│   └── function.json      # Function configuration
├── host.json              # Host configuration
├── local.settings.json    # Local settings
└── requirements.txt       # Python dependencies
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Azure Functions Core Tools:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Run locally:
```bash
func start
```

## API Endpoints

- GET /api/ - Welcome message
- GET /api/carpools - List all carpools
- GET /api/carpools/{id} - Get specific carpool
- POST /api/carpools - Create new carpool
- PUT /api/carpools/{id} - Update carpool
- DELETE /api/carpools/{id} - Delete carpool

## Deployment to Azure

1. Create Azure Function App:
```bash
az functionapp create --name your-app-name --storage-account your-storage-account --resource-group your-resource-group --consumption-plan-location your-region --runtime python --runtime-version 3.9 --functions-version 4
```

2. Deploy using Azure Functions Core Tools:
```bash
func azure functionapp publish your-app-name
```

## Notes

- The API currently uses in-memory storage. For production, implement proper database storage.
- Add authentication and authorization as needed.
- Configure CORS settings in Azure Portal if required.
