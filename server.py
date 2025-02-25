''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request # Import Flask, render_template, request from the flask pramework package : TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer# Import the sentiment_analyzer function from the package created: TODO

app = Flask("Sentiment Analyzer")#Initiate the flask app : TODO

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response["label"]
    score = response["score"]
    if label is None:
        return "Invalid input! Try again!"
    else:
        return "Your text {} has a score of {}.".format(label.split("_")[1], score)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")#TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run(host="0.0.0.0", port=5000, debug=True)
