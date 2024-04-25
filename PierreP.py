import streamlit as st
from utils import recommendations, read_object

with st.sidebar:
    def load_data():
        cos_simi_mat_desc = read_object('artifacts/cosine_similarity_desc.pkl')
        df_manga_rel = pd.read_csv('artifacts/manga_clean.csv', index_col='manga_id')
        titles = df_manga_rel['ctitle'].dropna().tolist()
        return cos_simi_mat_desc, titles

    if "titles_dict" not in st.session_state:
        st.session_state["titles_dict"] = {}
    simi_mat, titles = load_data()
    st.session_state["titles_dict"]["titles"] = titles
    titles = st.session_state.get("titles_dict", {}).get("titles", [])
    page_number = st.session_state.get("page_number", 0)
    if "next_page" in st.session_state:
        page_number += 1
    elif "prev_page" in st.session_state:
        page_number -= 1
    with st.expander('Popular Titles'):
        start_idx = page_number * 20
        end_idx = min((page_number + 1) * 20, len(titles))
        for title in titles[start_idx:end_idx]:
            st.write(title)
        if page_number > 0:
            st.button("Previous", key="prev_page")
        st.write(f"Page {page_number + 1}")
        if end_idx < len(titles):
            st.button("Next", key="next_page")
    st.session_state["page_number"] = page_number
