import streamlit as st
import pandas as pd
import numpy as np 


st.set_page_config(page_title='Home page', page_icon='🏛️', initial_sidebar_state='collapsed')



st.title('Main page')

st.header('A navigation menu for those who do not know how to work a web page')
with st.container():
        st.write('See the very most important page')
        

        col1, col2, col3 = st.columns(3)
        
        with col1:
                st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/2_Watch_list.py', icon='⏰', label='Watch list')
        with col2:
                st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/3_Random_ass_shit.py', icon='🌤️', label='Weather forecast')
                
        with col3:
                st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/4_Projects.py', icon='🚀', label='Projects')
        st.divider()
          
          
        col11, col22, col33 = st.columns(3)      
        with col11:
                st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/5_Learnings_ToDo.py', icon='🤔', label='Things to learn')

        with col22:
                with st.expander("Due you dare clicking me??"):
                        st.markdown("Hello my freind 👋")
                        name = st.text_input("What's your name?")
                                
                if name:
                        st.write('What a stupid name')
                else:
                        st.write('Click the button, or stay a moran')
        
        with col33:
                st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/news.py', icon='🚀', label='News')
                