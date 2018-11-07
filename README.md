<div align="center">
    <img src="https://zekro.de/src/ds-logo.png" width="300"/>
    <h1>~ DiscordScript ~</h1>
    <strong>Manage your Discord server with scripts!</strong><br><br>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="30" />&nbsp;
    <img src="https://forthebadge.com/images/badges/built-with-love.svg" height="30" />&nbsp;
</div>

---

# Motivation

If you are an owner of a larger Discord guild or a guild with a lot of roles and channels to manage, you may be annoyed by clicking and tweaking around in the discord overlay to create channels, roles and permissions for each of them. So, I thought, the best way to make this a bit easier, there must be a script-like tool which you can use to batch-execute Discord guild management operations - in best case timable and repeatable. So, I decited to create this script "language" to do so ;)

---

# Development state

This projekt is currently in a very early state of development. Actually, there is nothing really working currently, but I want to share the development phase of this project and maybe collect some tips to improve this plan.

---

# SYNTAX

> Generally, commands **must** be seperated with `;`. Lines, beginning with `#` are interpretet as comments and will be ignored completely.

### Commands

| Command | Description | State of implementation |
|---------|-------------|-------------------------|
| `HELP ([COMMAND])` | Display all commands or specific help for a command | ![](https://img.shields.io/badge/implemented-no-red.svg) |
| `TOKEN [TOKEN]` | Set Discord Bot API token to use other API endpoints with. This function is required to execute before every other action with the API | ![](https://img.shields.io/badge/implemented-yes-green.svg) |
| `SELECT [GUILD(S)\|CHANNEL(S)\|ROLE(S)\|USER(S)] (BY NAME [ID\|NAME])` | Select an object of GUILD, CHANNEL, ROLE or USER by ID (defaultly) or NAME. All follwoing queries will theb ne executed to the selected object. | ![](https://img.shields.io/badge/implemented-no-red.svg) |
| `DESCRIBE (GUILD(S)\|CHANNEL(S)\|ROLES(S)\|USERS(S) (, GUILD(S)\|...)...)` | Displays and lists information about all objects (or specific ones by passing filter) of the currently selected object. | ![](https://img.shields.io/badge/implemented-no-red.svg) |
| `CREATE (AND SELECT) GUILD\|CHANNEL\|ROLE [OPTIONS]` | Create an object inside of the selected object with property options passed by OPTIONS argument in form of JSON string like `"{'name': 'my-cool-channel', 'type': 0}"`. For documentation, take a look [here](https://discordapp.com/developers/docs/intro). If AND SELECT is included, the created object will automatically be selected after. | ![](https://img.shields.io/badge/implemented-no-red.svg) |
| `MODIFY [OPTIONS]` | Modify the selected type. Properies are passed here as same as for CREATE command. | ![](https://img.shields.io/badge/implemented-no-red.svg) |
| `DELETE` | Delete the currently selected object. Using this on USER objects, this will mean a kick of the user! | ![](https://img.shields.io/badge/implemented-no-red.svg) |


---

# Don't be rude, contribute!

Yes, I am an absolute python noob and I have never written a kind of language interpreter before, so this will be a quite interisting learining situation for me working at this project. So, if you are more confortable with python and language interpreter design, I would really appreciate your contribution. :)

---

© 2018 zekro Development  
[zekro.de](https://zekro.de) | contact[at]zekro.de  
Licence: MIT
