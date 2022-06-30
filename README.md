
## APP FOR AUTOMATED SHEAR WALLS CALCULATIONS

![Capture][main-view]


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
  The application use only the txt file, which can be exported from Radimpex Software Tower in Shear Walls calculate mode. From this file the app reads the provided information, which is the square cеntimeters of any type of reinforcement (for example: Aa1=30 cm2, Aa2=30 cm2, Aav=5.62 cm2/m', Aah=3.51 cm2/m') in a shear wall and calculates the needed reinforcement bar diameters.
  The app iterate through every wall in xls file (respectively in txt file), reads the size information in xls file and the reinforcement information from txt file and makes calculations about the needed reinforcement.
<p align="right"><a href="#top">back to top</a></p>

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
<p align="right"><a href="#top">back to top</a></p>

### Usage
![Initial Excel](https://user-images.githubusercontent.com/18015470/176461688-ad1d9b7d-e41d-45fa-82cc-9d8ee6d81b23.PNG)

![Usage](https://user-images.githubusercontent.com/18015470/176461647-1d06b50f-b50c-4577-a423-927ee5e7c8e6.PNG)

![After_get_tower_results](https://user-images.githubusercontent.com/18015470/176461744-77fd5684-7b77-4d53-8ba1-55bf2185e9e7.PNG)

![automatically regerated pdf](https://user-images.githubusercontent.com/18015470/176461872-3faf34de-be06-48b8-88c7-c1d80bb81be5.PNG)

![After_calculations](https://user-images.githubusercontent.com/18015470/176461897-11c0afd9-d60b-45cd-a9ce-d6e4f00ee4e3.PNG)

<p align="right">(<a href="#top">back to top</a>)</p>

### Roadmap

- [ ] ENTRY FIELDS
  - [ ] TXT FILE PATH - not obligatory field
  - [ ] XLS FILE PATH - the path to xls file, in which the app will save the calculations
  - [ ] SHEET NAME - sheet name in xls file (case-sensitive)
  - [ ] SHEAR WALLS COUNT - total number of all walls, represented in specific cells in xls
  - [ ] STOREY LEVELS COUNT - total number of all levels, represented in specific cells in xls
- [ ] FUNCTIONALITY BUTTONS
  - [ ] GET INPUT - an obligatory action before anything else in functionallity, saves user input in db file
  - [ ] GET TOWER RESULTS - open and read txt file, finds the needed information, save it to xls file and generate additional PDF file with extreme value for each wall per level
  - [ ] CALCULATE - open and read xls file, calculate the required reinforcement for each wall at each level and save the calculations back to xls file
  - [ ] CLEAR CELLS - clear all cell from automatically pasted information from app


<p align="right"><a href="#top">back to top</a></p>

### License

<p align="right"><a href="#top">back to top</a></p>

### Contact

Tanya Angelova - [LinkedIn](https://www.linkedin.com/in/tanya-angelova-44b03590/) - t.j.angelova@gmail.com

Project Link: [github link]

<p align="right"><a href="#top">back to top</a></p>

[main-view]: https://user-images.githubusercontent.com/18015470/174805811-5eb5a033-0e9d-4da7-9ad0-f2c18620f20d.PNG
[LinkedIn]: https://www.linkedin.com/in/tanya-angelova-44b03590/
[github link]: https://github.com/TanyaAng/Automated_Shear_Walls_Calculations
