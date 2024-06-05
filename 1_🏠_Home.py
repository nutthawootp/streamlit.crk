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
    st.sidebar.image(r'images/molochth_logo.jpeg',use_column_width=True,width=244)
    
    
    
    # -- Body        
def cs_body():              
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('Dark Cacao server\'s Guild Battle Leader Board')
    st.divider()  # 👈 Another horizontal rule
    st.markdown("""
    Welcome! 👋

This is a demo app showcasing the top guilds in the Cookie Run: Kingdom's dark cacao server. The data is manually collected from the game interface. This app is intentionally created for use within the guild, MolochTH, but it can be shared and used by anyone. 

👈 Check them out by browsing the pages in the sidebar!
                """)
    
    
    
    
    
if __name__ == '__main__':
    main()    