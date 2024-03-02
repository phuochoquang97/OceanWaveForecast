# starting-kit for OceanWaveForecast challenge

Using Météo-France's global ocean wave forecast dataset, the challenge here is to predict VPED(Prediction of wave direction based on spectral peak from the instrument SWIM-nadir of CFOSAT Mission)

The challenge is designed by:
Pavlo Poliuha, Junjie Chen, Pablo Mollá, Quang Phuoc Ho, Kumari Nageeta, Louis Betzer

## To get started follow the steps given below

### Install

To run a submission and the notebook file `wave_forecast_starting_kit.ipynb` you will need the some dependencies listed in `requirements.txt` file. You can install the dependencies with the following command:
open bash/command prompt

```bash
pip install -U -r requirements.txt

If you are using `conda`, we have provided another file named `environment.yml` to install all dependencies.

### Starting Notebook file

To Get started with the challenge we have provided you a file name `wave_forecast_starting_kit.ipynb`, where you will find the goal of this challenge with description about the dataset including the features, some statistics about data and simple baseline method.

### To Test a submission

To Test a submission make sure that it is located in the `submissions` folder.
For instance: for `my_submission`, it should be located in `submissions/my_submission`.

### To Run a submission

To run a specific submission, you can use the `ramp-test` command:
open bash/command prompt

```bash
ramp-test --submission my_submission


You can get more information regarding this command ramp-test by using the the command below

```bash
ramp-test --help

### For Further Information

If you want more information regarding the `ramp-workflow` you can go to following space.
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
