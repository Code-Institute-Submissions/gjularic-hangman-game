## Flowchart

![Flowchart](images//flowchart.png)

## Technologies used

- Python
- [Lucidchart](https://lucid.co/) - for flowchart

## Testing

- tested if the HANGMAN variable is displaying hangman graphic correctly in the console
- tested random word generation
- tested user input guess
- used letters are being added to the list correctly
- status of the word is being updated correctly every turn
- tested while loops that are checking if user is typing numbers or multiple letters
- tested if play_again function works properly

## Bugs
- main while loop is stopping before user runs out of 7 tries - condition set up in the while loop needed to be changed
- it's possible to type in the same letter infinite number of times - added while loop to fix this
- user could type in the numbers - added while loop to fix, it will check if the user input is a number or letter
- user can type in multiple letters - added this into while loop so that only one letter can be typed in
- there's no way to play again when the game ends - put the code into separate functions as it has became more complex and to allow replayability

## Deployment

### Heroku
- Navigate to heroku dashboard
- Click "New" and select "Create new app"
- Input unique name for the app
- Select "Settings" from the tabs
- Click "Reveal Config Vars"
- Input PORT and 8000 and click add
- Click "Add buildpack"
- Add "nodejs" and "python" from the list, click save
- Select "Deploy" tab
- Select "GitHub - Connect to GitHub"
- Search for the GitHub repository by name
- Click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually

## Credits

- [W3schools](https://www.w3schools.com/)
- [Hangman ASCII art](https://github.com/gieseanw/Hangman/blob/master/HangmanLogo2.txt) - made and adjusted the states from it
- [StackOwerflow](https://stackoverflow.com/)