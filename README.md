# Example Extension

This extension adds a beautiful Card Stack Widget. The Widget enables you to create a stack of three cards that can be animated to move to the next card infinetly. The widget is designed in a way that three `MDCards` get reused infinetly to give the impression of an infinte stack of cards. You can add your own widgets to the front most card.

### Dependencies:

- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.1
- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)

## Documentation

* `Radius`: Accepts a list and sets the radius of all cards in the stack
* `first_color`: Accepts a list and sets the color for the front most card(Defaults to `primary_light_color` of theme class)
* `second_color`: Accepts a list and sets the color for the middle card(Defaults to `primary_color` of theme class)
* `third_color`: Accepts a list and sets the color for the last card(Defaults to `primary_dark` of theme class)
* `current_card`: Returns the front most card object. This can be used to add widgets to the front most card. The value is returned before the animation starts to allow the user to load new widgets before they are seen and thus make the transition fluent.
* `transition`: Accepts a string and sets the transition interpolation type to use for animations.
* `card_out_direction` : The Direction the fron tmost cards exists the screen. The availbale options are `down`, `up`, `left` and `right`. This property defaults to `down`
* `card_in_direction` : The direction in which the new card comes in on the screen. The available options are `side`, `bottom` and `top`. This property defaults to `side`
* `elevation` : The elevation of the front most card. This property defaults to `0`

## Examples

Check the `example.py` on how to use this Kivy Widget

### Pictures
This is the widget using default app theme colors.
![1](https://user-images.githubusercontent.com/22190891/116127145-1da4e700-a6e5-11eb-8059-7fe302c6f46f.png)
![ezgif-2-eb1232048f40](https://user-images.githubusercontent.com/22190891/116127157-209fd780-a6e5-11eb-996a-01e769db57e3.gif)
