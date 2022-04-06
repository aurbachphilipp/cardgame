import socket


class Connection:

    def __init__(self, host_address, port):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host_address  # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
        # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
        # ipv4 address. This feild will be the same for all your clients.
        self.port = port
        self.addr = (self.host, self.port)
        self.id = int(self.connect())


    def connect(self):
        self.client_sock.connect(self.addr)
        msg = self.client_sock.recv(2048).decode()
        print("connection established: ID = " + msg)
        return msg

    # -------  client request:    -------------
    #  id:opcode:data
    #  id = 0...3
    #  opcode = "a" oder "g" oder "c""
    #  data = "0" für request gamestate (opcode g)
    #  data = "message content" für request_chat_msg_append (opcode c)
    #  data = <action_type>,<card_position>, für request_action (opcode a)

    # ------- server reply:      -------------
    #   request_action:
    #
    #
    #   play_facedown_card: reply = <facedown_card>:<turn_was_valid>
    #
    #   request_gamestate:
    #   #9h, 10h, 5h/4h,fd,3h:b,0,b:4h,5h,3h:0,0,0/(hand_cards_self_id)6h,7h,8h/(turn)0/(deck)1/"message"
    #   reply = <pile_top_cards>/<open_cards:id0>:<open_cards:id1>:<open_cards:id2>:<open_cards:id3>/number_of_handcards id0, id1, id2, id2/<hand_cards_"self.id">/<flag_is_turn>/<flag_deck_is_not_empty>/<message>
    #
    #   request_chat_msg_append:
    #   reply = 1 if server approves
    #   else = 0


    # my_string = "0,3s,10h/4h,fd,3h:fd,0,fd:4h,5h,3h:0,0,0/8,7,6,5/6h,7h,8h,8h/0/1/messagecontent-lastmessage"
    # list = my_string.split("/")
    # length = len(list)
    # if length == 6: # msg dabei
    # if length == 5: # msg nicht dabei

    def request_action(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            data = str(self.id) + ":a:" + data
            self.client_sock.send(str.encode(data))
            reply = self.client_sock.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

    def request_gamestate(self):
        """
        :param data: str
        :return: str
        """
        try:
            data = str(self.id) + ":g:0"
            self.client_sock.send(str.encode(data))
            reply = self.client_sock.recv(2048).decode()
            # res = reply.split(":") ...     tbd check if chatmsg is included!
            # client.chatbox.append(res[-1])
            return reply
        except socket.error as e:
            return str(e)

    def request_chat_msg_append(self, data):
        """
        :param data: str
        :return: str
        """

        try:
            data = str(self.id) + ":c:" + data
            self.client_sock.send(str.encode(data))
            reply = self.client_sock.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

    def request_start_game(self):
        """
        :param data: str
        :return: str
        """

        try:
            data = str(self.id) + ":s:0"
            self.client_sock.send(str.encode(data))
            reply = self.client_sock.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)