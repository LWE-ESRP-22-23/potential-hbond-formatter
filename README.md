# potential-hbond-formatter

The purpose of this repository is to automatically format the output from the Potential HBond server found at https://swift.cmbi.umcn.nl. This server takes in a PDB file and ouputs a long list of potential hydrogen bonds in a protein.

--------------------

## Usage
When the script requests for the "get request URL", please use dev tools in your browser to see the get request URL. Ctrl + Shift + I should accomplish this on most browsers for Windows.

[![Dev Tools Screenshot](https://i.postimg.cc/jjH8Smz3/download.png)](https://postimg.cc/sB2PnnH5)

You will then right click the bottom red box and click "Copy link address" or something along those lines. You can then paste this link into the input.

[![download.png](https://i.postimg.cc/kXWTnDWF/download.png)](https://postimg.cc/Xp7fLjHp)

**Note: This is temporary while I figure out how to automate this process.**

-------------------
## Dependencies

This repository has the dependencies requests and openpyxl. The link to those are as follows:
    https://pypi.org/project/openpyxl/
    https://pypi.org/project/requests/


They can both be downloaded using pip in the command prompt:
> pip install openpyxl

> pip install requests

-------------------

### Future

In a future commit, there will be a way to include the angle of the hydrogen bond using Coot.