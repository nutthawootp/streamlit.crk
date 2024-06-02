import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
# from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Improvement", 
    page_icon="👍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Developed and Maintained by **SantaMonica @ MolochTH**"}
)
st.logo(r"images\grandmaster_1.png",icon_image=r"images\grandmaster_1.png")

st.sidebar.image(
    r"images\molochth_logo.jpeg", use_column_width=True, output_format="PNG"
)

@st.cache_data
def load_data() -> pd.DataFrame:
    csv_data_path = 'https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv'
    data = pd.read_csv(csv_data_path)
    return data


data=load_data()



top10_recent = data[
    (data.SeasonRank <= 10) & (data.Round == data.Round.max())
].GuildName.unique()
max_date = str(data[data.GuildName.isin(top10_recent)].Date.max()).split(" ")[0]

fig2 = go.Figure()


for guild, dat in data[data.GuildName.isin(top10_recent)].groupby("GuildNameExtra"):
    growth_rates_percentage = dat["GrowthRate"]
    fig2.add_trace(
        go.Waterfall(
            orientation="v",
            x=dat["Round"],
            y=growth_rates_percentage,
            name=guild,
            # text=f"{guild}",
            decreasing=dict(marker=dict(color="red")),
            increasing=dict(marker=dict(color="green")),
        )
    )
annotations = []
annotations.append(
    dict(
        text=f"Created by: SantaMonica @ MolochTH<br>Last update: {max_date}",
        xref="paper",
        yref="paper",
        x=1.16,
        y=-0.05,
        xanchor="right",
        yanchor="top",
        font=dict(family="Arial", size=12, color="rgb(150,150,150)"),
        showarrow=False,
    )
)    

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
    # traceorder="reversed",
    title = "Guild",
    font=dict(family="Arial", size=15),
    bgcolor=None,
    bordercolor=None,
    borderwidth=0,
                ),
    annotations=annotations,
)

st.plotly_chart(fig2, theme="streamlit", use_container_width=True)