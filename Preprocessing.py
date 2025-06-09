# -*- coding: utf-8 -*-
# %%

"""
This script provides a collection of functions to clean and style dataframes. It includes functions for renaming columns, correcting data types, estimating trophies, removing unnecessary rows, 
and adding rank change information. The main function clean_data applies these functions to a dataframe. Additionally, it includes functions for styling dataframes, renaming guild names, 
and adding extra guild information. The script can be run as a standalone module to clean a specific file, MolochTHbackup.xlsx.
"""
# Ignore warning
import warnings
warnings.filterwarnings(action='ignore')

from datetime import datetime
from typing import Sequence

import numpy as np
import pandas as pd
from pandas.io.formats.style import Styler


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


def edit_GuildName(name: str) -> str:
    """
    edit_GuildName
        edit guild names that are not in English by adding the pronunciation in English after the name.

    Args:
        name (str): the name of the guild

    Returns:
        str: the name of the guild with pronunciation
    """
    RENAME_DICT: dict = {
        "미라클": "미라클 (miracle)",
        "님": "님 (nim)",
        "오로라": "오로라 (aurora)",
        "무야호": "무야호 (mu-ya-ho)",
        "열매": "열매 (yeol-mae)",
        "이지스": "이지스 (aegis)",
        "재난경보": "재난경보 (jae-nan-gyeong-bo)",
        "사혼": "사혼 (sa-hon)",
        "쿠벤저스": "쿠벤저스 (cubengers)",
        "秋": "秋 (aki)",
        "감동": "감동 (gam-dong)",
        "夏至": "夏至 (xià-zhì)",
    }

    if name in RENAME_DICT.keys():

        return RENAME_DICT[name]
    else:
        return name


def rename_columns(df: pd.DataFrame, column_names: dict) -> pd.DataFrame:
    """
    rename_columns
        Rename the columns in the dataframe

    Args:
        df (DataFrame): the dataframe
        column_names (dict): the mapping of old column names to new column names

    Returns:
        DataFrame: the dataframe with renamed columns
    """
    df = df.rename(column_names, axis=1)
    return df


