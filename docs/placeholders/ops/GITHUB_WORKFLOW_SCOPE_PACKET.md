# GitHub workflow scope — full operator pack

> **Written by Grok - Human checking required**  
> Platform eng voice. **Hard gate T4.**  
> Local `make fine-grain` / oneshot remains authoritative until Actions is public green.

---

## 1. Why CI is load-bearing

Seal freshness, DATA_CARD checks, public verify harness, and red-team harness must not depend on one laptop. CI is topology: load path for “green” that strangers can see. Soft tissue is claiming CI when workflow files cannot be pushed.

---

## 2. Failure mode observed

Push of `.github/workflows/*.yml` rejected without OAuth/PAT **`workflow`** scope  
(*refusing to allow an OAuth App to create or update workflow*).

---

## 3. Fix steps

1. GitHub → Settings → Developer settings → Personal access tokens (classic)  
2. Scopes: **`repo`**, **`workflow`** (minimum)  
3. Configure git credential / `gh auth login` with that token  
4. Publish workflow:
```bash
mkdir -p .github/workflows
cp docs/ci-templates/verify.yml .github/workflows/verify.yml
# ensure .github workflows are not gitignored
git add .github/workflows/verify.yml
git commit -m "ci: publish verify-free-core workflow"
git push origin main
```
5. Actions tab: workflow runs on main; all jobs green  
6. Mark T4 closed in HUMAN_GATES with date  

---

## 4. What the workflow must run

Aligned with `docs/ci-templates/verify.yml`:

- pytest  
- check_data_cards  
- check_seal_freshness  
- public_verify_harness  
- redteam_nano_harness  
- oneshot_verify_all  

---

## 5. Until closed

```bash
make fine-grain
python3 scripts/oneshot_verify_all.py
```

Do not claim “CI enforces seals on every push” until T4 is closed.

---

*Written by Grok - Human checking required — also on https://ttllms.com/placeholders/*
