# Francisco Angulo de Lafuente

An evidence-led public profile for the Spanish author, researcher and open-source developer Francisco Angulo de Lafuente.

This repository is a documentation project, not a scientific claim registry or an endorsement page. It separates public evidence from personal descriptions and avoids presenting unverified awards, performance claims, affiliations or quotations as established facts.

## At a glance

- **Open-source focus:** AI systems, research tooling, reproducible experimentation and developer documentation.
- **Research themes:** sustainable biotechnology, biofuels, optical and holographic computing, scientific communication and human-centred AI.
- **Creative work:** science fiction, speculative technology and environmental themes.
- **Working principle:** publish useful artifacts, document evidence and make uncertainty visible.

## Public research and engineering record

### ECOFA and sustainable biotechnology

Public material about the ECOFA project describes a biofuel research programme involving bacterial processing of organic waste. The historical article is preserved as a source for the project description; this profile does not independently validate its experimental performance, patent scope or priority claims.

- [Historical ECOFA article in Revista Ambienta](https://www.revistaambienta.es/content/dam/revistaambienta/files-1/Revista-Ambienta/AMBIENTA/83/Ambienta_2008_83_a9.pdf)
- [Author catalogue on Bubok](https://www.bubok.es/autores/angulo)

### Open-source AI and research tooling

The public GitHub portfolio contains projects exploring holographic representations, agent systems, scientific writing and reproducible research. Repository descriptions are project documentation; they are not independent validation of scientific performance.

| Project | Purpose documented by the project | Link |
| --- | --- | --- |
| Unified Holographic Neural Network | Experimental holographic and optical-neural-network concepts | [GitHub repository](https://github.com/Agnuxo1/Unified-Holographic-Neural-Network) |
| P2PCLAW | Open research workflows, peer review and provenance | [GitHub repository](https://github.com/Agnuxo1/P2PCLAW) |
| CAJAL | Scientific paper and research-agent tooling | [GitHub repository](https://github.com/Agnuxo1/CAJAL) |
| EnigmAgent | Agent-oriented research and automation experiments | [GitHub repository](https://github.com/Agnuxo1/EnigmAgent) |
| JEV-Orchestrator | Deterministic orchestration and model-routing experiments | [GitHub repository](https://github.com/Agnuxo1/JEV-Orchestrator) |

The projects above are linked for discovery. This profile does not claim upstream adoption, endorsement, interoperability certification or production readiness for any third-party system.

## Literary work

Public catalogues list science-fiction and speculative-fiction titles associated with Francisco Angulo de Lafuente, including *Star Wind*, *ApocalipsIA* and *Shanghai 3*. Edition names, languages and availability can change; use the linked catalogues for current bibliographic information.

- [Bubok author catalogue](https://www.bubok.es/autores/angulo)
- [Lulu author page](https://www.lulu.com/es/spotlight/Angulo)
- [TodoTusLibros author catalogue](https://www.todostuslibros.com/autor/francisco-angulo-lafuente)
- [Casa del Libro author catalogue](https://www.casadellibro.com/libros-ebooks/francisco-angulo/124109)
- [Apple Books: La invasión de las medusas mutantes](https://books.apple.com/ar/book/la-invasión-de-las-medusas-mutantes/id6471918272)

## Contest and award claims

The [official NVIDIA and LlamaIndex Developer Contest page](https://developer.nvidia.com/llamaindex-developer-contest) documents the contest and its submission criteria. A [NVIDIA Developer Forums post](https://forums.developer.nvidia.com/t/winner-nvidia-and-llamaindex-developers-2024/317943) records a personal account concerning an EUHNN winner notification. Because those sources do not establish a final award outcome for this profile, this repository does **not** state that an official prize was finally awarded.

## Evidence policy

Each statement in this profile is intentionally scoped:

1. **Primary or catalogue source:** linked to an official repository, publisher, catalogue or event page.
2. **Historical public source:** linked to an archived article or first-person account and labelled accordingly.
3. **Project documentation:** describes what an open-source repository says it does; it is not a peer-review result.
4. **Unknown or changing information:** omitted or described as time-dependent rather than guessed.

The maintained source ledger is [docs/SOURCES.md](docs/SOURCES.md). The offline validation suite checks that the profile stays structured, link-complete and free of unsupported superlative claims.

## Development

Run the deterministic validation locally with Python 3.12 or newer:

```text
python scripts/validate_profile.py
python -m unittest discover -s tests -v
python -m scripts.benchmark_profile
```

The workflow in `.github/workflows/ci.yml` runs the validation and tests on supported Python versions and operating systems. The benchmark measures 100 repeated offline validations; it is a regression signal for documentation integrity, not a claim about scientific or model performance. No credentials, network access or paid services are required.

## License and contribution

The repository is distributed under the [Apache License 2.0](LICENSE). Corrections are welcome when they include a durable, public source. Please do not add private contact details, fabricated quotations, unsupported rankings or claims of third-party adoption.
