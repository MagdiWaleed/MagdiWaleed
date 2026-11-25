### Selected work

**Nabrah ASR** · private, in production<br>
Bilingual Arabic / English speech recognition with code-switching, streamed through Triton on GCP GPUs. 41% lower WER than Whisper large-v3, at 19× its real-time factor.<br>
<sub>Triton · GCP · FastAPI · Docker</sub>

**[asr-utils](https://github.com/MagdiWaleed/asr-utils)**<br>
The ASR helpers I kept rewriting, now one namespace with separately versioned packages: Arabic text and number normalization, WER / CER metrics, and noise simulation in progress.<br>
<sub>Python · pip-installable per package</sub>

**[nabrah-skills](https://github.com/MagdiWaleed/nabrah-skills)**<br>
Claude skills that build voice and WhatsApp agent prompts in Nabrah's V2 format, audit live agents, and convert V1 agents to V2. Installs as a Claude Code plugin.<br>
<sub>Claude Code · Shell</sub>

**[Signer](https://github.com/MagdiWaleed/Signer)**<br>
Turkish Sign Language to text. Boundary detection, MediaPipe landmarks and an attention-based multi-fusion model predict glosses from video; an LLM turns the glosses into a sentence.<br>
<sub>PyTorch · MediaPipe · Transformers</sub>

**Customer service agent** · [backend](https://github.com/MagdiWaleed/customer-service-backend) / [frontend](https://github.com/MagdiWaleed/customer-service-frontend)<br>
Retrieval, multi-step reasoning and conversation memory for many users at once, with service recommendations at the end of a chat.<br>
<sub>LangChain · Flask · Streamlit</sub>

**Market analyzer** · [backend](https://github.com/MagdiWaleed/market_analyzer_backend) / [frontend](https://github.com/MagdiWaleed/market_analyzer_frontend)<br>
An agent that benchmarks products in the Saudi market, finds gaps, and writes recommendations you can question interactively.<br>
<sub>LangGraph · Python</sub>
