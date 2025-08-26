# Ondoriya Data Platform

This project demonstrates a modern data pipeline and analytics workflow using DuckDB, MinIO, and Streamlit. It ingests raw CSV data, stages and cleans it, builds analytical marts, and visualizes key metrics and insights.

## Features

- **Data Ingestion:** Downloads CSV files from API and stores them in a MinIO object storage bucket.
- **Data Lake & Transformation:** Uses DuckDB and DuckLake to read, clean, and stage data from MinIO.
- **Medallion Architecture:** Organizes data into `main` (raw), `cleaned` (silver), and `marts` (gold) schemas.
- **Analytical Marts:** Computes KPIs and aggregates, such as total population, dominant faction, population density, and top regions.
- **Interactive Visualization:** Streamlit app for exploring KPIs and visualizations, including gradient bar charts.

## Project Structure

```
src/
  ingest.py         # Ingests CSV files into MinIO
  ducklake.py       # Loads data from MinIO, creates cleaned and marts tables
  logger.py         # Shared logger for ingestion and transformation
  data_viz.py       # Streamlit app for data visualization
SQL/
  cleaned.sql       # SQL for creating cleaned tables
  marts.sql         # SQL for creating marts tables
```

## Usage

### 1. Ingest Data

Download and store raw CSV files in MinIO:

```sh
python src/ingest.py
```

### 2. Build Cleaned and Marts Tables

Run DuckDB transformations and marts creation:

```sh
python src/ducklake.py
```

### 3. Visualize Data

Launch the Streamlit dashboard:

```sh
streamlit run src/data_viz.py
```

## Visualizations

- **Total Population:** KPI metric
- **Dominant Faction:** KPI metric
- **Faction Distribution:** Bar chart by faction
- **Top 5 Most Populous Regions:** Gradient bar chart by population

## Requirements

- Python 3.10+
- [DuckDB](https://duckdb.org/)
- [MinIO](https://min.io/)
- [Streamlit](https://streamlit.io/)
- [Altair](https://altair-viz.github.io/)
- pandas, requests, python-dotenv, minio

Install dependencies:

```sh
pip install duckdb minio streamlit altair pandas python-dotenv requests
```

## Notes

- SQL transformation logic is stored in `SQL/cleaned.sql` and `SQL/marts.sql`.
- Database and catalog files (`lab.db`, `lab.ducklake`) are gitignored.
- Logging is handled via a shared logger module.

---

**Enjoy exploring the Ondoriya