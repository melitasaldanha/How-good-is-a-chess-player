from flask import Flask, flash, request, redirect, render_template
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import tablib
import os
import pickle
import lichess.api
from lichess.format import PYCHESS
import chess.pgn


# App config.
# DEBUG = True

model_eloReg_white=pickle.load(open('models/lgbm_w2.sav', 'rb'))
model_eloReg_black=pickle.load(open('models/lgbm_b2.sav', 'rb'))

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
	
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def upload_file():
    link_text=request.form['link_text']
    pred_type=request.form['submit_button']
    if pred_type=='Predict Elo Rating':
        print('yo')        
    if pred_type=='Classify Elo Rating':
        print('yo Classify') 
    if pred_type=='Predict Game Type':
        print('yo game type')

        
    
    game = lichess.api.game(link_text, format=PYCHESS)

    # final_board=game.end().board()
    
    return render_template('result.html',pred_type=pred_type)

if __name__ == "__main__":
    app.run()