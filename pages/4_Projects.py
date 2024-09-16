import streamlit as st 
import pandas as pd
st.set_page_config('Projects', page_icon='🚀', initial_sidebar_state='collapsed')


st.page_link('/Users/mikkelpedersen/Desktop/project_vs_studio/streamlit_app/Main_page.py', icon='🏛️', label='Home')


st.title('Projects')
st.write('Just give it a minute, why you in such a hurry??!!')
with st.container():


    import pandas as pd

    # https://files.grouplens.org/datasets/movielens/ml-25m.zip
    movies = pd.read_csv('/Users/mikkelpedersen/Desktop/project_vs_studio/random projekter/ml-25m/movies.csv')
    #movies.head()
    import re

    def clean_title(title):
        title = re.sub("[^a-zA-Z0-9 ]", "", title)
        return title
    movies["clean_title"] = movies["title"].apply(clean_title)
    movies


    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1,2))

    tfidf = vectorizer.fit_transform(movies["clean_title"])
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np

    def search(title):
        title = clean_title(title)
        query_vec = vectorizer.transform([title])
        similarity = cosine_similarity(query_vec, tfidf).flatten()
        indices = np.argpartition(similarity, -5)[-5:]
        results = movies.iloc[indices].iloc[::-1]
        
        return results
    # pip install ipywidgets
    #jupyter labextension install @jupyter-widgets/jupyterlab-manager
    import ipywidgets as widgets
    from IPython.display import display

    movie_input = widgets.Text(
        value='Toy Story',
        description='Movie Title:',
        disabled=False
    )
    movie_list = widgets.Output()

    def on_type(data):
        with movie_list:
            movie_list.clear_output()
            title = data["new"]
            if len(title) > 5:
                display(search(title))

    movie_input.observe(on_type, names='value')


    display(movie_input, movie_list)
    movie_id = 89745

    #def find_similar_movies(movie_id):
    movie = movies[movies["movieId"] == movie_id]
    ratings = pd.read_csv('/Users/mikkelpedersen/Desktop/project_vs_studio/random projekter/ml-25m/ratings.csv')
    #ratings.dtypes
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    #rec_percentages
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")
    def find_similar_movies(movie_id):
        similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
        similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
        similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

        similar_user_recs = similar_user_recs[similar_user_recs > .10]
        all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
        all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
        rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
        rec_percentages.columns = ["similar", "all"]
        
        rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
        rec_percentages = rec_percentages.sort_values("score", ascending=False)
        return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]


    movie_title = st.text_input("Enter a movie title you like:")

    # Display recommendations
    if movie_title:
        results = search(movie_title)
        if not results.empty:
            st.write("Top search results:")
            for idx, row in results.iterrows():
                st.write(f"{row['title']} ({row['genres']})")

            movie_id = results.iloc[0]["movieId"]
            similar_movies = find_similar_movies(movie_id)
            st.write('')
            st.write('')
            st.write('')
            st.write("Recommended movies based on similar user ratings:")
            for idx, row in similar_movies.iterrows():
                st.write(f"{row['title']} ({row['genres']}) - Score: {row['score']:.2f}")
        else:
            st.write("No movies found. Please try another title.")