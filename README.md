# potential-hbond-formatter

The purpose of this repository is to automatically format the output from the Potential HBond server found at https://swift.cmbi.umcn.nl. This server takes in a PDB file and ouputs a long list of potential hydrogen bonds in a protein.

--------------------

## Usage
The first step is to install the dependencies. Please jump to the "Dependencies" section to complete this step.

Next, open up the command prompt and run the Python file:
> python3 formatter.py

Lastly, you will be prompted to:

1. Enter the minimum HBond distance.
2. Select the Excel save file location.
3. Select the PDB file.

That's it! You can find the .xlsx file at the location you specified.

-------------------
## Dependencies

This repository has the dependencies requests and openpyxl. The link to those are as follows:
> https://pypi.org/project/openpyxl/

> https://pypi.org/project/requests/


They can both be downloaded using pip in the command prompt:
> pip install openpyxl

> pip install requests

-------------------

### Future

In a future commit, there will be a way to include the angle of the hydrogen bond using Coot.