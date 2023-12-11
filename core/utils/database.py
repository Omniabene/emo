import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('film.db')
    cur = db.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS comedy(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS drama(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS fantasy(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS thriller(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS fighters(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS adventures(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS detectives(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS cartoons(id TEXT PRYMARY KEY, name TEXT, discription TEXT, link TEXT, poster TEXT)")
    # cur.execute("CREATE TABLE IF NOT EXISTS emo(id TEXT PRYMARY KEY, name TEXT)")
    db.commit()


async def get_info(genre, num):
    film = cur.execute(
        "SELECT name,discription,link,poster FROM '{genre}' WHERE id == '{id}'".format(genre=genre, id=num)).fetchone()
    return film


# async def get_emo():
#     emo = cur.execute("SELECT name FROM emo WHERE id == 1").fetchone()
#     return emo
#
#
# async def set_emo():
#     emo = cur.execute("SELECT name FROM emo WHERE id == 1").fetchone()
#     return emo















    # cur.execute("CREATE TABLE IF NOT EXISTS films(id genre TEXT, name TEXT, discription TEXT, link TEXT, poster TEXT)")