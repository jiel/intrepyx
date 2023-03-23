# INTREPYX

This is a python client for 🚀 [lunar-lander](https://github.com/Firnael/lunar-lander). This module is named after [the 6° Lunar Excursion Module](https://en.wikipedia.org/wiki/Apollo_Lunar_Module) of the Apollo program (_intrepid_).

![Apollo16LM](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Apollo16LM.jpg/390px-Apollo16LM.jpg)

## How to run

```
poetry install
poetry run start
```

# How to hack

Please read the [LunarLander README](https://github.com/Firnael/lunar-lander/blob/main/README.md) for the full rules.

You can set a few environment variables:
* SERVER_URL
* PLAYER_NAME
* PLAYER_EMOJI
* PLAYER_COLOR

Client logic is implemented in [brain.py](./intrepyx/brain.py).
