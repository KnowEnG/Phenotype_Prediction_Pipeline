# Verification directory files are benchmark result files
The Makefile in the test directory contains the targets, needed to build the **Prediction Phenotype Pipeline** benchmarks.
For estimating base memory requirements use the above heuristic _phenotype_prediction_p_memory_estimator.xlsx_


* Follow the instructions on the **Phenotype Prediction Pipeline** landing page to set up the environment:
```
    cd Phenotype_Prediction_Pipeline/test
    make env_setup
```
### 1. Run the lasso data test
```
    make run_lasso
```

* Compare the results with files in directory: **data/verification/BENCHMARK_1_PPP_Lasso/**

* The local result files will be in **run_dir/results/** 

### 2. Run the elastic net test **test/Makefile**

```
    make run_elastic_net
```
* Results will match **data/verification/BENCHMARK_2_ElasticNet/** (when unzipped)

### The file **phenotype_prediction_runtime_memory.xlsx** is a development tool for estimating memory in different environments
