 


```bash
Main()
├── collection()
├── analysis()
└── storage()
```

```bash
Main()
├── API Collection module
│   └── Filtering and Collection
├── AI/LLM Analysis Module
│   ├── Analysis
│   └── Categorization
└── Storage Module
    ├── Integrity check
    └── Forensic Package
```

```bash
run_main()
├── collection()
│   └── saves query as .json
├── load json_dump from file
└── loop(raw_item in json_dump)
    ├── collect_item(raw_item)
    │   └── returns raw_json, col_log
    ├── analysis(raw_json)
    │   └── returns analysis_json, ana_log
    └── evidence_storage(raw_json, analysis_json, col_log, ana_log)
        └── returns forensic_package
```

```bash
collect_item(raw_item)
├── add_chain_of_custody_entry()
│   ├── action="collected"
│   └──performed_by="collection_module"
├── col_log = [ chain_of_custody_entry ]
└── returns raw_item, col_log
```
```bash
chain_of_custody.py
├── utc_now()
│   └── returns timestamp
└── add_chain_of_custody_entry(action, performed_by)
    ├── calls utc_now()
    ├── build JSON:
    │   ├── timestamp
    │   ├── action
    │   └── performed_by
    └── returns chain_of_custody_entry
```
```bash
evidence_storage(raw_json, analysis_output, col_log, ana_log)
├── integrity checks
│   └──compare hash 
├── add_chain_of_custody_entry()
│   ├── action="stored"
│   └──performed_by="storage_module"
├── merge chain‑of‑custody logs
│   └── final_chain = col_log + ana_log + storage_log
└── build forensic_package (JSON)
    ├── raw_json
    ├── analysis_output
    ├── hashes
    └── chain_of_custody
```
```bash
collection(link)
├── get video from link
│   ├── get metadata
│   └── hash vid
├── get comments(x)
│   ├── get metadata
│   └── get hash
└── build raw_json
    ├── video metadata
    ├── comments
    └── hashes
```
```bash
analysis(raw_json)
├── LLM Promt
│   ├── pass raw JSON in
│   ├── specify LLM JSON output   
│   └── get analysis_output
├── add_chain_of_custody_entry()
│   ├── action="analysis"
│   └──performed_by="analysis_module"
└── return nalysis_output
```
```bash
Methodology
├── Filtering
├── Collection
├── Analysis
├── Categorisation
└── Storage
```
```bash
Methodology
├── Collection
├── Analysis
└── Storage
```

```bash
collect_item(raw_item)
├── add_chain_of_custody_entry()
│   ├── action="collected"
│   └──performed_by="collection_module"
├── col_log = [ chain_of_custody_entry ]
└── returns raw_item, col_log
```

