## Import python packages
from snowflake.snowpark.functions import col
import streamlit as st

# Get the Snowflake connection
conn = st.connection("snowflake", type="snowflake")

# Retrieve the Snowpark session
session = conn.session

# Query the table
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
    , max_selections = 5
    )


if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

   
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

   
    time_to_insert = st.button ('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered, ' +name_on_order+'!', icon="✅")













