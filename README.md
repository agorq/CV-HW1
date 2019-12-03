# CV-HW1
This is the repository for first homework of Fall 2018 semester course BLG453E Computer Vision. In this homework we were asked to make a histogram matching program using PyQt as UI.

## What is Histogram Matching?
Histogram Matching is the action of matching an image's histogram to another specified histogram. To do that we first generate the CDF's of the input and target images then construct a look up table then change the values of input image corresponding to the forementioned table

## Dependencies
The program is implemented on python 3.6.6 and should support all the versions which are compatible with python 3.5+. The libraries are required to run this program are these:
- numpy
- matplotlib
- qt5
- cv2

## How to use the program
From file use Open Input to choose the input image then use Open Target to open the target image and finally press Equalize Histogram Button on menubar to match the histograms.

![An image showcasing basic user interface](/doc/image/howtouse.png)

To run the program use the following command from code directory

```console
foo@bar:~$ python3 ui.py
```
