import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

APP_TITLE = '📊Election Metrics'
APP_SUB_TITLE = 'Source: Elections Department Singapore (ELD)'

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # Load Data
    df = pd.read_csv('GE2025_MP Data/GE2025_Results.csv')

    elector_column = 'Number of Electors'
    constituency_type = 'Type'

    eligible_voter_count = df[elector_column].sum()
    total_reject_count = 42945  # Taken from ELD Media Release Report

    grc_count = df.loc[df[constituency_type] == 2].shape[0]
    smc_count = df.loc[df[constituency_type] == 1].shape[0]

    # Pie Chart for eligible valid votes
    total_valid_votes = df["Total Valid Votes"].sum()

    # Pie chart for participating voters
    no_show = eligible_voter_count - total_valid_votes - total_reject_count

    labels = ["Valid Votes", "Rejected Votes", "Did not vote"]
    sizes = [total_valid_votes, total_reject_count, no_show]
    colors = ['#05d800','#ff6464', '#6464ff']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=90, pctdistance=0.9)
    ax.axis('equal')

    # Metric Data
    st.write("")
    col1, col2, = st.columns([3, 1])
    col3, col4 = st.columns([3, 1])
    col5, col6 = st.columns([3, 1])

    with col1:
        st.metric(f'Registered Voters', '{:,}'.format(eligible_voter_count))
    with col2:
        st.metric(f"Total Votes Cast (Valid + Rejected)", "{:,}".format(total_valid_votes + total_reject_count))

    with col3:
        st.metric(f"Total Valid Votes", "{:,}".format(total_valid_votes))
    with col4:
        st.metric(f"Total Rejected Votes", "{:,}".format(total_reject_count))

    with col5:
        st.metric('Total GRC Count', '{:,}'.format(grc_count))
    with col6:
        st.metric('Total SMC Count', '{:,}'.format(smc_count))

    st.write("")
    st.write(f"**Registered Voters Count: {'{:,}'.format(eligible_voter_count)}**")
    st.caption("Note: Value may not be exact due to rounding.")
    st.pyplot(fig)


if __name__ == '__main__':
    main()