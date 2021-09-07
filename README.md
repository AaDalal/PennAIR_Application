# Problem Parameters
* 4 parts to the QR code
* All of approximately equal size
* May be some ovealap between the pieces
* Pieces may need to be re-oriented to fit
* QR code is of version 1 and error correction level H

## Assumptions
* The qr codes are of roughly equal sizes

# QR Code Version 1 Design
* Version 1 means a 21 x 21 px qr code
![Version 1](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Qr-1.svg/220px-Qr-1.svg.png)
* V1 QR code in H mode can store up to 41
* Sizing information

![QR Code Size : Data](https://www.qrcode.com/en/img/version/decisionMap.png)

## ECC (Level H)
* Level H is 30% ECC
  * Means if 30% of 8bit code words are lost, the value of the QR code can still be recovered
  * *Potentially, this means only 3 quarters are needed*
* Uses reed-solomon

## Encoding information
* Core unit appears to be 4x2 rectangle (total of 8 bits, 1 byte)
 * This is called a module (per [this detailed doc on QR specs](./qr_standard.pdf))
 * According to this, the module are read right to left, bottom to top (when we look at the QR code s.t. the eyes are at top left, bottom left, top right)
* There is a mode indicator at the bottom right
  * 0001 indicates numerical
* Then above that is the char count indicator ()
* Then data starts by snaking around each column


### Orientation Information
* 3 eyes in top left, bottom left, top right
* Potentially a small orientation one in the bottom right

### Data Masking
* Data is masked to ensure best efficiency

# Most Naive Solution: Photoshop
![Photoshop Pieced Together](./Images/Pieced_Together_QR.png)
* When scanned, produces a value of 0106
  * We can also see by examining the very bottom left 2x2 square that the encoding mode must be numerical

# Part 1: Computer Vision

## Defining Characteristics of a QR code
### Shape
QR code pieces are square, which means that they will always have 4 corners (no matter angle of photography etc)

### Color
* Our QR codes are white with black data
  * This contrast with their background which is black (but also can have lots of glare, making it appear close to yellow)
* The given QR code has a greater lustrousness than its surroundings

### Pattern
* The QR alternates between white and black, producing high contrast regions
* The QR has eyes which encode orientation

## Defining the solution
### Understanding
* **Core problem** is to determine where the relevant pixels lie
* see above

### Defining In/Out
* In: an image (rgb?)
* Out: any of
  * a list of pixels
  * bounding box (l, r) (t, b)
  * lines

### Test Cases
* The given images (visually analyzing them)
* Any additional test cases will be added under test

### Implementation (see code)
* The method of using the color difference seems most promising
* Potentially will need to regularize this to a 4-gon (e.g., a trapezoid, or a parallelogram )

___

# Challenge Summary

# Code Summary

## How to Run

# Other Info