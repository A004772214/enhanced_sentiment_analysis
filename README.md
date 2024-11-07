# Enhanced Sentiment Analysis

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

This project leverages the Python sentiment analysis library Pysentiment and extends its capabilities by incorporating additional sentiment categories.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About the Project

This project leverages the Python sentiment analysis library Pysentiment and extends its capabilities by incorporating additional sentiment categories, including "Uncertainty" and "Litigious". It also integrates the Loughran-McDonald Dictionary for more specialized financial and economic sentiment analysis. Additionally, the project includes a feature to count the total number of words in the analyzed text files, resulting in a more comprehensive and detailed sentiment analysis outputs.

### Prerequisites

Required python libraries: Pysentiment2, pandas, nltk, abc, re, numpy, os  
Python version: 3.11

### Installation

Step-by-step instructions to install the project:

```bash
# Clone the repository
git clone https://github.com/A004772214/enhanced_sentiment_analysis.git

# Navigate to the project directory
cd enhanced_sentiment_analysis

# Install dependencies
pip install -r requirements.txt
```

### Usage

Instructions on how to use the project:
```python

**Import necessary blocks**
from lm import LM
import datetime
import os
import csv


**Example usage**
# Replace with your file path
start_time = datetime.datetime.now()  
ca_pdf_path = "Your_file_path"  
header_written = False

# Replace with your file name
csv_file = root + "//" + "Your_file_name.csv"
```
### Features

List of key features of the project:

- Sentiment Analysis: Detects positive, negative, and neutral sentiments.
- Extended Sentiments: Includes categories like "Uncertainty" and "Litigious".
- Word Count: Calculates the total number of words in the analyzed text.
- Loughran-McDonald Dictionary: Integration for financial sentiment analysis.

### Contributing

Instructions for contributing to the project:

**Fork the repository to your GitHub account**

**Clone your forked repository**  
git clone https://github.com/A004772214/enhanced_sentiment_analysis.git

**Create a new branch for your changes**  
git checkout -b feature/YourFeatureName

**Make changes and commit**  
git add .  
git commit -m "Add YourFeatureName"

**Push your changes to GitHub**  
git push origin feature/YourFeatureName

**Open a pull request to the main repository**  

### Contact

Project Link: https://github.com/A004772214/enhanced_sentiment_analysis
