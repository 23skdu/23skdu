<!-- weather:start -->
```mermaid
%%{init: {'flowchart': {'nodeSpacing': 10, 'rankSpacing': 8, 'padding': 6}}}%%
flowchart TB
    subgraph top[" "]
        T["🎄 Seattle · 47.6062 N, 122.3321 W"]
    end
    subgraph r1[" "]
        direction LR
        N["🌤️ Now: 56 F\nPartly cloudy"]
        D1["Sun · 51/42 F\n🌦️ Drizzle"]
        N ~~~ D1
    end
    subgraph r2[" "]
        direction LR
        D2["Mon · 52/41 F\n🌦️ Drizzle"]
        D3["Tue · 50/41 F\n🌤️ Partly cloudy"]
        D2 ~~~ D3
    end
    top ~~~ r1 ~~~ r2
    classDef hdr fill:#B45309,stroke:#FCD34D,stroke-width:2px,color:#FFFBEB
    classDef red fill:#B91C1C,stroke:#FBBF24,stroke-width:2px,color:#FFFBEB
    classDef grn fill:#166534,stroke:#FBBF24,stroke-width:2px,color:#ECFDF5
    class T hdr
    class N,D3 red
    class D1,D2 grn
    style top fill:none,stroke:none
    style r1 fill:none,stroke:none
    style r2 fill:none,stroke:none
```
<!-- weather:end -->

[![Lint](https://github.com/23skdu/23skdu/actions/workflows/lint.yml/badge.svg)](https://github.com/23skdu/23skdu/actions/workflows/lint.yml)

## About

I'm a DevOps/Site-Reliability Engineer who builds high-performance systems and developer tooling, with a focus on observability
