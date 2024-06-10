import streamlit as st

# -- Set page config
apptitle = 'Cookie Run Kingdom: Guild Leaderboard'
st.set_page_config(page_title=apptitle
                    , page_icon=r"images/grandmaster_1.png"
                    , layout="wide"
                    ,initial_sidebar_state="auto"
                    ,menu_items={                        
                        'About': "Developed and Maintained by **SantaMonica @ MolochTH**"
                                }                     
                    )
st.logo(r"images/grandmaster_1.png",icon_image=r"images/grandmaster_1.png")


def main():
    cs_sidebar()
    cs_body()
    return None

# -- Sidebar
def cs_sidebar(): 
    # st.sidebar.header('Developed and Maintained by **SantaMonica @ MolochTH**')
    st.sidebar.image(r'images/molochth_logo_15transparent.png',use_column_width=True,width=244)
    
    
    
    # -- Body        
def cs_body():              
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('Dark Cacao server\'s Guild Battle Leaderboard',divider='gray')
    st.markdown("""
### :blue[**Welcome!**] 👋

Check out this demo app that highlights the guild boss battle performances of the top guilds on the Cookie Run: Kingdom's dark cacao server. 
I manually collect the data from the game each week. Originally made for my guild, **_MolochTH_**. It's meant for internal use, 
but feel free to share it if you think others might find it handy! 

👈 **Check them out by browsing the pages in the sidebar!**
                """) 
    st.divider()
    
    with st.expander("❓:blue[Tell me more about Cookie Run: Kingdom & Guild battle]"):
        st.subheader('Cookie Run: Kingdom & Guild battle',divider='gray')                     
        st.markdown(body="""        
        [:orange[**Cookie Run: Kingdom**]](https://www.cookierun-kingdom.com/en/) is a free-to-play game by [:orange[Devsisters]](https://devsisters.com) that mixes action RPG, gacha, and city-building. Players build their own Cookie Kingdom, collect Cookies, and battle in different modes. It launched on Android and iOS in January 2021, and on PC via Google Play Games in July 2023.
        """)           
        st.image(image=r'images/guildboss_page.png',use_column_width=True,caption="Guild Battle Mode",)

        st.markdown("""
        #### :violet[Guild Battle]⚔️

        Guild Battle is a permanent, seasonal game mode, consists of three individual bosses: :red[Red Velvet Dragon], :violet[Avatar of Destiny], and :green[Living Abyss]. 
        Each boss has individual skills, strengths and weaknesses, and strategies needed to defeat them. Damage inflicted on any of the bosses is shared between all 30 guild members, 
        allowing all members to contribute towards the same goals and rewards.

        #### :violet[Seasons & Rounds]📅

        Each Guild Battle season consist of 4 rounds, one per week, for a total of 24 playable days and 4 tallying days. 
        Players can fight each boss a maximum of 9 times per round. Guilds as a whole can fight a maximum of 540 battles per round.

        #### :violet[Guild Trophies]🏆

        Guild Trophies are used in determining a guild's overall ranking. 
        Guild Trophies are obtained by participating in Guild Battle and defeating bosses. 
        The amount of trophies earned depends on the boss level and the damage inflicted by guild members during battles.

        #### :violet[Ranking Calculation]🥇

        The total number of Guild Trophies accumulated by all guild members contributes to the guild's overall ranking. 
        Guilds are ranked based on their cumulative trophies across all rounds of the season.

        #### :violet[Rewards]🎁

        After each tallying day, guilds receive rewards based on their ranking.
        Higher-ranked guilds receive better rewards, which can include in-game items, currency, or other bonuses.
        Active participation and effective teamwork are essential for earning more Guild Trophies and climbing the ranks!.
        """  
        )

    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)     
    
    
        
if __name__ == '__main__':
    main()    