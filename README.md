# Fun NumWorks Scripts
A collection of fun little Python scripts for the NumWorks calculator.  


## Installation

### NumWorks Calculator

1. Go to https://my.numworks.com/python/shrub719
1. Connect to your calculator by USB 
2. Click Load to Calculator on any scripts you want (make sure your browser has WebUSB capability)

### PC
Clone this repository, then run:
```
pip install -r requirements.txt 
```
Thanks to [@ZetaMap](https://github.com/ZetaMap) for porting the NumWorks modules to PC!


## Scripts

- [Renderer](#renderer)
- [Canvas](#canvas)
- [Drummer](#drummer)
- [Keys](#keys)
- [Picker](#picker)

### [Renderer](src/renderer/renderer.py)
A 3D object renderer which can rotate and scale an object.  
Also needs a component to be downloaded. Choose the component by changing the import.
```python
from <component> import OBJECT
```

**List of components:**
- Cube: [r_cube](src/renderer/r_cube.py)
- Cuboid: [r_cuboid](src/renderer/r_cuboid.py)

`D-Pad`: pitch & yaw  
`SHIFT / ALPHA`: roll  
`- / +`: scale

### [Canvas](src/canvas.py)
A canvas that you can draw on.

`D-Pad`: move cursor  
`OK`: draw  
`TOOLBOX`: hold to speed up  
`BACKSPACE`: hold to slow down  
`1`: switch colour to black  
`2`: switch to white/eraser  
`4 5 6`: red/green/blue

### [Drummer](src/drummer.py)
Like a drummer/launchpad.

Use the number keys to play the drums. Press `.` to change colours.

### [Keys](src/keys.py)
Like one of those MIDI piano YouTube videos.

Use the top row of numbers `7 8 9 ( )` to play the piano keys. Press `EXE` to change colours.

### [Picker](src/picker.py)
A simple colour picker.

`4 5 6`: increase R/G/B value  
`1 2 3`: decrease R/G/B value  
`BACK`: output RGB value and exit
