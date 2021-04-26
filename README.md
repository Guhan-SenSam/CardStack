# Example Extension

This extension adds a beautiful Card Stack Widget. The Widget enables you to create a stack of three cards that can be animated to move to the next card infinetly. The widget is designed in a way that three `MDCards` get reused infinetly to give the impression of an infinte stack of cards. You can add your own widgets to the front most card.

See [KivyMD_Extensions](https://github.com/kivymd-extensions/KivyMD_Extensions).

## Installation

```bash
pip install kivymd_extensions.CardStack
```

### Dependencies:

- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.1
- [Kivy](https://github.com/kivy/kivy) >= 1.10.1 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)

## Documentation

* `Radius`: Accepts a list and sets the radius of all cards in the stack
* `first_color`: Accepts a list and sets the color for the front most card(Defaults to `primary_light_color` of theme class)
* `second_color`: Accepts a list and sets the color for the middle card(Defaults to `primary_color` of theme class)
* `third_color`: Accepts a list and sets the color for the last card(Defaults to `primary_dark` of theme class)
* `current_card`: Returns the front most card object. This can be used to add widgets to the front most card. The value is returned before the animation starts to allow the user to load new widgets before they are seen and thus make the transition fluent.
* `transition`: Accepts a string and sets the transition interpolation type to use for animations.

## Examples

```bash
git clone https://github.com/kivymd-extensions/CardStack.git
cd CardStack
cd examples/full_example
python main.py
```
### Pictures


### Support

If you need assistance or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/wu3qBST
- _Email:_ kivydevelopment@gmail.com
