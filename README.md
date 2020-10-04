# How-good-is-a-chess-player

## Objective:
To build a model that will predict the Elo score of a chess player. Additionally, we are motivated to guess the type of game depending on the time limit of the game and predicting the result of the game, given a board position as an input.

## Datasets:
We used the [Lichess Dataset](https://database.lichess.org/) which is an open-source internet chess server. The data of all games since 2013 is available in LiChess Database. There are over 800,000,000 games in the database, each tagged with ratings of both players and the speed.

**Data format:** The format of the data in LiChess Database is Portable Game Notation (PGN). PGN is a plain text in computer-processable format for recording chess games (both the moves and related data), supported by many chess programs. PGN is structured "for easy reading and writing by human users and for easy parsing and generation by computer programs." The chess moves themselves are given in algebraic chess notation. Each game contains a header file and a sequence of moves made by each player.


## Project includes:
1. Conversion of PGN format to CSV format
2. Feature extraction and Pre-processing of data
3. Exploratory Analysis
4. Building models to predict:
    - The player's ELO rank (Classification and Regression)
    - Game type using the game transcript
    - Quality of play based on final board position
    - Next move prediction
5. User interface to help users interact with the model and get predictions using Flask. 

**Technologies being used:** PyTorch, Python (chess.pgn library)
