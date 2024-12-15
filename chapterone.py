from collections import Counter, defaultdict


'''What does this data dump look like? It consists of a list of users, each
represented by a dict that contains that user’s id (which is a number) and
name (which, in one of the great cosmic coincidences, rhymes with the
user’s id):'''

'''He also gives you the “friendship” data, represented as a list of pairs of
IDs:'''

users = [{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }]


interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0,
"Storm"), (0, "Cassandra"), (1, "NoSQL"), (1, "MongoDB"), (1,
"Cassandra"), (1, "HBase"), (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3,
"R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"), (4,
"machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
(5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5,
"programming languages"), (6, "statistics"), (6, "probability"), (6,
"mathematics"), (6, "theory"), (7, "machine learning"), (7, "scikit-learn"),
(7, "Mahout"), (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), (9,
"Java"), (9, "MapReduce"), (9, "Big Data")]


friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


friendships = {user["id"]:[]for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j) #add j as a friend of user i 
    friendships[j].append(i) #add i as a friend of user j 

print(friendships)

#what's the avg number of connections 

def number_of_friends(user):
    """how many friends doed _user_have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users) #lenght of users list
avg_connections = total_connections /num_users
print(avg_connections)


#Most connected people 
#create a list (user_id, numbrt_of_friends)
number_of_friends_by_Id = [(user["id"], number_of_friends(user)) for user in users]
number_of_friends_by_Id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

print(number_of_friends_by_Id)

#design a “Data Scientists You May Know”suggester.

def foaf_ids_bad(user):
    '''friend of friend'''
    return [foaf_id 
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]
    
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id 
        for friend_id in friendships[user_id] #for each of my friends
        for foaf_id in friendships[friend_id] # find their friend
        if foaf_id != user # who aren't me
        and foaf_id not in friendships[user_id] # and arent my friend
    )
    
print(friends_of_friends(users[3]))


# finding friend with interest 
#This works, but it has to examine the whole list of interests for everysearch If we have a lot of users and interests (or if we just want to do a lotof searches
def data_scientist_who_like(target_interest):
    '''Find the ids of all users who like the target interest'''
    return [ user_id
            for user_id, user_interest in interests
            if user_interest == target_interest
        
    ]
    
    
    
    
