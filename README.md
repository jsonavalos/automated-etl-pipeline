# Oscar Films Streaming Analysis

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