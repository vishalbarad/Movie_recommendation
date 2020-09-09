from flask import Flask,render_template,request
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

def load_movie():
    movies_df = pd.read_csv("movies.csv")
    return movies_df

def load_rating():
    rating_df = pd.read_csv("ratings.csv")
    return rating_df

def load_popular_movie():
    movies_df = load_movie()
    movies_df.drop('genres', axis=1, inplace=True)

    rating_df = load_rating()
    rating_df.drop("timestamp", axis=1, inplace=True)

    df = pd.merge(movies_df, rating_df, on='movieId')
    movie_ratingCount = (df.groupby(by=['title'])['rating'].count().reset_index().
        rename(columns={'rating': 'totalRatingCount'})[['title', 'totalRatingCount']])

    rating_with_totalRatingCount = pd.merge(df, movie_ratingCount, on=['title'])
    movierating_threshold = 50
    popular_movie = rating_with_totalRatingCount[rating_with_totalRatingCount['totalRatingCount'] > 50]
    return popular_movie

@app.route('/')
def home():
    popular_movie = load_popular_movie()
    title = list()

    for i in (popular_movie['title'].unique()):
        title.append(i)

    return render_template('index.html',title=title)

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            Movie_name = request.form['mname']

            movies_df = load_movie()
            movies_df.drop('genres',axis=1,inplace=True)

            rating_df = load_rating()
            rating_df.drop("timestamp",axis=1,inplace=True)

            df = pd.merge(movies_df,rating_df,on='movieId')
            movie_ratingCount = (df.groupby(by = ['title'])['rating'].count().reset_index().
            rename(columns = {'rating': 'totalRatingCount'})[['title', 'totalRatingCount']])

            rating_with_totalRatingCount = pd.merge(df,movie_ratingCount,on=['title'])
            movierating_threshold = 50
            popular_movie = rating_with_totalRatingCount[rating_with_totalRatingCount['totalRatingCount']>50]

            movie_feature_df=popular_movie.pivot_table(index='title',columns='userId',values='rating')
            movie_feature_df.fillna(0,inplace=True)

            movie_feature_df_matrix = csr_matrix(movie_feature_df.values)

            model = NearestNeighbors(metric='cosine',algorithm='brute')
            model.fit(movie_feature_df_matrix)#Fit spares matrix

            a = movie_feature_df.index
            movie_ind = pd.DataFrame({'asso_num':[i for i in range(movie_feature_df.shape[0])]},index=a)

            moive_index = movie_ind.asso_num[Movie_name]

            distance,indices = model.kneighbors(movie_feature_df.iloc[moive_index,:].values.reshape(1,-1),n_neighbors=11)

            title = list()
            for i in (popular_movie['title'].unique()):
                title.append(i)

            sent_2 = list()
            sent_3 = list()
            sent_4 = list()
            length = len(distance.flatten())
            for i in range(0,length):
                if i==0:
                    sent_1 = movie_feature_df.index[moive_index]
                else:
                    sent_2.append(i)
                    sent_3.append(movie_feature_df.index[indices.flatten()[i]])
                    sent_4.append(distance.flatten()[i])

            return render_template('index.html',sent_1=sent_1,sent_2=sent_2,sent_3=sent_3,sent_4=sent_4,length=length,title=title)

        except:
            popular_movie = load_popular_movie()

            title = list()
            for i in (popular_movie['title'].unique()):
                title.append(i)

            error = " Movie does not found please check spelling and case sensitivity or enter valid movie name with year."

            return render_template('index.html',error=error,title=title)

if __name__ == '__main__':
    app.run(debug=True)