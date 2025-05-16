import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space 

# -- Set page config
apptitle = r'Cookie Run Kingdom: Guild Battle Leaderboard'

# Error handling for setting the page configuration
try:
    st.set_page_config(
        page_title=apptitle,
        page_icon=r"images/grandmaster_1.png",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'About': "Developed and Maintained by :orange[**SantaMΦnica**]"
        }                     
    )
    st.logo(r"images/grandmaster_1.png", icon_image=r"images/grandmaster_1.png")
except Exception as e:
    st.error(f"Error setting up the page: {e}")

def main():
    cs_sidebar()
    cs_body()

# -- Sidebar
def cs_sidebar(): 
    st.sidebar.markdown('<small>Developed and Maintained by :orange[**SantaMΦnica**]</small>', unsafe_allow_html=True)

# -- Body        
def cs_body():              
    st.title('⚔️Guild Battle Leaderboard')
    st.subheader(':orange[🏰Cookie Run: Kingdom\'s Dark Cacao server🍫] ', divider='gray')
    
    col1, col2 = st.columns([3.5, 1.5])
    
    with col1:
        st.container().write("""### :blue[ **Welcome!** 👑 ] 
Hey there👋, check out this demo app we've put together. It's a handy tracker for how the top guilds are doing in Cookie Run: Kingdom's Dark Cacao server. We update the stats every week, straight from the game.🎮

Originally, it was just for our crew at **MolochTH** to check our own stats and see how we stack up against the competition and figure out ways to boost our game.📈 Feel free to use it if you think it's handy for your guild too.❤️🍪
        """) 

    with col2:
        add_vertical_space(4)
        st.image(r'images/molochth_logo_diffused_edge.png', use_column_width=True,  )
        add_vertical_space(2)
    
    st.write("👈 **Check them out by browsing the pages in the sidebar!**")
    
    st.divider()
    
    # Section for more information about the game
    with st.expander("💡:blue[Tell me more about the **guild battle** in the] :orange[Cookie Run: Kingdom]⚔️"):
        st.subheader('Cookie Run: Kingdom & Guild battle', divider='gray')
        
        st.markdown("""        
        [:orange[**Cookie Run: Kingdom**]](https://www.cookierun-kingdom.com/en/) is a free-to-play game by [:orange[***Devsisters***]](https://devsisters.com) that mixes action RPG, gacha, and city-building. Players build their own Cookie Kingdom, collect Cookies, and battle in different modes. It launched on Android and iOS in ***January 2021***, and on PC via Google Play Games in ***July 2023***.
        """)           
        
        st.image(r'images/guildboss_page.png', use_column_width=True, caption="Guild Battle Mode")
        
        st.markdown("""#### :violet[Guild Battle]⚔️
Guild Battle is a permanent, seasonal game mode consisting of three individual bosses: 
:red[**Red Velvet Dragon**]🐲, :red[**Avatar of Destiny**]🔮, and :red[**Living Abyss**]🌌. 
Each boss has individual skills, strengths, weaknesses, and strategies needed to defeat them. Damage inflicted on any of the bosses is shared between all 30 guild members, allowing contributions towards the same goals and rewards.
        """)
        
        # Function to load images in columns to avoid redundancy
        def load_boss_images():
            boss_images = [
                (r'images/rv-dragon-idle.webp', "Red Velvet Dragon"),
                (r'images/av_destiny_idle.webp', "Avatar of Destiny"),
                (r'images/abyss_idle.webp', "Living Abyss"),
            ]
            try:
                for image, caption in boss_images:
                    st.image(image=image, use_column_width=True, caption=caption, output_format='PNG')
            except Exception as e:
                st.error(f"Error loading boss images: {e}")

        boss_columns = st.columns(3)
        
        for col, (image, caption) in zip(boss_columns, [
            (r'images/rv-dragon-idle.webp', "Red Velvet Dragon"),
            (r'images/av_destiny_idle.webp', "Avatar of Destiny"),
            (r'images/abyss_idle.webp', "Living Abyss")
        ]):
            try:
                with col:
                    st.image(image=image, use_column_width=True, caption=caption, output_format='PNG')
            except Exception as e:
                st.error(f"Error loading image '{caption}': {e}")

        st.markdown("""#### :violet[Seasons & Rounds]📅
Each Guild Battle season consists of 4 rounds, one per week, for a total of 24 playable days and 4 tallying days. Players can fight each boss a maximum of 9 times per round. Guilds can fight a maximum of 540 battles per round.
        """)    
        
        st.markdown(
    """
    <div style="border: 1px solid orange; padding: 10px; border-radius: 5px;">
        <h6 style="color: orange;">Changes on the September 4 update! 📣</h6>
        Before the update, each Guild Battle round featured 3 boss enemies without any rotations, and players typically focused on the two bosses they could score higher damage against. The latest update reduces the number of boss enemies per round to 2, introduces rotations to keep things fresh, and maintains the ticket system with 3 daily tickets, allowing up to 9 tickets to be held and 18 battles per round. These changes aim to make battles more manageable and engaging, helping players earn more trophies and achieve higher ranks.
        <br>        
    </div>
    """,
    unsafe_allow_html=True
            )
        
        st.image(r'images/guildboss_rotation.png', use_column_width=True, caption="Guild Boss Rotation")
        
        
        st.markdown("""#### :violet[Guild Trophies]🏆
Guild Trophies determine a guild's overall ranking and are obtained by participating in Guild Battle and defeating bosses. The amount earned depends on the boss level and the damage inflicted by guild members.

#### :violet[Ranking Calculation]🥇
The total number of Guild Trophies accumulated contributes to the guild's ranking based on cumulative trophies across all rounds of the season.

#### :violet[Rewards]🎁
After each tallying day, guilds receive rewards based on their ranking. Higher-ranked guilds receive better rewards, including in-game items and currency.
        """)
        
    # Hide Streamlit footer and main menu
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
