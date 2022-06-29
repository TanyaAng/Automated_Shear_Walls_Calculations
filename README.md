## GUI APPLICATION FOR AUTOMATED SHEAR WALLS CALCULATIONS

<div id="top"></div>

![Capture](https://user-images.githubusercontent.com/18015470/174805811-5eb5a033-0e9d-4da7-9ad0-f2c18620f20d.PNG)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


### About The Project
The application use only the txt file, which can be exported from Radimpex Software Tower in Shear Walls calculate mode. From this file the app reads the provided information, which is the square cеntimeters of any type of reinforcement (for example: Aa1=30 cm2, Aa2=30 cm2, Aav=5.62 cm2/m', Aah=3.51 cm2/m') in a shear wall and calculate the needed reinforcement bar diameters and number as explained below:
 - boundary zone lenght or concrete confinements (required reinforcement Aa1 and Aa2): The application open an xls file with previously ordered information about building walls and their input information for calculations (widht, lenght and selected boundary zone lenght). The app iterate through every wall in xls file (respectively in txt file), reads the size information in xls file and the reinforcement information from txt file and makes calculations about how many rebars can be placed in the boundary zone and which bar diameter provides the needed reinforcement. The final result is for example 12N14 and the app saves that information in the xls file. 
 - vertical reiforcement(Aav) and horizontal reinforcement (Aah): The same as previous calculations, except that the needed reinforcement is for linear meter. There are many ways to provide the required reinforcement (for example: for 3.40 cm2/m' as structural engineers we can decide to construct it with N8/15 or N10/20), but the app finds the more economical solution instead of us and saves the information in the xls file. 

<p align="right">(<a href="#top">back to top</a>)</p>

#### Build With
* [Python](https://www.python.org/)
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [Figma](https://www.figma.com)

### Getting Started
#### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/TanyaAng/Automated_Shear_Walls_Calculations.git
   ```
3. Install all Python libraries
   ```sh
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

### Usage

<p align="right">(<a href="#top">back to top</a>)</p>


### Roadmap
- [ ] Main Screen

<p align="right">(<a href="#top">back to top</a>)</p>

### License

<p align="right">(<a href="#top">back to top</a>)</p>

### Contact

<p align="right">(<a href="#top">back to top</a>)</p>
