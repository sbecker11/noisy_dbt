#!/bin/bash

# Step 1: Generate clean data
python generate_clean_data.py

# Step 2: Add noise and errors
python add_noise_and_errors.py

# Step 3: Run DBT tests
dbt run

# Step 4: Compare errors
python compare_errors.py
