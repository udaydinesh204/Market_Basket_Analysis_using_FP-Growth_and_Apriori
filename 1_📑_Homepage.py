import streamlit as st 
# Import the pages
from pages import model
from pages import dashboard

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Model", "Dashboard"])

# Define the homepage content
if page == "Home":
    st.title("Welcome to the Market Basket Analysis App")
    st.write("This is the homepage of the Market Basket Analysis app.")
elif page == "Model":
    # Call the function from model.py
    model.run()
elif page == "Dashboard":
    # Call the function from dashboard.py
    dashboard.run()


st.set_page_config(
    page_title= "Market Basket Analysis",
    page_icon= "🧺",
    layout= "wide",
    initial_sidebar_state= "expanded",
)

st.title("Introduction to Market Basket Analysis")
st.sidebar.success("Select a page above.")


st.markdown( 


"""

![Market Basket Analysis](https://3.bp.blogspot.com/-i_KRZLp_mc4/VhVaP68aeuI/AAAAAAAAAVc/JyJEBUykrjM/s1600/cover%2Bphoto%2B-%2Bexample.jpg)

## Abstract

Market basket analysis is a critical tool in retail and e-commerce as it reveals patterns in customer behavior and purchasing trends. By examining transactional data, market basket analysis uncovers relationships between items commonly bought together, facilitating effective product recommendations, cross-selling strategies, and inventory management. Two widely used algorithms for association rule mining in this context are FP-Growth and Apriori. The FP-Growth algorithm employs a tree-based approach to efficiently generate frequent itemsets, minimizing computational complexity. In contrast, the Apriori algorithm, though conceptually straightforward, requires multiple passes through the data, potentially increasing computational overhead.

This research investigates the efficiency and performance of the Apriori and FP-Growth algorithms in market basket analysis using a UK-based online retail dataset sourced from the UCI Machine Learning Repository. We compare the algorithms' results and assess their ability to generate association rules while evaluating their computational requirements. The findings provide insights into the strengths and limitations of each approach, offering guidance for choosing the appropriate algorithm for specific market basket analysis needs.

## Tech Stack for Project:

Deploy: Streamlit 

Machine Learning: FP growth , Apriori , MLxtend and necessary libraries

Version Control: GitHub

Project Management: Notion , Whimsical

## Trends:
#### Personalization:

Trend: Growing demand for personalized shopping experiences.

Impact: Market basket analysis enables personalized recommendations, aligning with the trend.

#### Real-time Analytics:

Trend: Shift towards real-time data analysis for immediate insights.

Impact: The project's focus on real-time data fetching aligns with this trend, providing timely results.

#### Integration with E-commerce:

Trend: Increased integration of data analytics in e-commerce platforms.

Impact: The project's integration with the online grocery store aligns with this trend, contributing to enhanced analytics capabilities

## Project Impact:
#### Optimized Business Strategies
The research provides insights into consumer purchasing patterns, allowing businesses to optimize their strategies for product bundling, targeted promotions, and inventory management. These data-driven approaches lead to more efficient operations and better alignment with customer preferences.
#### Enhanced Customer Experience
By leveraging association rule mining to identify related products frequently purchased together, businesses can offer personalized product recommendations. This tailored shopping experience can enhance customer satisfaction and loyalty.
#### Increased Revenue
The study's findings can guide businesses in implementing effective cross-selling and upselling strategies, leading to increased average transaction values and overall revenue.
#### Data-Driven Decision Making
The project's use of advanced algorithms to analyze transactional data equips businesses with actionable insights for making informed decisions. This fosters a culture of data-driven decision-making across various aspects of business operations, from marketing to supply chain management.

### To know more about

https://www.javatpoint.com/market-basket-analysis-in-data-mining#:~:text=Examples%20of%20Market%20Basket%20Analysis&text=Retail%3A%20The%20most%20well%2Dknown,case%20study%20is%20Amazon.com

### Applications:
Amazon - Personalised product recommendations based on purchase history.

Walmart - Optimizing product placements and cross-selling.

Netflix - Movie and TV show recommendations based on viewing history.

Tesco - Understanding customer behaviour for tailored promotions.

Alibaba - Providing personalized product recommendations.

"""

                )
    
