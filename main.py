import os

import discord

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
    elif message.content.startswith('#hello'):
        await message.channel.send("Hai, how are u")

client.run(TOKEN)