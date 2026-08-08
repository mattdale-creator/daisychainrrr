# Precompact path preserve (always on)

## Why

Long builds (especially **TTLLMS.com BUILD** / TTLLM) must not lose the path when Grok **compacts** conversation history. Compaction is a summary step: it free tokens by dropping detail. That can erase vault paths, open blockers, domain/DNS state, and decisions. This rule keeps the **build path continuous** across compaction.

## Before compaction (agent duty)

If context is large, the user mentions compacting, or you sense compaction is near:

1. **Stop** other non-essential work.
2. Run:

```bash
python3 ~/.grok/skills/precompact-path-preserve/scripts/preserve_and_inject.py now
```

3. Confirm freeze under:

`/Users/hattr/Downloads/TTLLMS.com BUILD/09-precompact-snapshots/`

Hooks also run automatically on official `PreCompact` / `PostCompact` events.

## After compaction / every turn when inject is fresh

**First tool action of the turn** when any of these exist and are recent:

- `/Users/hattr/Downloads/TTLLMS.com BUILD/09-precompact-snapshots/CURRENT/POST_COMPACT_INJECT.md`
- `~/.grok/session-prompts/POST_COMPACT_INJECT.md`
- `~/.grok/session-prompts/CURRENT_POST_COMPACT.md`

→ **Read the inject file** and obey it. Do not reinvent the project plan.

## Source of truth (this Mac)

All TTLLM / ttllms.com work:

`/Users/hattr/Downloads/TTLLMS.com BUILD`

Code:

`/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr`

Contact: **md@0265.au**  
Primary site: **ttllms.com**  
Pages: **https://ttllms.pages.dev**
