# Oscar Films Streaming Analysis

This project develops an end‑to‑end ETL pipeline designed to collect, clean, and integrate multiple film datasets into a unified structure suitable for relational analysis. The pipeline brings together movie metadata, Oscar Awards data, and streaming availability to enable deeper insights into how film characteristics relate to award recognition and platform distribution.

The workflow extracts raw information from multiple APIs and datasets, applies transformations to standardize formats, resolve inconsistencies, and enrich the data, and then loads the cleaned output into an Azure SQL Database for analysis and reporting.

**Objectives**

- Build a reproducible, automated data integration pipeline that consolidates film‑related information from heterogeneous sources.

- Create a unified dataset that supports analysis of how genre, runtime, ratings, and other attributes correlate with award nominations and wins.

- Examine how award‑nominated films are distributed across major streaming platforms and whether availability patterns emerge.

- Prepare the integrated dataset for downstream SQL analysis, visualization, and reporting.

**Pipeline Overview**

- **_Extract:_** Retrieve raw film, award, and streaming data from public APIs and structured datasets.

- **_Transform:_** Clean and standardize fields, normalize categorical values, handle missing data, and create relational keys across datasets.

- **_Load:_** Insert the processed data into an Azure SQL relational schema optimized for querying and cross‑dataset joins.




## Setup Instructions

### Installation

1. **Clone or download this repository**
```bash
   cd path/to/project
```

2. **Create a virtual environment (recommended)**
```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
```

3. **Install required packages**
```bash
   pip install -r requirements.txt
```


### Running the Code
```bash
python pipeline.py
```

## Dependencies
- **pandas**: Data manipulation and analysis
- **IMDbPY**: Access to IMDb movie database
- **simple-justwatch-python-api**: Streaming availability data
