import pandas as pd

data = {
    'review': [
        "this movie is so good! i love it!",
        "worst film , i hate it the most!",
        "pakka 1000 cr, super hit! amazing",
        "loved it will watch again",
        "not bad , just okay!",
        "average, one time watch",
        "one man show",
        "great movie",
        "i hate that movie worst of all time",
        "good movie , can be done better",
        "had an amazing time there",
        "i personally didnt like it!",
        "dont go with family,",
        "can watch 1 time!"

    ],
    'sentiment': [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0 ]
}

df = pd.DataFrame(data)
df.to_csv('movie_reviews.csv', index=False)
print("dataset created and saved as 'movie_review.csv' ")