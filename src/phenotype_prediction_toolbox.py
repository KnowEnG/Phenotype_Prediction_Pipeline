# this is the toolbox of PPP
import os
import pandas as pd

from sklearn import linear_model

import knpackage.toolbox as kn

def run_elastic_predict(run_parameters):

    gene_samples_train_df = kn.get_spreadsheet_df(run_parameters['spreadsheet_name_full_path'])
    response_train_df = kn.get_spreadsheet_df(run_parameters['response_name_full_path'])
    gene_samples_test_df = kn.get_spreadsheet_df(run_parameters['test_spreadsheet_name_full_path'])
    response_test_sample_names = list(gene_samples_test_df.columns)

    reg_moE = linear_model.ElasticNetCV()
    response_predict = reg_moE.fit(gene_samples_train_df.transpose().values,
                                   response_train_df.values[0]).predict(gene_samples_test_df.transpose().values)

    predict_df = pd.DataFrame(response_predict.T, index=response_test_sample_names, columns=['predict'])
    write_predict_data(predict_df, run_parameters)


def write_predict_data(predict_df, run_parameters):
    deNada, output_file_name = os.path.split(run_parameters['test_spreadsheet_name_full_path'])
    output_file_name, deNada = os.path.splitext(output_file_name)
    output_file_name = os.path.join(run_parameters['results_directory'], output_file_name)
    output_file_name = kn.create_timestamped_filename(output_file_name) + '.tsv'

    predict_df.to_csv(output_file_name, sep='\t', header=True, index=True)
