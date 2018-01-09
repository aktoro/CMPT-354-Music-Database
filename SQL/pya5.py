import pymssql
conn = pymssql.connect (host='cypress.csil.sfu.ca', user='s_avneett', password='hG4GQ6F4gL6HnMnQ', database='avneett354')


conn.autocommit(True)
cursor = conn.cursor()

def part1():
    try:
        isrc = raw_input("Enter ISRC: ")
        title = raw_input ("Enter title: ")
        year = raw_input("Enter year: ")
        artistname = raw_input("Enter artist name: ")
        add_row = "INSERT INTO Song ([isrc], [title], [year], [artistname]) VALUES ('"+ isrc + "', '" + title +"', '" + year +"', '" + artistname +"')"
        if isrc=="":
            print "ERROR ***ISRC can't be blank*** TRY AGAIN"
            print ''
            part1()
        if title=="":
            print "ERROR ***Title can't be blank*** TRY AGAIN"
            print ''
            part1()
        if year=="" or year.isdigit()==False: 
            print "ERROR ***Year needs to be integer*** TRY AGAIN"
            print ''
            part1() 
        if artistname=="":
            print "ERROR ***Artist name can't be blank*** TRY AGAIN"
            print ''
            part1()    
        cursor.execute(add_row)
    except:
        print "ERROR ***Either year is less than start date or artist does not exist. Check and try again!***"
        print ''
        part1()
    print "***Successfully added into Song table!***"
    print ''
    print "***Listing all songs of that artist:***"
    print ''
    cursor.execute('SELECT * FROM Song WHERE artistname=%s', artistname)
    for row in cursor:
        print ("ISRC= %s, Song_name= %s" % (row[0], row[1]))
    print ''
    print "***Listing all musicians who play for that artist:***"
    print ''
    cursor.execute('SELECT DISTINCT m.msin, m.firstname, m.lastname, m.birthdate FROM Song s INNER JOIN Plays p ON s.artistname=p.artistname INNER JOIN Musician m ON p.msin=m.msin WHERE s.artistname=%s', artistname)
    for row in cursor:
        print ("first_name= %s, last_name= %s, birthdate= %s" % (row[1], row[2], row[3]))

part1()    
