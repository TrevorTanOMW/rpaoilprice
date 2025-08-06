import streamlit as st
import streamlit.components.v1 as components
import random

# Page configuration
st.set_page_config(
    page_title="Oil Price Dashboard",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Base data with realistic price ranges
base_oil_data = [
    ("🇺🇸", " WTI Crude", (65, 75), "crude"),
    ("🇬🇧", " Brent Crude", (67, 77), "crude"),
    ("🇦🇪", " Murban Crude", (68, 78), "crude"),
    ("🇺🇸", " Natural Gas", (2.8, 3.8), "gas"),
    ("🇺🇸", " Gasoline", (2.0, 2.4), "gasoline"),
    ("🇺🇸", " Heating Oil", (2.2, 2.7), "heating"),
    ("🇺🇸", " WTI Midland", (65, 75), "crude"),
    ("🇺🇸", " Mars", (70, 80), "crude"),
    ("🇺🇳", " Opec Basket", (66, 76), "crude"),
    ("🇴🇲", "DME Oman", (10, 75), "crude")
]

# Generate random data
oil_data = []
for country, name, price_range, commodity_type in base_oil_data:
    # Generate random price
    last_price = round(random.uniform(price_range[0], price_range[1]), 2)
    
    # Generate appropriate change based on commodity type
    if commodity_type == "crude":
        change_amount = round(random.uniform(-2.0, 2.0), 2)
    elif commodity_type == "gas":
        change_amount = round(random.uniform(-0.2, 0.2), 3)
    else:  # gasoline, heating
        change_amount = round(random.uniform(-0.1, 0.1), 3)
    
    # Calculate percentage change
    pct_change = round((change_amount / last_price) * 100, 2)
    
    # Format change and percentage
    change_str = f"+{change_amount}" if change_amount >= 0 else str(change_amount)
    pct_str = f"+{pct_change}%" if pct_change >= 0 else f"{pct_change}%"
    
    # Random delay
    delays = ["(11 Minutes Delay)", "(13 Minutes Delay)", "(16 Minutes Delay)", 
              "(1 Hour Delay)", "(1 Day Delay)", "(2 Days Delay)"]
    delay = random.choice(delays)
    
    oil_data.append((country, name, str(last_price), change_str, pct_str, delay))

# Generate table rows
rows_html = ""
for country, name, last, change, pct_change, updated in oil_data:
    change_class = "positive" if "+" in change else "negative"
    pct_class = "positive" if "+" in pct_change else "negative"
    rows_html += f"""
    <tr>
        <td>{country}</td>
        <td>{name}</td>
        <td>{last}</td>
        <td class="{change_class}">{change}</td>
        <td class="{pct_class}">{pct_change}</td>
        <td>{updated}</td>
    </tr>
    """

# HTML + CSS
html_content = f"""
<style>
    table {{
        border-collapse: collapse;
        width: 100%;
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    th, td {{
        padding: 12px 15px;
        text-align: left;
        font-family: Arial, sans-serif;
    }}
    th {{
        background-color: #f1f1f1;
        font-weight: bold;
    }}
    tr:nth-child(even) {{
        background-color: #fafafa;
    }}
    .positive {{
        color: green;
        font-weight: bold;
    }}
    .negative {{
        color: red;
        font-weight: bold;
    }}
</style>


<table>
    <thead>
        <tr>
            <th>Column-0</th>
            <th>Futures & Indexes</th>
            <th>Last</th>
            <th>Change</th>
            <th>% Change</th>
            <th>Last Updated</th>
        </tr>
    </thead>
    <tbody>
        {rows_html}
    </tbody>
</table>
"""

# Display in Streamlit using components.html for full CSS support
st.title("🛢️ Oil Price Dashboard")
st.markdown("*Real-time oil and gas futures data simulation*")
components.html(html_content, height=800, scrolling=False)