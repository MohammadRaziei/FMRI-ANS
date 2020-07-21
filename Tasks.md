# Tasks

After installation of libraries and workspace here are the pre-defined tasks: (We recommend you to use Google/Colab)

## O. Preprocessing

At first, we will do some basic works with fMRI data on PyMVPA/NiBabel libraries of python that are implemented for NeuroImaging.

### a. Load and visualize data

Load fMRI data of subject 1; plot these images on 25th frame of time:
Set no mask for this part (mask=None)

* Mid-sagittal cut
* Mid-frontal cut

### b. Data management

Decompose data into different label-frame pairs; you'll use this mapping for next parts.
Example: {"Stimuli1": 1, 2, 12, 13, 14;"Stimuli2": 3, 4, 5, 6, 9, 10; ...}

### c. Maximum active voxels

With an arbitrary method, find 10 most active voxels; explain your method clearly. For example, you may use histogram of activities.


### d. Pearson correlation

The function: "mvpa2.measures.corrcoef.pearson_correlation" computes pearson correlation of two matrices; implement a method that takes two set of frames and computes their correlation; then upgrade your method to a function that takes two "stimuli_name" and size "X", then computes their correlation for X frames of each stimuli.

### e. Selective voxels

Add this option to your correlation function; find only non-zero elements of data, name them "masekd"; then find maximally active voxels and name them "maxim"; so your function should be able to do its calculations with excluded or included maxim voxels. note that you should always exclude always zero voxels (these voxels are always zero due to masking)


## I. Overlapping and distributed representation

This is the first main task in this assignment; according to paper "Distributed and Overlapping Representations of Faces and Objects in Ventral Temporal Cortex, J.Haxby et. al"
they concluded that object representation in the Ventral Temporal Cortex is distributed and overlapping; so they removed maximall active voxels of a specific object and computed correlations, and classified the data in order to show change in representation details.

### a. Within category correlations

Using your implemented function, compute correlations for a set of frames of a signle stimuli, and visualize it; that should be a NxN image indicating correlations between each frame with a colormap.

### b. Between category correlations

Now, compute overall correlation between set of frames from different categories; that should be a NxN image indivating correlations between each two stimulis.

### c. Maximally excluded correlations

Repeat last part with excluded maximall voxels, change maximall activeness threshold and report results.

## II. Hyperalignment

In the second paper "A Common, High-Dimensional Model of the Representational Space in Human Ventral Temporal Cortex, J.Haxby et. al" used a new method "hyperalignment" to present a common model not in one subject, but between subject; so then they used PCs to show power of this method in data seperation and reported the classification accuracy data.

### a. Anatomical aligned data classification

Based on library documentation, classifiy between subject data when alignment is anatomical, and save reportes.
Your classifier is optional.

### b. Hyperaligned data classification

Do previous part, when alignment is hyperaligned; use first 4 subjects as training data and last 2 subjects as test validators.

### c. Pricipal component analysis

Using an arbitrary dimensionality reduction method, get PCs from these hyperaligned data and find out how many PCs are sufficient for 90% of full PCs quality.



# End
