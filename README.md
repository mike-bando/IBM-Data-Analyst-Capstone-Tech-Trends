# IBM Data Analyst Capstone: End-to-End Tech Trends Analysis

## 🌟 Project Overview
This project is the culmination of the **IBM Data Analyst Professional Certificate**. It demonstrates a complete data lifecycle: from automated data collection (APIs & Web Scraping) and advanced data wrangling with Python, to professional business intelligence dashboarding using IBM Cognos Analytics.

## 🚀 Key Competencies & Skills
In addition to data collection, this project implements advanced analytical workflows:
* **Data Collection:** Automated retrieval via `requests` (APIs) and `BeautifulSoup` (Web Scraping).
* **Advanced Data Wrangling:** Normalizing multi-select survey responses using the **Pandas `explode()` method** to ensure granular analysis of technology stacks.
* **Business Intelligence:** Designing interactive, multi-tab dashboards in **IBM Cognos Analytics**.
* **Statistical Visualization:** Creating market-driven insights (Salary vs. Demand) using `Matplotlib`.

---

## 📁 Project Structure
The repository is organized to reflect the data pipeline stages:

| Folder / File | Description |
| :--- | :--- |
| `notebooks/` | Jupyter Notebooks for Scraping, API communication, and EDA. |
| `scripts/` | `prepare_data.py` - The core cleaning and normalization script. |
| `data/` | Raw and processed datasets (`dashboard_data_final.csv`). |
| `visualizations/` | PNG exports of Python charts and Dashboard screenshots. |
| `Final_Presentation.pdf` | The comprehensive final report and executive summary. |

---

## 🛠️ Tech Stack
* **Languages:** Python 3.x, SQL
* **Data Tools:** `Pandas`, `NumPy`, `Openpyxl`
* **Collection:** `BeautifulSoup4`, `Requests`, `Flask`
* **Visualization:** **IBM Cognos Analytics**, `Matplotlib`, `Seaborn`

---

## 📋 Project Highlights

### 1. Data Normalization (The "Explode" Methodology)
One of the most critical steps was handling the Stack Overflow multi-select columns. Using Python, I transformed combined strings (e.g., "C;C++;Java") into individual rows. This ensured that every technology mentioned was accurately counted in the "Top 10" visualizations, preventing data loss common in standard BI imports.

### 2. Interactive Dashboards (IBM Cognos)
I developed a 3-tab interactive dashboard providing:
* **Current Usage:** Real-time popularity of Languages, Databases, and Platforms.
* **Future Trends:** Identification of "Most Desired" technologies for the upcoming year.
* **Demographics:** Deep dive into respondent age, education, and geographic distribution.

### 3. Market Correlation Analysis
By merging survey results with salary data (`popular-languages.csv`) and job postings (`job-postings.csv`), I identified key correlations:
* **High-Value Skills:** Python and Swift show the strongest correlation between developer interest and high annual salaries.
* **Geographic Demand:** Job vacancies are heavily concentrated in specific tech hubs (NYC, DC), validating the geographic demographics found in the survey.

---

## 🔧 How to Run
1. **Clone the repository:** ```bash
   git clone [https://github.com/mike-bando/IBM-Data-Analyst-Capstone-Tech-Trends.git](https://github.com/mike-bando/IBM-Data-Analyst-Capstone-Tech-Trends.git)