def add_guildnameextra(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_guildnameextra
        Add 'GuildNameExtra' column

    Args:
        df (DataFrame): the dataframe

    Returns:
        DataFrame: the dataframe with 'GuildNameExtra' column
    """

    df["GuildNameExtra"] = df.GuildName.apply(edit_GuildName).astype("string")

    return df


def add_earned_trophies(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_earned_trophies
        Add the weekly earned trophies column

    Args:
        df (DataFrame): the dataframe

    Returns:
        pd.DataFrame: dataframe with 'Trophies' column added
    """

    # Sort values by Guild Name and Round
    df = df.sort_values(by=["GuildName", "Round"])

    # Look up the Trophies from the previous round
    df["PrevRoundTrophies"] = df["Trophies"].shift(periods=1).fillna(0).astype(int)

    # Replace the previous round values in rows with minimum Trophies of each season with zero
    for row in df.itertuples():

        guild_name = row.GuildName
        season = row.Season

        if (
            row.Trophies
            == df[(df.GuildName == guild_name) & (df.Season == season)].Trophies.min()
        ):

            df.loc[row.Index, "PrevRoundTrophies"] = 0

    # Calc the weekly earned
    df["Earned"] = df["Trophies"] - df["PrevRoundTrophies"]

    # drop look up column and rename Trophies
    df.drop(columns="PrevRoundTrophies", inplace=True)

    # rename columns again
    df.rename(columns={"Trophies": "SeasonTotal", "Earned": "Trophies"}, inplace=True)

    return df


def add_round_rank(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_round_rank Add a new column 'RoundRank' based on the 'Trophies' columns

    Args:
        df (pd.DataFrame): _description_

    Returns:
            pd.DataFrame: _description_
    """
    # Create a new column 'RoundRank' based on the 'Round' and 'Trophies' columns
    df["RoundRank"] = (
        df.sort_values(["Round", "Trophies"], ascending=[True, False])
        .groupby(["Round"], observed=True)["Trophies"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    return df


# def replace_initial_zero(df: pd.DataFrame, column: str) -> pd.DataFrame:
#     """
#     replace_initial_zero Replace values of column specified in argument with zero in minimum date rows of each guild

#     Args:
#         df (pd.DataFrame): the dataframe
#         column (str): the column name that needs to be cleaned

#     Returns:
#         Dataframe: the cleaned dataframe
#     """

#     for row in df.itertuples():

#         guild_name = row.GuildName

#         date = row.Date

#         if row.Date == df[df.GuildName == guild_name].Date.min():

#             df.loc[row.Index, column] = 0
#     return df


def add_improvment_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_improvment_col Add "Improvement" column to dataframe, which is the difference between the current week's Trophies and the previous week's Trophies for each guild

    Args:
        df (pd.DataFrame): the dataframe

    Returns:
        pd.DataFrame: the cleaned dataframe
    """

    # Sort values by Guild Name and Round
    df = df.sort_values(by=["GuildName", "Round"])

    df["Improvement"] = df.groupby("GuildName")["Trophies"].diff().fillna(0).astype(int)

    return df


def add_growthrate_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_growthrate_col
        Add 'GrowthRate' column, the growth rate (a.k.a. %change) of Trophies earned round over round for each guild,
        calculated by dividing the difference between the current week's Trophies and the previous week's Trophies
        for each guild by the previous week's Trophies, then multiply by 100.

    Args:
        df (DataFrame): the dataframe

    Returns:
        DataFrame: the dataframe with 'GrowthRate' column
    """

    # Sort values by Guild Name and Round
    df = df.sort_values(by=["GuildName", "Round"])

    # Calculate the growth rate use pct_change() method

    df["GrowthRate"] = df.groupby("GuildName")["Trophies"].pct_change() * 100

    # Fill NaN values with zero

    df["GrowthRate"] = df.GrowthRate.fillna(0)

    return df


def correct_dtype(df: pd.DataFrame) -> pd.DataFrame:
    """
    correct_dtype
        Correct the data type of dataframe

    Args:
        df (DataFrame): the dataframe

    Returns:
        DataFrame: corrected dataframe
    """
    # Change column type to category for column: 'Season','Round','Rank'
    df = df.astype(
        {
            "Season": "category",
            "SeasonRank": "category",
            "Round": "category",
            "GuildName": "string",
            "Trophies": "int64",
        }
    )

    df.Season = df.Season.cat.as_ordered()
    df.Round = df.Round.cat.as_ordered()
    df.SeasonRank = df.SeasonRank.cat.as_ordered()

    return df


def estimate_trophies(df: pd.DataFrame) -> pd.DataFrame:
    """
    estimate_trophies
        Estimate Trophies values for the guild that just made it to Top 20 after the season has started (Round 1).
        The Trophies value cannot be calculated due to the fact that baseline trophies data is not available.

    Args:
        df (DataFrame): the dataframe

    Returns:
        DataFrame: dataframe with estimated Trophies
    """

    # for "秋" guild we only had just made it to the leaderboard in season 3-3.
    # The estimation of the Trophies value will be done by divide the SeasonTotal value by 3,
    # which is the average of total trophies in season 3.

    # get row index value
    idx = df.loc[(df.GuildName == "秋") & (df.Round == "3-3"), "Trophies"].index

    # add the estimated value
    df.loc[idx, "Trophies"] = int(df.loc[idx, "SeasonTotal"].values[0] / 3)
    return df


def drop_columns(df: pd.DataFrame, column: str | Sequence) -> pd.DataFrame:
    """
    drop_columns
        Drop unnecessary columns
    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.drop(column, axis=1)

    return df


def rearrange_columns(df: pd.DataFrame, column_order: list) -> pd.DataFrame:
    """
    rearrange_columns
        Rearrange the columns in the dataframe.

    Args:
        df (DataFrame): the dataframe
        column_order (list): the order of the columns in the dataframe

    Returns:
        DataFrame: _description_
    """

    # rearrange columns
    df = df[column_order]
    return df


def drop_unnecessary_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    drop_unnecessary_rows
        Drop rows before 2024-02-27 and rows with null values in Trophies column
    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    # filter rows before 2024-02-27
    df = df[df["Date"].dt.date >= datetime(2024, 2, 27).date()]

    # drop rows with null values in Trophies column
    df = df.loc[df["Trophies"].notna()]

    return df


def add_rank_change(df: pd.DataFrame) -> pd.DataFrame:
    """
    add_rank_change
        Add change in 'Rank' column for each guild compared to the previous round.

    Args:
        df (DataFrame): the dataframe

    Returns:
        pd.DataFrame: the dataframe with added 'DiffRank____' column
    """
    rank_col_list = [
        ("".join(["Diff", col]), col) for col in df.columns if "Rank" in col
    ]

    for diff_col_name, rank_col_name in rank_col_list:
        df[diff_col_name] = (
            df.sort_values(["GuildName", "Round"], ascending=[True, True])
            .astype({rank_col_name: "int"})
            .groupby(["GuildName"])[rank_col_name]
            .diff()
            .fillna(0)
            .astype(int)
            * -1
        )
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    clean_data
        Clean the df_raw dataframe

    Args:
        df (DataFrame): the dataframe

    Returns:
        DataFrame: cleaned dataframe
    """

    # rename columns
    df = (
        df.pipe(
            rename_columns,
            column_names={"Rank": "SeasonRank"
                          , "Total Trophies": "Trophies"
                          }
                    )
        .pipe(drop_unnecessary_rows)
        .pipe(correct_dtype)
        .pipe(add_guildnameextra)
        .pipe(add_earned_trophies)
        .pipe(
            rearrange_columns,
            column_order=[
                "Date",
                "Season",
                "Round",
                "SeasonRank",
                "GuildName",
                "GuildNameExtra",
                "Trophies",
                "SeasonTotal",
            ],
        )
        .pipe(add_round_rank)
        .pipe(estimate_trophies)
        .pipe(add_improvment_col)
        .pipe(add_growthrate_col)
        .pipe(add_rank_change)
        .pipe(
            rearrange_columns,
            column_order=[
                "Date",
                "Season",
                "Round",
                "GuildName",
                "GuildNameExtra",
                "Trophies",
                "SeasonTotal",
                "RoundRank",
                "DiffRoundRank",
                "SeasonRank",
                "DiffSeasonRank",
                "Improvement",
                "GrowthRate",
            ],
        )
    )  # type: ignore

    # sort df values by Round and Rank
    df.sort_values(by=["Round", "SeasonRank"], inplace=True)

    # reset row imdex
    df.reset_index(drop=True, inplace=True)

    return df

def save_cleaned_data(df: pd.DataFrame, file_path: str=r"CRK_guild_boss") -> None:
    """
    save_cleaned_data
        Save the cleaned dataframe to an csv and pkl.

    Args:
        df (DataFrame): the cleaned dataframe
        file_path (str): the path to save the cleaned dataframe
    """
    csv_path = f"{file_path}.csv"
    pkl_path = f"{file_path}.pkl"
    
    df.to_csv(csv_path, index=False)    
    df.to_pickle(path=pkl_path)
    return None


#%%
if __name__ == "__main__":
    # file_path = r"MolochTHbackup.xlsx"
    # df_raw = pd.read_excel(file_path, sheet_name=6, header=1, usecols=range(1, 8))
    file_path = r"guild_battle.xlsx"
    df_raw = pd.read_excel(file_path, sheet_name=0, header=0, usecols=range(0, 6))    
    df = clean_data(df_raw)
    save_cleaned_data(df, file_path=r"CRK_guild_boss")

# %%
