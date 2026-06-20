import streamlit as st
import pandas as pd
import sqlite3
from datetime import date, datetime, timedelta

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="Food Waste Management",
    page_icon="🥗",
    layout="wide"
)

# --------------------------------
# DATABASE CONNECTION
# --------------------------------
@st.cache_resource
def get_connection():
    conn = sqlite3.connect(
        "food_inventory.db",
        check_same_thread=False
    )
    return conn

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS food_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT,
    quantity INTEGER,
    purchase_date TEXT,
    usable_days INTEGER,
    expiry_date TEXT
)
""")

conn.commit()

# --------------------------------
# FUNCTIONS
# --------------------------------
def add_food(
    food_name,
    quantity,
    purchase_date,
    usable_days,
    expiry_date
):
    cursor.execute("""
    INSERT INTO food_items(
        food_name,
        quantity,
        purchase_date,
        usable_days,
        expiry_date
    )
    VALUES(?,?,?,?,?)
    """,
    (
        food_name,
        quantity,
        str(purchase_date),
        usable_days,
        str(expiry_date)
    ))

    conn.commit()


def load_data():
    return pd.read_sql(
        "SELECT * FROM food_items",
        conn
    )


def delete_item(item_id):
    cursor.execute(
        "DELETE FROM food_items WHERE id=?",
        (item_id,)
    )
    conn.commit()

# --------------------------------
# STYLING
# --------------------------------
st.markdown("""
<style>

.big-title{
font-size:40px;
font-weight:bold;
color:#2E8B57;
text-align:center;
}

.metric-card{
padding:10px;
border-radius:10px;
background:#ffffff;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# HEADER
# --------------------------------
st.markdown(
    "<div class='big-title'>🥗 Food Waste Management System</div>",
    unsafe_allow_html=True
)

st.write(
    "Track food expiry dates and reduce food waste."
)

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.header("Add Food Item")

with st.sidebar.form("food_form"):

    food_name = st.text_input(
        "Food Name"
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    purchase_date = st.date_input(
        "Purchase Date",
        value=date.today()
    )

    usable_days = st.number_input(
        "Usable Days",
        min_value=1,
        value=7
    )

    expiry_date = st.date_input(
        "Expiry Date",
        value=date.today()
        + timedelta(days=usable_days)
    )

    submitted = st.form_submit_button(
        "Add Item"
    )

    if submitted:

        if food_name:

            add_food(
                food_name,
                quantity,
                purchase_date,
                usable_days,
                expiry_date
            )

            st.success(
                "Food Item Added!"
            )

            st.rerun()

# --------------------------------
# LOAD DATA
# --------------------------------
df = load_data()

# --------------------------------
# SEARCH
# --------------------------------
search = st.text_input(
    "🔍 Search Food Item"
)

if search:
    df = df[
        df["food_name"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# --------------------------------
# STATUS CALCULATION
# --------------------------------
today = date.today()

fresh = 0
near = 0
expired = 0

if not df.empty:

    remaining = []
    status = []

    for exp in df["expiry_date"]:

        exp_date = datetime.strptime(
            exp,
            "%Y-%m-%d"
        ).date()

        days_left = (
            exp_date - today
        ).days

        remaining.append(days_left)

        if days_left < 0:
            status.append("Expired")
            expired += 1

        elif days_left <= 3:
            status.append("Near Expiry")
            near += 1

        else:
            status.append("Fresh")
            fresh += 1

    df["Remaining Days"] = remaining
    df["Status"] = status

# --------------------------------
# DASHBOARD
# --------------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Items",
    len(df)
)

c2.metric(
    "Fresh",
    fresh
)

c3.metric(
    "Near Expiry",
    near
)

c4.metric(
    "Expired",
    expired
)

st.divider()

# --------------------------------
# INVENTORY
# --------------------------------
st.subheader("Food Inventory")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info(
        "No food items available."
    )

# --------------------------------
# ALERTS
# --------------------------------
st.subheader("Expiry Alerts")

if not df.empty:

    alerts = df[
        df["Status"].isin(
            [
                "Near Expiry",
                "Expired"
            ]
        )
    ]

    if alerts.empty:

        st.success(
            "No food items are close to expiry."
        )

    else:

        for _, row in alerts.iterrows():

            if row["Status"] == "Expired":

                st.error(
                    f"{row['food_name']} expired "
                    f"{abs(row['Remaining Days'])} days ago."
                )

            else:

                st.warning(
                    f"{row['food_name']} expires in "
                    f"{row['Remaining Days']} days."
                )

# --------------------------------
# DELETE
# --------------------------------
if not df.empty:

    st.subheader("Delete Item")

    selected = st.selectbox(
        "Choose Food",
        df["food_name"]
    )

    if st.button(
        "Delete Selected"
    ):

        item_id = df[
            df["food_name"]
            == selected
        ]["id"].iloc[0]

        delete_item(item_id)

        st.success(
            "Deleted Successfully"
        )

        st.rerun()

# --------------------------------
# DOWNLOAD CSV
# --------------------------------
if not df.empty:

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "food_inventory.csv",
        "text/csv"
    )