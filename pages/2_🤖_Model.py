import streamlit as st 
import pandas as pd
import pickle
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning, module='openpyxl')

def run():
    st.title("Model Page")

st.title("Model")
@st.cache_data
def load_data(pickle_file):
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
    return data
data= load_data('data.pickle')
data = data.astype(bool)


# Choose minimum support
min_support = st.slider('Choose minimum support', 0.02, 0.1, 0.03)

st.header('Apriori Algorithm')

try:
    # Try running the Apriori algorithm with the specified min support
    frequent_itemsets_apriori = apriori(data, min_support=min_support, use_colnames=True)
    
    # Check if the frequent itemsets DataFrame is empty
    if frequent_itemsets_apriori.empty:
        # Display a warning if no frequent itemsets were found
        st.warning(f"No frequent itemsets found with minimum support = {min_support}. Please try a higher support value.")
    else:
        # Display the frequent itemsets if found
        st.write("Frequent itemsets found:")
        st.write(frequent_itemsets_apriori)

except MemoryError:
    # If a MemoryError occurs, display a warning to the user
    st.warning("MemoryError occurred while running Apriori with minimum support = 0.03. Please try a higher support value or use a different algorithm such as FP-Growth.")



st.header('FP-Growth Algorithm')

frequent_itemsets_fpgrowth = fpgrowth(data, min_support=min_support, use_colnames=True)
st.write(frequent_itemsets_fpgrowth)

# Assume you have already calculated frequent itemsets and stored them in a variable called frequent_itemsets

min_confidence = st.slider('Choose minimum confidence', 0.1, 1.0, 0.3)

if frequent_itemsets_fpgrowth is not None:
    # Generate association rules
    rules = association_rules(frequent_itemsets_fpgrowth, metric='confidence', min_threshold= min_confidence )
    
    # Display the association rules DataFrame
    st.header("Association rules")
    st.write(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

    # Calculate and display the average confidence of the rules
    avg_confidence = rules['confidence'].mean()
    st.write(f"Average confidence of the rules: {avg_confidence:.2f}")
    
    # Store the rules DataFrame in Streamlit session state
    st.session_state['rules'] = rules

    