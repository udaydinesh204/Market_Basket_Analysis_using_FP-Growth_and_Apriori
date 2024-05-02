import streamlit as st 
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # for data visualization
import plotly.graph_objects as go
import plotly.express as px


rules = st.session_state.get('rules')

st.title("Dashboard")

def plot_top_rules(rules, metric='confidence', top_n=10):
    # Sort the rules DataFrame by the chosen metric in descending order
    sorted_rules = rules.sort_values(by=metric, ascending=False)

    # Select the top N rules
    top_rules = sorted_rules.head(top_n)

    # Create lists to hold the data for plotting
    rule_labels = []
    metric_values = []

    # Prepare data for the plot
    for idx, rule in top_rules.iterrows():
        antecedents = ", ".join([str(item) for item in rule['antecedents']])
        consequents = ", ".join([str(item) for item in rule['consequents']])
        rule_label = f"{antecedents} => {consequents}"
        rule_labels.append(rule_label)
        metric_values.append(rule[metric])

    # Create a horizontal bar plot using Plotly
    fig = go.Figure(go.Bar(
        x=metric_values,
        y=rule_labels,
        orientation='h'
    ))

    # Set labels and title
    fig.update_layout(
        xaxis_title=metric.capitalize(),
        yaxis_title='Rules',
        title=f'Top N Rules based on {metric.capitalize()}',
        yaxis=dict(autorange="reversed")  # Reverse the y-axis to display the top rule at the top
    )

    # Return the Plotly figure
    return fig

st.header(f'Top N Rules based on Confidence')
top_rules_fig = plot_top_rules(rules)
st.plotly_chart(top_rules_fig)


# Calculate leverage
rules['leverage'] = rules['confidence'] - rules['support']

# Create a scatter plot using Plotly Express
fig = px.scatter(
    rules,
    x='lift',
    y='leverage',
    color_discrete_sequence=['blue'],
    labels={'lift': 'Lift', 'leverage': 'Leverage'},
    size_max=20,
    opacity=0.8,
    render_mode='svg',
    template='plotly_white',
)
# Update marker size and opacity to make the dots thicker
fig.update_traces(marker=dict(size=10))
# Customize the figure
fig.update_layout(
    width=500,
    height=500,
    plot_bgcolor='#fafafa',  # Set plot background color to white
   # paper_bgcolor='white',  # Set paper background color to white
)

# Display the plot in Streamlit
st.header('Lift vs. Leverage of Association Rules')
st.plotly_chart(fig)

# Display the rules dataframe with names, lift, and leverage
st.write("Rules with names, lift, and leverage:")
st.write(rules[['antecedents', 'consequents', 'lift', 'leverage']])


