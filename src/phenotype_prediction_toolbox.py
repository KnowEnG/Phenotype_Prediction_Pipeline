
import os
import pandas as pd
import numpy as np
import pickle
from   sklearn import linear_model

import knpackage.toolbox as kn

def run_lasso_predict(run_parameters):

    gene_file = run_parameters['spreadsheet_name_full_path'     ]
    sign_file = run_parameters['response_name_full_path'        ]
    test_file = run_parameters['test_spreadsheet_name_full_path']

    gene_df   = kn.get_spreadsheet_df(gene_file)
    sign_df   = kn.get_spreadsheet_df(sign_file)
    test_df   = kn.get_spreadsheet_df(test_file)

    row_names = test_df.columns

    gene_mat  = gene_df.values
    sign_mat  = sign_df.values[0]
    test_mat  = test_df.values

    min_alpha     = run_parameters['min_alpha']
    max_alpha     = run_parameters['max_alpha']
    n_alpha       = run_parameters['n_alpha']
    intercept     = run_parameters['fit_intercept']
    normalization = run_parameters['normalize']
    max_iter      = run_parameters['max_iter']
    tolerance     = run_parameters['tolerance']

    alpha_grid    = np.linspace(min_alpha, max_alpha, num=n_alpha)
    reg_model     = linear_model.LassoCV(
        alphas=alpha_grid, fit_intercept=intercept, \
        normalize=normalization, max_iter=max_iter, tol=tolerance, cv=5)

    reg_model.fit( gene_mat.T, sign_mat)
    filename      = os.path.join(run_parameters['results_directory'], 'lasso_model.pkl') 
    pickle.dump(reg_model, open(filename, 'wb'))
    response_predict   = reg_model.predict(test_mat.T)
    predict_df         = pd.DataFrame(response_predict.T, index=row_names, columns=['predict'])
    write_predict_data(predict_df, run_parameters)
    

def run_elastic_predict(run_parameters):

    gene_file = run_parameters['spreadsheet_name_full_path'     ]
    sign_file = run_parameters['response_name_full_path'        ]
    test_file = run_parameters['test_spreadsheet_name_full_path']

    gene_df   = kn.get_spreadsheet_df(gene_file)
    sign_df   = kn.get_spreadsheet_df(sign_file)
    test_df   = kn.get_spreadsheet_df(test_file)

    row_names = test_df.columns

    gene_mat  = gene_df.values
    sign_mat  = sign_df.values[0]
    test_mat  = test_df.values

    eps       = run_parameters['eps']    
    min_alpha = run_parameters['min_alpha']
    max_alpha = run_parameters['max_alpha']
    n_alpha   = run_parameters['n_alpha']
    min_l1    = run_parameters['min_l1']
    max_l1    = run_parameters['max_l1']
    n_l1      = run_parameters['n_l1']
    intercept = run_parameters['fit_intercept']
    normalize = run_parameters['normalize']
    max_iter      = run_parameters['max_iter']
    tolerance     = run_parameters['tolerance']

    alpha_grid= np.linspace(min_alpha, max_alpha, num=n_alpha)
    l1_grid   = np.linspace(min_l1, max_l1, num=n_l1)


    reg_model = linear_model.ElasticNetCV(
        l1_ratio=l1_grid, alphas=alpha_grid, fit_intercept=intercept, eps = eps,\
        normalize=normalize, max_iter=max_iter, tol=tolerance, cv=5)

    reg_model.fit(gene_mat.T, sign_mat)

    filename      = os.path.join(run_parameters['results_directory'], 'elastic_net_model.pkl') 
    pickle.dump(reg_model, open(filename, 'wb'))
    response_predict = reg_model.predict(test_mat.T)
    predict_df        = pd.DataFrame(response_predict.T, index=row_names, columns=['predict'])
    write_predict_data(predict_df, run_parameters)


def write_predict_data(predict_df, run_parameters):

    test_spreadsheet_name_full_path = run_parameters['test_spreadsheet_name_full_path']
    results_directory               = run_parameters['results_directory']
    method                          = run_parameters['method']
    _, output_file_name             = os.path.split(test_spreadsheet_name_full_path)

    output_file_name, _             = os.path.splitext(output_file_name)
    output_file_name                = os.path.join(results_directory, output_file_name + '_' + method)
    output_file_name                = kn.create_timestamped_filename(output_file_name) + '.tsv'

    predict_df.to_csv(output_file_name, sep='\t', header=True, index=True, float_format='%g')

