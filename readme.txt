Erin Fago


> File name : reg.py

> Function  : can read a data file (e.g., syn_train.txt) to train the nth degree polynomial function (n = 1, 2, 3, etc.), and make predictions on the validation set (e.g., syn_validation.txt)

> How to run: $python reg.py syn_train.txt syn_validation.txt 3

	      where ...
		- degree is what nth degree polynomial function you want the data to be trained to.
		
		- syn_training.txt is the training data organized in two columns where the left column is the x input data and the right column is the t output data.

		- syn_validation.txt is the validation data with the same file organization as the training data.

> Output    : Plots the training data (blue), validation data (green), and nth degree regression (red) with x data on the x axis and t data on the y axis.
	      Prints to terminal the MSE (average loss value) and the regression function that was calculated and plotted.

> Notes     : heavily based on code from powerusage-polynomial.py and powerusage.py

--------------------------------------------------------------------------------------

> File name : nscript.py

> Function  : Randomly splits the training data set into 5 parts and calls reg.py 5 times performing 5-fold cross-validation

> How to run: $python nscript.py

> Output    : Returns loss value for each n (polynomial order) from 1-10
	      Creates files named training.txt and valid.txt to use as the training and validation data sets when the script calls reg.py
--------------------------------------------------------------------------------------

> File name : results.txt

> Function : copied results from the terminal from running nscript.py. shows results from each of the 5 fold rounds and for each round shows what the MSE and function would be for n spanning from 1-10.

--------------------------------------------------------------------------------------

> File name : data points.xlsx

> Function : Organizes in a table the MSE for degrees 1-10 for each round of the 5-fold cross-validation and the average MSE per degree. 
	
