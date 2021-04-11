from flask import Flask, flash, session, render_template, redirect, url_for, request
from datetime import datetime
import pymysql
import os

# set var
total_playerInRoom = 0

# set list
room_list = []
player_list = []
num_of_ppl_list = []
playerInRoom_list = []
currentRoom_list= []

app = Flask(__name__)

def readSQL_room():
    '''
    read all room data from sql
    '''
    global total_room
    
    # reset room list
    room_list = []
    num_of_ppl_list = []
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select * from room"
    
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        
        #store total room no.
        total_room = len(data)
        
        for e in range(len(data)):
            room_list.append(data[e][0])
            room_list.append(data[e][1])
            room_list.append(data[e][2])
            room_list.append(data[e][3])
            room_list.append(data[e][4])
            room_list.append(str(data[e][5]))
            room_list.append(str(data[e][6]))
            room_list.append(data[e][7])
            
            num_of_ppl = str(data[e][5])+"/"+str(data[e][6])
            num_of_ppl_list.append(num_of_ppl)
        
        return room_list, total_room, num_of_ppl_list
    
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
def readSQL_game():
    '''
    read all games data from sql
    '''
    # reset game list
    game_list = []
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select * from game"
    
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        
        #store total game no.
        total_game = len(data)
        
        for e in range(len(data)):
            game_list.append(data[e][0])
            game_list.append(data[e][1])
            
        return game_list, total_game
    
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()

def readSQL_allplayer():
    '''
    read all player data from sql
    '''
    # reset all player list
    allPlayer_list = []
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql_query = "select player_id, room_id, name, username, language, gender from player"
    
    try:
        cursor.execute(sql_query)
        data = cursor.fetchall()
        
        #store total player num
        total_player = len(data)
        
        for e in range(len(data)):
            allPlayer_list.append(data[e][0])
            allPlayer_list.append(data[e][1])
            allPlayer_list.append(data[e][2])
            allPlayer_list.append(data[e][3])
            allPlayer_list.append(data[e][4])
            allPlayer_list.append(data[e][5])
        
        return allPlayer_list, total_player
    
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
def readSQL_playerInRoom():
    '''
    read all player in the room from sql
    '''
    # reset list
    playerInRoom_list = []
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    try:
        cursor.execute("select player_id, room_id, name, username, language, gender from player where room_id = %s", (player_list[1]))
        data = cursor.fetchall()
        
        #store total player num in the room
        total_playerInRoom = len(data)
        
        for e in range(len(data)):
            if data[e][0] != player_list[0]:
                playerInRoom_list.append(data[e][0])
                playerInRoom_list.append(data[e][1])
                playerInRoom_list.append(data[e][2])
                playerInRoom_list.append(data[e][3])
                playerInRoom_list.append(data[e][4])
                playerInRoom_list.append(data[e][5])
        
        return playerInRoom_list, total_playerInRoom
    
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()

def readSQL_currentPlayer():
    '''
    read current player data from sql
    '''
    global player_list
    
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    #prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select * from player where player_id = %s"
    adr = (player_list[0])
    
    try:
        cursor.execute(sql, adr)
        data = cursor.fetchall()
        
        # set var
        player_list = []
        
        for e in range(len(data)):
            player_list.append(data[e][0])
            player_list.append(data[e][1])
            player_list.append(data[e][2])
            player_list.append(data[e][3])
            player_list.append(data[e][4])
            player_list.append(data[e][5])
            player_list.append(data[e][6])
            player_list.append(data[e][7])
            player_list.append(data[e][9])
                
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    return player_list

def readSQL_currentRoom():
    '''
    read current room data from sql
    '''
    global currentRoom_list
    
    # set list
    currentRoom_list = []
    
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    #prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select * from room where room_id = %s"
    adr = (player_list[1])
    
    try:
        cursor.execute(sql, adr)
        data = cursor.fetchall()
        
        for e in range(len(data)):
            currentRoom_list.append(data[e][0])
            currentRoom_list.append(data[e][1])
            currentRoom_list.append(data[e][2])
            currentRoom_list.append(data[e][3])
            currentRoom_list.append(data[e][4])
            currentRoom_list.append(data[e][5])
            currentRoom_list.append(data[e][6])
            currentRoom_list.append(data[e][7])
                
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    return True

@app.route('/login', methods = ['post'])
def form_login():
    '''
    check submitted form in login modal
    '''
    global player_list

    #set var
    player_list = []
    
    #get form data
    uname = request.form['uname']
    pw = request.form['pw']
    
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    #prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select * from player where (username = %s and pw = %s) or (email = %s and pw = %s)"
    adr = (uname, pw, uname, pw)
    
    try:
        cursor.execute(sql, adr)
        data = cursor.fetchall()
        
        if cursor.rowcount != 0:
            if data[0][8] == "verifying":
                flash("Verify your email to activate the account", "warning")
            else:
                for e in range(len(data)):
                    player_list.append(data[e][0])
                    player_list.append(data[e][1])
                    player_list.append(data[e][2])
                    player_list.append(data[e][3])
                    player_list.append(data[e][4])
                    player_list.append(data[e][5])
                    player_list.append(data[e][6])
                    player_list.append(data[e][7])
                    player_list.append(data[e][9])
                
                session['logged_in'] = True
        else:
            flash("Login failed", "danger")

    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    return redirect("/")

