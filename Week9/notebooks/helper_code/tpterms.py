# Function to compute top topic terms from given model (i.e., LDA or NMF)

def get_topics(cv, model):
    # Number of terms per topic to display
    max_topics = 10

    # Number of terms per topic to retain
    max_labels = 5

    topics = []
    feature_names = cv.get_feature_names()

    # Iterate through the matrix components
    for idx, topic in enumerate(model.components_):

        # First we sort the terms in descending order ([::-1])
        # And then retiain only the top terms
        top_topics_idx = topic.argsort()[::-1][:max_topics]

        top_topics = [feature_names[jdx] for jdx in top_topics_idx]

        # Now extract out the terms themselves and display
        top_features = " ".join(top_topics)
        print('Topic {0:2d}: {1}'.format(idx, top_features))
        topics.append(", ".join(top_topics[:max_labels]))
        
    return(topics)