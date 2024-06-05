import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
# from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Leaderboard", page_icon="🥇",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={"About": "Developed and Maintained by `SantaMonica @ MolochTH`"},
)
st.logo(r"images/grandmaster_1.png",icon_image=r"images/grandmaster_1.png")
def main():
    cs_sidebar()
    cs_body()
    return None

# -- Sidebar
def cs_sidebar(): 
    # st.sidebar.header('Developed and Maintained by **SantaMonica @ MolochTH**')
    st.sidebar.image(r'images/molochth_logo.jpeg',use_column_width=True,width=244)


def cs_body()  :
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.title('🥇Dark Cacao server Leaderboard')
    st.divider()  # 👈horizontal rule
    
    with st.expander('📝Leaderboard Information'):
        st.write("""
    The leaderboard of provide information of the top 10 guilds in Dark Cacao server, consists of the following columns: 

    `Rank`
    : The position of each guild in the leaderboard, based on their cumulative trophies across all rounds of the season.

    `Guild` 
    : The names of the different competitive teams or guilds.

    `Trophies (Round)` 
    : The number of trophies earned this round by each guild. The rank based on the number of trophies earned this round is also shown in the bracket.

    `Trophies (Season)`
    : The number of cumulative trophies within the season.

    `Improvement` 
    : Indicates how much each guild's performance improved or declined compared to the previous rounds.

    `Compare to MolochTH` 
    : The difference of total trophies(Season) between the MolochTH and the other guilds.

    """  
    )    
    
    st.divider()  # 👈horizontal rule
    #  Tableau public
    # st.subheader('📈Tableau Public')
    tableau_embed_code = """
    <div class='tableauPlaceholder' id='viz1717593798557' style='position: relative'><noscript><a href='#'><img alt='Leaderboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717593798557');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1024px';vizElement.style.height='1427px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    components.html(tableau_embed_code, height=900, scrolling=True)
    
if __name__ == '__main__':
    main()    


