# Elevate-Labs-Task-1

The dataset has 2,823 rows and 25 columns. Here are the initial observations before cleaning:

#Issues Identified:
1. Missing Values:
   - `ADDRESSLINE2`, `STATE`, `POSTALCODE`, and `TERRITORY` have missing values.
2. Duplicate Rows:
   - Need to check and remove any.
3. Inconsistent Formats:
   - `ORDERDATE` is an object (string) and needs conversion to datetime.
4. Column Names:
   - Column headers are mixed-case and contain spaces.
5. Data Types:
   - `ORDERDATE` should be datetime.
   - `POSTALCODE` might be better as string, not float/object, due to leading zeros.
6. Text Standardization:
   - `COUNTRY`, `STATUS`, `DEALSIZE`, etc., could have inconsistent casing or typos.



 #Summary of Cleaning Steps:
1. Removed Duplicates:
   - Dropped exact duplicate rows — reduced dataset from 2,823 to 263 rows (many records had incomplete location data).
2. Handled Missing Values:
   - Filled `addressline2` with empty strings (optional field).
   - Dropped rows missing critical values in `state`, `postalcode`, and `territory`.
3. Standardized Formats:
   - Converted `orderdate` to `datetime` format.
   - Renamed all column headers to lowercase with underscores (e.g., `ORDERNUMBER → ordernumber`).
   - Converted `postalcode` to string to preserve leading zeros.
   - Standardized casing in key text columns (`status`, `productline`, `country`, `territory`, `dealsize`) using title case.

