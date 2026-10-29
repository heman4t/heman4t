<div align="center">

# Hemant Kumar · Project Portfolio

**AI / LLM engineering · business platforms · integrations · infrastructure**<br>
Independent AI & software engineer · Rohtak, India · building software since 2010

[![Profile](https://img.shields.io/badge/Profile-README-24292F?style=for-the-badge&logo=github&logoColor=white)](README.md) [![Resume](https://img.shields.io/badge/Resume-2--page_PDF-176B5B?style=for-the-badge)](output/pdf/Hemant_Kumar_Resume.pdf) [![Telegram](https://img.shields.io/badge/Telegram-%40heman4t-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/heman4t)

</div>

**Jump to:** [At a glance](#at-a-glance) · [AI & LLM](#ai-and-llm-engineering) · [HariDream](#haridream--ai-and-meta-apis-in-lending) · [AVS Holidays](#avs-holidays--speech-analytics) · [Products & tooling](#products-and-developer-tooling) · [Platforms](#platforms-and-integrations) · [Infrastructure](#infrastructure-and-operations) · [Web platforms](#web-platforms-for-organisations) · [Earlier work](#earlier-engineering) · [Open source](#open-source-contributions)

## At a glance

| Area | Highlights | Years |
|---|---|---|
| **AI & LLM engineering** | 100+ tool MCP server, offline RAG, retrieval-honesty evals, multi-agent development | 2026–now |
| **HariDream** | ERPNext lending platform over 74M records, WhatsApp + OpenAI, Meta Marketing & Conversions APIs | 2025–now |
| **AVS Holidays** | Self-hosted speech analytics: Canary-1B ASR, silero-vad, GPU inference | 2025 |
| **Products & tooling** | VS Code / JetBrains extension for LLM context, Flutter libraries, ERP products | 2022–now |
| **Platforms & integrations** | Travel booking on Cloudflare Workers, SMS gateway, flight and hotel APIs | 2024–now |
| **Infrastructure** | 2,100+-commit Ansible codebase, monitoring, deployment tooling, performance tuning | 2022–now |
| **Web platforms** | Society portals, payment integration, attendance sync, booking apps | 2023–2025 |
| **Earlier engineering** | Home automation & IoT, computer vision, education software, mobile apps | 2010–2023 |

---

## AI and LLM engineering

### Source-bound prediction engine · *own product · Mar 2026 – now*

An astrology prediction engine where every generated claim must trace back to a verse in a classical text held in the corpus.

| | |
|---|---|
| **MCP server** | 100+ tools over stdio (Claude Code) and SSE (web clients), layered data → domain → orchestration → prediction |
| **Grounding** | CI lint gates bind each claim to a held source locator; no fabricated citations, no silent fallbacks |
| **Quality** | 11k+ tests, ruff, pyright, import-linter architecture rules, ~4,800 commits |
| **Process** | Claude Code, Codex and Gemini working concurrently under a written orchestration policy, per-agent git worktrees, ADRs |
| **Stack** | Python 3.12 · FastAPI · PostgreSQL · Anthropic & OpenAI SDKs · Docker |

### Local retrieval and agent evaluation · *2026*

| | |
|---|---|
| **Offline semantic memory** | MCP retrieval service on Ollama `nomic-embed-text` embeddings over an allow-listed corpus; fails closed, nothing leaves the machine |
| **Retrieval-honesty evals** | 34 deterministic cases on Prime Intellect verifiers: decoy rejection, missing-source handling, verbatim-quote checks, trace-grounded tool-use credit |

---

## HariDream · AI and Meta APIs in lending

Microfinance lending platform. Main author across the applications below; ERPNext is the hub, with AI and Meta's APIs inside the workflows.

| Project | When | What I built |
|---|---|---|
| **Loan-management ERP** | 2025–2026 | Frappe/ERPNext app reading 74M applicant and credit-bureau records from Elasticsearch through virtual DocTypes; role and territory access, PII masking, audit logs, Docker deployment |
| **WhatsApp Business app** | 2026 | Meta WhatsApp Cloud API (Graph API v25): templates, interactive messages, broadcasts, webhooks, catalog and flows; leads created and assigned in ERPNext |
| **AI auto-replies** | 2026 | OpenAI replies using conversation history and lead context; Hinglish, EMI and eligibility maths, human hand-off, guardrails against approval promises and credential requests |
| **Vision KYC** | 2026 | OpenAI Vision reads identity documents sent on WhatsApp; pattern validation, private attachments, retention-based deletion |
| **Meta audience sync** | Oct 2026 | Marketing API custom audiences from 10M+ bureau records and ERP leads; idempotent delta-sync, SHA-256-hashed identifiers, batching, backoff, exclusion audiences |
| **Loan marketplace** | 2026 | Next.js 15 / TypeScript site in Hindi and English with EMI tools, lead capture and server-side Meta Conversions API events |
| **ERP MCP interface** | 2025–2026 | MCP server exposing ERP operations to LLM agents, with a Docker bridge and validation tests |
| **Loan-data pipeline** | 2025–2026 | Python/Pydantic ingestion merging application, disbursal and bureau feeds into Elasticsearch, with enrichment and Playwright automation |
| **Desktop data sync** | 2025–2026 | PySide6 app syncing loan cases into per-product Elasticsearch indexes with upload receipts, retries, and macOS/Windows release builds |
| **AI-assisted ad production** | 2026 | Hinglish financial-literacy videos with HeyGen avatars and AI-assisted scripting, review and scene planning |

---

## AVS Holidays · speech analytics

Self-hosted platform that turns recorded multi-channel calls into **transcripts, sentiment and toxicity flags, summaries, topics and next steps**. My focus was inference and the AI services.

| Component | When | What I built |
|---|---|---|
| **Speech-analysis service** | Jan–May 2025 | NVIDIA Canary-1B ASR service with per-channel transcription and downstream analysis; FastAPI, Redis, PyTorch, Hugging Face |
| **Voice-activity detection** | Apr–May 2025 | silero-vad microservice and container packaging |
| **ASR module** | May 2025 | Inference module on the NVIDIA PyTorch base image |
| **GPU deployment** | Mar–Jun 2025 | Docker and Compose stack for running the inference services |
| **Web application** | Dec 2024–Mar 2025 | Contributions to the Next.js (T3) front end |

---

## Products and developer tooling

| Project | When | What it is | Links |
|---|---|---|---|
| **Combine with Context** | 2025 | Main author. VS Code and JetBrains extension that exports a project's code context to Markdown or a zip for LLM workflows, with filtering, file trees and undo history. TypeScript and Kotlin. | [Source](https://github.com/mohesu/combine-with-context) · [VS Code](https://marketplace.visualstudio.com/items?itemName=mohesu.combine-with-context) · [Open VSX](https://open-vsx.org/extension/mohesu/combine-with-context) · [JetBrains](https://plugins.jetbrains.com/plugin/28309-combine-with-context) |
| **Dio API Client** | 2023 | Co-author. Flutter networking library for authentication, caching, logging and error handling. | [Source](https://github.com/mohesu/dio_api_client) |
| **Flutter theme & utilities** | 2022–2023 | Shared Flutter theme, utility and model packages. | [Theme](https://github.com/mohesu/flutter_theme) · [Utilities](https://github.com/mohesu/utils) |
| **Staff-operations ERP** | Sep–Oct 2026 | Frappe, ERPNext, Frappe HR and India Compliance v16 with a custom app; staff see only their own records. | private |
| **Real-estate ERP** | Sep 2026 | Multi-tenant product for property builders: inventory, pricing, sales, bookings, collections, construction and RERA workflows; one Frappe site per builder. | private |

---

## Platforms and integrations

| Project | When | What I built |
|---|---|---|
| **[Premium Class Travel](https://premiumclasstravel.co.uk/)** | Apr 2025–now | Main author. Next.js 15 site and admin (fare search, destinations, quotes, bookings, packages) on a Cloudflare Workers API (Hono, D1/Drizzle, KV, email); Vitest, Playwright, Lighthouse CI, security headers and edge caching |
| **SMS gateway** · Nextpage | Dec 2024–Jan 2026 | Jasmin-based gateway: Docker deployment, routing, accounts and balances, billing, message priority, health probes, HAProxy, Prometheus and Grafana; plus related SMS ERP and route-trading apps |
| **Flight & hotel APIs** · Software Xprts | 2026 | Maintenance and deployment of PHP flight (Amadeus, SOAP suppliers) and hotel aggregation APIs covering search, pricing and booking flows |

---

## Infrastructure and operations

| Project | When | What I built |
|---|---|---|
| **Server automation** · Software Xprts | Jan 2022–now | Main author of a 2,100+-commit Ansible codebase provisioning and running staging and production fleets: Linux, Docker, Nginx/Apache, TLS, PHP-FPM pools, UFW, log rotation, Prometheus and Grafana |
| **Production tuning** · Nakoda | May 2026 | Cloudflare caching and HTTPS, exclusions for dynamic and payment routes, OS and web-server tuning, runbooks with rollback steps |
| **Deployment tooling** · DiscountDaddy | Dec 2023 | Docker-based [site deployment image](https://github.com/DiscountDaddy/site-deploy) and a [GitHub Action for WordPress deploys](https://github.com/DiscountDaddy/wp-site-deploy) |

---

## Web platforms for organisations

| Project | When | What I built |
|---|---|---|
| **[RSACP](https://rsacp.com/)** | Aug 2023–Sep 2026 | Society website, member portal and admin on Angular, Tailwind and Appwrite: notices, council, awards, galleries, member records, account linking and password recovery |
| **[ISA-NHQ](https://www.isaweb.in/)** | Jun 2023 | .NET 6 backend work: deployment workflows, caching and routing |
| **Goshu** | Aug–Dec 2023 | Angular 16 web app with Appwrite and Firebase, and a Node.js/Express payment service with CCAvenue handlers |
| **[Attendance sync](https://github.com/mohesu-aisin/attendance)** | Feb–Mar 2025 | Frappe app syncing attendance from Microsoft SQL Server on a schedule, with validation and error handling |
| **Roomist** | — | Hotel-booking application with inventory and booking workflows |
| **Number Wala Bhai** | — | VIP mobile-number business website and application |

---

## Earlier engineering

| Project | When | What I built |
|---|---|---|
| **Home automation & IoT** | 2014–2016 | Retrofittable wireless home automation with Teensy, XBee radios and Raspberry Pi on openHAB; an Arduino sensor-network framework; MQTT on ESP8266 · [openHAB thread](https://community.openhab.org/t/choosing-a-framework-for-arduino-sensor-net/7094) |
| **Computer vision** | 2015–2017 | Face-recognition and number-plate-recognition experiments with OpenCV, OpenFace and TensorFlow |
| **[Education information system](https://github.com/heman4t/eduis)** | 2012–2019 | PHP/Zend system with academic, admission, authentication, library and placement modules |
| **Mobile apps** | 2019–2023 | Flutter apps and plugins (SMS, audio streams, maps, HTTP caching) with Firebase and Parse back ends |
| **Solar-structure tooling** | 2026 | Python toolchain for rooftop structure design: FEM frame checks and DXF/3D drawing generation |

---

## Open-source contributions

| Project | When | Contribution |
|---|---|---|
| [agent-primer](https://github.com/itsarvinddev/agent-primer) | 2026 | Two merged PRs hardening CodeGraph MCP setup for AI coding agents · [#1](https://github.com/itsarvinddev/agent-primer/pull/1) · [#2](https://github.com/itsarvinddev/agent-primer/pull/2) |
| [frappe/telephony](https://github.com/frappe/telephony/issues/7) | 2025 | Proposed a provider-agnostic SMS and call-log layer for Frappe apps |
| [frappe/frappe_docker](https://github.com/frappe/frappe_docker/pull/1602) | 2025 | Proposed Traefik and dev-service updates |
| [barcode_scanner](https://github.com/itsarvinddev/barcode_scanner/pull/12) | 2022 | Merged UI changes |
| [flutter/samples](https://github.com/flutter/samples/pull/285) | 2020 | Merged fix |
| [OpenFace](https://github.com/cmusatyalab/openface/pull/155) | 2016 | Merged web-demo dependency update |
| [jquerySessionTimeoutHandler](https://github.com/juanperi/jquerySessionTimeoutHandler/pull/1) | 2013 | Merged fix |
| Arduino, PHP and Flutter libraries | 2012–2022 | Patches to [ArduinoJson](https://github.com/bblanchon/ArduinoJson/pull/121), [XBee](https://github.com/andrewrapp/xbee-arduino/pull/4), [dio-http-cache](https://github.com/hurshi/dio-http-cache/pull/76) and others |

---

<sub>Most of this work lives in private client repositories, so source links are given only where code is public. Dates reflect project activity. Team projects are described by my own contribution.</sub>
