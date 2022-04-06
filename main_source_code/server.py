import socket
from game import Game
from _thread import *

number_max_player = 4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '127.0.0.1'
port = 5555
server_ip = socket.gethostbyname(server_address)
current_client_id = 0
#number_of_players = 1
start_game = False
game_running = False
game_started = [False, False, False, False]

try:
    sock.bind((server_address, port))

except socket.error as e:
    print(str(e))

             # tbd: nachfragen wie viele Spieler
sock.listen(number_max_player)      # tbd: wie viele Spieler? hier ist die maximalanzahl

print("Waiting for a connection")



def threaded_start_game():
    global start_game, current_client_id, game_running
#    while start_game == False:
#        pass
#    game.initiate_new_game()

    while True:
        if start_game == True:
            #print("Starting game ...")
            game_running = True
            game.initiate_new_game(current_client_id)
            start_game = False
        else:
            pass

def threaded_client(conn):

    global current_client_id, pos, game, start_game, game_running, game_started  # make current_client_id variable global
    # tbd: ip addresse an client ID binden  (global)
    conn.send(str.encode(str(current_client_id)))  # hier wird die ID als string gesendet
    current_client_id += 1
    reply = ''

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                conn.send(str.encode("Goodbye"))
                # tbd reconnect?
                # socket -> listen/accept incoming connections
                #sock.accept(id) ?
                break

            else:
                print("Received: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                #reply = "Hello Client " + str(id) + "! (from server)"
                opcode = arr[1]
                data = arr[2]

                if opcode == 's' :
                    start_game = True
                    reply = "starting game ..."
                    game_started = [True, True, True, True]

                if opcode == 'g' :       # r: requesting state  example: "1:r"
                    if id == 1:
                        if game_running:
                            pass
                    # tbd: anfragen des aktuellen standes des Objektes "game"
                    #reply = #get_game_state(id) # zustand karten need to know
                    #reply = "gamestate... "
                    jump_chat = False
                    if game_running:
                        reply = game.get_gamestate_string(id)
                        if game_started[id] == True:
                            reply = reply + "/game_started"
                            game_started[id] = False
                            #print("setting flag for game start!")
                            jump_chat = True
                        # print("Test: " + reply)
                    else:
                        reply = "0s,0s,0s/0s,0s,0s:0s,0s,0s:0s,0s,0s:0s,0s,0s/0,0,0,0/0s/0/1"

                    if jump_chat == False:
                        if game.chatbox.update[id] == True:
                            reply = reply + '/' + game.chatbox.last_line()
                            game.chatbox.update[id] = False

                elif opcode == 'a' and game_running:  # t: turn to game-logic
                    reply = game.action(id, data)
                    print("action: " + reply)
                    # tbd: give turn-request to game.py
                    # return 1 if turn is valid + return new state
                    # return 0 if turn is invalid
                    # send command to game logic
                    # if gültig: zug beendet, else weiter warten

                elif opcode == 'c':  # m: message to chat-box

                    reply = game.chatbox.new_line(id, data) # tbd !

                    #tbd: parse msg to chat-box and send chat to all clients
                else:
                    reply = "no valid request"
                print("Sending: " + reply)

            conn.sendall(str.encode(reply)) # sent to client
        except:
            break

    print("Connection Closed")
    conn.close()


game = Game()
start_new_thread(threaded_start_game,())


while True:     # tbd: here the number of wanted players-1 must be inserted - game starts when all players are connected
    conn, addr = sock.accept()    # conn ist ein Socket Objekt, addr ist die IP addresse
    # print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,))