@app.route('/forgot_password/submit', methods = ['post'])
def form_forgotPW():
    '''
    check submitted form in forgot password
    '''
    email = request.form['email']

    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "select email from player where email = %s"
    adr = (email)
    try:
        cursor.execute(sql, adr)
        
        if cursor.rowcount != 0:
            # send email validation
            flash("Sent email validation, please check your email", "warning")
        else:
            flash("Email doesn't exist", "danger")
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    return redirect('/forgot_password')

@app.route('/createAC/submit', methods = ['post'])
def form_createAC():
    '''
    check submitted form in create account
    '''
    #set var
    flag = "true"
    
    name = request.form['playerName']
    uname = request.form['uname']
    email = request.form['email']
    gender = request.form['gender']
    language = request.form['language']
    pw = request.form['pw1']
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    #get the datetime now
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute("select username, email from player")
        data = cursor.fetchall()
        for row in data:
            if uname == row[0]:
                flag = "false"
                flash("Username exists", "danger")
            elif email == row[1]:
                flag = "false"
                flash("Email exists", "danger")
                
        if flag == "true":
            cursor.execute("INSERT INTO player(room_id,name, username, pw, language, gender, email, status, createdSince) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(0,name,uname,pw,language,gender,email,"verifying",dt))
            db.commit()
            
            flash("Please check your email validation to activate your account", "warning")
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    return redirect('/createAC')

@app.route('/create_room/submit', methods = ['post'])
def form_createRoom():
    '''
    check submitted form in create room
    '''
    title = request.form['title']
    game = request.form['game']
    maxPlayer = request.form['maxPlayer']
    language = request.form['language']
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # get the datetime now
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # set var
        counter = 0
        # check if room num in sql is in sequence
        for e in range(0, len(room_list), 8):
            counter = counter + 1
            roomNum = room_list[e]
            if counter != roomNum:
                cursor.execute("INSERT INTO room(room_id, host_username, title, game, language, joinedPlayer, maxPlayer, createdSince) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter,player_list[3],title,game,language,"1",maxPlayer,dt))
                cursor.execute("UPDATE player SET room_id = %s where player_id = %s", (counter,player_list[0]))
                break
        
        if counter == roomNum:
            cursor.execute("INSERT INTO room(room_id,host_username, title, game, language, joinedPlayer, maxPlayer, createdSince) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(roomNum+1,player_list[3],title,game,language,"1",maxPlayer,dt))    
            cursor.execute("UPDATE player SET room_id = %s where player_id = %s", (roomNum+1,player_list[0]))
        
        db.commit()
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    readSQL_currentPlayer()
    return redirect('/member')

@app.route('/returnJoinRoom', methods = ['post'])
def returnJoinRoom():
    '''
    receive joined room num from js
    '''
    global joinRoom
    
    joinRoom = request.form['joinRoom']
    
    return joinRoom
    
@app.route('/join', methods = ['post'])
def form_joinRoom():
    '''
    join room
    '''
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    try:
        cursor.execute("UPDATE player SET room_id = %s where player_id = %s", (joinRoom, player_list[0]))
        sql="select joinedPlayer from room where room_id = %s"
        cursor.execute(sql,(joinRoom))
        joinedPlayer = cursor.fetchall()
        cursor.execute("UPDATE room SET joinedPlayer = %s where room_id = %s", (joinedPlayer[0][0]+1, joinRoom))
        db.commit()
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    readSQL_currentPlayer()
    return redirect("/member")

@app.route('/member/deleteRoom', methods = ['post'])
def form_deleteRoom():
    '''
    delete room from sql
    '''
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    try:
        cursor.execute("UPDATE player SET room_id = 0 where room_id = %s", (player_list[1]))
        cursor.execute("DELETE from room where room_id = %s", (player_list[1]))
        db.commit()
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    readSQL_currentPlayer()
    return redirect("/member")

@app.route('/member/quitRoom', methods = ['post'])
def form_quitRoom():
    '''
    quit room in sql
    '''
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    try:
        cursor.execute("UPDATE player SET room_id = 0 where player_id = %s", (player_list[0]))
        cursor.execute("UPDATE room SET joinedPlayer = %s where room_id = %s", (currentRoom_list[5]-1, player_list[1]))
        db.commit()
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    readSQL_currentPlayer()
    return redirect("/member")

@app.route('/returnKickID', methods = ['post'])
def returnKickID():
    '''
    receive kicked player ID from js
    '''
    global kickID
    
    kickID = request.form['kickID']
    
    return True

@app.route('/kick', methods = ['post'])
def form_kick():
    '''
    kick player from room in sql
    '''
    #open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    try:
        cursor.execute("UPDATE player SET room_id = 0 where player_id = %s", (kickID))
        db.commit()
        cursor.execute("UPDATE room SET joinedPlayer = %s where room_id = %s", (currentRoom_list[5]-1, player_list[1]))
        db.commit()
            
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    readSQL_currentPlayer()
    return redirect("/member")

@app.route('/about/contact_us/submit', methods = ['post'])
def form_contact_us():
    '''
    check submitted form in contact us
    '''
    # if player is not logged in, player ID sets to 0, and read name and email from input
    if not player_list:
        player_id = 0
        name = request.form['playerName']
        email = request.form['email']
    # else read player ID, name, email from existing data
    else:
        player_id = player_list[0]
        name = player_list[2]
        email = player_list[7]
    subject = request.form['subject']
    
    # open database connection
    db = pymysql.connect(host="localhost", user="root", password="", database="matching_players")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # get the datetime now
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute("INSERT INTO contact_us(player_id, name, email, subject, status, createdSince) VALUES (%s,%s,%s,%s,%s,%s)",(player_id,name,email,subject,"waiting",dt))
        db.commit()
        
        flash("Submitted, please wait for 2-3 working days for email respond")
        
    except Exception as e:
        print("Error reading data from MySQL table", e)
    
    db.close()
    
    return redirect('/about/contact_us')

@app.route('/')
def home():
    '''
    home page
    '''
    global room_list, total_room, num_of_ppl_list
    
    room_list, total_room, num_of_ppl_list = readSQL_room()
    
    if not session.get('logged_in'):
        flash("Login to create or join a room", "warning")
        return render_template("home.html", loginSuccess="false",room_list=room_list, total_room=total_room, num_of_ppl_list=num_of_ppl_list)
    else:
        return render_template("home_member.html", loginSuccess="true", player_list=player_list, room_list=room_list, total_room=total_room, num_of_ppl_list=num_of_ppl_list)

@app.route('/createAC')
def createAC():
    '''
    create account page
    '''
    if not session.get('logged_in'):
        return render_template("createAC.html", loginSuccess="false")
    else:
        return render_template("createAC.html", loginSuccess="true")

@app.route('/forgot_password')
def forgotPW():
    '''
    forgot password page
    '''
    if not session.get('logged_in'):
        return render_template("forgotPW.html", loginSuccess="false")
    else:
        return render_template("forgotPW.html", loginSuccess="true")

@app.route('/create_room')
def create_room():
    '''
    create room page
    '''
    return render_template("create_room.html")

@app.route('/games')
def games():
    '''
    games page
    '''
    game_list, total_game = readSQL_game()
    
    if not session.get('logged_in'):
        return render_template("games.html", loginSuccess="false",game_list=game_list, total_game=total_game)
    else:
        return render_template("games.html", loginSuccess="true",game_list=game_list, total_game=total_game)

@app.route('/about/our_story')
def our_story():
    '''
    our story page
    '''
    if not session.get('logged_in'):
        return render_template("our_story.html", loginSuccess="false")
    else:
        return render_template("our_story.html", loginSuccess="true")

@app.route('/about/contact_us')
def contact_us():
    '''
    contact us page
    '''
    if not session.get('logged_in'):
        return render_template("contact_us.html", loginSuccess="false")
    else:
        return render_template("contact_us.html", loginSuccess="true")

@app.route('/member')
def member():
    '''
    member page
    '''
    room_list, total_room, num_of_ppl_list = readSQL_room()
    allPlayer_list, total_player = readSQL_allplayer()
    # get data if player has a room
    if player_list[1] != 0:
        playerInRoom_list, total_playerInRoom = readSQL_playerInRoom()
        readSQL_currentRoom()
    else:
        #currentRoom_list = []
        currentRoom_list.clear()
        currentRoom_list.append("N/A")
        currentRoom_list.append("N/A")
        playerInRoom_list = []
        total_playerInRoom = 0
    
    if session.get('logged_in'):
        return render_template("member.html", currentRoom_list=currentRoom_list,playerInRoom_list=playerInRoom_list, total_playerInRoom=total_playerInRoom,allPlayer_list=allPlayer_list, total_player=total_player,player_list=player_list, total_room=total_room, num_of_ppl_list=num_of_ppl_list, room_list=room_list)

@app.route('/logout')
def logout():
    '''
    logout function
    '''
    session['logged_in'] = False
    playerID = 0
    
    return home()

# debug

if __name__ == '__main__':
    app.debug = True
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0", port = 100)