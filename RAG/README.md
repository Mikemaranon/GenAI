# Azure AI Search and OpenAI Integration Quickstart

This guide provides step-by-step instructions to configure and use Azure AI Search and Azure OpenAI for building a search and recommendation application. 

## Prerequisites

- Access to an Azure subscription.
- Azure AI Search and Azure OpenAI resources created in the Azure portal.
- Visual Studio Code installed locally.
- Python and pip installed on your system.

---

## 1. Configure Access

### Authentication and Authorization
Azure AI Search and OpenAI require role-based access control. Assign the appropriate roles to your Microsoft Entra ID user identity:
1. **Azure AI Search**
   - If the sample index (`hotels-sample-index`) exists:
     - Assign **Search Index Data Reader**.
   - If the sample index doesn't exist:
     - Assign **Search Service Contributor** and **Search Index Data Contributor**.
2. **Azure OpenAI**
   - Assign **Cognitive Services OpenAI User**.

### Steps:
1. Sign in to the Azure portal.
2. Navigate to your **Azure AI Search** service.
   - Go to **Settings > Keys** and select **Role-based access control**.
   - Under **Access control (IAM)**, assign the necessary roles.
3. Navigate to **Azure OpenAI**.
   - Go to **Access control (IAM)** and assign **Cognitive Services OpenAI User**.

*Note: Role assignments can take a few minutes to propagate.*

---

## 2. Create a Search Index

A search index provides the grounding data for the application. Use the `hotels-sample-index` for this quickstart.

### Steps:
1. In the Azure portal, go to your **Azure AI Search** service.
2. On the **Overview** page, select **Import data** to start the wizard.
3. Under **Connect to your data**, select **Samples** and choose `hotels-sample`.
4. Proceed through the wizard, accepting the default values.
5. Once the index is created:
   - Navigate to **Search management > Indexes**.
   - Open the index, select **Edit JSON**, and append the following semantic configuration:
     ```json
     "semantic": {
         "defaultConfiguration": "semantic-config",
         "configurations": [
             {
                 "name": "semantic-config",
                 "prioritizedFields": {
                     "titleField": { "fieldName": "HotelName" },
                     "prioritizedContentFields": [{ "fieldName": "Description" }],
                     "prioritizedKeywordsFields": [
                         { "fieldName": "Category" },
                         { "fieldName": "Tags" }
                     ]
                 }
             }
         ]
     },
     ```
6. Save your changes.

---

## 3. Set Up the Development Environment

### Create a Virtual Environment
1. Open Visual Studio Code.
2. Create a new folder for the project and open it in VS Code.
3. Press `Ctrl+Shift+P`, search for **Python: Create Environment**, and select `Venv`.
4. Use `Quickstart-RAG/requirements.txt` for dependencies.

### Install Dependencies
Run the following commands:
```bash
pip install azure-search-documents==11.6.0b5
pip install azure-identity==1.16.1
pip install openai
pip install aiohttp
pip install ipykernel
```

## 4. Sign In to Azure CLI

### Log in to Azure CLI using the following commands
``` bash
az account show
az account set --subscription <YOUR_SUBSCRIPTION_ID>
az login --tenant <YOUR_TENANT_ID>
```

## 5. Set Up Query and Chat

### Replace placeholders with your service endpoints:
``` bash
AZURE_SEARCH_SERVICE = "PUT YOUR SEARCH SERVICE ENDPOINT HERE"
AZURE_OPENAI_ACCOUNT = "PUT YOUR AZURE OPENAI ENDPOINT HERE"
AZURE_DEPLOYMENT_MODEL = "gpt-4o"
```