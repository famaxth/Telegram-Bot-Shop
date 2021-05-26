Bot Automatic Shop
==================
AutoShop in Telegram. There is a cool admin panel where you can configure everything.

Hi! I present to you the update of my AutoShop.
A lot of work was done, the bot was completely rewritten from scratch. The bot is written using pyTelegramBotApi(telebot).
The update added new features, improved existing ones, and optimized the operation of the bot itself.

# Features

## General

* Information - an informative, changeable message with a prepared syntax.
* Detailed information about the bot. (Number of users, products, positions, categories, profit)
* A separate file with the bot settings. You don't have to go into the bot code. (config.py)
* Automatic creation and configuration of the database (Database) when the bot is launched.
* Support(contacts) - A button with the output of the administrator's contacts.
* When the bot starts, the update is automatically checked.
* A small design part (buttons, text).
* Convenient and multifunctional admin panel.
* Change of language (English and Russian are available)
* Edit all buttons directly from the admin panel.
* Sending logs (in file format or by message)
* Payment systems are connected (Qiwi and BTC)

## Payment systems:

* If the user's QIWI wallet does not work when adding funds to the balance, the administrators will receive a notification.
* When adding/changing a QIWI wallet, the bot automatically checks its functionality.
* When displaying errors from QIWI, the bot decodes the error code into text.
* You can choose the deposit method (by form, by number)
* Change the QIWI wallet via the bot's admin panel
* Checking the health of the QIWI wallet
* View your QIWI wallet balance.
* View your Coinbase balance.
* Sending and receiving BTC.
* Generating random BTC wallets.
* Topping up your balance with BTC.

## Products:

* Commands for getting a list of all products, items, and categories
* Convenient pages for scrolling through categories and positions.
* Get a list of all products and categories.
* Delete all products, items, and categories at once.
* Mass and single loading of goods.


# Installation Instructions

1. Download [Telegram](https://pypi.org/project/pyTelegramBotAPI/)
2. Download [Python 3.9.1](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)
3. Download, unpack the archive with the bot and open the file `config.py`
4. Edit `token` and `admin_id`
5. Open the command line (cmd), go to the directory with the bot and write:
```
pip install pyTelegramBotApi
```
```
pip install requests
```
```
pip install SimpleQIWI
```
```
python app.py
```
Congratulations! The bot is running.

# Coming soon
Features that will be added in the future:
* Aiogram

# Requirements
* [pyTelegramBotApi 3.7.4](https://pypi.org/project/pyTelegramBotAPI/)
* [Python 3.9.1](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)
* [Telegram](https://desktop.telegram.org/)
* [SimpleQIWI](https://github.com/Emberium/SimpleQIWI)
* [Coinbase Wallet Client](https://wallet.coinbase.com/)

# F.A.Q
   ▉  
   ▉  
   ▉ ▉ ▉ ▉ ▉ ▉ __Writes that the module was not found__
   
                           Restart CMD after installing the module  
   ▉  
   ▉  
   ▉ ▉ ▉ ▉ ▉ ▉ __What permissions are needed for QIWI__
   
                           The first 3 permissions are enough  
   ▉  
   ▉  
   ▉ ▉ ▉ ▉ ▉ ▉ __Can I add files?__
   
                           Yes, you can add links to your files  
   ▉  
   ▉  
   ▉ ▉ ▉ ▉ ▉ ▉ __How do I go to the directory with the bot?__
   
                           Open the command line (cmd), write: cd path/to/folder/with/bot




