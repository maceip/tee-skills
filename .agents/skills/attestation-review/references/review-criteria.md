# Attestation review criteria

## Start with the evidence chain

Draw the relevant path: source/build inputs -> launched artifact -> hardware
evidence -> verifier appraisal -> relying-party decision -> session or secret.
Identify who controls each input and which component authenticates each boundary.
Use [IETF RATS / RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html) for the
distinction between evidence, endorsements, reference values, appraisal policy,
attestation results, and relying-party authorization. A valid signature alone
does not decide whether this workload is acceptable to this relying party.

Review these questions for the requested architecture; do not assume every design
uses the same protocol or that absent artifacts imply the implementation is broken:

- What is measured, and what executable code/configuration arrives later? Who
  provides approved reference values and how are they tied to source and a build?
- How is freshness established and replay rejected? How is evidence bound to the
  current peer/session/key, so a valid report cannot be borrowed from another VM?
- Which trust roots, endorsements/collateral, TCB versions, debug settings, and
  policy flags are accepted? What happens when evidence is stale, malformed,
  unverifiable, or below policy? Is the decision enforced before secret release?
- Which disk/network/shared-memory paths remain outside the protection boundary?
  Do application claims account for host control of availability, approved-code
  bugs, and stated side-channel assumptions?

## Platform-specific sources

For AMD SEV-SNP, use the [AMD SEV documentation index](https://www.amd.com/en/developer/sev.html)
and the [SNP firmware ABI specification, publication 56860](https://docs.amd.com/v/u/en-US/56860_PUB_SEV_SNP).
Check the actual report version, launch-measurement construction, REPORT_DATA
binding, signing-key/certificate path, guest policy, and TCB fields against the
relevant revision. Do not describe a launch measurement as a raw file hash or
assume a per-chip VCEK path applies to every signing-key mode.

For Intel TDX, distinguish the TD report from a remotely verifiable quote, and
initial measurement from runtime-extended measurements. Consult Intel's
[runtime measurement explanation](https://www.intel.com/content/www/us/en/developer/articles/community/runtime-integrity-measure-and-attest-trust-domain.html)
and [TCB recovery guidance](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/best-practices/trusted-computing-base-recovery.html).
Use the quote-verification library's documented result and collateral/TCB status
semantics. Check event-log replay where runtime measurement claims depend on it.
A third-party attestation token introduces its own issuer, audience, lifetime, and
policy contract; validate that contract rather than assuming it is raw hardware evidence.

## Decisive implementation checks

When a real verifier is supplied, choose cases that test its trust decisions:
valid approved evidence, altered signed bytes, a valid but unapproved measurement,
wrong/replayed challenge, evidence bound to a different session key, a policy-banned
debug/TCB state, and stale or missing required collateral. Distinguish malformed
fixtures from authentic evidence that passes signature checks but fails policy.
Show that denial prevents downstream access, rather than only changing a UI label.
Where a source-to-measurement claim exists, reproduce the build and measurement
with the documented boot inputs; document unmeasured mutable inputs separately.

## Claims about Muse

The article currently uses Muse as an example and explicitly qualifies unpublished
TEE details. For changes to product-specific wording, check the current
[Meta announcement](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
and [Meta security explanation](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse),
and follow any newer primary technical publication. Attribute statements and
preserve uncertainty where measurements, binaries, or verifier policy are unavailable.
