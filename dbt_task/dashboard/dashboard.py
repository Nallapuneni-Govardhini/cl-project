import streamlit as st
import pandas as pd

FIRST_CLICK_PATH = "data/first_click_op.csv"
LAST_CLICK_PATH = "data/last_click_op.csv"

st.set_page_config(
    page_title="CL Project Dashboard",
    layout="wide"
)

st.title("Dashboard")
st.caption("First-Click vs Last-Click (dbt + BigQuery)")

# Loading data
@st.cache_data
def load_data():
    first = pd.read_csv(FIRST_CLICK_PATH)
    last = pd.read_csv(LAST_CLICK_PATH)
    return first, last

first_df, last_df = load_data()

st.subheader("Key Metrics")

col1, col2 = st.columns(2)

col1.metric(
    "First-Click Orders",
    first_df["order_id"].nunique() if "order_id" in first_df else len(first_df)
)

col2.metric(
    "Last-Click Orders",
    last_df["order_id"].nunique() if "order_id" in last_df else len(last_df)
)

st.subheader("Traffic Source")

fc_source = first_df.groupby("first_click_source").size().reset_index(name="orders")
lc_source = last_df.groupby("last_click_source").size().reset_index(name="orders")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### First-Click")
    st.bar_chart(fc_source.set_index("first_click_source"))

with col2:
    st.markdown("### Last-Click")
    st.bar_chart(lc_source.set_index("last_click_source"))


if "event_date" in first_df.columns:
    st.subheader("14-Day Attribution Trend")

    fc_ts = first_df.groupby("event_date").size()
    lc_ts = last_df.groupby("event_date").size()

    st.line_chart(
        pd.DataFrame({
            "First Click": fc_ts,
            "Last Click": lc_ts
        })
    )


with st.expander("To View First Click Raw Data expand this"):
    st.write("First Click")
    st.dataframe(first_df)

with st.expander("To View Last Click Raw Data expand this"):
    st.write("Last Click")
    st.dataframe(last_df)
