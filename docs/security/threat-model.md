# Threat Model (Free Core + ttlink)

## Model layer

- Jailbreak / capability elicitation  
- Membership inference & extraction (public data changes, does not eliminate)  
- Poisoning / backdoors in train & post-train  
- Adversarial inputs  

## Transparency infrastructure

- Index integrity (tamper / selective rewrite)  
- Availability (DoS on stream/query)  
- Query abuse (bulk scrape via link API)  
- Supply-chain swaps of checkpoints/index shards  

## Organisational

- Insider threat  
- Legal/abuse pressure used to force opacity  
- Incident response that “turns off” transparency  

## Mitigations (skeleton)

- Cryptographic manifests + signed releases  
- Rate limits that do not erase the public promise  
- Published threat model + red-team register  
- Continuity covenant against unilateral withdrawal  
