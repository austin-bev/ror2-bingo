# Ror2 (Risk of Rain 2) Bingo Board Generator

Intended to be used with [Bingosync](https://bingosync.com/)

## Why not just create a Bingosync PR?

Bingosync is great but functionally all it does it pick randomly from a pool of objectives.
This project will randonly generate objectives from the item/equipment/enemy pools provided, leading to over 500+ possible squares.
This also allows more customization of the bingo board generated, including flags for turning off DLC items, allowing items, and changing the weights of objectives.

## Running

Pretty simple. just run the code and the bingo board will be copied to your clipboard. The `pyperclip` library will need to be installed for this, but that is about it.
Once the bingo board is copied, go to https://bingosync.com/, Select `Custom (Advanced)` as your game (should be at the end), leave everything as default, and then paste in the board into the "board" section.
