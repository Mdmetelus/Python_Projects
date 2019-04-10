import random
import math
import time

class Queue:
  # bfs
  def __init__(self):
      self.queue =[]
  def enqueue(self,value):
      self.queue.append(value)
  def dequeue(self)
      if(self.size) > 0
          return self.queu.pop(0)
      else:
          return None
  def size(self):
      return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
  
    def addFriendship(self, userID, FriendID):
        if userID('You cannot be you own friend")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("You already are friends with this person")
        else:
            self.friendships[userId].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        self.lastID += 1
        self.users[self.lastId] = User(name)
        self.friendship[self.lastId] = set()

    def populateGraph(self, nunUsers, avgFriendships):
        self.lstId = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, numUsers):
            self.addUsers(f"User {i}")
        possibleFriendships = []
        
