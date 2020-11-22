https://sk.acord.software/4df182adca1e4f6387fedecb31e9d9c2
https://github.com/irisdroidology/python-learning/issues/3
https://acord.software/stellarios/hydejack/arcadia/games/python/librariesmodules/2020-11-20-announcing-chocobars/

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b3bef2e-7e42-44fd-9ffa-0180cee1ccd8/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b3bef2e-7e42-44fd-9ffa-0180cee1ccd8/Untitled.png)

- First PyQt application:

# Considering Code styles

## PyQt concepts & elements

> These elements will be the building blocks of your PyQt GUI applications. Most of them are represented as Python classes. PyQt5.QtWidgets is the module that provides all these classes

- Widgets

    `Qwidget` is the **base class** for all user interface objects (aka widgets):

    - Rectangular-shaped graphical components that you can place on your application's window  to build the gui
    - Widgets contain a series of attributes and methods that allow you to model their appearance and behaviour
    - They also paint a representation of themselves on the screen

    Widgets also receive mouse clicks, keypresses and other events from the user, the window system and other sources. Each time a widget catches an event, it emits a signal to announce its state change

    Some common and useful PyQt5 widgets include:

    - Buttons

        > You can create a button by instantiating QPushButton, a class that provides a classical command button. Typical buttons are OK, Cancel, Apply, Yes, No, and Close.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3fd81cb-4543-40cb-b53d-8e6993a76476/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3fd81cb-4543-40cb-b53d-8e6993a76476/Untitled.png)

        When you click them, you can command the computer to perform actions. You can even perform actions in response to a user clicking a button.

    - Labels

        > create with QLabel. Labels give you a way to display useful information in the form of text or images:

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7475d979-4267-490f-8f3f-f7b2ded3a56a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7475d979-4267-490f-8f3f-f7b2ded3a56a/Untitled.png)

    - Line edits
    - Combo boxes
    - Radio buttons
