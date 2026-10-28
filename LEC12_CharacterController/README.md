# LEC12 Character Controller

## Run

Run python main.py from this directory. The Pico2D course environment must be available. Install the state-machine dependency with pip install -r requirements.txt.

## Controls

- Left/right arrow: run in the pressed direction; release all direction keys to return to IDLE.
- a while IDLE: start AUTO_RUN for five seconds.
- Direction key during AUTO_RUN: cancel it and enter ordinary RUN.
- SPACE while SLEEP: wake to IDLE.
- ESC: quit.

## States

boy.py uses transitions.Machine for IDLE, RUN, SLEEP, and AUTO_RUN. auto_run.py contains the dedicated AutoRun behavior class. AUTO_RUN moves faster, draws the sprite at 1.6x, bounces within the screen, and exposes Boy.is_invincible for future damage checks.
