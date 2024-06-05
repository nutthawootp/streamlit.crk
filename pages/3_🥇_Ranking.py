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
    menu_items={"About": "Developed and Maintained by **SantaMonica @ MolochTH**"}
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

    
    
@st.cache_data
def load_data() -> pd.DataFrame:
    csv_data_path = 'https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv'
    data = pd.read_csv(csv_data_path)
    return data


def rankchart(data=pd.DataFrame) -> go.Figure:
    
    if 'Date' in data.columns:
        max_date = str(data.Date.max()).split(" ")[0]
    
    fig = px.line(data,
                    x="Round",
                    y="SeasonRank",
                    color="GuildNameExtra",
                    color_discrete_sequence=px.colors.qualitative.G10,
                    text="SeasonRank",
                    markers=True,
                    line_shape="linear",
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
        title="SeasonRank", ticklabelstep=1, range=[max_rank+1, 0], showgrid=False, visible=False, 
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
            x=1.16,
            y=-0.03,
            xanchor="right",
            yanchor="top",
            font=dict(family="Arial", size=12, color="rgb(150,150,150)"),
            showarrow=False,
        )
    )

    fig.update_layout(
        annotations=annotations,
        title_text=f"Guild Battle Ranking Over Time",
        title_font_family="Arial",
        title_font_size=25,
        legend=dict(
            # x=0,
            # y=1,
            # traceorder="reversed",
            title = "Guild",
            font=dict(family="Arial", size=15),
            bgcolor=None,
            bordercolor=None,
            borderwidth=0,
        ),
        hovermode="closest",
    )

    return st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# %%
    
# -- Body        
def cs_body():              
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('Guild battle ranking over time')
    st.divider()  # 👈 Another horizontal rule
        
    data=load_data()

    top10_recent = data[
        (data.SeasonRank <= 10) & (data.Round == data.Round.max())    
    ].GuildName.unique()

    top10data = data[data.GuildName.isin(top10_recent)]
    
    overview = """        
This chart tracking the ranking progression of the top guildsin the Dark Cacao Server over time. The top three guilds consistently maintain a high rank, indicating a consistent top performance. The `이지스 (aegis)` shows a notable rise, indicating significant improvment within the guild  over time. The other guilds exhibit fluctuations in rankings, indicating their active competition and continuous improvement in their standings within the server. This highlights the competitive nature and dynamic shifts within the guild rankings over time.
    """

    with st.expander("🔎What's this chart about?"): 
        st.write(overview)

    
    st.divider()  
    top10filter = st.checkbox(label="Show only the top 10 guilds", value=False,)
    st.divider()  
    
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
