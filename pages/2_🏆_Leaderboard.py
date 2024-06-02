import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
# from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Leaderboard", page_icon="🥇",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Developed and Maintained by **SantaMonica @ MolochTH**"},
)
st.logo(r"images/grandmaster_1.webp",icon_image=r"images/grandmaster_1.webp")

st.sidebar.image(
    r"images/molochth_logo.jpeg", use_column_width=True, output_format="PNG"
)

# -- Main        
st.title('🥇Guild Leaderboard')

st.divider()  # 👈horizontal rule

#  Tableau public
# st.subheader('📈Tableau Public')
tableau_embed_code = """
<div class='tableauPlaceholder' id='viz1717339653496' style='position: relative'><noscript><a href='#'><img alt='Leaderboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao&#47;Leaderboard&#47;1_rss.webp' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LeaderboardGuildsDarkCacao&#47;Leaderboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao&#47;Leaderboard&#47;1.webp' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717339653496');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1024px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1024px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(tableau_embed_code, height=900, scrolling=True)

st.write("""
# Description

This is a leaderboard of the top 10 guilds in Dark Cacao.

Compare - The difference of total trophies(Season) between the MolochTH and the other guilds.

**Note:** More information will be addd soon.



"""  
)    

