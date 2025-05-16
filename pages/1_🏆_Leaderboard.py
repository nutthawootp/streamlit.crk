from matplotlib.pylab import f
import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
from datetime import datetime
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
    st.sidebar.markdown('<small>Developed and Maintained by **SantaMonica**</small>', unsafe_allow_html=True)
    # st.sidebar.image(r'images/molochth_logo_15transparent.png',use_column_width=True,width=244)


def cs_body()  :
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('🥇Dark Cacao server Leaderboard', divider='gray')
    explain_tableau = """
    The leaderboard of provide information of the top 10 guilds in Dark Cacao server, consists of the following columns: 

| Column | Description |
|:--------:|:-------------|
| `Rank` | The position of each guild in the leaderboard, based on their cumulative trophies across all rounds of the season. |
| `Guild` | The names of the different competitive teams or guilds. |
| `Trophies (Round)` | The number of trophies earned this round by each guild. The rank based on the number of trophies earned this round is also shown in the bracket. |
| `Trophies (Season)` | The number of cumulative trophies within the season. |
| `Improvement` | Indicates how much each guild's performance improved or declined compared to the previous rounds. |
| `Compare to MolochTH` | The difference of total trophies(Season) between the MolochTH and the other guilds. |
    """  
    
    explain_st_table = """
    The leaderboard of provide information of the top 10 guilds in Dark Cacao server, consists of the following columns: 

| Column | Description |
|:--------:|:-------------|
| `Rank` | The position of each guild in the leaderboard, based on their cumulative trophies across all rounds of the season. |
| `Change` | The change in the guild's overall rank compared to the previous round. |
| `Guild` | The names of the different competitive teams or guilds. |
| `Total Trophies` | The number of cumulative trophies within the season. |
    """
    with st.expander('📝Leaderboard Information'):
        st.write(explain_st_table)    
    
    #
    #Table
    #
    
    @st.cache_data
    def load_data() -> pd.DataFrame:
        csv_data_path = "https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv"
        data = pd.read_csv(csv_data_path)
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    
    def leaderboard(data):
        """
        Generate a leaderboard dataframe based on the input data.

        Args:
            data (pandas.DataFrame): The input data containing guild information.

        Returns:
            pandas.DataFrame: The leaderboard dataframe with the following columns:
                - Round: The round number.
                - SeasonRank: The season rank of the guild.
                - GuildNameExtra: The name of the guild.
                - Trophies(round): The number of trophies earned in each round, .
                - Trophies(Season): The cumulative trophies earned in the season, formatted with commas.
                - Improvement: The improvement in performance compared to previous rounds.
                - TrophiesOverTime: A list of all Trophies(Round) values available for each guild.
        """
        data["Season"] = data.Round + " (" + data.Date.apply(lambda x: datetime.strftime(x, "%d %b %Y")) + ")"
        
        data["Trophies(round)"] = data.Trophies.apply(lambda x: "{:,.0f}".format(x)) + " (#" + data.RoundRank.astype(str) + ")"
        
        data["Trophies(Season)"] = data.SeasonTotal.apply(lambda x: "{:,.0f}".format(x)) 

        data["Season"] = data.Round.astype(str) + " (" + data.Date.dt.strftime("%d %b %Y") + ")"
        
        data["DiffSeasonRank"] = data["DiffSeasonRank"].apply(lambda x: (
                                                            " ▲{:.0f}".format(x) if x > 0  # type: ignore
                                                            else " ▼{:.0f}".format(abs(x)) if x < 0 else " "  # type: ignore
                                                                            ))
        
        # Add a new column 'TrophiesOverTime' that contains a list of all Trophies(Round) values available for each guild
        data["TrophiesOverTime"] = None
        # for idx, row in data.head().iterrows():
        #     data.loc[idx, "TrophiesOverTime"] = str(data[data.GuildNameExtra == row.GuildNameExtra].Trophies.tolist())
            
        
        board = data[
            [
                "Season",
                "SeasonRank",
                "DiffSeasonRank",
                "GuildNameExtra",
                "Trophies(round)",
                "Trophies(Season)",
                "Improvement",
                "GrowthRate",
                "TrophiesOverTime",
            ]
        ]
        
        board_group = board.groupby(["Season",  "SeasonRank", "DiffSeasonRank","GuildNameExtra"]).max().reset_index()#["Trophies(round)","Trophies(Season)","Improvement","GrowthRate","TrophiesOverTime"]
        
        return board_group
    
    #
    # Load data
    #
    
    data= load_data()      
    
    board = leaderboard(data)    
    
    # st.dataframe(board , use_container_width=True,hide_index=True,)

    # if "select_season" not in st.session_state:
    #     st.session_state.select_season = 
        

    def show_leaderboard(data: pd.DataFrame, filter_by_season=None):
        
        if filter_by_season is None:
            display_data = data
        else:
            # display_data = data[data.index.get_level_values("Season") == filter_by_season]
            display_data = data[data.Season == filter_by_season]
            
        leader_board = st.dataframe(data=display_data
                                    ,hide_index=True
                            , use_container_width=True
                            ,column_order=["SeasonRank","DiffSeasonRank","GuildNameExtra","Trophies(Season)"]
                            , column_config = {
                                "Season": st.column_config.TextColumn(
                                            label="Season",
                                            help="Season-Round (Date)",
                                            width="medium"
                                            ),
                                "SeasonRank": st.column_config.NumberColumn(
                                            label="Rank",
                                            help="The overall rank based on the number of total trophies(season).",
                                            format="%i",
                                            width="small"
                                            ),       
                                "DiffSeasonRank": st.column_config.TextColumn(
                                            label="Change",
                                            help="The rank change from the previous round.",
                                            width="small"
                                            ),
                                "GuildNameExtra": st.column_config.TextColumn(
                                            label="Guild",
                                            help="The name of the guild.",
                                            width="medium"
                                            ),   
                                "Trophies(round)": st.column_config.TextColumn(
                                            label="Trophies",
                                            help=" The number of trophies and rank within a round.",
                                            width="medium"
                                            ),   
                                "Trophies(Season)": st.column_config.TextColumn(
                                            label="Total Trophies",
                                            help=" The running total of the number of trophies earned within a season.",
                                            width="small"
                                            ),                                                                                       
                                "Improvement": st.column_config.NumberColumn(
                                            label="Improvement",
                                            help="The different between the number of trophies earned this round compared to the previous round.",
                                            # format="%i",
                                            # min_value=board[board.Season.isin(options)].Improvement.min(),
                                            # max_value=board[board.Season.isin(options)].Improvement.max(),
                                            ),
                                "GrowthRate": st.column_config.ProgressColumn(
                                            label="%Improvement",
                                            help=r"% difference between the number of trophies earned this round compared to the previous round.",
                                            format= "%.2f%%",
                                            min_value=0,
                                            max_value=100,
                                            ),                                                           
                                            
                                            }
                )
        return leader_board
    
    selected_season = st.select_slider(
                                label="Use slider to select a season",
                                # options=board.index.get_level_values("Season").tolist(),
                                options=board.Season.tolist(),                                
                                value= max(board.Season.tolist()),
                                key="select_season"
                                )

    st.write(f'##### Leaderboard of season {selected_season}')
    show_leaderboard(board, filter_by_season=selected_season)
    
    
    st.divider()  # 👈horizontal rule
    #  Tableau public
    # st.subheader('📈Tableau Public')
    # tableau_embed_code = """
    # <div class='tableauPlaceholder' id='viz1717593798557' style='position: relative'><noscript><a href='#'><img alt='Leaderboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Le&#47;LeaderboardGuildsDarkCacao_17175843531340&#47;Leaderboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717593798557');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1024px';vizElement.style.height='1427px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    # """
    # components.html(tableau_embed_code, height=900, scrolling=True)
    
if __name__ == '__main__':
    main()    
    

