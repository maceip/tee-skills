---
name: attestation-review
description: Review TEE and remote-attestation claims, trust boundaries, and verifier policy in this article or related implementation artifacts, separating illustrative examples from exercised evidence.
---

# Attestation review

Identify whether the request concerns article accuracy, an architecture, or a real
verifier/deployment. Use only the scope and artifacts provided; do not turn an
editorial review into infrastructure work. This repository contains an explainer
and browser demos, not an attester, verifier, or confidential VM.

For article work, inspect the relevant copy, captions, diagrams, and JavaScript
together. The SHA-256 demo hashes a single text line; the measurement toggle uses
fixed example values. Keep both clearly illustrative. A value displayed by the
browser, a transcript, a green badge, or an expected fixture cannot establish that
a real report was obtained and appraised. Preserve qualifications around Meta's
unpublished implementation details; verify current product claims from primary
sources before strengthening them.

Read [review criteria](references/review-criteria.md) for the applicable evidence
chain. Consult the linked vendor specification for exact fields, formats, sizes,
algorithms, and TCB interpretation. Keep SNP and TDX mechanisms distinct rather
than generalizing one platform's field names or launch sequence to the other.

For implementation work, trace actual report bytes through verification, policy,
and secret/session release. Record the tested build, platform, policy, and evidence
provenance. Exercise meaningful rejection cases from the reference when the needed
implementation and authorization exist. If only fixtures or source are available,
report that boundary and the missing decisive test; do not certify a deployment.

Lead with the highest-impact unsupported claim or missing mechanism. Each finding
should name the claim/code location, evidence, consequence, and a concrete fix or
decisive test. Separate verified facts, assumptions, and unresolved questions.
Security wording changes should remain readable in the article's established voice.
Publishing, changing trust policy, or releasing secrets requires authorization in
the current task; this skill itself grants none.
