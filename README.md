<div align="center">

# Hemant

**AI/LLM engineer · MCP servers, RAG, agents and evals · Python/FastAPI · founder of [Mohesu](https://www.mohesu.com)**

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1200&color=2F81F7&center=true&vCenter=true&width=640&lines=LLM+systems+that+show+their+sources;MCP+servers+%C2%B7+local+RAG+%C2%B7+agent+evals;WhatsApp+%2B+Meta+APIs+%2B+OpenAI+in+ERPNext;14%2B+years+of+web%2C+mobile+and+infrastructure" alt="LLM systems that show their sources · MCP servers, local RAG, agent evals · WhatsApp + Meta APIs + OpenAI in ERPNext · 14+ years of web, mobile and infrastructure" />

<sub>heman4t · Rohtak, India (IST) · open to opportunities</sub>

</div>

I build LLM systems that have to show their sources: MCP servers, local RAG, agent workflows, and the eval harnesses that check whether an agent really used them. I also wire AI into business systems: OpenAI and Meta's APIs inside ERPNext for a lending platform. Underneath: Python, FastAPI, PostgreSQL, Elasticsearch. Around it: Docker, Ansible, Cloudflare. Behind it: 14+ years of web, mobile, automation and infrastructure work.

**Secure-agent practices, as applied:** fail-closed retrieval · allow-listed corpora · no data egress to hosted services for sensitive corpora · customer PII SHA-256-hashed before it reaches Meta · prompt-level guardrails on customer-facing AI · PII masked by role · no model output treated as evidence until verified.

## Now

**Source-bound prediction engine** — my own product, since March 2026. Every predictive claim must trace to a verse in a classical text we hold (the domain is Vedic astrology); lint gates in the build bind each verse claim to a held locator, never a URL. No fabricated citation, ever. No fallbacks: raise instead. Python 3.12, FastAPI, PostgreSQL, Anthropic and OpenAI SDKs.

- **100+ tool MCP server**: stdio for Claude Code, SSE for web clients; tools layered data → domain reads → orchestration → prediction → utilities.
- **Local RAG for the coding agents**: an offline semantic-memory MCP server used by Codex and Claude Code, on Ollama `nomic-embed-text` embeddings over an allow-listed corpus. No query or document leaves the machine; the index fails closed.
- **Retrieval-honesty evals**: 34 deterministic golden cases on Prime Intellect verifiers v1. Decoys must be rejected, a missing source must fail closed, and tool-use credit is trace-grounded, so guessed evidence earns none.
- **Multi-agent engineering**: Claude Code, Codex and Gemini (Antigravity) work the repo concurrently under a written orchestration policy, with a git worktree per agent and decisions recorded as ADRs. Checked mechanically: 11k+ tests, ruff, pyright, import-linter.

## AI and Meta APIs in production — HariDream

A microfinance lending platform where I am the main author across the stack (2025–2026). ERPNext is the hub; AI and Meta's APIs sit inside the workflows.

- **WhatsApp Business app for ERPNext** on Meta's WhatsApp Cloud API (Graph API v25): templates, interactive messages, broadcasts, webhooks, catalog and flows, with leads created and assigned inside ERPNext.
  - **AI auto-replies (OpenAI)** with the customer's history and lead profile as context, replies in Hinglish when the customer writes that way, EMI and eligibility maths, and guardrails: never promise approval, never ask for an OTP or password, hand off to a human on request.
  - **KYC by OpenAI Vision**: identity documents sent on WhatsApp are read, validated with pattern checks, attached privately to the lead and deleted on a retention schedule.
- **Meta Ads audiences from the ERP**: Marketing API custom audiences built from 10M+ bureau records and WhatsApp leads. Idempotent delta-sync with SHA-256-hashed phones, batching and rate-limit backoff; conversions move people into exclusion audiences. No raw PII leaves the system.
- **Meta Conversions API** on the Next.js 15 loan marketplace: server-side events from an edge route, customer data hashed to Meta's spec.
- **Loan-management ERP on Frappe/ERPNext** reading 74M applicant records from Elasticsearch through virtual DocTypes, with role-scoped access, PII masking and audit logs; plus an **MCP server** that exposes ERP operations to LLM agents.
- **Data pipelines into Elasticsearch**: loan-application, disbursal and credit-bureau feeds merged and enriched (Python, Pydantic, Playwright), and a Qt desktop syncer with validated uploads and zero-data-loss guards.

## Selected work

- **Self-hosted speech analytics** — AVS Holidays, 2025, where I focused on inference and the AI services. NVIDIA Canary-1B ASR and silero-vad on GPU behind a FastAPI/Redis job pipeline, deployed with Docker Compose. Recorded multi-channel calls become transcripts, sentiment and toxicity flags, summaries, topics and next steps.
- **Travel booking platform** for a UK agency: Cloudflare Workers API (Hono, D1/Drizzle, KV) and a Next.js 15 front end, tested with Vitest, Playwright and Lighthouse CI. Main author.
- **Server automation**: main author of a 2,100+-commit Ansible codebase (since 2022) that provisions and runs staging and production Linux fleets: Docker, Nginx/Apache, TLS, PHP-FPM pools, UFW, Prometheus and Grafana.
- **ERP products on Frappe/ERPNext v16** at Mohesu: custom apps, multi-tenant, Docker.

## Open source

- **[combine-with-context](https://github.com/mohesu/combine-with-context)** — main author. VS Code and JetBrains extension that exports a project's code context to clean Markdown for LLM workflows.<br>
  [![VS Code Marketplace](https://img.shields.io/badge/VS%20Code-Marketplace-007ACC?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=mohesu.combine-with-context) [![Open VSX](https://img.shields.io/open-vsx/dt/mohesu/combine-with-context?style=flat-square&label=Open%20VSX)](https://open-vsx.org/extension/mohesu/combine-with-context) [![JetBrains](https://img.shields.io/jetbrains/plugin/d/28309-combine-with-context?style=flat-square&label=JetBrains)](https://plugins.jetbrains.com/plugin/28309-combine-with-context)
- **[agent-primer](https://github.com/itsarvinddev/agent-primer)** — two merged PRs ([#1](https://github.com/itsarvinddev/agent-primer/pull/1), [#2](https://github.com/itsarvinddev/agent-primer/pull/2)) hardening its CodeGraph MCP setup for AI coding agents.
- **[frappe/telephony](https://github.com/frappe/telephony/issues/7)** — proposed a provider-agnostic telephony layer (SMS and call logs over hooks) for Frappe apps.
- **Since 2012**: small fixes to [flutter/samples](https://github.com/flutter/samples/pull/285), [openface](https://github.com/cmusatyalab/openface/pull/155), ArduinoJson, XBee and Flutter plugins. The Mohesu team also maintains six Flutter packages on pub.dev as verified publisher mohesu.com.

## Earlier: home automation and IoT

From 2014 to 2016 I built a retrofittable wireless home-automation system (Teensy + XBee radios + Raspberry Pi on [openHAB](https://community.openhab.org/u/heman4t)) and an Arduino sensor-network framework. Alongside it: MQTT on ESP8266, Home Assistant, GPS tracking, and face-recognition and number-plate experiments with OpenCV and TensorFlow. Before that, PHP/Zend, WordPress and Selenium automation.

## Stack

<table>
  <tr>
    <td><b>AI / LLM</b></td>
    <td>
      <img src="https://img.shields.io/badge/Anthropic-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic" />
      <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square" alt="OpenAI" />
      <img src="https://img.shields.io/badge/MCP-0B0B0B?style=flat-square&logo=modelcontextprotocol&logoColor=white" alt="Model Context Protocol" />
      <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" alt="Ollama" />
      <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" />
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
    </td>
  </tr>
  <tr>
    <td><b>Integrations</b></td>
    <td>
      <img src="https://img.shields.io/badge/Meta%20Graph%20API-0467DF?style=flat-square&logo=meta&logoColor=white" alt="Meta Graph API" />
      <img src="https://img.shields.io/badge/WhatsApp%20Cloud%20API-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="WhatsApp Cloud API" />
      <img src="https://img.shields.io/badge/Frappe%20%2F%20ERPNext-0089FF?style=flat-square&logo=erpnext&logoColor=white" alt="Frappe / ERPNext" />
      <img src="https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white" alt="Elasticsearch" />
    </td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td><img src="https://skillicons.dev/icons?i=py,fastapi,postgres,redis,ts,nodejs,php" height="36" alt="Python, FastAPI, PostgreSQL, Redis, TypeScript, Node.js, PHP" /></td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td><img src="https://skillicons.dev/icons?i=nextjs,react,angular,tailwind,flutter" height="36" alt="Next.js, React, Angular, Tailwind, Flutter" /></td>
  </tr>
  <tr>
    <td><b>Infra</b></td>
    <td><img src="https://skillicons.dev/icons?i=docker,ansible,cloudflare,linux,nginx,githubactions" height="36" alt="Docker, Ansible, Cloudflare, Linux, Nginx, GitHub Actions" /></td>
  </tr>
  <tr>
    <td><b>IoT</b></td>
    <td><img src="https://skillicons.dev/icons?i=raspberrypi,arduino,opencv" height="36" alt="Raspberry Pi, Arduino, OpenCV" /></td>
  </tr>
</table>

## Activity

<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=heman4t&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true" />
    <img height="165" alt="GitHub stats for heman4t" src="https://github-stats-extended.vercel.app/api?username=heman4t&show_icons=true&theme=default&hide_border=true&count_private=true&include_all_commits=true" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=heman4t&theme=tokyonight&hide_border=true" />
    <img height="165" alt="GitHub contribution streak for heman4t" src="https://streak-stats.demolab.com?user=heman4t&theme=default&hide_border=true" />
  </picture>
</p>

<sub>2,700+ contributions in the past year, almost all in private client and product repos.</sub>

## Contact

**[Telegram](https://t.me/heman4t)** (fastest) · [LinkedIn](https://www.linkedin.com/in/heman4t) · [X](https://x.com/heman4t) · [YouTube](https://www.youtube.com/@heman4t) · [mohesu.com](https://www.mohesu.com)
