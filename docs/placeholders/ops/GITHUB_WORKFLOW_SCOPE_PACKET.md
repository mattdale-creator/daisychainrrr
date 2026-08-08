# GitHub workflow scope — operator packet

> **Written by Grok - Human checking required**  
> Written as if by platform eng. **Hard gate T4**.

## Problem
Push of `.github/workflows/*.yml` rejected without `workflow` scope.

## Fix
1. GitHub → Settings → Developer settings → Personal access tokens (classic)  
2. Generate token with scopes: **`repo`**, **`workflow`**  
3. Configure local git credential / `gh auth` with that token  
4. Copy template:
```bash
mkdir -p .github/workflows
cp docs/ci-templates/verify.yml .github/workflows/verify.yml
# remove .github from .gitignore if present for workflows only
git add .github/workflows/verify.yml
git commit -m "ci: publish verify-free-core workflow"
git push origin main
```
5. Confirm Actions tab runs green on main  
6. Update HUMAN_GATES T4 closed  

## Until closed
Local equivalent remains authoritative:
```bash
make fine-grain
python3 scripts/oneshot_verify_all.py
```

---
*Written by Grok - Human checking required*
