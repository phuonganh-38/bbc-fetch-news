import streamlit as st
from scraper import Scraper

class App:
    def __init__(self) -> None:
        self.scraper = Scraper()
        self.categories = {
            "News": ["War in Ukraine", "US & Canada", "UK", "Africa", "Asia", "Australia", "Europe", "Latin America", "Middle East", "BBC InDepth"],
            "Sport": ["Football", "Cricket", "Formula 1", "Rugby Union", "Golf", "Athletics", "Cycling"],
            "Business": ["Executive Lounge", "Technology of Business", "Future of Business"],
            "Innovation": ["Technology", "Science", "Artificial Intelligence", "AI v the Mind"],
            "Culture": ["Film & TV", "Music", "Art", "Style", "Books", "Entertainment News"],
            "Travel": ["Destinations", "Worlds Table", "Cultural Experiences", "Adventures", "Specialist"],
        }

    def run(self):
        st.set_page_config(page_title="BBC News", layout="wide", initial_sidebar_state="expanded")

        st.markdown(
        """
        <style>
        /* Main background */
        body {
            background-color: black; /* Black background */
            color: white; /* White text */
        }

        /* Title styling */
        h1, h2, h3, h4, h5, h6 {
            color: #FF9415; /* Orange for headings */
        }

        /* Sidebar styling */
        .stSidebar {
            background-color: black; /* Black sidebar */
            color: white; /* White text in sidebar */
        }
        .stSidebar div {
            color: white; /* White for sidebar text */
        }

        /* Sidebar title styling */
        .sidebar-title {
            font-size: 30px; /* Larger font size */
            font-weight: bold; /* Bold text */
            color: white; /* White color */
            margin-bottom: 10px; /* Add spacing below */
        }

        /* Fetch News Button styling */
        div.stButton > button {
            background-color: #FF9415; /* Orange button fill */
            color: black; /* Black text */
            border: none; /* Remove border */
            border-radius: 8px; /* Rounded corners */
            padding: 0.5em 1em; /* Padding for buttons */
            font-size: 18px; /* Font size for buttons */
            font-weight: bold; /* Bold text */
        }

        }
        div.stButton > button:hover {
            background-color: #ff7700; /* Darker orange on hover */
            color: black; /* Black text on hover */
        }

        /* Divider styling */
        hr {
            border: 1px solid #FF9415; /* Orange dividers */
        }
        </style>
        """,
        unsafe_allow_html=True
        )


        # Sidebar for navigation
        st.sidebar.markdown("<div class='sidebar-title'>Navigator</div>", unsafe_allow_html=True)
        selected_category = st.sidebar.selectbox("Select a category:", list(self.categories.keys()))
        subcategories = self.categories.get(selected_category, [])
        selected_subcategory = st.sidebar.selectbox("Select a subcategory:", subcategories)

        fetch_news_btn = st.sidebar.button("Fetch News", type="primary")

        # Main content area
        st.markdown("<h1 style='color: #FF9415;'>BBC News</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            **Welcome to BBC News Scraper!**  
            Use the sidebar to select a category, then fetch the latest news articles.
            """
        )


        if fetch_news_btn:
            news_articles = self.scraper.scrape_bbc_subcategory(selected_category, selected_subcategory)

            if news_articles:
                for article in news_articles:
                    st.divider()
                    st.subheader(article["headline"])
                    st.write(article["description"])
            else:
                st.error("No articles found or failed to fetch.")

app = App()
app.run()
