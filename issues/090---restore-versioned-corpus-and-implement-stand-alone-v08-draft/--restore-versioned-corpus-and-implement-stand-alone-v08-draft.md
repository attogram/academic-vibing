# Issue #90: Restore Versioned Corpus and Implement Stand-alone v0.8 Draft

## Body

This submission addresses the critical loss of the versioned research corpus due to a session cutoff and iterates the methodology to version 0.8.

Key changes:
1. **Corpus Restoration**: Recovered versioned directories (v0.1-v0.6 for the core paper and v0.1-v0.3 for receipts) that were lost. These are now properly organized in `papers/academic-vibing/` and `papers/receipts/`.
2. **Academic Vibing v0.8**: Introduced a new, stand-alone draft (v0.8) that merges the structural elegance of v0.5 with the advanced features of v0.7 (CDI, Leapfrog Mechanism, Adversarial Rigor). It includes all core definitions to ensure it can be read independently.
3. **Robust Citation System**: Implemented a bi-directional linking system. Inline citations in v0.8 now link directly to a master registry in `CITATIONS.md`, which in turn links back to specific paper versions.
4. **Project Tracking**: Updated `README.md` to reflect the complete version history and marked the corresponding issue (F7) as closed pending review.
5. **Validation**: Verified the integrity of the directory structure and the functionality of the CDI calculation script.

This restoration ensures the project maintains its full ethnographic audit trail and provides a solid foundation for the upcoming arXiv submission.

---
*PR created automatically by Jules for task [8248378737856959272](https://jules.google.com/task/8248378737856959272) started by @attogram*

## Comments

### Comment by google-labs-jules[bot] at 2026-06-20T01:18:01Z

👋 Jules, reporting for duty! I'm here to lend a hand with this pull request.

When you start a review, I'll add a 👀 emoji to each comment to let you know I've read it. I'll focus on feedback directed at me and will do my best to stay out of conversations between you and other bots or reviewers to keep the noise down.

I'll push a commit with your requested changes shortly after. Please note there might be a delay between these steps, but rest assured I'm on the job!

For more direct control, you can switch me to **Reactive Mode**. When this mode is on, I will only act on comments where you specifically mention me with `@jules`. You can find this option in the **Pull Request** section of your [global Jules UI settings](https://jules.google.com/settings). You can always switch back!

New to Jules? Learn more at [jules.google/docs](https://jules.google/docs).

---
*_For security, I will only act on instructions from the user who triggered this task._*

---
