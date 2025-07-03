## .gitignore
__pycache__/
*.pyc
.env
*.db
*.sqlite
.DS_Store
.vscode/
.idea/


## requirements.txt
yfinance
pandas
sqlalchemy
schedule
python-dotenv


## README.md
# 📊 Live Stock Market Dashboard – Power BI + Python

A real-time stock market dashboard project that combines **Power BI**, **Python**, and **SQL** to show minute-wise live price movement, volume, and trends.

---

## 🔧 Tech Stack
- Python (for fetching live stock data using `yfinance`)
- Power BI (dashboard & data visualization)
- SQL Database (for storing stock data)
- GitHub (project version control)

---

## 📂 Folder Structure
```
stock-dashboard-project/
|
├── dashboard/
│   └── stock_dashboard.pbix         # Power BI dashboard file
|
├── scripts/
│   ├── fetch_and_store.py           # Python script for fetching stock data
|
├── .gitignore                       # Ignore files/folders
├── requirements.txt                 # Python package list
└── README.md                        # Project documentation
```

---

## 🌐 Features
- Fetches **live 1-minute interval data** for selected stocks (e.g. TCS, HDFCBANK, RELIANCE)
- Dashboard with dynamic slicers (e.g. Today, Last 5 Days, Last 1 Month)
- Percentage change, volume analysis, and intraday trend line
- Integrated market hours check (9:15 AM to 3:30 PM)
- Designed for Power BI Service with scheduled refresh support

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/stock-dashboard-powerbi.git
cd stock-dashboard-powerbi
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Python Script
```bash
python scripts/fetch_and_store.py
```
*(This will fetch live stock data and insert it into your SQL database)*

### 4. Launch the Power BI Dashboard
- Open `dashboard/stock_dashboard.pbix` using Power BI Desktop
- Configure your SQL connection if needed
- Interact with dynamic slicers (e.g. date range, stock selection)

---

## 📸 Dashboard Preview
![dashboard_img](https://github.com/user-attachments/assets/6e2aa846-ff6c-4b15-8756-9a95801320ae)




---

## 🚧 Roadmap
- [x] Live 1-minute interval stock data fetcher
- [x] Power BI dashboard with dynamic visuals
- [ ] Deploy Python script to cloud (Railway / GCP / Render)
- [ ] Auto-refresh dashboard in Power BI Service
- [ ] Add email alerts using Power Automate

---

## 📚 License
This project is open-source and available under the **MIT License**.

---

Made with ❤️ by **Sahil Rawat**
