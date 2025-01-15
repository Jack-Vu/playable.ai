LOL Imma be real it took me hours to get this to work on my local machine so lets hope that you can also get it to work

To run locally you want to create a local environment and have python installed ensuring that python version is between 3.10-3.12 unfortunately it can be lower or higher since the installed packages will conflict and welp you won't be able to use it

Windows:
    create virtual environment:
    python -m venv yourenv

    activate it:
    .\yourenv\Scripts\activate

    install required packages:
    pip install -r requirements.txt

    start backend:
    python main.py

Linux:
    create virtual environment:
    python -m venv yourenv

    activate it:
    source venv/bin/activate

    install required packages:
    pip install -r requirements.txt

    start backend:
    python main.py

Mac: Lol I don't know google it

once you have the virtual environment running you can the frontend will work as intended good luck cause you'll need it
