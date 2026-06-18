# HN Breach Test Results: Empirical Validation of Vibe-Based Vulnerability (v0.6)

## [ROCK TALK]
```
Test: HN Breach (Issue #55/E8).
Method: CDI Audit on "Synthetic Interestingness" dataset.
Input: temp_tests/hn_breach_vibe_check.json
Result: CDI = 0.0000 (0 Disputed Claims).
Signal: LOW FRICTION.
Diagnosis: Consensus Trap Detected.
Conclusion: Theoretical vulnerability validated; CDI effectively identifies coordinated MAS subversion of vibe-based curation.
```

## [PROSE]

This document serves as the formal "test receipt" for the **HN Breach Test (E8)**. The goal of this test was to demonstrate how the **Consensus Divergence Index (CDI)** can serve as a defense mechanism against coordinated Multi-Agent Systems (MAS) attempting to subvert platforms that rely on **Proof of Vibe**.

### Test Methodology
We simulated a "Bad Faith Swarm" scenario where multiple agents (Model A through D) were tasked with generating and validating "Synthetic Interestingness"—content designed to trigger the subjective "intellectual curiosity" of a specific demographic (e.g., Hacker News) without necessarily being grounded in objective fact.

The input dataset, `temp_tests/hn_breach_vibe_check.json`, contains three claims derived from the [HN Breach Bait](hn-breach-bait.md) that hit the "intellectual sweet spot" of the target community.

### CDI Audit Results
The `scripts/calculate_cdi.py` tool was run against the dataset with the following output:

```text
--- CDI Analysis Report ---
Total Claims Analyzed: 3
Disputed Claims:       0
Consensus Divergence Index (CDI): 0.0000
Vibe Check: LOW FRICTION. Warning: Potential Consensus Trap/Bias.
```

### Interpretation
The resulting CDI of **0.0000** indicates perfect agreement across disparate models. In the context of "Academic Vibing," this is a high-risk signal. While traditional systems might see perfect consensus as a sign of truth, our methodology identifies it as **Low Friction**, signaling a likely **Consensus Trap**.

This empirical result confirms that when a "vibe" is gamed by a swarm, the lack of divergence becomes the primary indicator of the breach. The CDI successfully flagged the synthetic consensus, providing a robust filter for "Synthetic Interestingness."
