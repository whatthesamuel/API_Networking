from flask import Flask, request, jsonify
import time
import threading


app = Flask(__name__)

players = []

def find_player(name):
    for dictionary in players:
        if name in dictionary.values():
            return dictionary
    return None

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/UpdatePlayer', methods=['POST'])
def UpdatePlayer():
    data = request.get_json()

    player = find_player(data.get('name'))
    if player is None:
        print("Player Not found ")
        return jsonify("Player Not found")

    player['hp'] = data.get('hp')
    print(player)

    # process data
    return jsonify(player)

@app.route('/AddPlayer', methods=['POST'])
def AddPlayer():
    data = request.get_json()

    player = find_player(data.get('name'))
    if player is not None:
        print('player not found ', data)
        return jsonify('player already exists')

    NewPlayer = {'name': data.get('name'), 'hp': 100}
    players.append(NewPlayer)
    print(data.get('name') + " logged in")
    # process data
    return jsonify(NewPlayer)


@app.route('/GetPlayer', methods=['GET'])
def GetPlayer():
    data = request.get_json()

    player = find_player(data.get('name'))
    if player is None:
        print('player not found ', data)
        return jsonify('player not found')
    print(player)
    # process data
    return jsonify(player)

def Update():
    while True:
        # do main logic
        time.sleep(1/60)

x = threading.Thread(target = Update, daemon=True)
x.start()

if __name__ == '__main__':
    app.run()