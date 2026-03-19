# Car Dealer MCP Server

This project implements an MCP (Model Context Protocol) server for a car dealership use case.  
The goal is to provide useful, data-driven insights about cars that help sales representatives highlight positive features and recommend vehicles to customers.

---

## Features

The MCP server exposes several tools based on the automobile dataset:

- **Highest horsepower cars**  
  Identify cars with powerful engines for performance-focused customers.

- **Most fuel-efficient cars**  
  Recommend vehicles with low fuel consumption for cost- and environment-conscious buyers.

- **Power-to-weight ratio cars**  
  Highlight cars that balance performance and weight, offering a more responsive driving experience.

- **Cars by origin**  
  Provide insights into regional differences in performance and efficiency.

All tools are designed to support **sales-oriented recommendations**.

---


## Tech Stack

- Python 3.11  
- pandas  
- MCP SDK (`mcp[cli]`)  
- Docker  

---

## How to Run the Project
> Note: Python 3.11 is required to run the MCP server locally.

### 1. Clone the repository

```bash
git clone https://github.com/tirilsjoberg/car-dealer-mcp.git
cd car-dealer-mcp

```

---

### 2. Run with Docker (recommended)

```bash
docker compose up --build
```

This will:
- build the Docker image
- install all dependencies
- start the MCP server

---

### 3. Run locally (optional)

Make sure Python 3.11 is installed, then run:

```bash
pip install -r requirements.txt
python3.11 server.py
```

---

## MCP Client (Claude)

The server is designed to be used with an MCP-compatible client such as **Claude Desktop**.

Example prompts:
- "Show me cars with the highest horsepower"
- "Which cars are the most fuel efficient?"
- "Show me cars with the best power-to-weight ratio"

Claude will automatically select the correct tool and retrieve data from the MCP server.

---


## Use Case

This system is designed for a **car dealer** who wants to:

- highlight positive aspects of vehicles  
- tailor recommendations to customer preferences  
- use data to support sales conversations  

---

## Exploratory Data Analysis (EDA)

An exploratory analysis of the dataset is included in `eda.md`.

Key findings:
- Trade-off between horsepower and fuel efficiency  
- American cars dominate the high-performance segment  
- Japanese and European cars are more fuel efficient  
- Heavier cars tend to have higher horsepower but lower efficiency  
- Power-to-weight ratio highlights more balanced vehicles  

These insights are used to design the MCP tools.

---

