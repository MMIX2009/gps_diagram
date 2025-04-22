# gps_diagram

# GPS Upload Flowchart

This project generates a flowchart using the `graphviz` Python package to represent the logic of a GPS-based data upload system. The resulting image mimics a structured, horizontally and vertically spaced flow diagram.

## 📌 Features

- Flowchart structure with conditional and process nodes
- Auto-layout using Graphviz's `dot` engine
- Outputs a PNG image (`gps_upload_flowchart.png`)
- Clean vertical orientation for readability

## 🖥️ Requirements

Ensure the following are installed inside your GitHub Codespace or local environment:

### Python Packages
```bash
pip install graphviz
```

### System Dependencies
The script depends on the Graphviz **CLI tools**, especially the `dot` binary. Install with:

```bash
sudo apt update && sudo apt install graphviz -y
```

## ▶️ Usage

To generate the diagram:

```bash
python3 script.py
```

This will produce:

```
gps_upload_flowchart.png
```

## 📁 File Structure

```
.
├── script.py                # Python script that generates the flowchart
├── gps_upload_flowchart.png  # Output PNG (after running script)
└── README.md                # This file
```

## 🧠 Logic Summary

The flowchart captures logic such as:
- Initialization of GPS and serial interfaces
- Validation of GPS data
- Conditional upload triggers based on time and GPS state
- Handling offline data sync and success/failure outcomes

## 🔄 Future Ideas

- Convert into an interactive Streamlit app
- Output SVG or PDF versions
- Parametrize node contents or layout

---

**Author:** [MMIX2009]  
**License:** MIT
