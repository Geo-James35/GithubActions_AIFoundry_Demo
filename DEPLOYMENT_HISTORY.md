# Deployment History

This file tracks deployment history for the AI Foundry agent.

## Latest Deployment

- **Version:** 1.0.0
- **Date:** 2025-11-07
- **Commit:** TBD (updated by GitHub Actions)
- **Author:** TBD
- **Status:** ✅ Deployed

## Deployment History

| Version | Date | Commit | Status | Notes |
|---------|------|--------|--------|-------|
| 1.0.0 | 2025-11-07 | Initial | ✅ | Initial deployment with GitHub Actions |

## How to Verify Changes

### Method 1: Azure Portal Resource Tags (Best Visual Proof) ⭐
This is the **most effective way** to show deployment changes during your demo!

1. **Navigate to Azure Portal**:
   - Go to https://portal.azure.com
   - Search for: `githubactionsdemo-resource`
   - Or navigate: Resource Groups → rg-GithubActionsDemo → githubactionsdemo-resource
   
2. **View Deployment Tags**:
   - Click on "Tags" in the left sidebar
   - You'll see:
     - **LastDeployment**: Timestamp when last deployed (e.g., "2025-01-07T14:30:00Z")
     - **Version**: Current agent version (e.g., "1.0.0")
     - **GitCommit**: The exact commit that was deployed
     - **DeployedBy**: "GitHubActions"
   
3. **Demo Strategy**:
   - Take a screenshot of Tags BEFORE making changes
   - Make a code change and push
   - Wait for GitHub Actions to complete
   - Refresh the Tags page
   - Show the updated LastDeployment, Version, and GitCommit

### Method 2: GitHub Actions Logs
1. **View Workflow Runs**:
   - Go to: https://github.com/Geo-James35/GithubActions_AIFoundry_Demo/actions
   - Click on the latest workflow run
   - Expand "🚀 Deploy agent to AI Foundry" step
   - See deployment confirmation with version and commit info

### Method 3: Command Line Verification
```bash
# Check current Azure resource tags
az cognitiveservices account show \
  --name githubactionsdemo-resource \
  --resource-group rg-GithubActionsDemo \
  --query tags

# Get just the deployment info
az cognitiveservices account show \
  --name githubactionsdemo-resource \
  --resource-group rg-GithubActionsDemo \
  --query "{Version:tags.Version, LastDeployment:tags.LastDeployment, GitCommit:tags.GitCommit}"
```

### Method 4: Check AI Foundry Portal
- Go to: https://ai.azure.com
- Navigate to your project
- Check Activity Log or Resource Details sections

## Quick Demo Flow

1. **Make a change:** Update `__version__` in `agent/simple_agent.py`
2. **Commit & Push:**
   ```bash
   git add .
   git commit -m "Update to version 1.1.0"
   git push
   ```
3. **Watch GitHub Actions:** See the workflow run automatically
4. **Verify:** Check this file - it will update with new version info
