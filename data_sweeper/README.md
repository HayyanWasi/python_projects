# 💿 Data Sweeper

A Streamlit-powered web application for transforming files between CSV/Excel formats with built-in data cleaning and visualization capabilities.

![image](https://github.com/user-attachments/assets/a641804f-c6e9-4a42-bfec-d748efbead31)


## 🌟 Features

- **Multi-File Processing**
  - Handle multiple CSV/XLSX files simultaneously
  - Support for mixed file type uploads
- **Data Transformation**
  - CSV ↔ Excel bidirectional conversion
  - Column selection interface
- **Data Cleaning Tools**
  - Duplicate removal
  - Missing value imputation (numeric columns)
- **Data Visualization**
  - Automatic numeric column preview
  - Interactive bar charts
- **File Management**
  - File size display
  - Data preview (first 5 rows)
  - Instant download converted files

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
git clone https://github.com/your-username/data-sweeper.git
cd data-sweeper
pip install streamlit pandas openpyxl
