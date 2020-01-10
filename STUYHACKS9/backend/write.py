import dbm.gnu
import json



#ye it should make a db file i think/ kinda like a dictionary
# neight
#i searched this up on the python documentation and it said that this is used for small amounts of data that can be stored in key value pairs/ uh i got a back up plan if this doesnt work -> i just wanna test it for now

"""
if dbm.whichdb('Database') == '':
  x = 'dbm'
else:
  x = dbm.whichdb('Database')


dbm.whichdb(filename)
his function attempts to guess which of the several simple database modules available — dbm.gnu, dbm.ndbm or dbm.dumb — should be used to open a given file.

Returns one of the following values: None if the file can’t be opened because it’s unreadable or doesn’t exist; the empty string ('') if the file’s format can’t be guessed; or a string containing the required module name, such as 'dbm.ndbm' or 'dbm.gnu'.

"""

#Product_Info is a tuple with (UPC, (number_of_items, AvgPrice, Name)   

# UPC = b"123123123123"
# Num_of_items = b'3'
# Avg = b'5'
# Name = b"Applex"
    
def write(product_info):
  with dbm.gnu.open('Database', 'c') as db:
    db[product_info[0]] = product_info[1]
    
    print('added keyvalue pair')
    #db.sync()
  #how to store values of a class
  # answer: products.to_dict()
  
  #ig imma try running this and c if it works
  #
  # though I'm not sure what will happen with the nested objects
def get_user(UPC): 
  with dbm.gnu.open('Users', 'c') as db:
    #dbm = []
    k = db.firstkey()
    while k != None:
      print(k)
      if json.loads(k) == UPC:
        return db[UPC]
      k = db.nextkey(k)
      print(k)
    print('User Name not found')
    return False


def add_name(name):
  with dbm.gnu.open('Database', 'c') as db:
    db[key] = json.dumps(value)

## we can store anything with this that is json-serializable
def generic_write(*key_value_pair):
    with dbm.gnu.open('Database', 'c') as db:
        for key, value in key_value_pair:
            db[key] = json.dumps(value)
        db.sync()
        print('added keyvalue pair')
        

def read(UPC): #UPC is string
  #dbm.whichdb('Database')
  with dbm.gnu.open('Database', 'c') as db:
    k = db.firstkey()
    while k != None:
      print(k)
      if k == UPC:
        print('predecode:' + db[UPC])
        return json.loads(db[UPC])
      k = db.nextkey(k)
    print('UPC isnt in dictionary')
    return None
    
    
    
  
  #find distance
#p.finddistance((40.6102, -73.9193), (((40.909880 , -74.934588), 1), ((40.909880 , -74.934588), 1) ))

def find_distance(user_location, locations): 
  #locations is list of ((lat, long), price)
  import math
  close_enough = []
  R = 6371e3       
  for i in locations:
    φ1 = math.radians(user_location[0])
    φ2 = math.radians(i[0][0]);
    Δφ = math.radians(i[0][0] - user_location[0]);
    Δλ = math.radians(i[0][1] - user_location[1]);
    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    print(i, d)
    if d < 50000: #meters
      close_enough.append(i[1])
  return close_enough #returns a list of prices close enough
  
#write((UPC, (Num_of_items + Avg + Name)))
#print(read(UPC))

#using dbm


# Open database, creating it if necessary.


    # # Record some values
    # db[b'hello'] = b'there'
    # db['www.python.org'] = 'Python Website'
    # db['www.cnn.com'] = 'Cable News Network'

    # # Note that the keys are considered bytes now.
    # assert db[b'www.python.org'] == b'Python Website'
    # # Notice how the value is now in bytes.
    # assert db['www.cnn.com'] == b'Cable News Network'

    # # Often-used methods of the dict interface work too.
    # print(db.get('python.org', b'not present'))

    # # Storing a non-string key or value will raise an exception (most
    # # likely a TypeError).
    # db['www.yahoo.com'] = 4

  #how UPC codes work 

#   A UPC code is a 12 digit code displayed in two different ways.

# The first is a barcode, which is designed to be easily read by computer scanners. It consists of alternating white and black bars of various widths. Each numeral from zero to nine corresponds to a specific pattern of bars.

# For example, a one would be written as three bars each two lengths wide followed by a bar one length wide. Remember that you need to consider both the white and black bars when deciphering the code.

# The barcode starts and ends with a black bar, a white bar, and a black bar, each one unit in width. These are called the start code and the end code. Between the start and end codes, you'll find the bars indicating the numbers in the code.

# The 12-digit UPC code is actually three groups of numbers with different purposes. In a product UPC, the first six numbers indicate the manufacturer, the next five digits are an item number, and the final number is the check digit.


# The check digit is there to help ensure that the right number has been scanned or hand-entered. To check whether the correct numbers are in the code, add up all of the odd digits in the code and multiply the result by three. Then add up all of the even digits and add them to the result. The amount you would need to add to that amount to reach a multiple of ten should match the check digit. If not, something has gone wrong.