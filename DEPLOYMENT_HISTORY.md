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

### Option 1: Check This File
- After each push, check if the "Latest Deployment" section updates
- The commit hash and timestamp will change

### Option 2: Check GitHub Actions
- Go to: https://github.com/Geo-James35/GithubActions_AIFoundry_Demo/actions
- Click on the latest workflow run
- Look at the "Verify deployment" step for version info

### Option 3: Check Azure Portal
- Go to: https://portal.azure.com
- Navigate to Resource Group: `rg-GithubActionsDemo`
- Check the Activity Log for recent operations

### Option 4: Check AI Foundry
- Go to: https://ai.azure.com
- Navigate to your project
- Check Deployments or Activity sections

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
