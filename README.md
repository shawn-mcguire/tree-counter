# TreeCounter

Codebase for tree identification from satellite imagery
8/11/20

# Code Flow
See included df_unique.pkl file for annotation data format example. 

Step 1: Create lookup table using counter_cnn_lookup_table
	This code creates a lookup table with pixel centers for the x by y grid.  Lookup_table is used in counter_cnn1 	script. The lookup_table is used to find the center of the cropped image thumbnail based on the grid data in the file
Step 2: Run countr_div_train_test_images.py
	Creates train and test splits at the IMAGE LEVEL to prep for thumbnail extraction in countr_cnn_1
Step 3: Run countr_cnn_1.py to extract grid cropped images and locate images in train/test folder
	Uses the pickled lookup_table.pkl file created by 'counter_cnn_lookup_table.py'
	Uses the annotation dataframe file selected by user in root directory.  Either df_train_val.pkl or df_test.pkl
Step 4: Run countr_cnn_2.py to train on cropped images from grid points
	Outputs the model to 'model.h5' in root directory
Step 5: Run countr_cnn_3.py to classify cropped images in test directory and output truth_table dataframe
Step 6: Run countr_cnn_image_counts.py to get image level counts
