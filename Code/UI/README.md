# README

We have created a user interface to help users interact with the model and get predictions using Flask. Flask is a is a lightweight WSGI web application framework. Every game on Lichess has a unique
ID in the URL which differentiates each game. We take this unique ID as input and from this we get the entire game in PGN format. We extracted this game and converted it to CSV. We then extracted detailed
features and performed pre-processing in the same way as it was performed to build the model. The final result will be one dataframe tuple. For the UI, we use the best model for each prediction which we had
generated and saved. We give this tuple as input to the model and get the desired output.

## Main Page:
![Main Page](https://drive.google.com/uc?export=view&id=13hxU_hv4PFnfSoKkFoCWDmCuiSCgclzb)

## Predict Elo Rating (Classification):
![Elo Rating - Classification](https://drive.google.com/uc?export=view&id=1Su6qkMVsGys9LWv_tVYi7aTIuNLg3BJv)

## Predict Elo Rating (Regression):
![Elo Rating - Regression](https://drive.google.com/uc?export=view&id=1avn-ntgv8HVMU0-gbCDA71nYAwCl07VZ)

## Predict Game Type (Classification):
![Game Type](https://drive.google.com/uc?export=view&id=18dMSuSgP-3UEJHbPVyfjhtUSlKuysGLZ)
