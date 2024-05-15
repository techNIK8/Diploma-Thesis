"""
@author: Nikos Kosioris
"""

import pandas as pd
import warnings
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from causalml.propensity import ElasticNetPropensityModel
from causalml.dataset import *
from causalml.metrics import *
from causalml.metrics.sensitivity import Sensitivity
from causalml.inference.meta import LRSRegressor
from causalml.inference.meta import XGBTRegressor, MLPTRegressor
from causalml.inference.meta import BaseXRegressor, BaseRRegressor, BaseTRegressor
from xgboost import XGBRegressor

warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\er_15temp.csv')
df_2 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\er_15temp.csv')

treatment = df['many_electric_heaters']
y = df['high_temperature']
df.drop('many_electric_heaters', axis=1, inplace=True)
df.drop('high_temperature', axis=1, inplace=True)
X = df

# Ready-to-use S-Learner
learner_s = LRSRegressor()
te, lb, ub = learner_s.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Ready-to-use S-Learner using Linear Regression): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# Ready-to-use T-Learner
learner_t = XGBTRegressor()
te, lb, ub = learner_t.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Ready-to-use T-Learner using XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# Sensitivity Analysis
pm = ElasticNetPropensityModel(n_fold=5, random_state=42)
propensity_score = pm.fit_predict(X, y)
df_2['prop_score'] = propensity_score.tolist()
prop_score_col_name = 'prop_score'
inf_feat_col_names = list(df)
treat_col_name = 'many_electric_heaters'
outcome_col_name = 'high_temperature'

sens_x = Sensitivity(df=df_2, inference_features=inf_feat_col_names, p_col=prop_score_col_name,
                      treatment_col=treat_col_name, outcome_col=outcome_col_name, learner=learner_t)
sens_sumary_x = sens_x.sensitivity_analysis(methods=['Placebo Treatment',
                                                      'Random Cause',
                                                      'Subset Data',
                                                      'Random Replace',
                                                      'Selection Bias'], sample_size=0.5)

# T Learner
learner_t = BaseTRegressor(learner=LinearRegression())
te, lb, ub = learner_t.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base T-Learner class and feeding in Linear Regression): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# T Learner
learner_t = BaseTRegressor(learner=XGBRegressor())
te, lb, ub = learner_t.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base T-Learner class and feeding in XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# R Learner without propensity score input
learner_r = BaseRRegressor(learner=LinearRegression())
te, lb, ub = learner_r.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base R-Learner class and feeding in Linear Regression): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# R Learner without propensity score input
learner_r = BaseRRegressor(learner=XGBRegressor())
te, lb, ub = learner_r.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base R-Learner class and feeding in XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# X Learner without propensity score input
learner_x = BaseXRegressor(learner=LinearRegression())
te, lb, ub = learner_x.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base X-Learner class and feeding in Linear Regression): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# X Learner without propensity score input
learner_x = BaseXRegressor(learner=XGBRegressor())
te, lb, ub = learner_x.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Base X-Learner class and feeding in XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))

# Multi-layer Perceptron
nn = MLPTRegressor(hidden_layer_sizes=(10, 10),
                 learning_rate_init=.1,
                 early_stopping=True,
                 random_state=42)
te, lb, ub = nn.estimate_ate(X, treatment, y)
print('Average Treatment Effect (Neural Network (MLP)): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))


# Generate Synthetic Dataset, Multiple Simulations (10) 
train_summary, validation_summary = get_synthetic_summary_holdout(simulate_nuisance_and_easy_treatment,
                                                                  n=10000,
                                                                  valid_size=0.2,
                                                                  k=10)

# Bar Plot Summary
bar_plot_summary_holdout(train_summary,
                          validation_summary,
                          k=10,
                          drop_learners=['S Learner (XGB)'],
                          drop_cols=[])

# Scatter Plot Summary
scatter_plot_summary_holdout(train_summary,
                             validation_summary,
                             k=10,
                             label=['Train', 'Validation'],
                             drop_learners=[],
                             drop_cols=[])

# Generate Synthetic Dataset, Single Simulation
train_preds, valid_preds = get_synthetic_preds_holdout(simulate_nuisance_and_easy_treatment,
                                                        n=50000,
                                                        valid_size=0.2)

# Distribution Plot for Single Simulation of Training
distr_plot_single_sim(train_preds, kind='kde', linewidth=2, bw_method=0.5,
                      drop_learners=['S Learner (XGB)','S Learner (LR)'])

# Distribution Plot for Single Simulation of Validation
distr_plot_single_sim(valid_preds, kind='kde', linewidth=2, bw_method=0.5,
                      drop_learners=['S Learner (XGB)','S Learner (LR)'])

# Scatter Plots for a Single Simulation of Training Data
scatter_plot_single_sim(train_preds)

# Scatter Plots for a Single Simulation of Validation Data
scatter_plot_single_sim(valid_preds)

# Cumulative Gain AUUC Values for a Single Simulation of Training Data
get_synthetic_auuc(train_preds, drop_learners=['S Learner (XGB)'])

# Cumulative Gain AUUC Values for a Single Simulation of Validation Data
get_synthetic_auuc(valid_preds, drop_learners=['S Learner (XGB)'])