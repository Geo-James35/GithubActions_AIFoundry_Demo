# GitHub Actions + AI Foundry Demo - Presentation Checklist

## 🎯 Demo Goal
Show how GitHub Actions automatically deploys an AI agent to Azure AI Foundry when code is pushed.

## 📋 Pre-Demo Preparation (Do This First!)

### 1. Take "Before" Screenshots
- [ ] Open Azure Portal: https://portal.azure.com
- [ ] Navigate to: `githubactionsdemo-resource` (Cognitive Services)
- [ ] Click "Tags" in the left sidebar
- [ ] **Take Screenshot #1** - Shows current Version, LastDeployment, GitCommit
- [ ] Save as "before_deployment.png"

### 2. Prepare Your Browser Tabs
- [ ] Tab 1: GitHub repo (https://github.com/Geo-James35/GithubActions_AIFoundry_Demo)
- [ ] Tab 2: GitHub Actions page (same repo, Actions tab)
- [ ] Tab 3: Azure Portal resource Tags page (from step 1)
- [ ] Tab 4: VS Code or terminal (ready to push)

### 3. Verify Current State
- [ ] Check current version in `agent/simple_agent.py` (currently 1.0.1)
- [ ] Ensure no pending changes in git
- [ ] Ensure you're on the `main` branch

---

## 🎬 Demo Flow (15 minutes)

### Part 1: Introduction (2 minutes)
**Say:** "Today I'm demonstrating CI/CD for AI agents. When I push code to GitHub, it automatically deploys to Azure AI Foundry with zero manual steps."

**Show:**
- [ ] GitHub repo main page
- [ ] Point out `.github/workflows/deploy-to-foundry.yml`
- [ ] Show `agent/simple_agent.py` file

### Part 2: Show Current Deployment (2 minutes)
**Say:** "Here's what's currently deployed in Azure."

**Show:**
- [ ] Switch to Azure Portal (Tab 3)
- [ ] Show the Tags page
- [ ] Point out:
  - Version: 1.0.1
  - LastDeployment: [timestamp]
  - GitCommit: [hash]
  - DeployedBy: GitHubActions

**Say:** "These tags prove this was deployed automatically by GitHub Actions."

### Part 3: Make a Code Change (3 minutes)
**Say:** "Now I'll make a simple change - bumping the version to 1.0.2."

**Do:**
- [ ] Open `agent/simple_agent.py` in VS Code
- [ ] Change `__version__ = "1.0.1"` to `__version__ = "1.0.2"`
- [ ] Point out the version number on screen
- [ ] Save the file

**Say:** "Just a simple version bump. Now I'll commit and push."

**Run:**
```bash
git add agent/simple_agent.py
git commit -m "Bump version to 1.0.2 for demo"
git push
```

### Part 4: Watch GitHub Actions (5 minutes)
**Say:** "The moment I pushed, GitHub Actions automatically triggered."

**Show:**
- [ ] Switch to GitHub Actions tab (Tab 2)
- [ ] Show the workflow run that just started (top of the list)
- [ ] Click on the workflow run
- [ ] Show the progress through steps:
  - ✅ Checkout code
  - ✅ Set up Python
  - ✅ Install dependencies
  - ✅ Azure login (with OIDC - no secrets!)
  - ✅ Verify Azure AI Foundry
  - ✅ **Deploy agent** (this is the key step!)

**While waiting:**
- [ ] Explain OIDC authentication (no passwords stored)
- [ ] Explain the deployment script tags the Azure resource
- [ ] Answer any questions

**Wait for:**
- [ ] All steps to complete (green checkmarks)
- [ ] Total time: ~2-3 minutes

### Part 5: Show the Results (3 minutes)
**Say:** "Now let's verify the deployment in Azure."

**Do:**
- [ ] Switch back to Azure Portal (Tab 3)
- [ ] Click the **Refresh** button on the Tags page
- [ ] **Take Screenshot #2** - Shows new Version, LastDeployment, GitCommit

**Show:**
- [ ] **Version** changed from 1.0.1 → **1.0.2** ✨
- [ ] **LastDeployment** updated to new timestamp ✨
- [ ] **GitCommit** changed to new commit hash ✨
- [ ] **DeployedBy** still shows "GitHubActions"

**Say:** "See? The version, timestamp, and commit hash all updated automatically. This proves the deployment happened."

### Part 6: Bonus - Show Deployment Details (Optional, 2 minutes)
**Do:**
- [ ] Switch to GitHub Actions workflow run
- [ ] Expand "🚀 Deploy agent to AI Foundry" step
- [ ] Show the deployment logs with version confirmation

**Say:** "The deployment script tags the Azure resource with version info, making changes visible and traceable."

---

## 💡 Key Talking Points

### Why This Matters
- **No manual deployments** - Reduces human error
- **Traceability** - Every deployment linked to a git commit
- **Fast feedback** - Know within minutes if deployment succeeded
- **Secure** - Uses OIDC, no long-lived credentials

### Technical Highlights
- **OIDC Authentication** - Passwordless, more secure than storing secrets
- **Azure AI Foundry** - Modern AI platform for production agents
- **Resource Tagging** - Makes deployments visible in Azure Portal
- **Version Tracking** - Embedded in agent code, tracked in Azure tags

### Common Questions & Answers

**Q: "What if the deployment fails?"**
A: GitHub Actions will show red X's. You see exactly which step failed in the logs. Nothing gets deployed if tests fail.

**Q: "Can you deploy to multiple environments?"**
A: Yes! You can add branches like `dev`, `staging`, `production` with separate workflows and Azure resources.

**Q: "How do you handle secrets?"**
A: We use OIDC federated credentials - no secrets stored in GitHub. Azure trusts GitHub's identity tokens.

**Q: "What about rollbacks?"**
A: You can revert the git commit and push again. Or manually update the Azure resource tags to a previous commit and redeploy.

---

## 🚨 Troubleshooting (If Something Goes Wrong)

### Workflow Fails
1. Click on the failed step
2. Read the error message
3. Common issues:
   - Authentication: Check federated credential is still valid
   - Permissions: Ensure service principal has Cognitive Services Contributor role
   - Package issues: Check `requirements.txt` versions

### Tags Don't Update
1. Verify workflow completed successfully (all green)
2. Hard refresh Azure Portal (Ctrl+F5)
3. Check workflow logs to confirm tagging command ran
4. Manually run: `az cognitiveservices account show --name githubactionsdemo-resource --resource-group rg-GithubActionsDemo --query tags`

### GitHub Actions Doesn't Trigger
1. Ensure you pushed to `main` branch
2. Check workflow file: `.github/workflows/deploy-to-foundry.yml` exists
3. Verify workflow is enabled (Actions tab → All workflows)

---

## ✅ Post-Demo Cleanup

- [ ] Show before/after screenshots side by side
- [ ] Offer to share the GitHub repo link
- [ ] Mention the documentation files (README, DEMO_GUIDE, etc.)
- [ ] Answer follow-up questions

---

## 📸 Screenshot Comparison Template

### Before Deployment (Version 1.0.1)
- Version: 1.0.1
- LastDeployment: [old timestamp]
- GitCommit: [old hash]

### After Deployment (Version 1.0.2)
- Version: **1.0.2** ✨
- LastDeployment: **[new timestamp]** ✨
- GitCommit: **[new hash]** ✨

**Result:** Automatic deployment confirmed! 🎉

---

## 🎓 For Absolute Beginners

If your audience is new to CI/CD:

1. **Start with the problem:** "Manual deployments are slow, error-prone, and hard to track."
2. **Show the solution:** "We automate it with GitHub Actions."
3. **Demo the value:** "Watch how a simple code push becomes a production deployment in 2 minutes."
4. **Keep it simple:** Focus on the before/after tags comparison, not the workflow internals.

Good luck with your demo! 🚀
