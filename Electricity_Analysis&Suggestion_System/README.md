<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/EASE_Logo_Final.png" alt="..."></p>
**EASE-Project_v1.0**

</p><a href="https://travis-ci.org/danielfather7/EASE-Project"><img src="https://travis-ci.org/danielfather7/EASE-Project.svg?branch=master" border="0"></a></p>

------------------------
Background and Objective
------------------------

Electricity is a globally consumed energy source, such that electricity generation based on conventional energy sources (Petroleum, Coal, and Natrual Gas) are accompanied with large amount of greanhouse gas emission, particularly the carbon dioxide gas. Figure below mapped out the electricity generation plants with different type of energy sources within the United States in year 2015.

<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/Background_2015_EDM.png" alt="...">

Electricity Analysis Suggestion Ensemble, or short for EASE, is a Proejct guided by the eScience Insititue and Chemical Engineering Department at the University of Washington. 

EASE is a suggestion model with an aim to help industrial users who desire to build an electricity generation plant that offsets long term cost from continuously buying electricity from the Government. User inputs weather information and plant capacity (average summer temperature, average winter temperature, annual precipitation, and average wind speed), EASE will automatically allocate energy information that can be utilized and provide suggestions on electricity generation sources.

Based on RandomForest classification model from scikit-learn, EASE considers weather, cost, carbon dioxide emission/taxation, and energy source distribution information. The output of the model is an optimized suggestion with most economical, best weather suitable, clean, and most efficient.

<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/Updated_workflow_fig.png" alt="...">

Please give credits for the contributors if you use this code.

**EASE_RF_v1.0**

Jiarong I. Cui**(1)**, Tai-Yu D. Pan**(1)**, Jiayuan Guo**(1)**, Yongquan Xie**(2)**

**(1)** University of Washington, Department of Chemical Engineering, Seattle, WA </p>
**(2)** University of Washington, Department of Material Science and Engineering, Seattle, WA


---------
License
---------
This work is under GNU GPLv3 licence, such that it requires anyone who distributes this code or a derivative work to make the source available under the same terms, and also provides an express grant of patent rights from contributors to users.

-------------------
Database Sources
-------------------
**All the database are either self-constructed, or obtained from open sources.**

