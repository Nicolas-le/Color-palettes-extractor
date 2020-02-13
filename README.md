# Color-palettes-extractor


This tool is a **work in progress** project that started 2017 and not been worked at since then. It was related to the digital humanities research *"Colour palettes and their social expression during realism and impressionism"*.


>The tool must be effective and fast. At the moment one painting is processed in less than a second. From our point of view this is already quite fast, but nonetheless if you want to analyse for example 10000 paintings the script >will need over 2 hours. This should also be considered in another improving circle. The second task to consider was that we extracted the colours through the rig-model and this led to the fact that there are up to 16,7 million >possible colours. Because we wanted to count the colours we had to reduce the variety down to 125 colours.


![Reduced Colors](https://commons.wikimedia.org/wiki/File:RGB_color_solid_cube.png)


A GUI was added a little bit later. At the moment the tool is capable of processing a directory of **.jpg** files and then output the main colors as a palette.
The project is added to GitHub for further work and optimization.

## Use

```git clone https://github.com/Nicolas-le/color-palettes-extractor.git```
```cd color-palettes-extractor```
```pip3 install -r requirements.txt```
```python3 paletteExtractor.py ```

--> go in the directory your files are in and hit run.


## to-do

* implement user input
	* number of wanted colors
	* redo analysis
* process other file formats, such as .png
* style the gui
* get output formants
	* json
	* see color codes of palette
	* maybe safe outout in DB
* optimize calculation time
* add loading bar
* comment code

