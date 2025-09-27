🛠️ US Shein Appliances Data Cleaner
This script processes and cleans product data scraped from Shein’s US appliance listings. It standardizes column names, handles missing values, and outputs a clean CSV file ready for analysis or reporting.
📦 Dataset
- Input: us-shein-appliances-3987.csv
- Output: US Shein Appliances.csv
  
🔧 What It Does
- Loads the raw CSV file containing Shein appliance product data.
- Renames columns for clarity and consistency:
- goods-title-link--jump → Title
- goods-title-link--jump href → Ref-link
- rank-title → Ranking
- rank-sub → Category
- price → Price
- discount → Discount
- selling_proposition → Pitch
- goods-title-link → Type
- Fills missing values with default placeholders:
- Title, Ref-link → 'No link'
- Ranking → 'Unranked'
- Category → 'No Category'
- Price → 'No price'
- Discount → 'No Discount'
- Pitch → 'No sales recently'
- Type → 'No Type'
- Exports the cleaned DataFrame to a new CSV file.
  
📁 Usage
pip install pandas
python clean_shein_data.py


Make sure the input file us-shein-appliances-3987.csv is in the same directory as the script.
✅ Output
A clean, structured CSV file named US Shein Appliances.csv with standardized columns and no missing values.
📌 Notes
This script is ideal for preprocessing scraped e-commerce data before visualization, analysis, or integration into dashboards.

Let me know if you want to add a section for future enhancements like price parsing, currency conversion, or category grouping!

Contact: 
Carlos Jamito
carlosjamito@gmail.com
