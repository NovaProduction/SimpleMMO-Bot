# Simple MMO Bot

## Update: Got banned because I was stepping for too long. If you're gonna use this, only used for up to 12 hours per day. Make spaces in-between them like 3 4-hour sessions.

## To the Devs: FU

### Features:
- Auto Step
- Auto Mine, Fish, Salvaging and Cutting
- Auto Battle
- Auto PVE (To be added, not anymore)
- Auto Wave

### Features to be Considered (before I got banned):
- Auto-job (Not priority but can be done and was already done. Removed due to lack of usability.)
- Auto PVP (Not priority)
- Auto-Bank (I mostly do safe-mode so maybe)
- Auto-Heal (I do safe mode so not really priority right now)

### Requirements:
- Chrome
- Python

### Library used:
- [Selenium](https://github.com/SeleniumHQ/selenium)
- [Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

### Things to consider:
- This does not handle the internal captcha system inside the gane although the bot detects if a captcha is shown and will promptly shut down until a command "reset" has been given. You need to solve that captcha by yourself. Implementing an image recognition software on these types of application is a bad idea. I'm not gonna spend that much time on this.

### Instructions:
This bot requires [Selenium](https://github.com/SeleniumHQ/selenium) to run.
```sh
python -m pip install selenium
```

This bot also requires [Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager) to run to run.
```sh
python -m pip install webdriver-manager
```

This will require that you login every time since I got banned and I can't update.

# Disclaimer:
I was and never shall be responsible for any ban or punishment brought by using this tool. This is for educational purposes only. No harm was intended in the making of this tool.
