# Color-palettes-extractor


This tool is a **work in progress** project that started 2017 and has not been worked on since then. It was originally related to the digital humanities research *"Colour palettes and their social expression during realism and impressionism"*.

>**The project**
>Taking the point, that art structurally reproduces the society the artist was living in, as an initial point we >will focus our research on paintings as an art form. We want to study how exactly the coherence of an art work >and the society in which it was created appears. [...] But we think that there is a major characteristic of >paintings describing the emotion and the meaning behind a single image and even the whole art style that is >analysable through computer science: **the used colours or consciously not used colours.**

>**The analysing tool**
>[...] The tool must be effective and fast. At the moment one painting is processed in less than a second. From our point of view this is already quite fast, but nonetheless if you want to analyse for example 10000 paintings the script >will need over 2 hours. This should also be considered in another improving circle. The second task to consider was that we extracted the colours through the rig-model and this led to the fact that there are up to 16,7 million >possible colours. Because we wanted to count the colours we had to reduce the variety down to 125 colours.

![Reduced Colors](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/RGB_Cube_Show_lowgamma_cutout_b.png/1280px-RGB_Cube_Show_lowgamma_cutout_b.png = x300 )

**Process of reducing the colors to 125.**

A GUI was added a little bit later. At the moment the tool is capable of processing a directory of **.jpg** files and then show the main colors as a palette.
The project is now added to GitHub for further work and optimization.

## Use

```git clone https://github.com/Nicolas-le/color-palettes-extractor.git```

```cd color-palettes-extractor```

```pip3 install -r requirements.txt```

```python3 paletteExtractor.py ```

--> go in the directory your files are in and hit run.


## to-do

* implement user input
	* number of wanted colors
	* possibility of redoing the analysis
* process other file formats, such as .png
* style the gui
* implement output formats
	* json
	* see color codes of palette
	* maybe safe output in DB
* optimize calculation time
* add loading bar
* comment code

