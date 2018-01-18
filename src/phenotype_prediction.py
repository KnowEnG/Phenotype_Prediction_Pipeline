# this is the main function of PPP

def lasso_predict(run_parameters):
    from phenotype_prediction_toolbox import run_lasso_predict
    run_lasso_predict(run_parameters)
    

def elastic_net_predict(run_parameters):
    from phenotype_prediction_toolbox import run_elastic_predict
    run_elastic_predict(run_parameters)

def svr_predict(run_parameters):
    from phenotype_prediction_toolbox import run_svr_predict
    run_svr_predict(run_parameters)

SELECT = {
            'lasso_predict': lasso_predict,
            'elastic_net_predict': elastic_net_predict,
            'svr_predict': svr_predict
        }

def main():
    import sys
    from knpackage.toolbox import get_run_directory_and_file
    from knpackage.toolbox import get_run_parameters

    run_directory, run_file = get_run_directory_and_file(sys.argv)
    run_parameters = get_run_parameters(run_directory, run_file)
    SELECT[run_parameters['method']](run_parameters)


if __name__ == "__main__":
    main()
