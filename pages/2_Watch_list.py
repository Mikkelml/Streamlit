import streamlit as st
import pandas as pd
import numpy as np 
st.set_page_config(page_title='Watch list', page_icon='⏱️', initial_sidebar_state='collapsed')


st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/pages/Main_page.py', icon='🏛️', label='Home')


st.title('Watch list')
with st.container():
        st.write('The absolute dream watch - VACHERON & CONSTANTIN Overseas 18K rose gold')
        st.image(image='https://asset.bucherer.com/image/upload/w_1920,f_auto/Assets/Watches/RICHEMONT/Vacheron%20Constantin/Automatic/1409-445-6_FP.png', caption='Dream watch')
        st.write('VACHERON & CONSTANTIN wristwatch, Overseas 41 mm, 18K rose gold, gold-bracelet, with folding clasp, green dial with index, automatic, Cal. 5100, centre seconds, sapphire-crystal, 15 atm, Ref.:4520V/210R-B967')

        st.write('Another one - Rolex DayDate 18k yellow gold')
        st.image(image='https://media.rolex.com/image/upload/q_auto:best/f_auto/c_limit,w_2440/v1711577094/rolexcom/collection/family-pages/classic-watches/day-date/family-page/2024/classic-watches-day-date-elegance-and-technical-M228238-0066_2401jva_002', caption='Could settle for this one')
        st.write('Instantly recognizable, its unique design has forged its identity. At its launch, the Day-Date was the only watch with a semi-circular window at 12 o’clock displaying the day of the week spelt out in full. With its specially-designed President bracelet available only in precious metal – gold or platinum – it is the watch of prestige par excellence')

