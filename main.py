import streamlit as st
import langchain_helper as lch

st.title('Restaurant Name Generator')

cuisine=st.sidebar.selectbox("Pick a cuisine",( 'American', 'Chinese', 'Indian', 'Italian', 'Japanese', 'Mexican', 'Thai'))

if cuisine:
    response=lch.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(',')
    
    st.write('Menu Items')
    for item in menu_items:
        st.write("-",item)