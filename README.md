# ASH 2025 B-Cell Lymphoma Updates

[![Publish to GitHub Pages](https://github.com/htlin222/ASH-MCL/actions/workflows/publish.yml/badge.svg)](https://github.com/htlin222/ASH-MCL/actions/workflows/publish.yml)

Quarto Reveal.js presentation covering practice-changing advances in B-cell lymphoma from ASH 2025.

**Live Presentation:** [htlin222.github.io/ASH-MCL](https://htlin222.github.io/ASH-MCL/)

## Topics Covered

### Mantle Cell Lymphoma (MCL)

- **GLPG5101**: Next-gen CAR-T with 7-day vein-to-vein manufacturing (100% ORR, 96% CR)
- **ECHO Trial**: Acalabrutinib + BR for frontline MCL (FDA approved Jan 2025)
- **BOVen**: Chemo-free triplet for TP53-mutant MCL (72% 2-year PFS)
- **MAVO**: Acalabrutinib + Venetoclax + Obinutuzumab
- **Pirtobrutinib**: Non-covalent BTKi for cBTKi-refractory disease

### Marginal Zone Lymphoma (MZL)

- **Liso-cel**: First CAR-T approved for MZL (FDA Dec 4, 2025)
- **BGB-16673**: BTK degrader for BTKi-resistant disease
- **Evorpacept**: CD47 blockade + R² for frontline iNHL

### Waldenström Macroglobulinemia (WM)

- **Pirtobrutinib + Venetoclax**: Fixed-duration therapy (100% ORR)
- **Loncastuximab Tesirine**: ADC for high-risk WM (100% response in TP53-altered)

## Features

- Interactive Reveal.js slides with R-generated visualizations
- Speaker notes in Traditional Chinese (繁體中文)
- Simplemenu navigation
- Auto-generated agenda

## Local Development

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/)
- R with packages: ggplot2, dplyr, tidyr, scales, knitr, rmarkdown

### Render

```bash
quarto render index.qmd
```

### Preview

```bash
quarto preview index.qmd
```

## Author

**林協霆**
和信治癌中心腫瘤內科部

## License

Content is for educational purposes. Clinical trial data sourced from ASH 2025 abstracts, FDA.gov, and peer-reviewed publications.
