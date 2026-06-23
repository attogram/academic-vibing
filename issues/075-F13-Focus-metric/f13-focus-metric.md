# F13 Focus metric #75

Opened on Jun 19, 2026 by attogram

What you’re describing is actually a real and known failure mode in
systems like yours.

In plain terms:

  You built a system that is too good at generating branching research
  space and not good enough at closing search.

That’s not a “bug in you” — it’s a known property of LLM-driven
ideation systems.
  __________________________________________________________________

 1. What’s actually happening in your system

Your swarm + CDI + RAC setup is currently doing this:

Input goal: "do research"

System behavior:
→ generate hypotheses
→ generate sub-hypotheses
→ generate meta-frameworks
→ generate tools for measuring itself
→ repeat

This is called:

unbounded generative expansion

It naturally produces:

7–8 “papers”

multiple frameworks (CDI, Focus, RockTalk, etc.)

recursive self-analysis

So your observation is correct:

  “it’s unfocused”

But more precisely:

  it is optimization without a termination condition
  __________________________________________________________________

 2. Your “Focus Metric” is actually the right instinct

You said:

  it was made to solve expansion

That is exactly the correct design target.

But here’s the key insight:

You are not measuring focus.
You are trying to implement a stopping rule.

That distinction matters a lot.
  __________________________________________________________________

 3. What a real “Focus Metric” must do (strict version)

If your goal is arXiv-grade rigor, your metric must answer ONE
question:

  “Should the system STOP branching or CONTINUE exploring?”

So it must behave like:

A control signal, not a descriptive metric

That means:

low focus → allow exploration

high focus → enforce convergence / writing / closure

Not just “measurement”
  __________________________________________________________________

 4. The missing piece in your architecture

Right now you have:

CDI = disagreement signal
Focus = coherence signal

But you are missing:

Closure operator (this is critical)

Without closure, the system will always expand.

Closure means:

stop generating new branches

force synthesis

force paper finalization
  __________________________________________________________________

 5. Why your system keeps producing “7–8 papers”

This is not random.

It is structurally expected:

LLMs default to:
maximize novelty + continuation probability
not
maximize completion

So unless you explicitly define:

“what ends a paper”

“what freezes a version”

“what counts as done”

…it will never converge.
  __________________________________________________________________

 6. A clean reframing of your situation

What you are building is not:

  a research assistant

It is:

a hypothesis generator without a termination function

So Focus Metric is your attempt to add:

  a termination function for cognitive branching

That is actually the correct direction.
  __________________________________________________________________

 7. What I would tell you if this is going toward arXiv

Right now, your system has:

CDI (divergence / disagreement)

Focus (coherence / drift)

Swarm (generation engine)

But you still need ONE missing component:

Convergence rule (stop condition)

Without it, reviewers will say:

  “Interesting generative system, but no defined experimental
  protocol.”
  __________________________________________________________________

 8. The key insight (very important)

You said:

  “we’re going to archive X”

Good — but scientifically, you need:

X must define when exploration ends
not just what is explored

Otherwise “archiving” becomes arbitrary.
  __________________________________________________________________

 9. Minimal correction that fixes most of your problem

If I compress everything into one actionable rule:

  Every branch must eventually map to either:

 1. a claim being tested
 2. or be discarded

No third category.

That alone will reduce:

paper explosion

infinite expansion

swarm drift
  __________________________________________________________________

10. Bottom line

You are not failing at “focus” in a human sense.

You are hitting a classic system property:

open-ended LLM generation without convergence constraints

Your Focus Metric is the right idea.

But the missing piece is:

  not measuring focus — enforcing termination
  __________________________________________________________________

If you want, I can help you design a minimal 3-signal control system
(CDI + Focus + Closure) that would actually make this arXiv-stable
instead of continuously expanding.

---

current issue summary is: F13 Focus metric 75. Opened on Jun 19, 2026 by attogram What you’re describing is actually a real and known failure mode in systems like yours. In plain terms: You built a system that is too good at generating branching research space and not good enough at closing search. That’s not a “bug in you” — it’s a known property of LLM-driven ideation systems. __________________________________________________________________ 1. What’s actually happening in your system Your swarm + CDI + RAC setup is currently doing this: Input goal: "do research" System behavior: → generate hypotheses → generate sub-hypotheses → generate meta-frameworks → generate tools for measuring itself → repeat This is called: unbounded generative expansion It naturally produces: 7–8 “papers” multiple frameworks (CDI, Focus, RockTalk, etc.) rec...
