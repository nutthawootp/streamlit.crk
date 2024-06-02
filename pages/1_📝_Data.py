import streamlit as st
import pandas as pd
from pandas.io.formats.style import Styler
# import pandas_profiling 
# from streamlit_pandas_profiling import st_profile_report
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.stoggle import stoggle

st.set_page_config(
    page_title="Data",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Developed and Maintained by **SantaMonica @ MolochTH**"},
)
st.logo(r"images\grandmaster_1.png",icon_image=r"images\grandmaster_1.png")

st.sidebar.image(
    r"images\molochth_logo.jpeg", use_column_width=True, output_format="PNG"
)
# st.sidebar.header("Raw Data")



@st.cache_data
def load_data() -> pd.DataFrame:
    csv_data_path = "https://raw.githubusercontent.com/nutthawootp/CRK_guild_boss/main/data/CRK_guild_boss.csv"
    data = pd.read_csv(csv_data_path)
    return data


def style_df(df: pd.DataFrame) -> Styler:
    """
    Apply styling to a DataFrame for better display in the notebook.

    Args:
        dataframe (pd.DataFrame): The dataframe to be styled.

    Returns:
        Styler: A styled DataFrame with applied formatting.
    """
    # ! TODO: make table disply more beautiful
    dataframe = df.copy()

    # Define properties
    null_cell_style = "background-color: rgba(238, 238, 238, 0.2);color:white"
    negative_zero_style = "color:red"
    plus_green_style = "color:darkgreen"

    # Define formatting
    formatting_dict = {
        "GrowthRate": "{:.2f}%",
    }

    for column in dataframe.select_dtypes(include=["datetime"]):
        dataframe[column] = dataframe[column].dt.strftime(date_format="%d %b %Y")

    # Apply formatting and styling
    styled_dataframe = (
        dataframe.style.highlight_null(props=null_cell_style)
        .highlight_between(
            left=None,
            right=0,
            props=negative_zero_style,
            subset=dataframe.select_dtypes(include=["int", "float"]).columns,
        )
        .highlight_between(
            left=0,
            right=None,
            props=plus_green_style,
            subset=["DiffSeasonRank", "DiffRoundRank"],
        )
        .format(formatter=formatting_dict, precision=2, thousands=",", decimal=".", na_rep="-")  # type: ignore
    )

    # Format "DiffSeasonRank" and "Diff RoundRank" columns
    for column in ["DiffSeasonRank", "DiffRoundRank"]:
        if column in dataframe.columns:
            styled_dataframe.format(
                formatter={
                    column: lambda x: (
                        " ▲{:.0f}".format(x)
                        if x > 0  # type: ignore
                        else " ▼{:.0f}".format(abs(x)) if x < 0 else " "  # type: ignore
                    )
                },
                subset=[column],
                precision=0,
            )

    return styled_dataframe




data = load_data()

# -- Main
st.title("📝 Data")
st.divider()  # 👈horizontal rule


st.subheader(
    ":blue[Data Dictionary]",
)

dict_content = f"""

The dataset contains {data.shape[1]} columns and {data.shape[0]} rows:

| Column Name       | Data Type | Description                                                                 |
|-------------------|-----------|-----------------------------------------------------------------------------|
| `Date`            | Date      | The date when the data was recorded, in YYYY-MM-DD format.                   |
| `Season`          | Integer   | The season number.                                                           |
| `Round`           | String    | The round within the season, formatted as 'X-Y', where X is the Season and Y is the Round. |
| `GuildName`       | String    | The name of the guild.                                                      |
| `GuildNameExtra`  | String    | Additional information or alias for the non-English guild name.                         |
| `Trophies`        | Integer   | The number of trophies the guild has earned in the current round.            |
| `SeasonTotal`     | Integer   | The running total of trophies the guild has earned in the current season.     |
| `RoundRank`       | Integer   | The rank of the guild in the current round based on the number of trophies in the current round.  |
| `DiffRoundRank`   | Integer   | The change in the guild's rank compared to the previous round.               |
| `SeasonRank`      | Integer   | The overall rank of the guild in the current round based on the number of total trophies.  |
| `DiffSeasonRank`  | Integer   | The change in the guild's overall rank compared to the previous round.              |
| `Improvement`     | Integer   | The improvement of the guild's trophies earned in the current round.compared to the previous round.  |
| `GrowthRate`      | Float     | The growth rate of the guild's performance (in term of trophies).                                  |



"""

st.markdown(dict_content)

st.divider()

st.subheader(
    ":blue[View Data]",
)

st.write('Choose the tab to view the raw data in different formats.')

tab1, tab2, tab3 = st.tabs(["Raw", "Styler", "Explorer"])

with tab1:
    st.dataframe(data)

with tab2:
    st.dataframe(style_df(data))

with tab3:
    st.dataframe(dataframe_explorer(df=data,case=False,))  


st.divider()

# stoggle(summary="📑 More info", content=)

# st.subheader(
    # ":blue[Exploratory Data Analysis]",
# )

# report = data.profile_report() # type: ignore

# st_profile_report(report)

