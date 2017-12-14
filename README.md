# KnowEnG's Phenotype Prediction Pipeline
This is the Knowledge Engine for Genomics (KnowEnG), an NIH BD2K Center of Excellence, Phenotype Prediction Pipeline.

This pipeline **predicts" the relative importance of a set of genes associated with a given phenotype.

This pipeline supports two regression models: 

| **Options**                                      | **Method**                           | **Parameters** |
| ------------------------------------------------ | -------------------------------------| -------------- |
| Elastic Net                                      | Elastic                              | elastic_net    |
| Lasso                                            | Lasso                                | Lasso          |

* * *
## How to run this pipeline with our data
* * *

### 1. Clone the Phenotype_Prediction_Pipeline
```
 git clone https://github.com/KnowEnG/Phenotype_Prediction_Pipeline.git
```
 
### 2. Install the following (Ubuntu or Linux)
  ```
 apt-get install -y python3-pip
 apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
 pip3 install numpy==1.11.1
 pip3 install pandas==0.18.1
 pip3 install scipy==0.18.0
 pip3 install scikit-learn==0.17.1
 apt-get install -y libfreetype6-dev libxft-dev
 pip3 install matplotlib=1.4.2
 pip3 install pyyaml
 pip3 install knpackage
```

### 3. Change directory to Phenotype_Prediction_Pipeline

```
cd Phenotype_Prediction_Pipeline
```

### 4. Change directory to test

```
cd test
```

### 5. Create a local directory "run_dir" and place all the run files in it
```
make env_setup
```

### 6. Select and run a phenotype prediction option:
  
 * Run Elastic Net pipeline</br>
  ```
  make run_elastic_net
  ```
 
 * Run Lasso pipeline</br>
 ```
 make run_lasso
 ```
 
__***Follow steps 1-3 above then do the following:***__

### * Create your results directory
 
 ```
 mkdir results_directory
 ```
 
### * Create run_parameters file (YAML Format)
 
 Look for examples of run_parameters in:
  ```
  Phenotype_Prediction_Pipeline/data/run_files BENCHMARK_2_ElasticNet.yml
  
  Phenotype_Prediction_Pipeline/data/run_files BENCHMARK_1_Lasso.yml

  ```
 
### * Run
Using Elastic net
  ```
 python3 ../src/phenotype_prediction.py -run_directory ./run_dir -run_file BENCHMARK_2_ElasticNet.yml
  ```
Using Lasso
 ```
 python3 ../src/phenotype_prediction.py -run_directory ./run_dir -run_file BENCHMARK_1_Lasso.yml
 ```
 
 * * *
 ## Description of "run_parameters" file
 * * *
 
| **Key**                        | **Value**            | **Comments**                       |
| -------------------------      | --------------       | ------------                       |
| Method                         | elastic_net_predict          | scikit-learn.org   elastic-net     |
| Method                         | lasso_predict                | scikit-learn.org   lasso           |
| results_directory              | directory            | Directory to save the output files |
| spreadsheet_name_full_path     | spreadsheet_name     | Input Gene Expression  data        |
| response_name_full_path        | response_name        | Input Drug Response data           |
| test_spreadsheet_name_full_path| test_spreadsheet_name| Input testing feature data         |
| min_alpha                      | float number         | Minimum number in alpha list       |
| max_alpha                      | float number         | Maximum number in alpha list       |
| tolerance                      | float number         | The tolerance for the optimization |
| fit_intercept                  | boolean value        | whether to calculate the intercept for this model | 
| normalize                      | boolean value        | whether the regressors will be normalized |
| max_iter                       | integer number       | The maximum number of iterations   |
| n_alpha                        | integer number       | Number of alphas in alpha list     |
| min_l1                    | float number       | Minimum l1 in the grid of l1|
| max_l1                    | float number         | Maximum l1 in the grid of l1|
| n_l1                      | integer number       | Length of grid of l1           | 
| eps                       | float number     | Length of the path|

spreadsheet_name = features_train_clean.df</br>
response_name = response_train_clean.df</br>
test_spreadsheet_name = features_test_clean.df

 * * * 
 ## Description of Output files are saved in results directory
 * * * 
 
 | **Gene Name** | **Relarive Importance**|
 | ------------- | ---------------------- |
 | User Gene 1   | Float                  |
 | ...           | ...                    |
 | User Gene n   | Float                  |
 
