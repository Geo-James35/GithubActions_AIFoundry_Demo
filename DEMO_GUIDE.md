# Demo Walkthrough Guide

This guide will help you present the GitHub Actions to AI Foundry deployment demo.

## Demo Flow (10-15 minutes)

### 1. Introduction (2 minutes)

**What to say:**
"Today I'm going to show you how to automatically deploy an AI agent to Azure AI Foundry using GitHub Actions. Every time we push code to GitHub, it will automatically deploy to the cloud. Let's see how this works!"

### 2. Show the Project Structure (2 minutes)

**Walk through:**
- `agent/simple_agent.py` - "This is our AI agent that uses Azure OpenAI"
- `agent/score.py` - "This is the scoring script that Azure uses to handle requests"
- `.github/workflows/deploy-to-foundry.yml` - "This is our GitHub Actions workflow"

**Key points:**
- Simple, production-ready code
- Follows Azure best practices
- Easy to extend and customize

### 3. Explain the GitHub Actions Workflow (3 minutes)

**Open `.github/workflows/deploy-to-foundry.yml` and highlight:**

```yaml
on:
  push:
    branches:
      - main  # Triggers on push to main
```

**Walk through the steps:**
1. ✅ Checkout code
2. ✅ Set up Python
3. ✅ Install dependencies
4. ✅ Run tests
5. ✅ Login to Azure
6. ✅ Create/update endpoint
7. ✅ Deploy agent
8. ✅ Test deployment

**What to say:**
"The workflow is triggered every time we push to the main branch. It sets up the environment, tests our code, deploys to Azure AI Foundry, and even runs a test to make sure everything is working."

### 4. Show the Azure Configuration (2 minutes)

**Explain the secrets needed:**
- `AZURE_CREDENTIALS` - For authentication
- `AZURE_SUBSCRIPTION_ID` - Your subscription
- `AZURE_RESOURCE_GROUP` - Where to deploy
- `AI_FOUNDRY_PROJECT_NAME` - Your AI Foundry project

**What to say:**
"We store sensitive information like credentials in GitHub Secrets. This keeps them secure and out of our code."

### 5. Demo the Deployment (3-5 minutes)

**Option A: Live deployment (if setup)**
1. Make a small change to the agent (e.g., update the system prompt)
2. Commit and push
3. Go to GitHub Actions tab
4. Watch the workflow run in real-time
5. Show the successful deployment

**Option B: Show a previous run**
1. Navigate to GitHub Actions tab
2. Show a completed workflow
3. Walk through each step's logs
4. Show the successful test at the end

### 6. Show the Deployed Agent (2 minutes)

**In Azure AI Foundry portal:**
1. Navigate to https://ai.azure.com
2. Show your project
3. Show the deployed endpoint
4. Demonstrate making a test call

**OR using Azure CLI:**
```bash
az ml online-endpoint invoke \
  --name foundry-agent-endpoint \
  --request-file test_request.json
```

### 7. Conclusion (1 minute)

**What to say:**
"And that's it! Now every time we push code, GitHub Actions automatically:
- Tests our code
- Deploys to Azure AI Foundry
- Validates the deployment

This means we can iterate quickly and deploy with confidence. The same approach works for more complex agents, multiple environments, and integration with other services."

## Demo Tips

### Before the Demo

- [ ] Have Azure AI Foundry project ready
- [ ] Configure GitHub secrets
- [ ] Do a test deployment
- [ ] Have both GitHub and Azure portal open in tabs
- [ ] Test your internet connection

### During the Demo

- Keep it high-level unless asked for details
- Show, don't just tell
- Have the README open for reference
- Be prepared to show logs if something fails

### Common Questions

**Q: How long does deployment take?**
A: Usually 5-10 minutes for the full workflow

**Q: Can this work with other models?**
A: Yes! Just update the model name in the configuration

**Q: What about costs?**
A: You pay for the Azure AI Foundry compute resources while they're running

**Q: Can we add staging environments?**
A: Absolutely! You can add branches for dev/staging/prod

**Q: How do we roll back?**
A: You can redeploy a previous version or use Azure's built-in versioning

## Troubleshooting During Demo

If something goes wrong:

1. **Authentication fails**: Check GitHub secrets are set correctly
2. **Deployment fails**: Show the logs, explain it's usually permissions or quota
3. **Test fails**: Explain this is why we test - catches issues before they reach users

## Extensions to Mention

"You could extend this to:"
- Multiple environments (dev/staging/prod)
- Integration tests with real data
- Performance monitoring
- A/B testing different agent versions
- Slack notifications on deployment
- Automatic rollback on failures

## Files to Have Open

1. `README.md` - For reference
2. `.github/workflows/deploy-to-foundry.yml` - Main workflow
3. `agent/simple_agent.py` - The agent code
4. GitHub Actions tab in browser
5. Azure AI Foundry portal
