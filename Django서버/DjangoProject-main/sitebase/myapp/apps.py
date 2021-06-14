from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

"""
이 부분은 프랜차이즈 분석 모델 
"""
import joblib


class FranchiseClassifier(AppConfig):
    load_model = joblib.load('/home/tpah20/model.pkl')
