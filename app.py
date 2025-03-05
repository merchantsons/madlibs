from flask import Flask, render_template, request

app = Flask(__name__)

# Simple Mad Libs story
story = """
Once upon a time in a {adjective} land, there lived a {noun1} named {name}.
{name} loved to {verb} and always wore a {adjective2} {noun2}.
One day, {name} found a {adjective3} {noun3} and decided to go on a {adjective4} adventure.
The adventure was filled with {plural_noun} and {adjective5} surprises.
In the end, {name} learned that the most important thing in life is to be {adjective6}.
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        name = request.form['name']
        adjective = request.form['adjective']
        noun1 = request.form['noun1']
        verb = request.form['verb']
        adjective2 = request.form['adjective2']
        noun2 = request.form['noun2']
        adjective3 = request.form['adjective3']
        noun3 = request.form['noun3']
        adjective4 = request.form['adjective4']
        plural_noun = request.form['plural_noun']
        adjective5 = request.form['adjective5']
        adjective6 = request.form['adjective6']

        # Generate the story
        filled_story = story.format(
            name=name,
            adjective=adjective,
            noun1=noun1,
            verb=verb,
            adjective2=adjective2,
            noun2=noun2,
            adjective3=adjective3,
            noun3=noun3,
            adjective4=adjective4,
            plural_noun=plural_noun,
            adjective5=adjective5,
            adjective6=adjective6
        )

        # Render the result page
        return render_template('result.html', story=filled_story)
    
    # Render the input form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)