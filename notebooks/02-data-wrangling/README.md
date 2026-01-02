# Module 2: Data Wrangling & Normalization

## Project Overview
This module focuses on cleaning and transforming the raw Stack Overflow survey dataset to ensure it is suitable for statistical analysis and visualization.

## Key Tasks Performed
* **Data Cleaning**: Identified and confirmed 0 duplicate rows in the target dataset.
* **Missing Value Handling**:
    * Identified 42,002 missing entries in `ConvertedCompYearly`.
    * Applied mode imputation for categorical features like `RemoteWork` and `EdLevel`.
* **Feature Engineering**: Created the `ExperienceLevel` feature based on `YearsCodePro` to categorize respondents into Junior, Intermediate, Senior, and Expert levels.
* **Normalization**: Applied **Min-Max Scaling** (range 0-1) and **Z-score Normalization** (standardized mean) to compensation data to prepare for cross-feature comparisons.

## Tools Used
* **Pandas**: For data manipulation and imputation.
* **Matplotlib**: For visualizing normalization distributions.
