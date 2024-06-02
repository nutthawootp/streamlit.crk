import streamlit as st
import pandas as pd

from pandas.io.formats.style import Styler
# from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle
import streamlit.components.v1 as components



# -- Set page config
apptitle = 'Cookie Run Kingdom: Guild Leaderboard'
st.set_page_config(page_title=apptitle
                    , page_icon=r"images/grandmaster_1.webp"
                    , layout="wide"
                    ,initial_sidebar_state="expanded"
                    ,menu_items={                        
                        'About': "Developed and Maintained by **SantaMonica @ MolochTH**"
                                }                     
                    )
st.logo(r"images/grandmaster_1.webp",icon_image=r"images/grandmaster_1.webp")

# -- Sidebar
st.sidebar.image(r'images/molochth_logo.jpeg',use_column_width=True)

        
        
# -- Main        
st.title('🏰Cookie Run Kingdom:')
st.subheader('Guild Leaderboard in Dark Cacao server')
st.divider()  # 👈 Another horizontal rule

st.markdown("""
### Description

This app provide the information of the top 10 guilds in the Dark Cacao server.

**Note:** More information will be addd soon.



"""  
)


# st.subheader('📋:blue[Embed code]')
