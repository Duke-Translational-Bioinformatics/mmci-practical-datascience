import pandas as pd
import numpy as np
df = pd.read_csv('/Users/nn31/Dropbox/40-githubRrepos/mmci-practical-datascience/lecture07_170624/dataset_diabetes/holdback/diabetic_data.csv',
                        na_values='?',
                        dtype={'encounter_id':object,'patient_nbr':object,'race':object,'gender':object,
                                'age':object,
                                'weight':object,
                                'admission_type_id':object,
                                'discharge_disposition_id':object,
                                'admission_source_id':object,
                                'time_in_hospital':object,
                                'payer_code':object,
                                'medical_specialty':object,
                                'num_lab_procedures':np.int,
                                'num_procedures':np.int,
                                'num_medications':np.int,
                                'number_outpatient':np.int,
                                'number_emergency':np.int,
                                'number_inpatient':np.int,
                                'diag_1':object,
                                'diag_2':object,
                                'diag_3':object,
                                'number_diagnoses':np.int,
                                'max_glu_serum':object,
                                'A1Cresult':object,
                                'metformin':object,
                                'repaglinide':object,
                                'nateglinide':object,
                                'chlorpropamide':object,
                                'glimepiride':object,
                                'acetohexamide':object,
                                'glipizide':object,
                                'glyburide':object,
                                'tolbutamide':object,
                                'pioglitazone':object,
                                'rosiglitazone':object,
                                'acarbose':object,
                                'miglitol':object,
                                'troglitazone':object,
                                'tolazamide':object,
                                'examide':object,
                                'citoglipton':object,
                                'insulin':object,
                                'glyburide-metformin':object,
                                'glipizide-metformin':object,
                                'glimepiride-pioglitazone':object,
                                'metformin-rosiglitazone':object,
                                'metformin-pioglitazone':object,
                                'change':object,
                                'diabetesMed':object,
                                'readmitted':object})
df['admitted'] = df['readmitted'].apply(lambda x: 0 if x=='NO' else 1)

np.random.seed(42)
msk = np.random.rand(len(df)) < 0.7

df_train = df[msk]
print(df_train.shape)
df_test = df[~msk]
print(df_test.shape)

df_train.to_csv('/Users/nn31/Dropbox/40-githubRrepos/mmci-practical-datascience/lecture07_170624/dataset_diabetes/diabetic-deliver.csv',
                index=False)
df_test.to_csv('/Users/nn31/Dropbox/40-githubRrepos/mmci-practical-datascience/lecture07_170624/dataset_diabetes/holdback/diabetic-holdback.csv',
                index=False)