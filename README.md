# tree-counter

Codebase for tree identification from satellite imagery.  This code takes binary (tree vs not tree) data from images and trains/tests a CNN for automated tree detection.  The annotations are derived from a point-grid overlaid on an existing image.  i.e. if a given x-y location "point" overlaps a tree, a value of 1 is assigned vs 0 for no tree.  User may modify grid geometry.
8/11/20

# Usage
See included df_unique.pkl file for annotation data format example. 

1.  counter_cnn_lookup_table
	Creates a lookup table with pixel centers for the x by y grid.  Used in counter_cnn1 script. 
	
2.  countr_div_train_test_images.py
	Creates train and test splits at the IMAGE LEVEL to prep for thumbnail extraction in countr_cnn_1
	
3.  countr_cnn_1.py to extract grid cropped images and locate images in train/test folder
	Uses the pickled lookup_table.pkl file created by 'counter_cnn_lookup_table.py'
	Uses the annotation dataframe file selected by user in root directory.  Either df_train_val.pkl or df_test.pkl
	
4.  countr_cnn_2.py to train on cropped images from grid points
	Outputs the model to 'model.h5' in root directory
	
5.  countr_cnn_3.py to classify cropped images in test directory and output truth_table dataframe

6.  countr_cnn_image_counts.py to get image level counts
