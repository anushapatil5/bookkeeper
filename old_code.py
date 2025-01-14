# streamlit_app.py - Spotify for Books

import streamlit as st
import random
import base64

# Streamlit App UI - MUST be the first command
st.set_page_config(page_title="Bookify - Spotify for Books", page_icon="📚", layout="wide")

# Custom CSS for Spotify-like theme
def set_background():
    st.markdown(
        """
        <style>
        /* Background and text styling */
        body {
            background-color: #191414;
            color: #FFFFFF;
        }
        .stApp {
            background-color: #191414;
        }
        h1, h2, h3, h4, h5, h6, .stTextInput, .stSelectbox, .stButton {
            color: #1DB954;
        }
        .css-1d391kg, .css-ffhzg2 {
            background-color: #212121;
            color: #FFFFFF;
        }
        .stButton > button {
            background-color: #1DB954;
            color: #FFFFFF;
            border: None;
            padding: 10px 24px;
            border-radius: 20px;
        }
        .stButton > button:hover {
            background-color: #1ed760;
            color: #191414;
        }
        .css-2trqyj {
            background-color: #212121;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sample book data
books = [
    {"title": "Atomic Habits", "genre": "Self-Help", "description": "An Easy & Proven Way to Build Good Habits & Break Bad Ones."},
    {"title": "The Midnight Library", "genre": "Fiction", "description": "A novel about all the choices that go into a life well lived."},
    {"title": "Becoming", "genre": "Biography", "description": "Michelle Obama's memoir exploring her life and journey."},
    {"title": "Educated", "genre": "Biography", "description": "A memoir by Tara Westover about growing up in a survivalist family."},
    {"title": "Deep Work", "genre": "Productivity", "description": "Rules for focused success in a distracted world."},
]

# Genres for filtering
genres = list(set(book['genre'] for book in books))

def recommend_books(selected_genre):
    return [book for book in books if book['genre'] == selected_genre]

# Apply custom theme
set_background()

# Streamlit UI
st.markdown("""<h1 style='color:#1DB954;'>📚 Bookify - Spotify for Books</h1>""", unsafe_allow_html=True)
st.markdown("""<h3 style='color:#FFFFFF;'>Discover your next favorite book!</h3>""", unsafe_allow_html=True)

# Genre selection
selected_genre = st.selectbox("Choose a genre", ["All"] + genres)

# Recommend books based on genre
if selected_genre == "All":
    recommended = random.sample(books, k=min(3, len(books)))
else:
    recommended = recommend_books(selected_genre)

# Display recommended books
st.markdown("### Recommended Books:")
for book in recommended:
    st.markdown(f"""
    <div style='background-color:#212121; padding:10px; border-radius:10px; margin-bottom:10px;'>
        <h4 style='color:#1DB954;'>{book['title']}</h4>
        <p style='color:#FFFFFF;'>*Genre:* {book['genre']}</p>
        <p style='color:#FFFFFF;'>{book['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Playlist creation
st.markdown("---")
st.markdown("""<h3 style='color:#1DB954;'>📖 Create Your Reading Playlist</h3>""", unsafe_allow_html=True)
playlist = st.text_input("Name your playlist:")
selected_books = st.multiselect("Select books to add:", [book['title'] for book in books])

if st.button("Save Playlist"):
    if playlist and selected_books:
        st.success(f"Playlist '{playlist}' created with {len(selected_books)} books!")
    else:
        st.warning("Please enter a playlist name and select at least one book.")

# Metrics Tracking Placeholder
st.markdown("---")
st.caption("Prototype for user testing. Metrics tracking coming soon!")

# Footer
st.markdown("""<p style='color:#FFFFFF;'>Created by Anusha Patil | Share your feedback!</p>""", unsafe_allow_html=True)
