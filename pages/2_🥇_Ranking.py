import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.stoggle import stoggle


st.set_page_config(
    page_title="Ranking", 
    page_icon="🥇",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
            'About': "Developed and Maintained by :orange[**SantaMΦnica**]"
        })
st.logo(r"images/grandmaster_1.png",icon_image=r"images/grandmaster_1.png")


def main():
    cs_sidebar()
    cs_body()
    return None

# -- Sidebar
def cs_sidebar(): 
    st.sidebar.markdown('<small>Developed and Maintained by :orange[**SantaMΦnica**]</small>', unsafe_allow_html=True)
    # st.sidebar.image(r'images/molochth_logo_15transparent.png',use_column_width=True,width=244)

    
    
@st.cache_data
def load_data() -> pd.DataFrame:
    csv_data_path = 'https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv'
    data = pd.read_csv(csv_data_path)
    return data


def rankchart(data:pd.DataFrame):
    
    if 'Date' in data.columns:
        max_date = str(data.Date.max()).split(" ")[0]
    
    
    if data.GuildNameExtra.nunique() == 10:
        fig = px.line(data,
                x="Round",
                y="SeasonRank",
                color="GuildNameExtra",
                color_discrete_sequence=px.colors.qualitative.G10,
                text="SeasonRank",
                markers=True,
                symbol="GuildNameExtra",
                line_shape="hvh",
                labels={"GuildNameExtra": "Guild", "Round": "Season"},
                template="plotly_white",
                hover_name="GuildNameExtra",
                hover_data={
                    "GuildNameExtra": False,
                    "Round": True,
                    "SeasonRank": False,
                    "Date": "|%d %B %Y",
                    "Trophies": ":,.0f",
                    "SeasonTotal": ":,.0f",
                },
                height=900,
                width=1200,
            )
        
        max_rank = data.SeasonRank.max()
        
        fig.update_yaxes(
                title="SeasonRank", 
                ticklabelstep=1, 
                range=[max_rank+1, 0],   
                showgrid=False, 
                visible=False, 
                        )
    else:
        fig = px.line(data,
                        x="Round",
                        y="SeasonRank",
                        color="GuildNameExtra",
                        color_discrete_sequence=px.colors.qualitative.G10,
                        text="SeasonRank",
                        markers=True,
                        symbol="GuildNameExtra",
                        line_shape="hvh",
                        labels={"GuildNameExtra": "Guild", "Round": "Season"},
                        template="plotly_white",
                        hover_name="GuildNameExtra",
                        hover_data={
                            "GuildNameExtra": False,
                            "Round": True,
                            "SeasonRank": False,
                            "Date": "|%d %B %Y",
                            "Trophies": ":,.0f",
                            "SeasonTotal": ":,.0f",
                        },
                        height=1300,
                        width=1200,
                    )
        max_rank = data.SeasonRank.max()
        
        fig.update_yaxes(
                        title="SeasonRank", 
                        ticklabelstep=1, 
                        range=[max_rank+1, 0], 
                        showgrid=False, 
                        visible=False, 
                        )

    fig.update_xaxes(title="Season", showgrid=False,)

    fig.update_traces(
        marker_symbol="circle",
        marker_size=20,
        textposition="middle center",
        textfont=dict(family="Arial", size=12,color="white")
    )

    annotations = []

    annotations.append(
        dict(
            text=f"Created by: SantaMonica @ MolochTH<br>Last update: {max_date}",
            xref="paper",
            yref="paper",
            x=0,
            y=0,
            xanchor="right",
            yanchor="bottom",
            font=dict(family="Arial", size=12, color="rgb(150,150,150)"),
            showarrow=False,
        )
    )

    fig.update_layout(
        annotations=annotations,
        title_text=f"Guild Battle Ranking Over Time",
        title_font_family="Arial",
        title_font_size=20,
        hovermode="closest",
        legend=dict(
            # x=0,
            # y=1,
            # traceorder="reversed",
            title = "Guild",
            orientation="h",
            font=dict(family="Arial", size=14),
            bgcolor=None,
            bordercolor='gray',
            borderwidth=0.5,
        ),
    )

    return st.plotly_chart(fig
                        , theme="streamlit"
                        , use_container_width=True
                        # , selection_mode='point'
                        , zoom=False
                        ) 

# %%
    
# -- Body        
def cs_body():              
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('Guild battle ranking over time',divider=True)
        
    data=load_data()

    top10_recent = data[
        (data.SeasonRank <= 10) & (data.Round == data.Round.max())    
    ].GuildNameExtra.unique()

    top10data = data[data.GuildNameExtra.isin(top10_recent)]
    
    overview = """        
This chart tracking the **ranking progression** of the top guilds in the Dark Cacao Server over time.

> **Note📝**

- The top three guilds consistently maintain a high rank, indicating a consistent top performance among the three guilds.

    - **:orange[Spearmint]** had the longest streak of 10 consecutive rounds holding the first place, since the begining of the season. 

    - However, **:orange[Vivid]** made it to the first place in round 3-3 and still be tightly holding the top rank until now.
    
    - **:orange[Nobless]** is the most consistent guild in the server, holding the 3rd place troughout the seasons.  

- :orange[**이지스 (aegis)**] shows a notable rise, indicating significant improvment within the guild  over time. 

- The other guilds exhibit fluctuations in rankings, indicating their active competition and continuous improvement in their standings within the server. 

- This chart obviously highlights the competitive nature and dynamic shifts within the guild rankings over time.
    """

    with st.expander("❓What's this chart about?"): 
        st.write(overview)  

    # st.divider()
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=False):
            st.empty()
    with col2:
        with st.container(border=True):             
            top10filter = st.checkbox(label="Show only the top 10 guilds", value=False,)
            
    st.markdown('> 💡**Tips**: Double click guilds in the legend box to view only the selected guilds.')
    st.divider()  
    # selected_guild = st.selectbox("Select guild", options=top10_recent)
    
    if top10filter:
        st.markdown("### :blue[Top 10 guilds in Dark Cacao Server]")
        rankchart(top10data)
    else:
        st.markdown("### :blue[Top guilds in Dark Cacao Server]")
        rankchart(data)    
    
    st.divider()        
    
if __name__ == '__main__':
    main()    




# %%
