from flask import Flask
import sqlite3

#Syndesi me Vasi kai orismos kersora
conn = sqlite3.connect('Project.db')
c = conn.cursor()

#Customers
def create_tableC():
    c.execute('CREATE TABLE IF NOT EXISTS Customs(ID INTEGER PRIMARY KEY, Fullname TEXT, Surname TEXT, Email TEXT, Telephone TEXT, Age TEXT) ')
    

#kalesma twn function
create_tableC()


