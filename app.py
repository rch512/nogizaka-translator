import streamlit as st
import sqlite3

# 1. Page Config (Tab Title and Icon)
st.set_page_config(page_title="NogiTranslator", page_icon="💜")


# 2. Database Connection Function
def get_blogs():
    conn = sqlite3.connect("nogizaka.db")
    cursor = conn.cursor()
    # Get all blogs, sorted by newest date
    cursor.execute("SELECT author, title, date, content_jp, content_en, url FROM blogs ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# 3. Sidebar (The Menu)
st.sidebar.title("💜 NogiTranslator")
st.sidebar.write("Auto-translated blogs from Nogizaka46")

# Filter by Member (Bonus Feature!)
# We will just show "All" for now, but this is where you'd put a dropdown later.
selected_member = st.sidebar.selectbox("Filter by Member", ["All Members"])

# 4. Main Page Header
st.title("坂道 Blog Feed")
st.divider()  # Adds a nice line

# 5. Fetch Data
blogs = get_blogs()

if not blogs:
    st.info("No blogs found in database. Run main.py to scrape some!")
else:
    # 6. Loop through blogs and display them
    for blog in blogs:
        # Unpack the tuple
        author, title, date, content_jp, content_en, url = blog

        # Create a "Card" for each blog
        with st.container():
            # Header: Author Image (Placeholder) & Name
            col1, col2 = st.columns([1, 4])
            with col1:
                st.write("👤")  # Placeholder for member face
            with col2:
                st.subheader(f"{author}")
                st.caption(f"{date}")

            # Blog Title
            st.markdown(f"### {title}")

            # The Content (Using an "Expander" to keep it clean)
            with st.expander("📖 Read Translated Blog"):
                st.write(content_en)
                st.markdown("---")
                st.caption("Original Japanese Text:")
                st.text(content_jp[:200] + "...")  # Preview only
                st.link_button("Go to Official Blog", url)

            st.divider()  # Line between posts