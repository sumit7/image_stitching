This is opencv based stitching pipeline
for the video "underwater_video_sample_1.mp4", the camera is not rotating around a fixed pov but rather is translating.
Hence opencv's stitcher is initialised with SCAN mode.

Use stitching_part.py, changing a,b,c values appropriately to stitch suitable frames.

Used stitching_comp.py to sticth the results of stitching_part.py

results are stored in the stit folder.

TODO: the control options for which frames to choose can be shifted to cmmandline, instead of modyfing in code.
