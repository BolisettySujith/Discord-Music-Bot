#Sujith
import os
import pyjokes
import discord
import datetime
from pytube import YouTube

TOKEN = "<TOKEN>"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#CPL'):
        await message.channel.send("""Semester 3 Course Page
        https://amritauniv.sharepoint.com/sites/AIE2020/SitePages/Semester-3.aspx
        Operating Systems
        https://amritauniv.sharepoint.com/sites/19AIE202OperatingSystems40/SitePages/19AIE202-Operating-Systems.aspx?web=1&OR=Teams-HL&CT=1630477344936
        Data Structures and Algorithms 2
        https://amritauniv.sharepoint.com/sites/19AIE203DataStructuresAlgorithms-2?OR=Teams-HL&CT=1630650595179
        Introduction to Robotics
        https://amritauniv.sharepoint.com/sites/19AIE201_Intro_to_Robotics/SitePages/ProjectHome.aspx
        Intelligence of Biological Systems 3
        https://amritauniv.sharepoint.com/sites/IntelligenceofBiologicalSystems3?OR=Teams-HL&CT=1630639882730
        Mathematics for intelligent Systems 3 
        https://amritauniv.sharepoint.com/sites/MIS32020batch
        Python for Machine Learning
        https://amritauniv.sharepoint.com/sites/19AIE205PythonforMachineLearningS3-2020Admissions/SitePages/19AIE205-Python-for-Machine-Learning.aspx?originalPath=aHR0cHM6Ly9hbXJpdGF1bml2LnNoYXJlcG9pbnQuY29tLzp1Oi9zLzE5QUlFMjA1UHl0aG9uZm9yTWFjaGluZUxlYXJuaW5nUzMtMjAyMEFkbWlzc2lvbnMvRVdOZmpaVWRJWHBOaDhDc2FnZFRzOUlCSlU4LVoxZC1jUmo2Q1pXTGxrTXVwZz9ydGltZT1aWE4zRGhGdDJVZw""")
    elif message.content.startswith('#help'):
        await message.channel.send("""
        Share point course Page links
        #CPL - For all cource pages links
        #sp-os - Operating Systems
        #sp-dsa - Data Structures and Algorithms
        #sp-robotics - Introduction to Robotics
        #sp-bio - Intelligence of Biological Systems
        #sp-mat - Mathematics for intelligent Systems
        #sp-ml - Python for Machine Learning

        Interation commands:
        hello, i am fine, what about you, what is your name, you are lucky
        """)
    elif message.content.startswith('hello'):
        await message.channel.send("Hai, how are u")
    elif 'joke' in message.content:
        await message.channel.send(pyjokes.get_joke())
    elif 'current time' in message.content:
        await message.channel.send(datetime.datetime.now().strftime('%I:%M %p'))
    elif message.content.startswith('i am fine'):
        await message.channel.send("ohh...")
    elif message.content.startswith('download an youtube video'):
        await message.channel.send("Sorry the feature is not implemented")
    elif ('good morning' in message.content) or ('good evening' in message.content) or ('good night' in message.content) or ('good afternoon' in message.content):
        if 'morning' in message.content:
            await message.channel.send("Good Morning")
        elif 'evening' in message.content:
            await message.channel.send("Good Evening")
        elif 'night' in message.content:
            await message.channel.send("Good Night")
        elif 'afternoon' in message.content:
            await message.channel.send("Good Afternoon")
    # elif message.content.startswith('!yt'):
    #     link= message.content.replace("!yt", "")
    #     yt=YouTube(link)
    #     yt.streams.get_highest_resolution().download()
    #     await message.channel.send("Downloaded the video")
    elif message.content.startswith('what about you'):
        await message.channel.send("i am superb, having no assignments and tests")
    elif message.content.startswith('you are lucky'):
        await message.channel.send("yeah")
    elif message.content.startswith('what is your name'):
        await message.channel.send("i am a AI BOT")
    elif message.content.startswith('#sp-mat'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/MIS32020batch")
    elif message.content.startswith('#sp-ml'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/19AIE205PythonforMachineLearningS3-2020Admissions/SitePages/19AIE205-Python-for-Machine-Learning.aspx?originalPath=aHR0cHM6Ly9hbXJpdGF1bml2LnNoYXJlcG9pbnQuY29tLzp1Oi9zLzE5QUlFMjA1UHl0aG9uZm9yTWFjaGluZUxlYXJuaW5nUzMtMjAyMEFkbWlzc2lvbnMvRVdOZmpaVWRJWHBOaDhDc2FnZFRzOUlCSlU4LVoxZC1jUmo2Q1pXTGxrTXVwZz9ydGltZT1aWE4zRGhGdDJVZw")
    elif message.content.startswith('#sp-robotics'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/19AIE201_Intro_to_Robotics/SitePages/ProjectHome.aspx")
    elif message.content.startswith('#sp-bio'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/IntelligenceofBiologicalSystems3?OR=Teams-HL&CT=1630639882730")
    elif message.content.startswith('#sp-dsa'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/19AIE203DataStructuresAlgorithms-2?OR=Teams-HL&CT=1630650595179")
    elif message.content.startswith('#sp-os'):
        await message.channel.send("https://amritauniv.sharepoint.com/sites/19AIE202OperatingSystems40/SitePages/19AIE202-Operating-Systems.aspx?web=1&OR=Teams-HL&CT=1630477344936")

client.run(TOKEN)