* USA Electricity Souce Database [https://www.eia.gov/electricity/data/state/](https://www.eia.gov/electricity/data/state/)
* USA Weather-info Database [https://www.ncdc.noaa.gov/qclcd/QCLCD?prior=N](https://www.ncdc.noaa.gov/qclcd/QCLCD?prior=N)
* Carbon Dioxide Emssion/Taxation Database [http://www.eia.gov/environment/data.cfm](http://www.eia.gov/environment/data.cfm)
* Cost Dataset(Self-composed)
    * Revenue [https://www.eia.gov/electricity/data/state/](https://www.eia.gov/electricity/data/state/)
    * Cost of Conventional Source [http://www.eia.gov/electricity/data/browser/#/topic/15?agg=1,0,2&fuel=8&geo=vvvvvvvvvvvvo&sec=80o&linechart=ELEC.COST_BTU.COW-US-98.M&columnchart=ELEC.COST_BTU.COW-US-98.M&map=ELEC.COST_BTU.COW-US-98.M&freq=M&start=200801&end=201611&ctype=linechart&ltype=pin&rtype=s&maptype=0&rse=0&pin=](http://www.eia.gov/electricity/data/browser/#/topic/15?agg=1,0,2&fuel=8&geo=vvvvvvvvvvvvo&sec=80o&linechart=ELEC.COST_BTU.COW-US-98.M&columnchart=ELEC.COST_BTU.COW-US-98.M&map=ELEC.COST_BTU.COW-US-98.M&freq=M&start=200801&end=201611&ctype=linechart&ltype=pin&rtype=s&maptype=0&rse=0&pin=)
    * Cost of Solar Resource [https://openpv.nrel.gov/search](https://openpv.nrel.gov/search)
    * Cost of Wind Resource [https://emp.lbl.gov/projects/wind](https://emp.lbl.gov/projects/wind)
  
EASE cost prediction is largely based on 2015 average plant construction cost data, this includes but not limited to installation cost, maintenance cost,  operation cost, and electricity sale price. Carbon dioxide taxation is based on a 2013 proposed legislation (S. 332 of the 113th) 

-----------------------
Software Dependencies
-----------------------
**Package is written in Python 3.x version**</p>
**All the required software is open source.**

Numpy:  [http://www.numpy.org/](http://www.numpy.org/)</p>
Pandas:  [http://pandas.pydata.org/](http://pandas.pydata.org/)</p>
Scikit-Learn:  [http://scikit-learn.org/stable/](http://scikit-learn.org/stable/)</p>
Matplotlib:  [http://matplotlib.org](http://matplotlib.org)</p>
Tkinter:  a built-in package in Python [https://wiki.python.org/moin/TkInter](https://wiki.python.org/moin/TkInter)</p>

**Operating system information**

Both Mac OS X and Windows operating system should be able to execute the package in default Python environment.
MAC OS X provides the best user experience*

----------------------
Unittest Results
----------------------
<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/unittest_result.png" alt="...">

----------------------
Package Usage
----------------------
**For Mac:**</p>
Step 1: Open the terminal, type </p>
    `$ python --version`</p>
If your Python version is `Python 3.5.0` or later, skip step 2 & 3.</p>
Step 2: Install Homebrew, type</p>
    `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`</p>
For more information, visit [Homebrew](https://brew.sh).</p>
Step 3: Use Homebrew to install Python, type</p>
    `$ brew install python3`</p>
Once Python 3 is installed, we’re going to check that is it ready to use or our system by launching the interactive console. Type</p>
    `$ python3`</p>
and you should see `Python 3.6.0`. Type</p>
    `>>> exit()`</p>
Step 4: Install dependencies, type</p>
    `$ brew tap homebrew/science`</p>
    `$ brew install matplotlib pandaseq`</p>
    `$ pip3 install numpy scipy scikit-learn`</p>
Step 5: Get our package, type</p>
    `$ git clone https://github.com/danielfather7/EASE-Project.git`</p>
Step 6: Change directory, type</p>
    `$ cd EASE-Project/GUI/`</p>
Step 7: Open our package, type</p>
    `$ python3 EASE_GUI.py`</p>
Enjoy!

-------------
GUI Example
------------
Step 1: GUI license page:
<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/GUI_license_page.png" alt="...">

Step 2: GUI prompts user input values:
<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/GUI_user_input.png" alt="...">

Step3: GUI output suggestion model:
<img align="center" src="https://github.com/danielfather7/EASE-Project/blob/master/Project_Goal/figs/GUI_output.png" alt="...">

---------
Folders
---------
**Project_Goal** - The folder contains the project scope, example of use case of the package, user interactive diagram, as well as all other brainstorming thoughts and dataset descriptions relative to the project from the very beginning.

**Original_Data** - The folder contains the orginal datasets downloaded from all the open sources stated above, these raw dataset contains information that are not useful for the package development.

**Arrange_Data** - The folder contains the iPython scripts that import and clean different original raw dataset from the **Original_Data** folder. 

**EASE** - The code for the model, EASE_v1.0, and all other scripts for the model development.

**GUI** -  The folder contains GUI development code.

**Test** - The folder contains unittest codes.

**README.md** - descrption of background, License, Database Sources, Unittest, Software Installation, Folder Descriptions and Acknowledgement

**LICENSE.md** - Outlines of the GPL-3.0 license for this package.

-------------------
Acknowledgements
-------------------
David A. Beck and Jim Pfaendtner, eScience Institue, Chemical Engineering Department, as well as Directors for the DIRECT program at University of Washington, served as mentors for the development of this package.
