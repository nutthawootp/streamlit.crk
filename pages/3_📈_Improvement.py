import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
# from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Improvement", 
    page_icon="📈",
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
def cs_sidebar() -> None: 
    st.sidebar.markdown('<small>Developed and Maintained by **SantaMonica**</small>', unsafe_allow_html=True)
    # st.sidebar.image(r'images/molochth_logo_15transparent.png',use_column_width=True,width=244)
    return None

# -- Body

def cs_body() -> None:      
    st.title(body=':orange[Cookie Run: Kingdom]🏰')
    st.subheader('Improvement of guilds over time')
    st.divider()  # 👈 Another horizontal rule
    @st.cache_data
    
    def load_data() -> pd.DataFrame:
        csv_data_path = 'https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv'
        data = pd.read_csv(csv_data_path)
        return data
    
    data=load_data()
    
    top10_recent = data[
        (data.SeasonRank <= 10) & (data.Round == data.Round.max())
    ].GuildName.unique()
    
    top10data = data[data.GuildName.isin(top10_recent)]
    
    max_date = str(data[data.GuildName.isin(top10_recent)].Date.max()).split(" ")[0]

    def linechart(data):
        
        fig = px.line(data,
        x="Round",
        y="Trophies",
        color="GuildNameExtra",
        color_discrete_sequence=px.colors.qualitative.G10_r,
        markers=True,
        hover_data={
            "GuildNameExtra": False,
            "SeasonRank": ":,.0f",
            "Date": "|%B %d, %Y",
            "Trophies": ":,.0f",
            "Improvement": ":,.0f",
        },
        hover_name="GuildNameExtra",
        title="Guild Boss Trophies Over Time",
        labels={"SeasonRank": "Rank", "Round": "Season", "Trophies": "Trophies"},
        template="simple_white",
        height=800,)


        fig.update_yaxes(showgrid=True)
        
        fig.update_layout(
        title_font_family="Arial",
        title_font_size=30,
        legend=dict(
            # x=0,
            # y=1,
            orientation='h',
            title = "Guild",
            font=dict(family="Arial", size=15),
            bgcolor=None,
            bordercolor=None,
            borderwidth=0,
        ),
        )

        return st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    

    def waterfall(data):
        
        fig2 = go.Figure()

        for guild, dat in data.groupby("GuildNameExtra"):
            growth_rates_percentage = dat["GrowthRate"]
            improve = dat["Improvement"]
            baseline = dat[dat['Round']==dat['Round'].min()]['Trophies']
            
            fig2.add_trace(
                go.Waterfall(
                    orientation="v",
                    x=dat["Round"],
                    y=improve,
                    name=guild,
                    # text=f"{guild}",
                    decreasing=dict(marker=dict(color="red")),
                    increasing=dict(marker=dict(color="green")),
                    # base=baseline
                )
            )
        annotations = []
        # annotations.append(
        #     dict(
        #         text=f"Created by: SantaMonica @ MolochTH<br>Last update: {max_date}",
        #         xref="paper",
        #         yref="paper",
        #         x=1.16,
        #         y=-0.05,
        #         xanchor="right",
        #         yanchor="top",
        #         font=dict(family="Arial", size=12, color="rgb(150,150,150)"),
        #         showarrow=False,
        #     )
        # )    

        fig2.update_layout(
            title="Waterfall Chart of Round over Round Trophies Growth Rate over Time",
            title_font_family="Arial",
            title_font_size=30,
            xaxis_title="Round",
            yaxis_title="Growth Rate (%)",
            # autosize=False,
            # width=800,
            height=900,
        # yaxis=dict(type="log"),  # Set the y-axis type to logarithmic
            legend=dict(
            # x=0,
            # y=1,
            orientation = 'h',
            title = "Guild",
            font=dict(family="Arial", size=15),
            bgcolor=None,
            bordercolor=None,
            borderwidth=0,
                        ),
            annotations=annotations,
        )
        return st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
        

    top10filter = st.checkbox(label="Show only the top 10 guilds", value=False,)
    st.divider()  
    if top10filter:
        st.markdown("### :blue[Top 10 guilds in Dark Cacao Server]")
        linechart(top10data)
        st.divider()
        waterfall(top10data)
    else:
        st.markdown("### :blue[Top guilds in Dark Cacao Server]")
        linechart(data)
        st.divider()
        waterfall(data)  
        
    
if __name__ == '__main__':
    main()    