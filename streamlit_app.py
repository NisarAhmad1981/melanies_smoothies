# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the app
st.title("cup_with_straw :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

# import streamlit as st

option = st.selectbox(
    "What is your favorite fruits?",
    ("Banana", "StrawBerries", "Peaces"))

st.write("your favorite fruits- is:", option)


session = get_active_session()
def main(session: snowpark.Session):

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'));

ingredients_list = st.multiselect(
    'choose up to 5 ingredients:' 
    , my_dataframe
    )

if ingredients_list:
    #st.write(ingredients_list) 
    #st.text(ingredients_list)
    ingredients_string = ' '
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ''
    st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)
    
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
