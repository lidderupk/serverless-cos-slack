# Automate a manual task using Apache OpenWhisk and Slack Bot

## Current situations
A team member analyses an excel file and sends stats to a slack channel everyday at 9AM

## Goal
1. Create an OpenWhisk action that will read the file from cloud object store and process it.
2. Create a second OpenWhisk action that will send the stats to slack.
3. Chain the two actions in a secquence and enable it to trigger daily at 9am.



