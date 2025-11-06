# AI Foundry GitHub Actions Deployment Demo

This demo shows how to automatically deploy an AI agent to Azure AI Foundry using GitHub Actions.

## Prerequisites

Before you begin, you'll need:

1. **Azure Account** with an active subscription
2. **Azure AI Foundry Hub & Project** set up
3. **GitHub Repository** (this one!)
4. **Azure Service Principal** for authentication

## Setup Steps

### Step 1: Create Azure Resources

1. Go to [Azure AI Foundry](https://ai.azure.com)
2. Create a new Hub (if you don't have one)
3. Create a new Project within your Hub
4. Note down:
   - Subscription ID
   - Resource Group name
   - AI Foundry project name
   - Location/Region

### Step 2: Create Service Principal

Run these commands in Azure Cloud Shell or local Azure CLI:

```bash
# Create a service principal
az ad sp create-for-rbac --name "github-actions-foundry-demo" \
  --role contributor \
  --scopes /subscriptions/{YOUR_SUBSCRIPTION_ID}/resourceGroups/{YOUR_RESOURCE_GROUP} \
  --sdk-auth
```

Copy the entire JSON output - you'll need it for GitHub secrets.

### Step 3: Configure GitHub Secrets

In your GitHub repository, go to Settings → Secrets and variables → Actions, and add these secrets:

- `AZURE_CREDENTIALS` - The entire JSON output from the service principal creation
- `AZURE_SUBSCRIPTION_ID` - Your Azure subscription ID
- `AZURE_RESOURCE_GROUP` - Your resource group name
- `AI_FOUNDRY_PROJECT_NAME` - Your AI Foundry project name

### Step 4: Push to GitHub

Once you push this code to GitHub, the workflow will automatically:
1. Trigger on push to the `main` branch
2. Install dependencies
3. Run tests (if any)
4. Deploy to Azure AI Foundry

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy-to-foundry.yml    # GitHub Actions workflow
├── agent/
│   ├── __init__.py
│   └── simple_agent.py              # AI agent code
├── requirements.txt                  # Python dependencies
├── agent_config.yaml                # Agent configuration
└── README.md                        # This file
```

## How It Works

1. **Agent Code**: The `agent/simple_agent.py` contains a simple AI agent that uses Azure OpenAI
2. **Configuration**: `agent_config.yaml` defines the agent's properties and deployment settings
3. **GitHub Action**: Automatically deploys when code is pushed to main branch
4. **Azure AI Foundry**: Hosts and runs the agent in the cloud

## Testing Locally

Before deploying, you can test the agent locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export AZURE_OPENAI_ENDPOINT="your-endpoint"
export AZURE_OPENAI_KEY="your-key"

# Run the agent
python agent/simple_agent.py
```

## Manual Deployment

If you want to deploy manually:

```bash
# Login to Azure
az login

# Deploy to AI Foundry
az ml online-deployment create --file agent_config.yaml \
  --resource-group {YOUR_RESOURCE_GROUP} \
  --workspace-name {YOUR_PROJECT_NAME}
```

## Troubleshooting

- **Authentication Failed**: Check your Azure credentials in GitHub secrets
- **Deployment Failed**: Verify your AI Foundry project exists and the service principal has proper permissions
- **Agent Not Responding**: Check the deployment logs in Azure AI Foundry portal

## Next Steps

- Customize the agent with your own logic
- Add more sophisticated prompts and tools
- Implement proper testing
- Add staging/production environments
- Monitor agent performance in AI Foundry

## Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/)
