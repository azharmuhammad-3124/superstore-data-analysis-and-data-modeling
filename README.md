# Superstore Sales Data Exploration

## Repository Outline
1. description.md                       - Penjelasan umum project
2. images                               - Dokumentasi visualisasi EDA di Kibana
3. P2M3_azhar_muhammad_data_raw.csv     - Dataset mentah
4. P2M3_azhar_muhammad_data_clean.csv   - Dataset setelah dilakukan cleaning
5. P2M3_azhar_muhammad_DAG.py           - DAG untuk proses data, seperti cleaning dan penjadwalan di airflow
6. P2M3_azhar_muhammad_DAG_graph.png    - Graph DAG
7. P2M3_azhar_muhammad_ddl.txt          - URL dataset dan syntax DDL
8. P2M3_azhar_muhammad_GX.ipynb         - Great Expectation Validation


## Problem Background
Penjualan di sektor ritel, termasuk superstore, menghadapi tantangan besar akibat perubahan perilaku konsumen dan persaingan dari e-commerce. Untuk tetap kompetitif, penting bagi superstore untuk memahami pola pembelian pelanggan serta faktor-faktor yang mendorong penjualan.

## Project Output
- Dashboard menggunakan Kibana untuk analisis penjualan.
- Validasi kualitas data menggunakan Great Expectations.
- Pipeline ETL otomatis menggunakan Airflow dan PostgreSQL.`

## Data
- Sumber: [Dataset publik “Superstore Sales](https://www.kaggle.com/datasets/bhanupratapbiswas/superstore-sales)
- Jumlah Kolom: 18 kolom
- Jumlah Baris: 9.789 rows
- Kolom utama: order_date, region, segment, sales, category, sub_category

## Method
- Validasi data menggunakan Great Expectations
- Otomatisasi pipeline data ETL dengan Apache Airflow
- Penyimpanan data menggunakan PostgreSQL
- Visualisasi data dengan Kibana

## Stacks
- ETL: Apache Airflow – untuk mengotomatiskan alur ekstraksi, transformasi, dan pemuatan data
- Basis Data: PostgreSQL – sebagai sistem database relasional utama
- Visualisasi: Kibana – untuk membuat dashboard analisis penjualan
- Bahasa Pemrograman: Python – untuk pengolahan data dan scripting
- Library Python: pandas, great_expectations
