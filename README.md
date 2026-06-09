<div align="center">
  <h1>Analyzing Customer Behavior for E-commerce Insights</h1>
  <p>This repository contains an analytical and machine learning pipeline. The project simulates an e-commerce platform, processes transactional and clickstream data, engineers high-order behavioral features, builds a predictive customer churn model with explainable AI (SHAP), and implements a real-time big data streaming pipeline simulation using Apache Kafka mechanics.</p>
</div>

## Preview
<img width="900" height="750" alt="confusion_matrix" src="https://github.com/user-attachments/assets/4a0bc785-70e8-4bbc-9701-fb7e7669b4a6" />
<img width="2671" height="1672" alt="insights_dashboard" src="https://github.com/user-attachments/assets/7210c93e-b82e-4404-9375-d8e40e10c18e" />



## 🚀 Getting Started & Execution Guide
Follow these sequential steps to set up the environment and run the entire implementation pipeline from scratch.  
### Clone or Extract the Directory
   Ensure all scripts are placed within the same working directory on your local file system.
### Set Up a Virtual Environment & Install Dependencies
  It is highly recommended to use a clean virtual environment (venv or conda) to isolate dependencies. 
  #### On Windows
  ```bash
# Create a fresh virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install all required libraries in one command
pip install -r requirements.txt
```
#### On MAC/Linux
```bash
# Create a fresh virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install all required libraries in one command
pip install -r requirements.txt
```

## 3. Generate the Synthetic Dataset
Before opening the Jupyter notebook, run the pipeline's data ingestion layer once to populate the raw data baselines.
```bash
python dataset_generator.py
```
## 4. Execute the Analytical Pipeline
Launch Jupyter Notebook or your preferred interactive environment (e.g., VS Code Jupyter Extension) and open the primary workbook
```bash
jupyter notebook ecommerce_analysis.ipynb
```
Select Kernel ➔ Restart & Run All to run the cells sequentially.




---------------------------------------------------------------------------------------------------------------------------------------------------------------
## 📁 Submission Directory Structure

```bash
├── dataset_generator.py            # Script to generate raw transactional & behavioral data
├── ecomm-notebook.ipynb            # Main interactive notebook (EDA, Features, ML, Kafka, Visuals)
├── requirements.txt                # Python package dependency manifest
├── README.md                       # Setup instructions and project overview (This file)
└── data-bin/                       # Generated automatically by dataset_generator.py (Ignored by git)
    ├── customers.csv               # Demographic profiles and loyalty tiers
    ├── products.csv                # SKU data and item pricing
    ├── browsing.csv                # Raw user clickstream and session micro-metrics
    └── purchases.csv               # Transactional history and payment logs
```
## 📝 Contact & Candidate Details
Candidate Name: Gordon D.K. Atsunyo

Role Assessment: Intelligent Systems & Security Officer 

Target Company: Npontu Technologies 

Submission Date: 9th June 2026


![Build Status](https://img.shields.io/github/actions/workflow/status/username/repo/main.yml)
![License](https://img.shields.io/github/license/username/repo)
