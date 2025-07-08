## Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

## Write directly to the app
st.title(f":balloon: Customize Your Smoothies! :balloon:")
st.write(
  """Chhose the fruits you want in your Smoothies!
  """
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be: ', name_on_order)

#option = st.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone"),
#)

#st.write("You selected:", option)

#option = st.selectbox(
#    "What is your favourite fruit?",
#    ("Banana", "Strawberry", "Peaches"))

#st.write("Your favourite fruit is:", option)

#option = st.selectbox(
#    "Default email",
#    ["foo@example.com", "bar@example.com", "baz@example.com"],
#    index=None,
#    placeholder="Select a saved email or enter a new one",
#    accept_new_options=True,
#)

#st.write("You selected:", option)

## Store the initial value of widgets in session state

#if "visibility" not in st.session_state:
#    st.session_state.visibility = "visible"
#    st.session_state.disabled = False#

#col1, col2 = st.columns(2)

#with col1:
#    st.checkbox("Disable selectbox widget", key="disabled")
#    st.radio(
#        "Set selectbox label visibility 👉",
#        key="visibility",
#        options=["visible", "hidden", "collapsed"],
#    )

#with col2:
#    option = st.selectbox(
#        "How would you like to be contacted?",
#        ("Email", "Home phone", "Mobile phone"),
#        label_visibility=st.session_state.visibility,
#        disabled=st.session_state.disabled,
#    )


from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
    , max_selections = 5
    )


if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)
   
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    #st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button ('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered, ' +name_on_order+'!', icon="✅")












