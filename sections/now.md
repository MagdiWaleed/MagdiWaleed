### Now

- **Arabic / English ASR.** Fine-tuning, decoding (beam vs. greedy), and streaming inference on Triton and GCP. I benchmark every model across SADA, Casablanca, MGB-2, MASC and Common Voice, and break the errors down by dialect, recording environment, gender and age, because one average WER hides where a model fails.
- **Voice and WhatsApp agents.** Phone and chat agents built on [LiveKit Agents](https://github.com/livekit/agents): latency, turn-taking, handoffs, and making sure an agent that says "booked" actually booked.
- **Making that work repeatable.** Shared tooling for the team: one package for text normalization and metrics, and Claude skills that build and audit agents from a company brief.
